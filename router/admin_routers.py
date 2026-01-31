from fastapi import APIRouter, Depends
from auth import admin_only

router = APIRouter()

@router.get("/admin")
def admin_route(current_user: dict = Depends(admin_only)):
    return {"message": f"Hello Admin {current_user['username']}"}
