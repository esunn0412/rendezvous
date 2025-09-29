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

## Template System

The application uses Django's template inheritance with a hierarchical structure: 

- `base.html` - Main layout template
- `head.html` - CSS/JS imports and meta tags
- `header.html` - Navigation and authentication UI
- `footer.html` - Site footer and branding
