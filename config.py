# config.py

from pathlib import Path


BASE_FOLDER = Path(__file__).parent

ORGANIZED_FOLDER = BASE_FOLDER / "organized_files"


FILE_CATEGORIES = {
    ".pdf": "PDF",

    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    ".webp": "Images",

    ".xls": "Excel",
    ".xlsx": "Excel",
    ".csv": "Excel",

    ".py": "Python",

    ".txt": "Others",
    ".doc": "Others",
    ".docx": "Others",
    ".zip": "Others",
    ".rar": "Others"
}