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

## Production Deployment
<img width="881" height="706" alt="service-comm" src="https://github.com/user-attachments/assets/ecfb82ce-2a42-4616-b94f-47d57c61a5ab" />
This application is containerized using a Docker build process handling dependency installation, code deployment, and service configuration. 

Database Configuration 
- DB: MariaDB
- Port: 3306

Application Server Configuration 
- Server: gunicorn
- WSGI Module: myPinterest.wsgi
- Settings Module: myPinterest.settings.deploy
- Bind Address: 0.0.0.0:8000
- Port Exposure: Container port 8000

Container Startup Sequence 
1. Static file collection
   - `python manage.py collectstatic --noinput --settings=myPinterest.settings.deploy`
3. Database migration
  - `python manage.py migrate --settings=myPinterest.settings.deploy`
5. WSGI server launch
  - `gunicorn myPinterest.wsgi --env DJANGO_SETTINGS_MODULE=myPinterest.settings.deploy --bind 0.0.0.0:8000`


## Request-flow
<img width="798" height="604" alt="request-flow" src="https://github.com/user-attachments/assets/dcee5ca4-13d7-44f5-9b63-f5e477cb6704" />


