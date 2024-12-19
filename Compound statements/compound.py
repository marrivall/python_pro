import time
import logging
# --------------------------------------------------------
# measuring and logging the execution time of a code block
# ---------------------------------------------------------
class TimerContext:
    def __enter__(self):
        self.begin = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end = time.time()
        elapsed_time = round(end - self.begin)
        logging.info(f"Execution time of a code block = {elapsed_time} seconds")

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

with TimerContext():
    time.sleep(2)

# -----------------------------------------------
# Managing Temporary In-Memory Data Structures
# -----------------------------------------------
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

GLOBAL_CONFIG = {
    "feature_a": True,
    "feature_b": False,
    "max_retries": 3
}
class Configuration:
    def __init__(self, updates, validator=None):
        self.updates = updates
        self.validator = validator
        self.original_config = None

    def __enter__(self):
        self.original_config = GLOBAL_CONFIG.copy()
        GLOBAL_CONFIG.update(self.updates)
        logging.info(f"Updates in the GLOBAL_CONFIG : {self.updates}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            if not self.validator(GLOBAL_CONFIG):
                raise ValueError("Validation failed")
        except Exception as error:
            logging.error(f"Configuration validation error: {error}")
        finally:
            GLOBAL_CONFIG.update(self.original_config)
            logging.info("Original configuration restored.")
        return False

def validate_config(config: dict) -> bool:
    if not isinstance(config["feature_a"], bool):
        return False
    if not isinstance(config["feature_b"], bool):
        return False
    if not isinstance(config["max_retries"],int):
        return False
    if config["max_retries"] not in range(0, 4):
        return False
    else:
        return True

if __name__ == "__main__":
    try:
        with Configuration({"feature_a": "invalid_value", "max_retries": -1}, validator=validate_config):
            logging.info("Inside context: %s", GLOBAL_CONFIG)
    except Exception as e:
        logging.error("Caught exception: %s", e)
    logging.info("After failed context: %s", GLOBAL_CONFIG)

