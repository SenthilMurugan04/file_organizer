# Smart File Organizer & Duplicate Detector

## Project Description

Smart File Organizer & Duplicate Detector is a Python application that automatically organizes files based on their extensions and identifies duplicate files using MD5 hashing.

The application also displays file information such as file name, size, extension and modified date.

## Technologies Used

- Python
- pathlib
- os
- shutil
- hashlib
- FastAPI
- Uvicorn

## Features

1. Automatically organizes files.
2. Creates folders based on file categories.
3. Supports PDF files.
4. Supports image files.
5. Supports Excel files.
6. Supports Python files.
7. Identifies duplicate files.
8. Uses MD5 hashing.
9. Displays file size.
10. Displays modified date.
11. Handles missing files.
12. Handles permission errors.
13. Prevents accidental file overwriting.
14. Requests user confirmation before moving files.
15. Provides FastAPI endpoint for file information.

## File Categories

| Extension | Category |
|----------|----------|
| .pdf | PDF |
| .jpg | Images |
| .jpeg | Images |
| .png | Images |
| .gif | Images |
| .xls | Excel |
| .xlsx | Excel |
| .csv | Excel |
| .py | Python |
| Other extensions | Others |

## Project Structure

```text
smart_file_organizer/
│
├── main.py
├── file_organizer.py
├── duplicate_detector.py
├── file_utils.py
├── config.py
├── api.py
├── requirements.txt
└── README.md