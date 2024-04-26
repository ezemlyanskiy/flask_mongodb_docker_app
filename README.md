# Test Task by DocuSketch

A simple application built with Flask, MongoDB, and Docker.

## Getting Started

1. Make sure you have Docker and Docker Compose installed on your machine.
2. Clone this repository.
3. Navigate to the project directory.
4. Run the following command to start the application:

```bash
git clone git@github.com:ezemlyanskiy/flask_mongodb_docker_app.git
cd flask_mongodb_docker_app
cat .env.example > .env
sudo docker compose up -d
```

## API Endpoints

- GET /items: Retrieves all items.
- POST /items: Creates a new item.
- GET /items/<item_id>: Retrieves a specific item.
- PUT /items/<item_id>: Updates a specific item.

## About

This project serves as a demonstration of a basic application using Flask, MongoDB, and Docker.  
Feel free to explore the code and have fun experimenting!

## Testing

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install -U pip
python -m pip install -r requirements.txt
pytest
```
