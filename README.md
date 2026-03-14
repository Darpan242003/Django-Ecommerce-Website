# E-Commerce Web Application

A web-based e-commerce platform built using Django that allows users to browse products, add items to a cart, and place orders through a secure authentication system.

## Overview

This project demonstrates a basic online shopping system where users can view products, manage a shopping cart, and place orders. The application uses Django ORM for database management and SQLite as the backend database.

## Features

- User registration and authentication
- Product catalog with product details
- Add/remove items from shopping cart
- Order placement and management
- Admin panel for managing products and orders
- Database operations using Django ORM

## Tech Stack

Backend: Django (Python)  
Database: SQLite  
ORM: Django ORM  
Frontend: HTML, CSS, Bootstrap  
Version Control: Git & GitHub

## Project Structure

ecommerce-project/
│
├── products/        # Product management app
├── orders/          # Order processing logic
├── users/           # Authentication system
├── cart/            # Shopping cart functionality
├── templates/       # HTML templates
├── static/          # CSS and assets
├── manage.py        # Django project manager
└── db.sqlite3

## Installation

1. Clone the repository

git clone https://github.com/yourusername/ecommerce-project.git

2. Navigate to project directory

cd ecommerce-project

3. Install dependencies

pip install -r requirements.txt

4. Run migrations

python manage.py migrate

5. Start the server

python manage.py runserver

## Future Improvements

- Integrate payment gateway
- Add product reviews and ratings
- Implement REST APIs using Django REST Framework
- Deploy the application on a cloud platform

## Screenshots

Product Listing Page  
![alt text](<Screenshot 2026-03-14 110722.png>)
Shopping Cart Pag
![alt text](<Screenshot 2026-03-14 110958.png>)
Order Confirmation Page
![alt text](<Screenshot 2026-03-14 111200.png>) ![alt text](<Screenshot 2026-03-14 111242.png>)

## Author

Darpan Bhamre  
LinkedIn: https://linkedin.com/in/darpanbhamre  
GitHub: https://github.com/Darpan242003