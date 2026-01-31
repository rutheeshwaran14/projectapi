from fastapi import APIRouter

router = APIRouter()

@router.get("/User")
def add_data():
    return "hello world"