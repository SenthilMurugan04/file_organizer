# main.py

from pathlib import Path

from file_organizer import FileOrganizer
from duplicate_detector import DuplicateDetector
from config import ORGANIZED_FOLDER


def print_header():

    print("\n==============================================")
    print("      SMART FILE ORGANIZER")
    print("      DUPLICATE FILE DETECTOR")
    print("==============================================")


def main():

    print_header()

    source_folder = input(
        "\nEnter the folder path to organize: "
    ).strip()

    source_path = Path(source_folder)

    if not source_path.exists():
        print("\nError: Folder does not exist.")
        return

    if not source_path.is_dir():
        print("\nError: The given path is not a folder.")
        return

    # Same folder used by FastAPI
    destination_folder = ORGANIZED_FOLDER

    organizer = FileOrganizer(
        source_path,
        destination_folder
    )

    organizer.create_folders()

    print("\nScanning files...")

    files = organizer.scan_files()

    organizer.display_files()

    if not files:
        print("\nNo files available.")
        return

    duplicate_detector = DuplicateDetector(
        source_path
    )

    duplicate_detector.display_duplicates()

    print("\n==============================================")
    print("Do you want to organize these files?")
    print("==============================================")

    organizer.move_files()

    print("\n==============================================")
    print("          PROCESS COMPLETED")
    print("==============================================")


if __name__ == "__main__":
    main()