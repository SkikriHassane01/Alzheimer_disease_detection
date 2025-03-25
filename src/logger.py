import logging 
import logging.handlers
from logging.handlers import RotatingFileHandler
import os 
import sys
from datetime import datetime
from pathlib import Path
import config

class AlzheimerLogger:
    """
    A custom logger for the Alzheimer's Disease classification project.
    """
    
    def __init__(self, log_dir = config.LOGS_DIR,
                 log_level = logging.INFO,
                 log_name: str = 'alzheimer',
                 max_file_size = 10* 1024 * 1024,
                 backup_count = 5):
        self.log_dir = log_dir if log_dir is not None else config.LOGS_DIR
        self.log_level = log_level
        
        # Create the log directory if it doesn't exist
        os.makedirs(self.log_dir, exist_ok=True)
        
        # generate  timestamp for this run 
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.log_file = os.path.join(self.log_dir, f"{log_name}_{self.timestamp}.log")
        
        # set up the logger 
        self.logger = logging.getLogger(log_name)
        self.logger.setLevel(self.log_level)
        self.logger.handlers = []
        
        self._setup_handlers(max_file_size, backup_count)
        
    def _setup_handlers(self, max_file_size, backup_count):
        
        # create a rotating file handler
        file_handler = RotatingFileHandler(
            self.log_file,
            maxBytes = max_file_size,
            backupCount= backup_count
        )
        file_handler.setLevel(self.log_level)
        
        # create a console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        
        # create a formatter
        file_formatter = logging.Formatter(
            '%(asctime)s | %(levelname)-8s | %(filename)s:%(lineno)d | %(message)s',
            datefmt="%Y%m%d %H:%M:%S",
        )
        
        console_formatter = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(message)s",
            datefmt="%H:%M:%S"
        )
        
        # set the formatters
        file_handler.setFormatter(file_formatter)
        console_handler.setFormatter(console_formatter)
        
        # add the handlers to the logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
        
    def get_logger(self):
        return self.logger
    
    def get_csv_logger(self, model_name = config.MODEL_NAME):
        """
        Create a CSV Logger callback to save training/validation metrics.

        Returns:
            tf.keras.callbacks.CSVLogger: Configured CSV Logger callback
        """
        
        # import tf here to avoid dependency if not needed
        from tensorflow.keras.callbacks import CSVLogger # type: ignore
        
        csv_log_file = os.path.join(self.log_dir, f"{model_name}_training_log_{self.timestamp}.csv")
        return CSVLogger(csv_log_file, separator=",", append=False)

    def log_model_summary(self, model):
        """
        Log the summary of a TensorFlow model architecture.
        
        Args:
            model: A TensorFlow/Keras model
        """
        # Capture model summary as a string
        model_summary_lines = []
        model.summary(print_fn=lambda x: model_summary_lines.append(x))
        
        # format the complete model summary string
        full_summary = ["Model Architecture Summary:", '-' * 80]
        full_summary.extend(model_summary_lines)
        full_summary.append('-' * 80)
        
        # log to the console
        for line in full_summary:
            self.logger.info(line)


def create_logger(log_level=logging.INFO):
    """
    Returns:
        logging.Logger: Configured logger instance
    """
    alzheimer_logger = AlzheimerLogger(log_level=log_level)
    return alzheimer_logger.get_logger()