# Rendezvous
<img width="1503" height="776" alt="ren" src="https://github.com/user-attachments/assets/ed2c5a18-bc04-42d2-b2cd-ef94aca77ee9" />

A Django-based social content platform that provides a Pinterest-like interface for sharing articles, organizing projects, and building communities through subscriptions and comments.

## Overview

Rendezvous is a web application built with Django that allows users to create and share articles, organize them into projects, and interact through comments and subscriptions. The platform features a modular architecture with six main Django applications handling different aspects of functionality.

## Features

### Core Functionality
- **Article Management**: Create, read, update, and delete articles with rich text editing 
- **Project Organization**: Group articles into themed projects
- **User Authentication**: Complete user registration, login, and profile management
- **Comments System**: Interactive commenting on articles 
- **Subscription System**: Follow projects of interest 

### User Interface
- Pinterest-like grid layout for browsing content 
- Responsive design with Bootstrap 5.2.3 integration 
- Clean navigation with authentication-aware UI elements 

## Technology Stack

- **Backend**: Django 5.1+ with Python
- **Frontend**: Bootstrap 5.2.3, Google Fonts (Material Icons, Antonio, Karla)
- **Database**: SQLite (development), MySQL/MariaDB (production)
- **Static Assets**: Django static files system
- **Rich Text Editing**: Medium Editor integration 

## Project Structure
<img width="739" height="593" alt="system" src="https://github.com/user-attachments/assets/5297d4ce-5d90-427f-984e-8f9b1da7d32c" />

The application follows Django's modular app architecture:

- `accountapp/` - User authentication and account management
- `profileapp/` - Extended user profiles
- `articleapp/` - Article creation and management
- `projectapp/` - Project organization
- `commentapp/` - Comment system
- `subscribeapp/` - Subscription functionality

## Getting Started

1. **Setup Environment**: Configure Django settings using the modular settings system 
2. **Install Dependencies**: Bootstrap4, Django, and other requirements
3. **Database Migration**: Run Django migrations for all apps
4. **Static Files**: Collect static files for production deployment
5. **Run Server**: Use `python manage.py runserver` for development

## Rendezvous AWS EC2 Deployment
Django social platform deployed on AWS EC2 using Docker Compose with automated builds from GitHub.

### Architecture
- **Nginx**: Serves static/media files, proxies to Django on port 80
- **Django + Gunicorn**: Auto-built from GitHub repo esunn0412/rendezvous
- **MariaDB**: Database with persistent storage on port 3306

### Process
Create Docker secrets on the EC2 instance:
```
echo "your-django-secret-key" | docker secret create DJANGO_SECRET_KEY -  
echo "mysql-password" | docker secret create MYSQL_PASSWORD -  
echo "root-password" | docker secret create MYSQL_ROOT_PASSWORD -
```
Deployment
```
# Build Django image  
docker build -t django_test_image:5 .  
  
# Deploy stack  
docker-compose up -d  
  
# Check status  
docker-compose ps
```
### Configuration Details
The Dockerfile automatically:
- Clones the latest code from GitHub
- Installs dependencies including gunicorn and mysqlclient
- Runs collectstatic and migrate with production settings
- Starts Gunicorn on port 8000

### Note 
- The production settings read Docker secrets and connect to MariaDB using the service name mariadb.
- Nginx serves static files from /data/static/ and media from /data/media/ with proper MIME types.
- Django uses the MySQL database backend to connect to MariaDB. MariaDB is a MySQL-compatible database, so Django treats it as MySQL from a driver perspective.

## Request-flow
<img width="798" height="604" alt="request-flow" src="https://github.com/user-attachments/assets/dcee5ca4-13d7-44f5-9b63-f5e477cb6704" />


