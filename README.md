# HotSpot

## Overview
HotSpot is a Django-based web application designed for hot sauce enthusiasts to discover, review, and shop for a curated selection of hot sauces. The platform combines a modern, responsive design (using Bootstrap 5) with robust user features, including authentication, product reviews, and admin management. The site holds a Products page with a collection of items with reviews, and a Blogs page with user created blogs for hot sauce related content like recipes. Product Reviews and Blog comments has full CRUD functionality, enabling users to create, read, update, and delete reviews efficiently.

## UX Design Process

- **Link to User Stories in GitHub Projects:**
  - [GitHub Projects Kanban Board](https://github.com/yourusername/hotspot/projects)
- **Wireframes:**
  - [Wireframe Designs](https://linktowireframes.com)
  - Wireframes were created to ensure intuitive navigation, clear product presentation, and accessibility for all users. High-contrast colours and descriptive alt text were used to maximise usability.
- **Design Rationale:**
  - The layout emphasises simplicity and clarity, with Bootstrap 5 ensuring a responsive experience across devices. The color palette and typography were chosen for readability and accessibility, following WCAG guidelines.
  - Accessibility features include keyboard navigation, ARIA labels, and screen reader support.
  Fonts
  
- **Reasoning For Any Final Changes:**
  - User feedback led to improvements in navigation flow, review visibility, and mobile responsiveness. Adjustments were made to enhance inclusivity and overall user satisfaction.

## Key Features

- **Product Catalogue:** Browse, filter, and search a wide range of hot sauces by category or brand.
- **Product Detail Pages:** View detailed information, images, and reviews for each sauce.
- **User Authentication:** Register, log in securely.
- **Product Reviews:** Leave and read reviews to help the community make informed choices.
- **Admin Management:** Admins can add, edit, or remove products, manage categories, and moderate reviews.
- **Notifications:** Users receive feedback on actions (e.g., successful login, review submission).
- **Inclusivity Notes:** Accessibility features include ARIA labels, alt text for images, and keyboard navigation.

## Deployment

- **Platform:** Heroku (or your chosen platform)
- **High-Level Deployment Steps:**
  1. Clone the repository.
  2. Set up the environment with PostgreSQL (or your chosen database).
  3. Configure environment variables for sensitive data (e.g., secret keys, API keys).
  4. Deploy using Heroku Git, GitHub integration, or your preferred method.
- **Verification and Validation:**
  - The deployed application was tested for consistent functionality, design, and accessibility using tools like Lighthouse and manual testing.
- **Security Measures:**
  - Sensitive data is stored in environment variables.
  - DEBUG mode is disabled in production for enhanced security.

## AI Implementation and Orchestration

### Use Cases and Reflections

Throughout the development of HotSpot, GitHub Copilot was used extensively to streamline coding, debugging, and testing.

- **Code Creation:**
  - Copilot accelerated the creation of Django models, views, and forms, suggesting best practices and efficient patterns. It was especially helpful for generating boilerplate code and exploring alternative approaches.
- **Debugging:**
  - Copilot provided insightful suggestions for resolving errors and simplifying complex logic, making the codebase more maintainable and accessible.
- **Performance and UX Optimisation:**
  - The AI suggested impactful Bootstrap tweaks, improving the visual polish and responsiveness of the site. These enhancements ensured a professional and accessible user experience.
- **Automated Unit Testing:**
  - Copilot assisted in generating initial test cases, helping to cover edge cases and improve the robustness of the application.

### Overall Impact

Using Copilot transformed the workflow, allowing for a focus on higher-level design and inclusivity. While not every suggestion was perfect, the AI served as a valuable collaborator, enhancing both technical and problem-solving skills.

## User Stories

### User
1. As a User, I can easily register, log in, and log out so I can browse and interact with the site.
2. As a User, I can easily navigate the website so that I can find and discover new items.
3. As a User, I can view a list of products so that I can find the item I want to buy.
4. As a User, I can filter and sort products so that I can find the item I want to buy.
5. As a User, I can search products so that I can find the item I want to buy.
6. As a User, I can view more information on a product so that I can decide whether to buy it.
7. As a User, I can add one or more products to my basket, view my basket, change item quantities, and remove items so that I can manage my order.
8. As a User, I can view products by category or brand so that I can find what I'm looking for.
9. As a User, I can update and save my profile information so that I can easily buy again.
10. As a User, I can contact the site admin so that I can get help or report issues.
11. As a User, I can see notifications when completing actions so that I know my action was successful.
12. As a User, I can see and write reviews so that I can give feedback and help others choose.
13. As a User, I can use a chatbot to get help on issues.

### Site Admin
14. As a Site Admin, I can add new products to the list so that customers can buy new products.
15. As a Site Admin, I can edit or remove existing products so that the product catalogue stays accurate and up to date.
16. As a Site Admin, I can manage product categories and brands so that products are organised for users.
17. As a Site Admin, I can view, approve, or remove user reviews so that product feedback remains appropriate.
18. As a Site Admin, I can view and manage customer orders so that I can process sales and handle issues.
19. As a Site Admin, I can access site analytics and reports so that I can monitor sales and user activity.

**Login Credential for testing:**  
Username: andrew  
Password: testerAA
a - andrew
b – benjamin
c – charlotte
d – daniel
e – emily
f – fiona
g – grace
h – henry
i – isaac
j – james
k – kevin
l – lucy
m – matthew
n – nathan
o – olivia
q – quinn
r – rachel
s – samuel
t – thomas
v – victoria
w – william
x – xavier
y – yvonne
z – zoe

## Testing Summary

- **Manual Testing:**
  - **Devices and Browsers Tested:** Windows 11 (Chrome, Edge, Brave), Android.
  - **Assistive Technologies:** Tested using Lighthouse and manual keyboard navigation.
  - **Features Tested:** Registration, login, product browsing, product editing, reviews, blog posts & comments, and admin features.
  - **Results:** All critical features, including accessibility checks, worked as expected.
- **Automated Testing:**
  - Tools Used: Django TestCase, GitHub Copilot.
  - Features Covered: User authentication, product CRUD, review system, and accessibility compliance.
  - Adjustments Made: Manual tweaks to ensure comprehensive test coverage and inclusivity.

## Future Enhancements

- Add real-time notifications for new reviews and order updates.
- Integrate advanced analytics for tracking user engagement and sales trends.
- Add chatbot capabilities for more interactive user assistance.
- Implement a recommendation system for personalised product suggestions.
- Enhance security features, including two-factor authentication and advanced data encryption.
- Optimise performance further with advanced caching strategies and code splitting.
- Regularly update the accessibility features to comply with the latest standards and guidelines.