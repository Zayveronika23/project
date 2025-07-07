from fastapi import FastAPI
from .api.routes.users import router as users_router
app = FastAPI()
app.include_router(users_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
