import json
import pathlib
import logging.config

# logging.debug() # BAD because it uses the root logger
logger = logging.getLogger("my_app") # GOOD because it uses one of your loggers

def logging_setup():
    config_file = pathlib.Path("logging_configs/medium.json")
    with open(config_file, "r") as f:
        config = json.load(f)
    logging.config.dictConfig(config=config)


def main():
    # logging.basicConfig(level=logging.DEBUG)
    logging_setup()

    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")
    try:
        1/0
    except ZeroDivisionError:
        logger.exception("exception message")


if __name__ == "__main__":
    main()
