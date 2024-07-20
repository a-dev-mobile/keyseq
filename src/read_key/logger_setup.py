import logging

def setup_logger():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
    logging.getLogger().setLevel(logging.INFO)
