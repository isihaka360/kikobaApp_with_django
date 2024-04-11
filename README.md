# kikobaAlert
# KikopaAlert

KikopaAlert is a Django application designed to send notifications to customers about paying "marejesho" on Kikoba day before the date of marejesho. These notifications can be triggered by an admin or manager of the group via SMS. Additionally, the messages will appear in the recent activity section of the customer's account.

## Table of Contents

- Features
- Installation
- Usage
- Contributing
- License

## Features

- **Automatic Notification Sending**: Notifications are sent to customers before the date of marejesho.
- **Trigger Notifications**: Admin or manager can trigger notifications via SMS.
- **Recent Activity Updates**: Customers can see updates in their recent activity section upon logging into their accounts.
- **Customizable Messages**: Messages sent via SMS and displayed in the recent activity section are customizable.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your_username/KikopaAlert.git

Navigate into the project directory:
>>cd KikopaAlert

Create a virtual environment (recommended) and activate it:
>>python3 -m venv env
>>source env/bin/activate  # On Windows, use 'env\Scripts\activate'

Install dependencies:
>>pip install -r requirements.txt

Apply migrations:
>>python manage.py migrate

Create a superuser for accessing the admin panel:
>>python manage.py createsuperuser

Run the development server:
>>python manage.py runserver
Access the application at http://localhost:8000/.

## Usage
Log in to the admin panel using the superuser credentials created during installation.

Add customers and groups as needed.

Trigger notifications by sending SMS from the admin interface.

Customers will receive notifications and see updates in their recent activity section upon logging into their accounts.

## Contributing
Contributions are welcome! Please follow these guidelines:

## Fork the repository.

Create your feature branch:
>>git checkout -b feature/NewFeature

Commit your changes:
>>git commit -am 'Add new feature'

Push to the branch:
>>git push origin feature/NewFeature
Submit a pull request.


