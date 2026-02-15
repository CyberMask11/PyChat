# 🚀 Real-Time WebChat Application

I built a real-time chat system from scratch — not just a messaging UI, but the full backend architecture that powers it.

This project includes secure account creation (SignUp & Login), password hashing, JWT-based authentication (HS256), and live global messaging using WebSockets. Every WebSocket connection requires a valid token before being accepted, meaning authentication isn’t just for HTTP — it protects real-time communication too.

User data is stored inside a Dockerized database container, separating application logic from persistence just like a production environment would. The backend follows a clean layered architecture (Router → Service → Repository), keeping business logic structured and maintainable instead of mixing everything together.

The real-time chat system manages active connections, broadcasts messages globally, and gracefully handles disconnects. No polling. No refresh spam. Just live communication.

The frontend includes:
• Login & Signup screens  
• Real-time global chat dashboard  
• Connection status indicator  
• User search functionality  
• Dark red / black / purple glass-style theme  

I don’t specialize in frontend development yet, so the UI was AI-assisted — but the integration, authentication flow, networking logic, deployment setup, and real-time system design were fully implemented by me.

This project pushed me beyond simple CRUD apps and into real-world challenges like:
• Cross-port frontend/backend communication  
• Public IP exposure and port forwarding  
• NAT loopback behavior  
• CORS configuration  
• WebSocket token validation  
• Debugging networking issues that don’t show up in tutorials  

Tech Stack: FastAPI · SQLAlchemy · WebSockets · JWT · Docker · PostgreSQL · HTML · CSS · JavaScript

To run locally:

```bash
git clone https://github.com/YourUsername/your-repo.git
cd your-repo
docker compose up -d
uvicorn main:app --host 0.0.0.0 --port 8080 --reload
python -m http.server 9999
