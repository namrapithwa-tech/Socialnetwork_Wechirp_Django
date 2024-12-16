# Socialnetwork_Wechirp_Django

# WeChirp

WeChirp is a clone version of Twitter (now X), developed using **Django**. This project demonstrates advanced skills in Python and Django, including user authentication, dynamic content rendering, and database interactions. 

---

## Features

- User Authentication (Login, Signup, Logout) using Django `allauth`.
- Profile management with avatars.
- Post creation, editing, and deletion.
- Following and unfollowing users.
- Real-time notifications.
- Responsive design using Bootstrap.
- Media uploads for posts and profiles.

---

## Dependencies

The following dependencies are required to run this project:

- **Django 4.1.5**  
- **django-allauth** (for user authentication)  
- **crispy-forms** (for enhanced forms)  
- **crispy-bootstrap5** (for Bootstrap integration)  
- **Pillow** (for image processing)  

---

## Getting Started

Follow the steps below to set up and run the project locally.

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/wechirp.git
cd wechirp
```

### 2. Set up a Virtual Environment

Create a virtual environment to isolate project dependencies:
```bash
python -m venv env
source env/bin/activate   # On Windows, use `env\Scripts\activate`
```

### 3. Install Dependencies

Install the required Python packages:
```bash
pip install django django-allauth crispy-forms crispy-bootstrap5 pillow
```

### 4. Configure the Environment

Update the `settings.py` file with your configurations:

- **SECRET_KEY:** Replace with your secret key.
- **DEBUG:** Set to `True` for development and `False` for production.
- **ALLOWED_HOSTS:** Add your domain or IP address.

### 5. Apply Migrations

Create and apply database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser

Create an admin account to manage the application:
```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

Start the server:
```bash
python manage.py runserver
```

Access the application at [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## Project Structure

```
wechirp/
├── socialnetwork/      # Core Django project settings
├── social/             # Main app handling posts, profiles, etc.
├── landing/            # Landing page app
├── static/             # CSS, JS, and images
├── templates/          # HTML templates
├── media/              # User-uploaded files (e.g., profile pictures, posts)
└── manage.py           # Django's CLI entry point
```

---

## Technologies Used

- **Backend:** Django 4.1.5, Python 3.x
- **Frontend:** Bootstrap 5, HTML5, CSS3
- **Database:** SQLite (default, can be replaced with PostgreSQL or MySQL)

---

## Skills Demonstrated

- **Django Expertise:** Mastery of models, views, templates, and middleware.
- **Authentication:** Seamless user registration and login system using `django-allauth`.
- **Dynamic Content:** Efficient use of Django ORM to fetch and display user-specific data.
- **Media Handling:** Secure and efficient handling of user-uploaded images with `Pillow`.
- **Responsive Design:** Integration of Bootstrap 5 for a responsive UI.
- **Project Setup:** Environment setup, migrations, and server configuration.

---


---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
