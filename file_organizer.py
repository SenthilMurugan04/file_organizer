# file_organizer.py

import shutil
from pathlib import Path

from config import FILE_CATEGORIES
from file_utils import FileUtils


class FileOrganizer:

    def __init__(self, source_folder, destination_folder):

        self.source_folder = Path(source_folder)
        self.destination_folder = Path(destination_folder)

        self.file_information = []

    def create_folders(self):

        categories = [
            "PDF",
            "Images",
            "Excel",
            "Python",
            "Others"
        ]

        for category in categories:

            folder = self.destination_folder / category

            try:
                folder.mkdir(parents=True, exist_ok=True)

            except PermissionError:
                print(
                    f"Permission denied while creating {folder}"
                )

            except OSError as error:
                print(
                    f"Could not create folder {folder}: {error}"
                )

    def get_category(self, file_path):

        extension = FileUtils.get_extension(file_path)

        return FILE_CATEGORIES.get(extension, "Others")

    def get_unique_destination(self, destination_path):

        if not destination_path.exists():
            return destination_path

        original_name = destination_path.stem
        extension = destination_path.suffix

        counter = 1

        while True:

            new_name = (
                f"{original_name}_{counter}{extension}"
            )

            new_path = destination_path.parent / new_name

            if not new_path.exists():
                return new_path

            counter += 1

    def scan_files(self):

        self.file_information = []

        try:

            for file_path in self.source_folder.iterdir():

                if not file_path.is_file():
                    continue

                extension = FileUtils.get_extension(file_path)

                category = self.get_category(file_path)

                size = FileUtils.get_file_size(file_path)

                modified_date = FileUtils.get_modified_date(
                    file_path
                )

                file_hash = FileUtils.get_md5_hash(
                    file_path
                )

                information = {
                    "name": file_path.name,
                    "path": str(file_path),
                    "size_kb": size,
                    "extension": extension,
                    "category": category,
                    "modified_date": modified_date,
                    "md5": file_hash
                }

                self.file_information.append(information)

        except FileNotFoundError:
            print("\nError: Source folder does not exist.")

        except PermissionError:
            print("\nError: Permission denied.")

        except OSError as error:
            print(f"\nError scanning folder: {error}")

        return self.file_information

    def display_files(self):

        if not self.file_information:
            print("\nNo files found.")
            return

        print("\n================ FILE INFORMATION ================")

        for file in self.file_information:

            print(f"\nFile Name     : {file['name']}")
            print(f"Size          : {file['size_kb']} KB")
            print(f"Extension     : {file['extension']}")
            print(f"Category      : {file['category']}")
            print(f"Modified Date : {file['modified_date']}")
            print(f"MD5           : {file['md5']}")

    def move_files(self):

        if not self.file_information:
            print("\nNo files available to move.")
            return

        print("\nFiles will be moved according to their category.")

        confirmation = input(
            "\nDo you want to continue? (yes/no): "
        ).strip().lower()

        if confirmation not in ["yes", "y"]:
            print("\nFile moving cancelled.")
            return

        print("\n========== MOVING FILES ==========")

        for file in self.file_information:

            source = Path(file["path"])

            if not source.exists():
                print(
                    f"Skipped: {source.name} - file no longer exists."
                )
                continue

            category_folder = (
                self.destination_folder /
                file["category"]
            )

            try:

                category_folder.mkdir(
                    parents=True,
                    exist_ok=True
                )

                destination = (
                    category_folder /
                    source.name
                )

                # Prevent accidental overwrite
                destination = self.get_unique_destination(
                    destination
                )

                shutil.move(
                    str(source),
                    str(destination)
                )

                print(
                    f"Moved: {source.name} "
                    f"-> {category_folder.name}"
                )

            except FileNotFoundError:
                print(
                    f"Skipped: {source.name} - file not found."
                )

            except PermissionError:
                print(
                    f"Permission denied: {source.name}"
                )

            except shutil.Error as error:
                print(
                    f"Could not move {source.name}: {error}"
                )

            except OSError as error:
                print(
                    f"OS error for {source.name}: {error}"
                )