# Task 1: Signup and Login

## Title:
Create APIs for User Signup and Login with JWT Authentication.

---

## Description:
As a user, I want to be able to create an account (signup) using my email and password, and then log in using those credentials to receive a secure JWT token.

---

## Acceptance Criteria:

### Signup API:
- The API should accept `email` and `password` in the request body.
- If the `email` is already registered, an appropriate error message should be returned.
- If the `email` is not registered, the credentials should be saved in the database, and a success message should be returned.

### Login API:
- The API should accept `email` and `password` in the request body.
- The API should validate the provided credentials against the database.
- If the credentials are correct, a JWT token containing the `email` should be generated and returned.
- If the credentials are incorrect, an appropriate error message should be returned.

---

## API Details:

### **Signup API**

#### Method:
- `POST`

#### Endpoint:
- `/api/v1/auth/signup/`

#### Request Body:
```json
{
  "email": "user@example.com",
  "password": "securepassword123"
}
```

### Response:
- Success:
```json
{
  "message": "User signed up successfully."
}
```

- Error:
```json
{
  "error": "Email is already registered."
}
```


### **Login API**

#### Method:
- `POST`

#### Endpoint:
- `/api/v1/auth/login/`

#### Request Body:
```json
{
  "email": "user@example.com",
  "password": "securepassword123"
}
```

### Response:
- Success:
```json
{
  "message": "Login successful.",
  "token": "jwt-token-string"
}
```

- Error:
```json
{
  "error": "Invalid email or password."
}
```


### Technical Notes

- Use Django REST Framework to implement the APIs.
- Use the PyJWT or djangorestframework-simplejwt library to generate and validate JWT tokens.
- Ensure email uniqueness in the database.

### Deliverables:
- Source code for both APIs (Signup and Login).
Postman
- A Postman Collection file containing tests for the API.