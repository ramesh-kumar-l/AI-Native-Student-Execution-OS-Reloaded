# API Contracts

## Base Path
- Backend API base: `/api`
- Versioning: `/api/v1`

## Endpoints

### Health Check

#### `GET /api/health/live`
- Description: Liveness probe. Returns immediately if HTTP server is running.
- Response (200 OK):
```json
{
  "status": "alive"
}
```

#### `GET /api/health/ready`
- Description: Readiness probe. Performs basic checks on database and Redis connections.
- Response (200 OK or 503 Service Unavailable):
```json
{
  "status": "ready",
  "checks": {
    "database": "healthy",
    "redis": "healthy"
  }
}
```

---

### Authentication

#### `POST /api/v1/auth/register`
- Description: Register a new user and triggers Resend verification email.
- Request Body:
```json
{
  "email": "student@example.com",
  "password": "secure_password_123",
  "full_name": "Jane Doe"
}
```
- Response (201 Created):
```json
{
  "id": "uuid-v4-string",
  "email": "student@example.com",
  "full_name": "Jane Doe",
  "email_verified": false,
  "message": "Verification email sent."
}
```

#### `GET /api/v1/auth/verify-email`
- Description: Verify email address using query token.
- Query Parameters: `token=<string>`
- Response (200 OK):
```json
{
  "status": "verified",
  "message": "Email successfully verified. You can now log in."
}
```

#### `POST /api/v1/auth/login`
- Description: Sign in with email and password. Returns tokens.
- Request Body:
```json
{
  "email": "student@example.com",
  "password": "secure_password_123"
}
```
- Response (200 OK):
```json
{
  "access_token": "jwt_token_string",
  "refresh_token": "refresh_token_string",
  "token_type": "bearer",
  "expires_in": 1800
}
```

#### `POST /api/v1/auth/google`
- Description: Verifies a Google sign-in ID token and logs in/registers user on the backend.
- Request Body:
```json
{
  "id_token": "google_oauth_id_token_string"
}
```
- Response (200 OK):
```json
{
  "access_token": "jwt_token_string",
  "refresh_token": "refresh_token_string",
  "token_type": "bearer",
  "expires_in": 1800
}
```

#### `POST /api/v1/auth/refresh`
- Description: Obtain a new access token using a valid refresh token.
- Request Body:
```json
{
  "refresh_token": "refresh_token_string"
}
```
- Response (200 OK):
```json
{
  "access_token": "jwt_token_string",
  "refresh_token": "refresh_token_string",
  "token_type": "bearer",
  "expires_in": 1800
}
```

#### `GET /api/v1/auth/me`
- Description: Get profile data for the authenticated user.
- Headers: `Authorization: Bearer <access_token>`
- Response (200 OK):
```json
{
  "id": "uuid-v4-string",
  "email": "student@example.com",
  "full_name": "Jane Doe",
  "role": "student",
  "avatar_url": null,
  "email_verified": true
}
```
