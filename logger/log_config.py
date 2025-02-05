import logging
import os

# Ensure the 'logs' directory exists
if not os.path.exists('logs'):
    os.makedirs('logs')

def setup_logging():
    logger = logging.getLogger('my_logger')
    
    # Check if handlers are already added to prevent duplicate logging
    if not logger.hasHandlers():
        logger.setLevel(logging.DEBUG)

        # Create a file handler that logs to 'logs/app.log'
        file_handler = logging.FileHandler('logs/app.log')
        file_handler.setLevel(logging.DEBUG)

        # Create a console handler that logs to the console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)  # You can adjust this level

        # Set up the log format
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add both handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

   
