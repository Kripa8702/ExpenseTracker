import logging 

def setup_logging(name):
    logger = logging.getLogger(name)

    file_handler = logging.FileHandler(f"{name}.log")
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)

    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    
    return logger