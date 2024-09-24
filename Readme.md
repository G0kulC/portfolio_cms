# Portfolio CMS

**Portfolio CMS** is a powerful backend system built with Django that allows users to easily manage their personal portfolios. It is designed to provide RESTful API endpoints for handling various aspects of a portfolio, such as projects, skills, experience, education, blogs, testimonials, and more. The system uses JWT authentication to secure user data, ensuring privacy and security.

Portfolio CMS is designed to integrate seamlessly with modern frontend frameworks like Next.js, giving users the flexibility to present their portfolios in a customized manner.

## Features

- **User Authentication**: Secure user authentication with JWT tokens.
- **Portfolio Templates**: Manage different portfolio layouts and templates.
- **Content Management**: APIs for managing:
  - Projects
  - Skills
  - Experience
  - Education
  - Testimonials
  - Blogs
  - Social Links
  - Contacts
- **Flexible Integration**: Can be easily integrated with frontend frameworks like Next.js.
- **Custom ViewSets**: API endpoints implemented using Django Rest Framework (DRF) ViewSets for ease of use and modularity.
- **Soft Delete**: Models implement a `DeletedQuerySet` to handle soft deletion of records.
  
## Modules

The key modules in the system include:

- **DeletedQuerySet**: A custom queryset manager that handles soft deletion of records.
- **User**: Handles user management and authentication.
- **Template**: Manages different templates for the portfolio layouts.
- **Portfolio**: The main portfolio entity that ties together all other components.
- **Project**: For managing user projects within their portfolio.
- **Skill**: Manages the user's professional skills.
- **Experience**: For documenting work experience in the portfolio.
- **Education**: Keeps track of educational background.
- **Testimonial**: Collects testimonials from clients or colleagues.
- **Contact**: Manages the contact information of the user.
- **SocialLink**: Stores social media and other external links relevant to the user.

## Requirements

- Python 3.x
- Django 4.x
- Django Rest Framework (DRF)
- djangorestframework-jwt (for JWT authentication)
- PostgreSQL (or any other compatible database)
- Docker (optional for containerization)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/portfolio-cms.git
    cd portfolio-cms
    ```

2. **Install dependencies**:
    Create a virtual environment and install the required packages:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. **Set up environment variables**:
    Create a `.env` file for managing environment variables like database credentials, JWT secret keys, etc.
    ```bash
    SECRET_KEY='your-django-secret-key'
    DEBUG=True
    DATABASE_URL=postgres://user:password@localhost:5432/yourdb
    ```

4. **Run migrations**:
    Apply database migrations.
    ```bash
    python manage.py migrate
    ```

5. **Run the development server**:
    Start the Django development server:
    ```bash
    python manage.py runserver
    ```

6. **Access the API**:
    You can now access the API at `http://127.0.0.1:8000/api/`.


## Environment Variables

The Portfolio CMS requires specific environment variables to be set for proper configuration. You can define these variables in a `config.env` file or pass them directly through Docker Compose.

## Required Environment Variables

| Variable Name               | Description                                            | Default Value          |
|-----------------------------|--------------------------------------------------------|------------------------|
| `SECRET_KEY`                 | A unique secret key for your Django project            | (required)             |
| `DEBUG`                      | Set to `1` to enable debug mode, `0` for production    | `1`                    |
| `DB_NAME`                    | Name of the PostgreSQL database                        | `django_test`          |
| `DB_USER`                    | PostgreSQL database username                           | `postgres`             |
| `DB_PASSWORD`                | PostgreSQL database password                           | `postgres`             |
| `DB_HOST`                    | Database host (e.g., the service name in Docker)       | `db`                   |
| `DB_PORT`                    | Port on which the PostgreSQL database is running       | `5432`                 |
| `DJANGO_SUPERUSER_USERNAME`  | Username for the Django admin superuser                | `admin`                |
| `DJANGO_SUPERUSER_EMAIL`     | Email address for the Django admin superuser           | `admin@example.com`    |
| `DJANGO_SUPERUSER_PASSWORD`  | Password for the Django admin superuser                | `admin`                |

### Example `config.env` File

You can create a `config.env` file to store these environment variables:

```env
# Django Settings
SECRET_KEY=your-very-secure-secret-key
DEBUG=1

# PostgreSQL Database Settings
DB_NAME=django_test
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432

# Django Superuser Credentials
DJANGO_SUPERUSER_USERNAME=your_admin_username
DJANGO_SUPERUSER_EMAIL=your_admin_email@example.com
DJANGO_SUPERUSER_PASSWORD=your_admin_password
```

## Build and Run Process

The Portfolio CMS is designed to run using Docker and Docker Compose for easy setup. Follow the steps below to build and run the application:

### Prerequisites

Before you start, ensure you have the following installed:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Step 1: Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/portfolio-cms.git
cd portfolio-cms

```
## API Endpoints

Below are the key endpoints that the CMS provides. All endpoints are secured with JWT authentication:

- **User Management**:
  - `POST /api/auth/register/`: Register a new user.
  - `POST /api/auth/login/`: Login and get a JWT token.
  
- **Portfolio Management**:
  - `GET /api/portfolios/`: Get the list of portfolios.
  - `POST /api/portfolios/`: Create a new portfolio.
  - `GET /api/portfolios/{id}/`: Get a specific portfolio by ID.
  - `PUT /api/portfolios/{id}/`: Update a specific portfolio by ID.
  - `DELETE /api/portfolios/{id}/`: Soft-delete a portfolio.

- **Other Resources**:
  - Projects: `/api/projects/`
  - Skills: `/api/skills/`
  - Experience: `/api/experience/`
  - Education: `/api/education/`
  - Testimonials: `/api/testimonials/`
  - Social Links: `/api/social-links/`
  - Contact Information: `/api/contacts/`

## Testing

You can run the tests for the project using:

```bash
python manage.py test
```

## JWT Authentication
All endpoints are protected with JWT authentication. To access any API resource, include the JWT token in the `Authorization` header of your request:

```bash
Authorization: Bearer <your-token>
```
## License

This `README.md` provides a structured overview of the project, including installation instructions, API endpoints, and features. You can adjust it as needed for your project specifics.