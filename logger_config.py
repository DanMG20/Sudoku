import logging
import sys
import os
from pathlib import Path

DEBUG = False   # True en desarrollo / False en release (.exe)

APP_NAME = "Sudoku"
LOG_FILE = "sudoku.log"


def setup_logger(name="sudoku"):
    # 📂 Carpeta correcta para logs en Windows
    # C:\Users\<user>\AppData\Local\Sudoku\logs
    base_dir = Path(os.getenv("LOCALAPPDATA", Path.home()))
    log_dir = base_dir / APP_NAME / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Evita duplicar handlers
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%H:%M:%S"
    )

    # 📄 Archivo de log
    file_handler = logging.FileHandler(
        log_dir / LOG_FILE,
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # 🖥️ Consola solo en desarrollo
    if DEBUG:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger
