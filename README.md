# Online Shopping System

A Django-based online shopping website that provides a user-friendly interface for browsing products across multiple categories and managing an online shopping experience.

## Overview

The Online Shopping System is a web application developed using Django.

The application organizes products into different categories and provides a structured shopping interface with promotional sections, product listings, and category-based browsing.

## Features

- Product category browsing
- Product listings
- Promotional banners and offers
- Top deals section
- Multiple product categories
- Product images and media management
- User interface for online shopping
- Django-based backend
- Dynamic HTML templates
- Static files and media management

## Product Categories

The application contains products from categories such as:

- Speakers
- Printers
- Smartwatches
- Headphones
- Monitors
- Tablets
- Footwear
- Bags
- Mobile Phones
- Home Appliances
- Decoration Items
- Cameras

## Technologies Used

- Python
- Django
- HTML
- CSS
- SQLite
- Git
- GitHub

## Screenshots

### Homepage

The homepage displays promotional banners, product categories, featured products, and shopping sections.

![Homepage](screenshots/homepage.png)

### Top Deals

The Top Deals section displays products across different categories with promotional offers.

![Top Deal 1](screenshots/topdeals/topdeal1.png)

![Top Deal 2](screenshots/topdeals/topdeal2.png)

![Top Deal 3](screenshots/topdeals/topdeal3.png)


## Project Structure

```text
Online-Shopping-System-Django/
│
├── ecommerceapp/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
│
├── ecommerceproject/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── media/
│   └── product images
│
├── static/
│   ├── css/
│   └── images/
│
├── templates/
│   └── HTML templates
│
├── manage.py
├── .gitignore
└── README.md