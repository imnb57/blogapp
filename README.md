# Simple Django Blogging Application

This is a simple blogging application built using the Django framework. The application allows users to register, log in, create, edit, and view blog posts. It also supports file uploads. Signed-in users can view all blog posts, but only the blog owner can edit or delete their own blogs.

## Features

- **User Authentication**: Users can sign up, log in, and log out.
- **Create Blog Posts**: Logged-in users can create new blog posts.
- **Edit Blog Posts**: Only the blog owner can edit their own blog posts.
- **View Blogs**: All signed-in users can view the list of blogs and individual blog posts.
- **File Upload**: Users can upload files along with their blog posts.

## Technologies Used

- **Backend**: Django (Python framework)
- **Frontend**: HTML (No external frontend libraries like React, Vue, or Bootstrap, but can be added)
- **Database**: SQLite (Django's default database; can be switched to PostgreSQL, MySQL, etc. easily)
- **Authentication**: Custom user model with email as the primary login field

## Prerequisites

Before you can run this application, you need to have the following installed:

- Python 3.x
- Git

## Getting Started

### 1. Clone the Repository

Clone the repository using the following command:

```bash
git clone <your-repository-url>
```

### 2. Create a Virtual Environment (Optional but Recommended)

It is recommended to create a virtual environment to avoid conflicts with other Python packages:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Requirements

After activating the virtual environment, install the required dependencies:

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

Run the following command to apply the initial database migrations:

```bash
python manage.py migrate
```

### 5. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

Your app will be accessible at http://127.0.0.1:8000/ in the browser.

### 6. Create a Superuser (Optional but Recommended)

To access the Django admin panel:

```bash
python manage.py createsuperuser
```

Follow the prompts to create a superuser, and then access the admin panel at http://127.0.0.1:8000/admin/.

### 7. Start Using the App

- Register a new user: Click on the "Sign up" link on the homepage
- Create blog posts: After logging in, you can create new blog posts
- Edit your own posts: Only the user who created a blog post can edit it

## App Structure

- `blog/`: The main app containing:
  - `models.py`: Database models for Blog and User
  - `views.py`: Views for rendering blog list, individual blogs, creating and editing posts
  - `urls.py`: URL patterns for routing views
  - `templates/blog/`: HTML templates for various views

- `myblog/`: The main project folder with settings, URLs, and configurations

## Usage

- **View Blogs**: After logging in, view all blog posts at the homepage (/)
- **Create Blog**: Click on the "Create New Blog" button
- **Edit Blog**: As the blog owner, edit posts by clicking the "Edit" button
- **File Upload**: Upload files while creating or editing blog posts (stored in the `media/` folder)

## Common Issues

### File Upload
If you're unable to upload files:
- Ensure the `media` folder exists in your project's root directory
- Configure Django's settings for file storage

### Database Migrations
After modifying models:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Contributing

Feel free to fork this repository and contribute by:
- Fixing bugs
- Adding new features (e.g., blog comments)
- Improving UI with CSS frameworks
- Updating documentation

## License

This project is open-source and available under the MIT License.

## Conclusion

This is a simple but effective blogging platform that demonstrates how Django can be used to build web applications quickly. The features like user authentication, blog creation and editing, and file upload are basic yet powerful, allowing you to create a fully functional blog application.

**Enjoy building with Django!**
