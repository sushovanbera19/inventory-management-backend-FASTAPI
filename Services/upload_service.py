from pathlib import Path

# Find the main project folder
BASE_DIR = Path(__file__).resolve().parent.parent

def get_upload_folder(folder_name: str):
    folder_path = BASE_DIR / "uploads" / folder_name

    # Automatically create the folder if it doesn't exist
    folder_path.mkdir(parents=True, exist_ok=True)

    return folder_path