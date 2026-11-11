# file_utils.py

import hashlib
import os
from datetime import datetime
from pathlib import Path


class FileUtils:

    @staticmethod
    def get_file_size(file_path):
        """
        Returns file size in KB.
        """
        try:
            size = os.path.getsize(file_path)
            return round(size / 1024, 2)

        except FileNotFoundError:
            return 0

        except PermissionError:
            return 0

        except OSError:
            return 0

    @staticmethod
    def get_modified_date(file_path):
        """
        Returns the last modified date of a file.
        """
        try:
            timestamp = os.path.getmtime(file_path)

            return datetime.fromtimestamp(
                timestamp
            ).strftime("%Y-%m-%d %H:%M:%S")

        except FileNotFoundError:
            return "File not found"

        except PermissionError:
            return "Permission denied"

        except OSError:
            return "Unable to read"

    @staticmethod
    def get_md5_hash(file_path):
        """
        Calculates MD5 hash of a file.
        """

        md5 = hashlib.md5()

        try:
            with open(file_path, "rb") as file:

                while True:
                    data = file.read(4096)

                    if not data:
                        break

                    md5.update(data)

            return md5.hexdigest()

        except FileNotFoundError:
            return None

        except PermissionError:
            return None

        except OSError:
            return None

    @staticmethod
    def get_extension(file_path):
        """
        Returns the file extension.
        """
        return Path(file_path).suffix.lower()