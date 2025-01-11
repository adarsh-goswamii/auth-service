from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import uvicorn
from configs.env import get_settings
from fastapi.middleware.gzip import GZipMiddleware
from src.routes.v1 import main as v1_routes

config = get_settings()

if config.env == "local":
  print("Server starting")
  
app = FastAPI(
  title="Auth service",
  description=""
)

# register_handlers(app)

@app.on_event("startup")
async def startup_event():
  # do something
  print("Server started")
  
@app.on_event("shutdown")
async def shutdown_event():
  # do something
  print("Server stopped")
  
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)

app.add_middleware(GZipMiddleware, minimum_size=1000)

app.include_router(v1_routes.api_router)

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=4001)
  
