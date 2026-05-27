# Security Model

## Authentication & Authorization
1. **Next.js Session Layer**: NextAuth.js (Auth.js) v5 runs on the edge/Node server. It coordinates OAuth flows and credentials login.
2. **FastAPI Resource Layer**: Protects API endpoints using standard bearer token verification.
   - Access token: HMAC SHA256 (`HS256`) signed with a shared key. Expires in 30 minutes.
   - Refresh token: Stored in backend database. Rotation happens on refresh, or expires in 7 days.
3. **Password Security**: Argon2 via `pwdlib[argon2]` using recommended parameters to hash user passwords.
4. **Email Verification**: Registrants using credentials must verify their email via Resend before their accounts are marked as active.

## Web Security & CORS
- **CORS Configuration**: Explicit origin matching in backend:
  - Allowed origin in dev: `http://localhost:3000` (Next.js server).
  - Credentials (`allow_credentials=True`) allowed.
  - Allowed headers: `Content-Type`, `Authorization`, `X-Request-ID`.
- **Session Protection**: NextAuth cookies are set to `SameSite=Lax` or `Strict` and `Secure`.
- **Docker Isolation**: Database credentials are not exposed to host ports directly unless configured. They reside safely in the internal docker bridge network.
