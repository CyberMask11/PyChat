# 🚀 Real-Time WebChat Application

This project is a full-stack real-time WebChat system built using FastAPI, WebSockets, and a Dockerized database. It demonstrates secure authentication, token-based session handling, and live messaging across network boundaries.

The application supports account creation (SignUp) and Login with securely hashed passwords, followed by JWT token generation using the HS256 algorithm. Tokens are required for WebSocket connections and are validated before a client is accepted into the chat session. User data is stored in a containerized database environment to simulate production-style separation between application and persistence layers.

The backend was fully designed and implemented by me using a clean layered architecture (Router → Service → Repository). The router handles HTTP and WebSocket endpoints, the service layer manages business logic and validation, and the repository layer interacts directly with the database. Real-time messaging is handled through a WebSocket connection manager that tracks active users and broadcasts messages accordingly while handling disconnections gracefully.

The frontend connects to the backend over separate ports and manages authentication state, token flow, and real-time UI updates. It includes login and signup screens, a live chat dashboard, user search functionality, connection status indicators, and a dark glass-style theme. While I do not specialize in frontend development yet, the UI was AI-assisted and fully integrated by me with the backend logic and real-time communication layer.

This project required handling cross-port communication, CORS configuration, public IP exposure, WebSocket token validation, and debugging real-world networking behavior such as NAT loopback and port forwarding. It reflects practical backend engineering beyond simple CRUD applications and demonstrates understanding of authentication flows, state management, and distributed communication.

Tech Stack: FastAPI · SQLAlchemy · WebSockets · JWT (HS256) · Docker · PostgreSQL · HTML · CSS · JavaScript

To run locally:

```bash
git clone https://github.com/YourUsername/your-repo.git
cd your-repo
docker compose up -d
uvicorn main:app --host 0.0.0.0 --port 8080 --reload
python -m http.server 9999
