import PyPDF2
import docx
import os
from logger.log_config import setup_logging
# Set up logging
logger = setup_logging()

# Extract text from PDF
def extract_pdf_text(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()
        logger.info("text extrcation done")
    return text

# Extract text from DOCX
def extract_docx_text(docx_path):
    doc = docx.Document(docx_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    logger.info("text extrcation done")
    return text

# Extract text from TXT
def extract_txt_text(txt_path):
    with open(txt_path, "r") as file:
        text = file.read()
    logger.info("text extrcation done")
    return text


def get_file_name(file_path):
    # Extract filename from the given file path
    filename = os.path.basename(file_path)
    return filename


def write_extracted_data(data, filename, folder='extracted_data'):
    """
    Write the extracted data to a file in the specified folder.
    
    :param data: The data to write to the file.
    :param filename: The name of the file to create (including the extension).
    :param folder: The folder where the file will be stored.
    """
    # Check if the folder exists, if not, create it
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    # Define the path to save the file
    file_path = os.path.join(folder, filename)
    
    try:
        # Open the file and write the data
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(data)
        print(f"Data successfully written to {file_path}")
    except Exception as e:
        print(f"Error writing to file {file_path}: {e}")

# Example usage in your main function

