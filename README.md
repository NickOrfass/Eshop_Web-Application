# Internet Programming Final Project: Eshop

A full-featured E-commerce web application built using the Django framework. This project provides a complete online shopping experience, including product browsing, shopping cart management, user authentication, and a custom manager dashboard.

## Features

- **User Authentication**: Custom user model (`accounts`) with registration, login, and profile management.
- **Product Catalog**: Browse products by categories, view product details, and ratings (`shop`).
- **Shopping Cart**: Session-based cart system allowing users to add, update, and remove items before checkout (`cart`).
- **Order Management**: Secure checkout process and order tracking (`orders`).
- **Custom Admin Dashboard**: A protected manager interface (`dashboard`) allowing privileged users (managers) to:
  - Add, edit, and delete products
  - Create new categories
  - View and manage customer orders
- **Responsive UI**: Integrated with Bootstrap 4 and `django-crispy-forms` for clean and responsive forms.

## Technologies Used

- **Backend**: Python, Django 4.0+
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 4
- **Database**: SQLite (default) / PostgreSQL (configurable)

## Local Setup Instructions

Follow these steps to set up and run the project locally.

### Prerequisites

- Python 3.8+
- Git

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/NickOrfass/Internet-Programming_Final-Project_Eshop.git
   cd Internet-Programming_Final-Project_Eshop/MyShop/online_shop
   ```

2. **Create a virtual environment (Optional but recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**:
   *(Assuming a `requirements.txt` exists, otherwise install Django and related packages manually)*
   ```bash
   pip install django django-crispy-forms crispy-bootstrap4
   ```

4. **Apply database migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (To access the Django admin and set up manager accounts):
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the Application**:
   - Main Storefront: `http://127.0.0.1:8000/`
   - Custom Admin Dashboard: `http://127.0.0.1:8000/dashboard/` (Requires a user account with `is_manager=True`)
   - Default Django Admin: `http://127.0.0.1:8000/admin/`

## Project Structure

- `accounts/`: Handles user authentication and custom User model.
- `shop/`: Core app for products, categories, and views.
- `cart/`: Manages shopping cart functionality.
- `orders/`: Handles checkout and order persistence.
- `dashboard/`: Custom interface for store managers.
- `online_shop/`: Project configuration and settings.
