# FASTAPI – COMPLETE 14 DAYS LEARNING NOTES
### Beginner to Advanced | Theory + Practical + Real-World Examples

**Author:** Shaik Yusuf Vali  
**Technology:** Python, FastAPI, REST API, SQL, JWT, React, LLM

---

# 1. INTRODUCTION TO FASTAPI

## What is an API?

API stands for Application Programming Interface.

API allows two different applications to communicate with each other.

### Real-world Example

Imagine a food delivery application.

1. User selects food in the frontend.
2. Frontend sends a request to the backend.
3. Backend processes the request.
4. Backend sends the response.
5. Frontend displays the result.

### API Communication

React Frontend → API Request → Python Backend → API Response → React Frontend

## What is FastAPI?

FastAPI is a modern Python web framework used to build APIs and backend applications.

### Why FastAPI?

- Build REST APIs.
- Deploy Machine Learning models.
- Build Deep Learning applications.
- Connect LLM models.
- Develop RAG applications.
- Upload images, videos and documents.
- Connect React frontend with Python backend.

### What is Uvicorn?

Uvicorn is an ASGI server used to run FastAPI applications.

| Technology | Purpose |
|---|---|
| Python | Programming language |
| FastAPI | Backend framework |
| Uvicorn | Runs FastAPI server |
| React | Frontend development |
| API | Application communication |
| Database | Stores application data |

### First FastAPI Application

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Welcome to FastAPI",
        "status": "Success"
    }
```

Run:

```bash
python -m uvicorn app.main:app --reload
```

Useful URLs:

- `/` – Main endpoint
- `/docs` – Swagger API documentation

---

# DAY 1 – FASTAPI FUNDAMENTALS

## Topics
1. What is API?
2. What is REST API?
3. What is FastAPI?
4. What is Uvicorn?
5. FastAPI application creation.
6. First API endpoint.
7. TestClient.

## What is an Endpoint?

An endpoint is a specific URL where an API can receive requests.

Example:

```python
@app.get("/")
def home():
    return {"message": "Welcome"}
```

Here:
- `/` is the endpoint.
- `GET` is the HTTP method.
- `home()` is the function.
- `return` sends the response.

## What is TestClient?

TestClient allows us to test FastAPI endpoints directly from Python without starting a separate server.

```python
from fastapi.testclient import TestClient

client = TestClient(app)

response = client.get("/")

print(response.status_code)
print(response.json())
```

Expected output:

```text
200
{'message': 'Welcome'}
```

## Real-world Example

Create a welcome API for an AI application.

```python
@app.get("/welcome")
def welcome():
    return {
        "application": "Aivora AI",
        "message": "Welcome to AI Application"
    }
```

---

# DAY 2 – HTTP METHODS

## What are HTTP Methods?

HTTP methods define what action the client wants to perform on the server.

There are five important methods.

| Method | Purpose | Example |
|---|---|---|
| GET | Retrieve data | Get student details |
| POST | Create data | Register student |
| PUT | Replace data | Update student |
| PATCH | Partially update data | Update student age |
| DELETE | Delete data | Delete student |

## 1. GET Method

GET retrieves information from the server.

```python
@app.get("/students")
def get_students():
    return {
        "students": ["Yusuf", "Rahul", "John"]
    }
```

Use case: Display all students.

## 2. POST Method

POST creates new information.

```python
from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int

@app.post("/students")
def create_student(student: Student):
    return {
        "message": "Student created",
        "student": student
    }
```

Use case: Register a new student.

## 3. PUT Method

PUT replaces an existing resource.

```python
@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    return {
        "message": "Student replaced",
        "id": student_id,
        "student": student
    }
```

## 4. PATCH Method

PATCH updates selected fields.

```python
@app.patch("/students/{student_id}")
def partial_update(student_id: int, age: int):
    return {
        "id": student_id,
        "updated_age": age
    }
```

## 5. DELETE Method

DELETE removes a resource.

```python
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    return {
        "message": "Student deleted",
        "id": student_id
    }
```

Important: These examples demonstrate endpoint structure. Real CRUD applications need database storage.

---

# DAY 3 – PATH PARAMETERS

## What are Path Parameters?

Path parameters are variables included directly in the URL.

Example:

```text
/students/101
/students/102
/students/103
```

Here, 101, 102 and 103 are student IDs.

## Why do we use them?

To access a particular resource using its unique identifier.

## Example

```python
@app.get("/students/{student_id}")
def get_student(student_id: int):

    return {
        "student_id": student_id,
        "message": "Student details"
    }
```

Request:

```text
/students/101
```

Response:

```json
{
    "student_id": 101,
    "message": "Student details"
}
```

## Multiple Path Parameters

```python
@app.get("/students/{student_id}/courses/{course_id}")
def get_course(student_id: int, course_id: int):

    return {
        "student_id": student_id,
        "course_id": course_id
    }
```

## Important Concepts

- Path parameters are part of the URL.
- They identify a particular resource.
- FastAPI supports type validation.
- Invalid integer values produce a validation error.

---

# DAY 4 – QUERY PARAMETERS

## What are Query Parameters?

Query parameters are additional values passed through the URL after `?`.

Example:

```text
/students?course=AI
```

Here:
- `?` starts the query parameters.
- `course` is the parameter name.
- `AI` is the parameter value.

## Why do we use Query Parameters?

- Searching.
- Filtering.
- Sorting.
- Pagination.
- Selecting specific information.

## Basic Example

```python
@app.get("/students")
def get_students(course: str):

    return {
        "selected_course": course
    }
```

Request:

```text
/students?course=AI
```

## Multiple Query Parameters

```python
@app.get("/search")
def search_students(course: str, city: str):

    return {
        "course": course,
        "city": city
    }
```

Request:

```text
/search?course=AI&city=Hyderabad
```

## Optional Query Parameters

```python
@app.get("/products")
def get_products(category: str = "electronics"):

    return {
        "category": category
    }
```

If the user does not provide a category, the default value is used.

## Path vs Query Parameters

| Path Parameter | Query Parameter |
|---|---|
| Part of URL path | Added after `?` |
| Identifies a resource | Filters or modifies results |
| `/users/10` | `/users?city=Hyderabad` |

---

# DAY 5 – REQUEST BODY AND PYDANTIC

## What is a Request Body?

A request body contains data sent by the client to the backend.

Example: User registration form.

```json
{
    "name": "Yusuf",
    "age": 23,
    "course": "AI"
}
```

## What is Pydantic?

Pydantic is a Python library used for data validation and parsing.

FastAPI uses Pydantic models to validate request data.

## Why do we use Pydantic?

- Validate input data.
- Define required fields.
- Check data types.
- Set default values.
- Define nested data structures.

## Create Pydantic Model

```python
from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int
    course: str
```

Explanation:

- `BaseModel` is the base class.
- `name: str` means name must be a string.
- `age: int` means age must be an integer.
- `course: str` means course must be a string.

## POST API

```python
@app.post("/students")
def create_student(student: Student):

    return {
        "message": "Student registered",
        "student_name": student.name,
        "student_age": student.age,
        "course": student.course
    }
```

## Optional Field

```python
class Student(BaseModel):
    name: str
    age: int
    city: str | None = None
```

Here, city is optional.

## Real-world Example

Registration form:

Frontend sends name, age and course.

FastAPI receives the data.

Pydantic validates it.

If the data is valid, the function executes.

If the data is invalid, FastAPI returns a validation error.

---

# DAY 6 – RESPONSE MODELS

## What is a Response Model?

A response model defines the structure of data returned by an API.

## Why do we use it?

- Maintain consistent responses.
- Validate output data.
- Control which fields are returned.
- Improve API documentation.

## Example

```python
from pydantic import BaseModel

class StudentResponse(BaseModel):
    name: str
    age: int
    course: str
```

```python
@app.get("/student", response_model=StudentResponse)
def get_student():

    return {
        "name": "Yusuf",
        "age": 23,
        "course": "AI"
    }
```

## Response Model vs Request Model

| Request Model | Response Model |
|---|---|
| Validates incoming data | Defines outgoing data |
| Client to backend | Backend to client |
| Used with request body | Used with response_model |

## Status Codes

| Code | Meaning |
|---|---|
| 200 | OK |
| 201 | Created |
| 204 | No Content |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 422 | Validation Error |
| 500 | Internal Server Error |

## Example – Custom Status Code

```python
from fastapi import status

@app.post("/students", status_code=status.HTTP_201_CREATED)
def create_student(student: Student):
    return {
        "message": "Student created"
    }
```

---

# DAY 7 – ERROR HANDLING

## What is Error Handling?

Error handling is the process of managing errors that occur during application execution.

## Why do we need it?

- Prevent unexpected application failures.
- Return meaningful error messages.
- Handle missing resources.
- Improve application reliability.

## What is HTTPException?

FastAPI provides HTTPException to return HTTP error responses.

## Example

```python
from fastapi import HTTPException

@app.get("/students/{student_id}")
def get_student(student_id: int):

    if student_id != 101:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "student_id": student_id,
        "name": "Yusuf"
    }
```

## Explanation

`raise HTTPException()` stops normal execution and returns an error response.

Example:

```json
{
    "detail": "Student not found"
}
```

Status code:

```text
404 Not Found
```

## Common Errors

- 400 – Invalid request.
- 401 – Authentication required.
- 403 – Access forbidden.
- 404 – Resource not found.
- 500 – Server error.

## Real-world Example

In an AI application, if a user requests an unavailable video, the backend can return a 404 error instead of failing unexpectedly.

---

# DAY 8 – FILE UPLOAD

## What is File Upload?

File upload allows clients to send files to the backend.

Supported examples:

- Images.
- Videos.
- PDFs.
- Documents.
- Audio files.

## Why do we use it?

GenAI and Computer Vision applications need user-provided files for analysis.

Example:

Aivora AI:

User uploads video → FastAPI receives video → AI analyzes video → Backend returns results.

## Required Library

```bash
pip install python-multipart
```

## UploadFile

FastAPI provides UploadFile for handling uploaded files.

## Example

```python
from fastapi import UploadFile, File

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    return {
        "filename": file.filename,
        "content_type": file.content_type
    }
```

## Explanation

- `UploadFile` represents an uploaded file.
- `File(...)` makes the file required.
- `file.filename` returns the filename.
- `file.content_type` returns the MIME type.
- `async` allows asynchronous request handling.

## Reading File Content

```python
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    content = await file.read()

    return {
        "filename": file.filename,
        "file_size": len(content)
    }
```

Important: Production applications should validate file size and file type, generate safe storage names, and avoid trusting user-provided filenames.

---

# DAY 9 – DATABASE INTEGRATION

## What is a Database?

A database stores application information permanently.

Example:

A student management application stores:

- Student ID.
- Name.
- Age.
- Course.
- Email.

## Why do we need a Database?

Without a database, information stored only in Python variables may disappear when the application restarts.

Database provides persistent storage.

## What is SQLite?

SQLite is a lightweight relational database.

It stores data in a local database file.

## What is SQLAlchemy?

SQLAlchemy is a Python SQL toolkit and ORM.

ORM stands for Object Relational Mapping.

It allows us to interact with database tables using Python objects.

## Installation

```bash
pip install sqlalchemy
```

## Basic SQLite Connection

```python
from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///./students.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

print("Database connected")
```

## Database Operations – CRUD

| Operation | Meaning |
|---|---|
| Create | Insert new data |
| Read | Retrieve data |
| Update | Modify existing data |
| Delete | Remove data |

## Real-world Example

Student registration:

1. User submits registration form.
2. FastAPI validates data.
3. Backend saves student in database.
4. Application retrieves student information when needed.

---

# DAY 10 – AUTHENTICATION AND JWT

## What is Authentication?

Authentication verifies the identity of a user.

Example:

User logs in using email and password.

The application verifies the credentials.

## What is Authorization?

Authorization determines what an authenticated user is allowed to access.

Example:

- Admin can manage all users.
- Normal user can access only permitted resources.

## Authentication vs Authorization

| Authentication | Authorization |
|---|---|
| Who are you? | What can you access? |
| Verifies identity | Checks permissions |
| Login | Access control |

## What is Password Hashing?

Password hashing converts a password into a one-way hash representation.

We should not store plain-text passwords.

## What is JWT?

JWT stands for JSON Web Token.

JWT is commonly used to represent authenticated claims between a client and server.

## JWT Structure

JWT contains three parts:

1. Header.
2. Payload.
3. Signature.

Format:

```text
header.payload.signature
```

## Authentication Flow

1. User submits login credentials.
2. Backend verifies password.
3. Backend creates a signed token.
4. Client stores the token securely.
5. Client sends token with protected requests.
6. Backend validates the token.

## Important Security Practices

- Never store plain-text passwords.
- Use a suitable password hashing algorithm.
- Keep signing secrets outside source code.
- Validate token expiration.
- Use HTTPS in production.
- Apply authorization checks.

---

# DAY 11 – ADVANCED FASTAPI

## Topics

1. Async and Await.
2. Middleware.
3. Dependency Injection.
4. Background Tasks.
5. Environment Variables.

## 1. What is Async?

Async programming allows an application to handle waiting operations efficiently.

Example:

When an API waits for an external AI model response, asynchronous execution can help handle other requests while waiting.

## Example

```python
import asyncio

@app.get("/async")
async def async_example():

    await asyncio.sleep(2)

    return {
        "message": "Async operation completed"
    }
```

### What is Await?

`await` pauses the current coroutine until the awaited operation completes, allowing the event loop to run other tasks.

Important: Async does not automatically make CPU-heavy work faster.

## 2. What is Middleware?

Middleware is code that runs during request and response processing.

Example uses:

- Logging.
- Request timing.
- Security headers.
- CORS configuration.

## 3. What is Dependency Injection?

Dependency Injection allows FastAPI to provide reusable dependencies to endpoint functions.

Example:

```python
from fastapi import Depends

def get_database():
    return "Database connection"

@app.get("/data")
def get_data(db=Depends(get_database)):

    return {
        "database": db
    }
```

## 4. Background Tasks

Background tasks execute work after a response is returned.

Example use cases:

- Sending notifications.
- Logging.
- Small background processing tasks.

For long-running or resource-intensive jobs, a dedicated task queue may be more suitable.

---

# DAY 12 – LLM INTEGRATION WITH FASTAPI

## What is an LLM?

LLM stands for Large Language Model.

LLMs are AI models trained on large amounts of text to understand and generate language.

Examples:

- GPT.
- Llama.
- Gemini.
- Claude.

## Why connect LLM with FastAPI?

FastAPI exposes an LLM through an API.

A frontend can send a question to the backend, and the backend can call the LLM and return its answer.

## Architecture

React Frontend → FastAPI → LLM API → FastAPI → React Frontend

## Example – LLM API Structure

```python
from pydantic import BaseModel

class Question(BaseModel):
    prompt: str

@app.post("/ask")
def ask_question(question: Question):

    return {
        "question": question.prompt,
        "message": "LLM integration will be added here"
    }
```

This example creates the API structure. It does not call a real LLM yet.

## Actual LLM Integration Flow

1. Receive user prompt.
2. Validate request.
3. Send prompt to LLM provider.
4. Receive generated response.
5. Return response to frontend.

## Important Concepts

- API Keys.
- Environment Variables.
- Prompt Engineering.
- LLM API Calls.
- Error Handling.
- Rate Limits.
- Token Usage.

## Real-world Example

User asks:

"What is Machine Learning?"

FastAPI receives the question.

LLM generates an answer.

FastAPI returns the answer as JSON.

---

# DAY 13 – REACT + FASTAPI INTEGRATION

## What is React?

React is a JavaScript library used to build user interfaces.

## Why React + FastAPI?

React handles frontend UI.

FastAPI handles backend logic.

Together they can build complete AI web applications.

## Architecture

React → HTTP Request → FastAPI → Database / AI Model

FastAPI → JSON Response → React

## What is CORS?

CORS stands for Cross-Origin Resource Sharing.

It controls whether a browser allows frontend code from one origin to access a different origin.

Example:

React frontend:

```text
http://localhost:5173
```

FastAPI backend:

```text
http://localhost:8000
```

These are different origins.

## Enable CORS in FastAPI

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
```

## React API Request Example

```javascript
async function getData() {

    const response = await fetch(
        "http://127.0.0.1:8000/"
    );

    const data = await response.json();

    console.log(data);
}
```

## Real-world Example

User clicks an Analyze button in React.

React sends the video to FastAPI.

FastAPI processes the video using an AI model.

Backend returns analysis results.

React displays the results.

---

# DAY 14 – FINAL GENAI BACKEND PROJECT

## Project: AI Question Answering Application

### Objective

Build a complete AI application using React, FastAPI and an LLM.

## Technologies

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| FastAPI | API development |
| React | Frontend |
| LLM | AI response generation |
| Pydantic | Input validation |
| SQLite | Data storage |
| Uvicorn | Backend server |

## Project Architecture

User → React UI → FastAPI → LLM → FastAPI → React UI

## Project Features

1. User interface.
2. Question input.
3. API request.
4. Input validation.
5. LLM integration.
6. AI response.
7. Error handling.
8. Conversation history.
9. Database storage.
10. API documentation.

## Example API

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Question(BaseModel):
    prompt: str

@app.get("/")
def home():

    return {
        "message": "Welcome to AI Assistant"
    }

@app.post("/ask")
def ask(question: Question):

    return {
        "question": question.prompt,
        "answer": "Connect your LLM here"
    }
```

This is the initial API structure. The final project will connect an actual LLM and database.

## Final Learning Outcome

After completing these 14 days, you should be able to:

- Create REST APIs.
- Build backend applications.
- Handle HTTP requests.
- Validate incoming data.
- Manage API responses.
- Handle errors.
- Upload files.
- Connect databases.
- Implement authentication.
- Use asynchronous endpoints.
- Integrate LLMs.
- Connect React with FastAPI.
- Build a GenAI backend application.

---

# COMPLETE 14-DAY ROADMAP

| Day | Topic | Main Outcome |
|---|---|---|
| 01 | FastAPI Fundamentals | First API |
| 02 | HTTP Methods | GET, POST, PUT, PATCH, DELETE |
| 03 | Path Parameters | Dynamic URLs |
| 04 | Query Parameters | Search and filtering |
| 05 | Pydantic | Input validation |
| 06 | Response Models | Structured responses |
| 07 | Error Handling | API error management |
| 08 | File Upload | Images and videos |
| 09 | Database | SQLAlchemy and CRUD |
| 10 | Authentication | Password hashing and JWT |
| 11 | Advanced FastAPI | Async, Middleware, Dependencies |
| 12 | LLM Integration | AI API |
| 13 | React Integration | Frontend + Backend |
| 14 | Final Project | Complete GenAI application |

---

# LEARNING RULES

1. Understand the theory before writing code.
2. Understand why each concept is used.
3. Write code independently after understanding examples.
4. Execute every code cell.
5. Check expected outputs.
6. Practice real-world examples.
7. Complete daily exercises.
8. Revise previous concepts before moving forward.

**Final Goal:** Become capable of building production-oriented Python APIs and integrating AI/LLM applications using FastAPI.

** AUTHOR ** 
SHAIK YUSUFVALI