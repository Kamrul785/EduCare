# TuitionHub API

A Django REST Framework-based platform connecting tutors with students for personalized tuition services. This API provides comprehensive functionality for tuition management, applications, enrollments, and progress tracking.

## 🚀 Features

- **User Management**: Role-based authentication (Students & Tutors)
- **Tuition Listings**: Create, browse, and manage tuition offerings
- **Application System**: Students can apply for tuitions, tutors can accept/reject
- **Enrollment Management**: Track student enrollments and progress
- **Progress Tracking**: Topics and assignments for enrolled students
- **Review System**: Students can review completed tuitions
- **Search & Filtering**: Advanced search with filters and pagination
- **JWT Authentication**: Secure token-based authentication
- **API Documentation**: Interactive Swagger/ReDoc documentation

## 🛠️ Technology Stack

- **Backend**: Django 5.2.6, Django REST Framework 3.16.1
- **Authentication**: JWT (using djoser and djangorestframework-simplejwt)
- **Database**: SQLite (development)
- **API Documentation**: drf-yasg (Swagger/OpenAPI)
- **Filtering**: django-filter, DRF search and ordering
- **Development Tools**: Django Debug Toolbar

## 📋 Prerequisites

- Python 3.8+
- pip
- Virtual environment (recommended)

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd tuition_media
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .tuition_env
   source .tuition_env/bin/activate  # On Windows: .tuition_env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   Create a `.env` file in the project root:
   ```env
   EMAIL_HOST=your_smtp_host
   EMAIL_USE_TLS=True
   EMAIL_PORT=587
   EMAIL_HOST_USER=your_email@gmail.com
   EMAIL_HOST_PASSWORD=your_app_password
   ```

5. **Database Setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create Superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/`

## 📚 API Documentation

- **Swagger UI**: `http://127.0.0.1:8000/swagger/`
- **ReDoc**: `http://127.0.0.1:8000/redoc/`
- **Django Admin**: `http://127.0.0.1:8000/admin/`

## 🔐 Authentication

The API uses JWT (JSON Web Tokens) for authentication. All endpoints except public ones require authentication.

### Authentication Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/auth/users/` | POST | User registration |
| `/api/v1/auth/jwt/create/` | POST | Login (get JWT tokens) |
| `/api/v1/auth/jwt/refresh/` | POST | Refresh access token |
| `/api/v1/auth/users/me/` | GET | Get current user profile |

### Example Registration
```json
POST /api/v1/auth/users/
{
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "password": "securepassword123",
    "role": "User",
    "phone_number": "+1234567890",
    "address": "123 Main St, City"
}
```

### Example Login
```json
POST /api/v1/auth/jwt/create/
{
    "email": "john.doe@example.com",
    "password": "securepassword123"
}
```

## 📖 API Endpoints

### Core Resources

#### Tuitions
- `GET /api/v1/tuitions/` - List all tuitions (with filtering and search)
- `POST /api/v1/tuitions/` - Create new tuition (Tutor only)
- `GET /api/v1/tuitions/{id}/` - Get tuition details
- `PUT/PATCH /api/v1/tuitions/{id}/` - Update tuition (Owner only)
- `DELETE /api/v1/tuitions/{id}/` - Delete tuition (Owner only)

#### Applications
- `GET /api/v1/applications/` - List user's applications
- `POST /api/v1/applications/` - Apply for tuition (Student only)
- `POST /api/v1/applications/{id}/select/` - Accept application (Tutor only)

#### Enrollments
- `GET /api/v1/enrollments/` - List user's enrollments
- `GET /api/v1/enrollments/{id}/` - Get enrollment details
- `GET /api/v1/enrollments/{id}/progress/` - Get enrollment progress

#### Topics (Nested under Enrollments)
- `GET /api/v1/enrollments/{enrollment_id}/topics/` - List topics
- `POST /api/v1/enrollments/{enrollment_id}/topics/` - Create topic (Tutor only)
- `PUT/PATCH /api/v1/enrollments/{enrollment_id}/topics/{id}/` - Update topic

#### Assignments (Nested under Enrollments)
- `GET /api/v1/enrollments/{enrollment_id}/assignments/` - List assignments
- `POST /api/v1/enrollments/{enrollment_id}/assignments/` - Create assignment (Tutor only)
- `PUT/PATCH /api/v1/enrollments/{enrollment_id}/assignments/{id}/` - Update assignment

#### Reviews
- `GET /api/v1/reviews/` - List all reviews
- `POST /api/v1/reviews/` - Create review (Enrolled students only)

### Query Parameters

#### Tuitions Filtering
- `?subject=Mathematics` - Filter by subject
- `?class_level=Grade 10` - Filter by class level
- `?tutor=1` - Filter by tutor ID
- `?search=algebra` - Search in title, description, subject, class_level
- `?ordering=-created_at` - Order by creation date (desc)
- `?page=2` - Pagination (10 items per page)

## 👥 User Roles

### Student (User)
- Browse and search tuitions
- Apply for tuitions
- View their enrollments and progress
- Complete topics and assignments
- Write reviews for completed tuitions

### Tutor
- Create and manage tuition listings
- Review and accept/reject applications
- Create topics and assignments for enrolled students
- Track student progress
- View reviews for their tuitions

## 🏗️ Project Structure

```
tuition_media/
├── api/                    # Main API configuration
├── applications/           # Applications, Enrollments, Topics, Assignments, Reviews
├── tuition/               # Tuition listings
├── users/                 # User management and authentication
├── tuition_media/         # Project settings
├── manage.py
├── requirements.txt
└── README.md
```

## 🔒 Permissions

- **Public**: View tuition listings
- **Authenticated**: Access personal data, apply for tuitions
- **Tutors**: Create/manage tuitions, accept applications, manage enrolled students
- **Students**: Apply for tuitions, access enrolled content, write reviews
- **Owners**: Modify/delete their own content

## 📱 Example Usage

### 1. Register as a Tutor
```bash
curl -X POST http://127.0.0.1:8000/api/v1/auth/users/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "tutor@example.com",
    "password": "securepass123",
    "first_name": "Jane",
    "last_name": "Smith",
    "role": "Tutor"
  }'
```

### 2. Login and Get Token
```bash
curl -X POST http://127.0.0.1:8000/api/v1/auth/jwt/create/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "tutor@example.com",
    "password": "securepass123"
  }'
```

### 3. Create a Tuition
```bash
curl -X POST http://127.0.0.1:8000/api/v1/tuitions/ \
  -H "Authorization: JWT your_access_token" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Advanced Mathematics Tutoring",
    "description": "Comprehensive math tutoring for high school students",
    "subject": "Mathematics",
    "class_level": "Grade 11-12",
    "availability": true
  }'
```

### 4. Apply for Tuition (as Student)
```bash
curl -X POST http://127.0.0.1:8000/api/v1/applications/ \
  -H "Authorization: JWT student_access_token" \
  -H "Content-Type: application/json" \
  -d '{
    "tuition": 1
  }'
```

## 🐛 Development

### Running Tests
```bash
python manage.py test
```

### Debug Mode
The project includes Django Debug Toolbar for development. Access it at `/__debug__/` when `DEBUG=True`.

### Database Management
```bash
# Create new migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Shell access
python manage.py shell
```

## 🚀 Deployment

1. Set `DEBUG=False` in production
2. Configure proper database (PostgreSQL recommended)
3. Set up proper email backend for notifications
4. Configure static files serving
5. Use environment variables for sensitive settings
6. Set up proper CORS headers if needed for frontend

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

For support, email kamrulkhan526785@gmail.com or create an issue in the repository.

---

**TuitionHub** - Connecting Knowledge Seekers with Knowledge Providers 🎓