import logging.config

# logging.debug() # BAD because it uses the root logger
logger = logging.getLogger("my_app") # GOOD because it uses one of your loggers

logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    # "filters": {},
    "formatters": {
        "simple": {
            "format": "%(levelname)s | %(name)s | %(message)s."
        }
    },
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        }
    },
    "loggers": {
        "root": {
            "level": "DEBUG",
            "handlers": ["stdout"]
        }
    },
}

def main():
    # logging.basicConfig(level=logging.DEBUG)
    logging.config.dictConfig(config=logging_config) # Use dictConfig()

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
