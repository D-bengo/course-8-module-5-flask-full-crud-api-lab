# Event Management CRUD API

## Description
This project is a simple RESTful API built using Python and Flask.  
The API allows users to create, update, retrieve, and delete events using HTTP requests.

The project demonstrates:
- RESTful API design
- CRUD operations
- JSON handling with Flask
- Route creation using Flask decorators
- In-memory data storage using Python objects

---

## Features

- Create a new event using POST
- Retrieve all events using GET
- Retrieve a single event using GET
- Update an event title using PATCH
- Delete an event using DELETE
- Return JSON responses with proper HTTP status codes

---

## Technologies Used

- Python 3
- Flask

---

## Project Structure

```text
project-folder/
│
├── app.py
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Navigate into the project folder

```bash
cd <project-folder>
```

### 3. Create and activate virtual environment (optional)

Using pipenv:

```bash
pipenv shell
```

### 4. Install Flask

```bash
pip install flask
```

or

```bash
pipenv install flask
```

---

## Running the Application

Start the Flask server:

```bash
python app.py
```

The application will run at:

```text
http://127.0.0.1:5000
```

---

## API Endpoints

### GET All Events

```http
GET /events
```

### GET Single Event

```http
GET /events/<id>
```

Example:

```http
GET /events/1
```

---

### Create Event

```http
POST /events
```

Request Body:

```json
{
    "title": "Hackathon"
}
```

---

### Update Event

```http
PATCH /events/<id>
```

Example:

```http
PATCH /events/1
```

Request Body:

```json
{
    "title": "Hackathon 2025"
}
```

---

### Delete Event

```http
DELETE /events/<id>
```

Example:

```http
DELETE /events/2
```

---

## Example JSON Response

```json
{
    "message": "Event created successfully",
    "event": {
        "id": 3,
        "title": "Hackathon"
    }
}
```

---

## HTTP Status Codes Used

| Status Code | Meaning |
|-------------|----------|
| 200 | OK |
| 201 | Created |
| 400 | Bad Request |
| 404 | Not Found |

---

## Testing

You can test the API using:
- Postman
- Browser (GET requests only)
- curl

---

## Git Workflow Used

```bash
git checkout -b feature-crud-api

git add .
git commit -m "Add POST, PATCH, and DELETE routes for events"

git push origin feature-crud-api

git checkout main
git pull origin main
git merge feature-crud-api

git branch -d feature-crud-api
```

---

