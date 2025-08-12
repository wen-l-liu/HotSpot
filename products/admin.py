from django.contrib import admin
from django import forms
from .models import Brand, Product, Review, Flavour


class FlavourAdminForm(forms.ModelForm):
    class Meta:
        model = Flavour
        fields = '__all__'
        widgets = {
            'fruit': forms.RadioSelect,
            'garlic': forms.RadioSelect,
            'sweet': forms.RadioSelect,
            'smoke': forms.RadioSelect,
            'salt': forms.RadioSelect,
            'vinegar': forms.RadioSelect,
        }


class FlavourInline(admin.StackedInline):
    model = Flavour
    max_num = 1
    can_delete = False
    form = FlavourAdminForm


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """ Product admin """
    list_display = ('name', 'brand', 'price', 'rating')
    search_fields = ('name', 'brand__name')
    list_filter = ('created_on',)
    prepopulated_fields = {'slug': ('name',)}
    inlines = [FlavourInline]  # Now this works


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    """ Brand admin """
    list_display = ('name',)
    search_fields = ('name',)
    text_fields = ('description',)
    list_filter = ('created_on',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """ Review admin """
    list_display = (
        'comment', 'product', 'author', 'rating', 'created_on', 'approved')
    list_filter = ('rating', 'created_on', 'approved')
    search_fields = ('product__name', 'author__username', 'comment')
    actions = ['approve_reviews']

    @admin.action(description="Approve selected reviews")
    def approve_reviews(self, request, queryset):
        updated = queryset.update(approved=True)
        self.message_user(request, f"{updated} review(s) approved.")
