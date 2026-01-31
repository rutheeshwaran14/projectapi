from fastapi import FastAPI
from database import Base, engine
from router.auth_routers import router as auth_router
from router.users_routers import router as user_router
from router.admin_routers import router as admin_router
from router.put import router as add_data


Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI JWT MySQL Example")

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(admin_router)
app.include_router(add_data)

@app.get("/")
def server_start():
    return {"message": "Server is running"}
