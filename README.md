
# Food Waste Reduction Platform

## Overview

This project is a Django-based web application designed to minimize food waste and create a win-win situation for restaurants, catering services, and budget-conscious users. The platform enables restaurants and caterers to sell their surplus food at a reduced price to the platform admin, who then resells the food to users at a budget-friendly rate. This approach ensures that less food is wasted and allows businesses to recover some of their costs.

## Features

### Admin (Superuser)
- **Manage Users**: Approve or reject registrations of restaurants and caterers based on submitted proof.
- **Manage Listings**: Collect surplus food from registered restaurants and caterers, list them on the platform,  and set prices.
- **View and Manage Orders**: Track user orders, manage deliveries, and handle payments.
- **Feedback Management**: View and respond to feedback from users.

### Restaurants & Caterers
- **Registration**: Register on the platform by submitting credentials and necessary proof (e.g., owner’s ID, restaurant license).
- **Listing Surplus Food**: Upload details of surplus food to sell to the admin at half the original price.
- **Order Tracking**: Track the status of food picked up by the admin.

### Users
- **Browse and Buy Food**: Explore available food items and purchase them at reduced prices.
- **View Bookings**: Track orders and view booking history.
- **Give Feedback**: Provide feedback on food quality and service.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/aswin8884/remain_food_booking_system.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd remain_food_booking_system
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the website**:
   Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Usage

### For Admin
- Log in using the superuser credentials.
- Manage restaurant and caterer registrations, food listings, and user feedback.
- Monitor orders and handle user requests.

### For Restaurants & Caterers
- Register your business by providing required credentials and proof.
- List surplus food items for sale after approval.
- Track orders and receive payments.

### For Users
- Browse available food items.
- Purchase food at reduced prices.
- View your booking history and provide feedback.



