# Mini AI Backend

A FastAPI backend.
## Features

- Student management APIs
- Text analysis API
- Calculator API
- Mock AI prompt API
- Request validation using Pydantic
- Error handling
- HTTP status codes
- Swagger API documentation

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Check API health |
| GET | `/students` | Get all students |
| POST | `/students` | Add a student |
| GET | `/students/{id}` | Get student by ID |
| POST | `/analyze-text` | Analyze text |
| POST | `/calculate` | Perform calculation |
| POST | `/generate` | Generate mock AI response |

## Technologies

- Python 3.12
- FastAPI
- Uvicorn
- Pydantic
- Postman
- Swagger/OpenAPI

## Running the Project

```bash
pip install -r requirements.txt
uvicorn main:app --reload