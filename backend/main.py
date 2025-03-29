from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
import json

from .database import Base, engine
from .routes import auth, cep, user, billing  

# === Inicializa a aplicação ===
app = FastAPI(
    title="Consulta de CEP",
    description="API com autenticação, cobrança por consulta e gerenciamento de usuários",
    version="1.0.0"
)

# === Cria as tabelas no banco ===
Base.metadata.create_all(bind=engine)

# === CORS (libera front-end para acessar) ===
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === Middleware para respostas padronizadas ===
class StandardizeResponseMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.url.path.startswith("/docs") or request.url.path.startswith("/redoc") or request.url.path.startswith("/openapi"):
            return await call_next(request)

        response = await call_next(request)

        if response.status_code < 400 and "application/json" in response.headers.get("content-type", ""):
            # Lê o corpo da resposta original
            body = b""
            async for chunk in response.body_iterator:
                body += chunk

            try:
                data = json.loads(body)
            except Exception:
                data = body.decode()

            new_body = json.dumps({
                "success": True,
                "status_code": response.status_code,
                "data": data
            })

            new_response = JSONResponse(content=json.loads(new_body), status_code=response.status_code)
            for key, value in response.headers.items():
                if key.lower() != "content-length":
                    new_response.headers[key] = value
            return new_response

        return response

app.add_middleware(StandardizeResponseMiddleware)

# === Registra as rotas ===
app.include_router(auth.router)
app.include_router(cep.router)
app.include_router(user.router)
app.include_router(billing.router)
