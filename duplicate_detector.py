# duplicate_detector.py

from collections import defaultdict
from pathlib import Path

from file_utils import FileUtils


class DuplicateDetector:

    def __init__(self, folder):
        self.folder = Path(folder)

    def find_duplicates(self):

        hash_groups = defaultdict(list)

        try:

            for file_path in self.folder.iterdir():

                if not file_path.is_file():
                    continue

                file_hash = FileUtils.get_md5_hash(file_path)

                if file_hash is not None:
                    hash_groups[file_hash].append(file_path)

        except FileNotFoundError:
            print("\nError: Folder does not exist.")

        except PermissionError:
            print("\nError: Permission denied while reading folder.")

        except OSError as error:
            print(f"\nError reading folder: {error}")

        duplicates = {}

        for file_hash, files in hash_groups.items():

            if len(files) > 1:
                duplicates[file_hash] = files

        return duplicates

    def display_duplicates(self):

        duplicates = self.find_duplicates()

        if not duplicates:
            print("\nNo duplicate files found.")
            return

        print("\n========== DUPLICATE FILES ==========")

        duplicate_number = 1

        for file_hash, files in duplicates.items():

            print(f"\nDuplicate Group {duplicate_number}")
            print(f"MD5 Hash: {file_hash}")

            for file in files:
                print(f"  - {file.name}")

            duplicate_number += 1