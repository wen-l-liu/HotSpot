from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Product, Brand, Review, Flavour
from .forms import ReviewForm, ProductForm

class ProductModelTest(TestCase):
    def setUp(self):
        self.brand = Brand.objects.create(name="TestBrand", slug="testbrand")
        self.product = Product.objects.create(
            name="Test Sauce",
            brand=self.brand,
            price=5.99,
            slug="test-sauce"
        )

    def test_product_str(self):
        self.assertEqual(str(self.product), "Test Sauce")

    def test_product_detail_view(self):
        url = reverse('product_detail', args=[self.product.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Sauce")

class ProductListViewTest(TestCase):
    def setUp(self):
        self.brand = Brand.objects.create(name="BrandA", slug="branda")
        for i in range(3):
            Product.objects.create(
                name=f"Product {i}",
                brand=self.brand,
                price=2.99 + i,
                slug=f"product-{i}"
            )

    def test_product_list_view(self):
        url = reverse('products')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Product 0")
        self.assertContains(response, "Product 1")
        self.assertContains(response, "Product 2")

class ReviewModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.brand = Brand.objects.create(name="BrandB", slug="brandb")
        self.product = Product.objects.create(
            name="Review Sauce",
            brand=self.brand,
            price=7.99,
            slug="review-sauce"
        )
        self.review = Review.objects.create(
            product=self.product,
            author=self.user,
            rating=4,
            comment="Great sauce!",
            approved=True
        )

    def test_review_str(self):
        self.assertIn("Review Sauce", str(self.review))

    def test_review_approval(self):
        self.assertTrue(self.review.approved)

class ProductFilterTest(TestCase):
    def setUp(self):
        self.brand1 = Brand.objects.create(name="Brand1", slug="brand1")
        self.brand2 = Brand.objects.create(name="Brand2", slug="brand2")
        Product.objects.create(name="Mild Sauce", brand=self.brand1, price=3.99, slug="mild-sauce")
        Product.objects.create(name="Hot Sauce", brand=self.brand2, price=4.99, slug="hot-sauce")

    def test_filter_by_brand(self):
        url = reverse('products')
        response = self.client.get(url, {'brand': [str(self.brand1.id)]})
        self.assertContains(response, "Mild Sauce")
        self.assertNotContains(response, "Hot Sauce")

class AuthTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="andrew", password="testerAA")

    def test_login(self):
        login = self.client.login(username="andrew", password="testerAA")
        self.assertTrue(login)

    def test_logout(self):
        self.client.login(username="andrew", password="testerAA")
        response = self.client.get(reverse('account_logout'))
        self.assertEqual(response.status_code, 200)

class ReviewFormTest(TestCase):
    def setUp(self):
        self.brand = Brand.objects.create(name="FormBrand", slug="formbrand")
        self.product = Product.objects.create(
            name="Form Sauce",
            brand=self.brand,
            price=4.99,
            slug="form-sauce"
        )

    def test_valid_review_form(self):
        form_data = {
            'rating': 5,
            'comment': "Amazing sauce!"
        }
        form = ReviewForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_review_form_missing_comment(self):
        form_data = {
            'rating': 4,
            'comment': ""
        }
        form = ReviewForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_invalid_review_form_invalid_rating(self):
        form_data = {
            'rating': 10,  # Out of allowed range
            'comment': "Too spicy!"
        }
        form = ReviewForm(data=form_data)
        self.assertFalse(form.is_valid())

class ProductFormTest(TestCase):
    def setUp(self):
        self.brand = Brand.objects.create(name="FormBrand2", slug="formbrand2")

    def test_valid_product_form(self):
        form_data = {
            'name': "Test Product",
            'brand': self.brand.id,
            'description': "A tasty sauce.",
            'price': 3.50,
            'ingredients': "Tomato, Chili"
        }
        form = ProductForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_product_form_missing_name(self):
        form_data = {
            'name': "",
            'brand': self.brand.id,
            'description': "Missing name.",
            'price': 2.00,
            'ingredients': "Salt"
        }
        form = ProductForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_invalid_product_form_negative_price(self):
        form_data = {
            'name': "Negative Price",
            'brand': self.brand.id,
            'description': "Should not allow negative price.",
            'price': -1.00,
            'ingredients': "Vinegar"
        }
        form = ProductForm(data=form_data)
        self.assertFalse(form.is_valid())

# Add more tests for forms, reviews, and edge cases as needed.
