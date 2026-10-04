from fastapi import APIRouter

router = APIRouter()

@router.post("/images")
def image_upload():
    return {"status": "ok"}
