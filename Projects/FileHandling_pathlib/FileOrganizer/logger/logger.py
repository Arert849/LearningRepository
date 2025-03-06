import logging
from pathlib import Path
from colorama import Fore, Style
from logging.handlers import RotatingFileHandler


# Color dictionary
COLORS = {
    "DEBUG": Fore.GREEN,
    "INFO": Fore.BLUE,
    "WARNING": Fore.YELLOW,
    "ERROR": Fore.RED,
    "CRITICAL": Fore.MAGENTA + Style.BRIGHT
}


class ColorFormatter(logging.Formatter):
    def format(self, record):
        log_color = COLORS.get(record.levelname, "")
        reset = Style.RESET_ALL
        message = super().format(record)
        return f"{log_color}{message}{reset}"


def get_logger(name="app", folder="logs"):
    """ Returns a configured logger instance """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Log folder path
    path = Path(folder)
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)

    if not logger.hasHandlers():
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(ColorFormatter("%(asctime)s - %(levelname)s - %(message)s"))

        # File handler
        file_handler = RotatingFileHandler(path / "log_file.txt", maxBytes=1000000, backupCount=5)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

        # Add handlers
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger
