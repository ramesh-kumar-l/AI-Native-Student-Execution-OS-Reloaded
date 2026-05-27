# Data Models

## Relational Models (PostgreSQL 16)

### User Table (`users`)
Stores user accounts, authentication types, and verification status.

```sql
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255),           -- NULL for OAuth-only users
    full_name VARCHAR(255) NOT NULL,
    avatar_url TEXT,
    auth_provider VARCHAR(50) DEFAULT 'credentials', -- credentials, google
    google_id VARCHAR(255) UNIQUE,        -- For Google OAuth accounts
    email_verified BOOLEAN DEFAULT FALSE, -- Must be TRUE to log in (if credentials)
    is_active BOOLEAN DEFAULT TRUE,
    role VARCHAR(50) DEFAULT 'student',   -- student, admin
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    last_login_at TIMESTAMPTZ
);

CREATE INDEX idx_users_email ON users(email);
```

### Verification Token Table (`verification_tokens`)
Stores tokens used for email verification and password resets.

```sql
CREATE TABLE verification_tokens (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    token VARCHAR(255) UNIQUE NOT NULL,
    token_type VARCHAR(50) NOT NULL,      -- email_verification, password_reset
    expires_at TIMESTAMPTZ NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_verification_tokens_token ON verification_tokens(token);
```

### Refresh Token Table (`refresh_tokens`)
Enables token rotation and user logout invalidation.

```sql
CREATE TABLE refresh_tokens (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    token VARCHAR(500) UNIQUE NOT NULL,
    is_revoked BOOLEAN DEFAULT FALSE,
    expires_at TIMESTAMPTZ NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
```
