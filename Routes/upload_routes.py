from fastapi import APIRouter, UploadFile, File, HTTPException
from Services.upload_service import get_upload_folder
import uuid

router = APIRouter(
    prefix="/uploads",
    tags=["Image Upload"]
)

# Allowed image formats
ALLOWED_TYPES = {
    "image/jpeg": ".jpg",
    "image/png": ".png",
    "image/webp": ".webp",
    "image/gif": ".gif"
}

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB


@router.post("/categories")
async def upload_category_image(file: UploadFile = File(...)):

    # Check image format
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Only JPG, PNG, WEBP and GIF images are allowed"
        )

    # Read image
    image_data = await file.read(MAX_FILE_SIZE + 1)

    # Check image size
    if len(image_data) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail="Image size must not exceed 5 MB"
        )

    # Get or automatically create categories folder
    folder_path = get_upload_folder("categories")

    # Generate a unique filename
    extension = ALLOWED_TYPES[file.content_type]
    filename = f"{uuid.uuid4().hex}{extension}"

    # Save image
    file_path = folder_path / filename
    file_path.write_bytes(image_data)

    # Return image URL
    return {
        "message": "Category image uploaded successfully",
        "imageUrl": f"/uploads/categories/{filename}"
    }