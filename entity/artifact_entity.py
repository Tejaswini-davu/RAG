import os
import shutil
from dataclasses import dataclass
from logger.log_config import setup_logging
import re
# Set up logging
logger = setup_logging()

@dataclass
class ArtifactEntity:
    folder_name: str = "extracted_data"  # Change folder name to 'extracted_data'

    def __post_init__(self):
        # Ensure the folder exists
        if not os.path.exists(self.folder_name):
            os.makedirs(self.folder_name)
            print(f"Folder '{self.folder_name}' created.")
        else:
            print(f"Folder '{self.folder_name}' already exists.")
    
    # Method to store files in the 'extracted_data' folder
    def store_file(self, file_name: str, content: str):
        # Construct the file path inside the extracted_data folder
        file_path = os.path.join(self.folder_name, file_name)
        
        with open(file_path, "w") as file:
            file.write(content)
        print(f"File '{file_name}' stored in '{self.folder_name}' folder.")

   


def get_file_name(self, file_path):
    # Extract the file name without extension
    file_name = os.path.splitext(os.path.basename(file_path))[0]

    # Strip any leading/trailing spaces from the file name
    file_name = file_name.strip()

    # Ensure that the file name is not empty
    if not file_name:
        raise ValueError("File name is empty after extraction!")

    # Sanitize the file name to only include lowercase alphanumeric characters and hyphens
    sanitized_file_name = re.sub(r'[^a-z0-9-]', '-', file_name.lower())

    # Ensure the name consists of lowercase alphanumeric characters and hyphens
    sanitized_file_name = sanitized_file_name.replace(" ", "-")

    # Print the sanitized file name for debugging purposes
    print(f"Sanitized file name: {sanitized_file_name}")

    return sanitized_file_name

# def get_file_name(self, file_path):
#     # Extract the file name without extension
#     return os.path.splitext(os.path.basename(file_path))[0]
#     logger.info("embedding are done")


# Method to store a source file in the 'extracted_data' folder
# def store_file_from_path(self, source_file_path: str):
#     # Copy the file to the 'extracted_data' folder
#     file_name = os.path.basename(source_file_path)
#     destination_file_path = os.path.join(self.folder_name, file_name)
    
#     shutil.copy(source_file_path, destination_file_path)
#     print(f"File '{file_name}' copied to '{self.folder_name}' folder.")
