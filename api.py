# api.py

from pathlib import Path

from fastapi import FastAPI, HTTPException

from file_utils import FileUtils
from config import ORGANIZED_FOLDER


app = FastAPI(
    title="Smart File Organizer API",
    description="API for retrieving organized file information"
)


@app.get("/")
def home():

    return {
        "message": "Smart File Organizer API is running"
    }


@app.get("/files")
def get_files():

    if not ORGANIZED_FOLDER.exists():

        return {
            "total_files": 0,
            "files": [],
            "message": "No organized files found"
        }

    result = []

    try:

        for category_folder in ORGANIZED_FOLDER.iterdir():

            if not category_folder.is_dir():
                continue

            for file_path in category_folder.iterdir():

                if not file_path.is_file():
                    continue

                result.append({
                    "file_name": file_path.name,
                    "category": category_folder.name,
                    "extension": FileUtils.get_extension(
                        file_path
                    ),
                    "size_kb": FileUtils.get_file_size(
                        file_path
                    ),
                    "modified_date":
                        FileUtils.get_modified_date(
                            file_path
                        )
                })

        return {
            "total_files": len(result),
            "files": result
        }

    except PermissionError:

        raise HTTPException(
            status_code=403,
            detail="Permission denied"
        )

    except OSError as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )