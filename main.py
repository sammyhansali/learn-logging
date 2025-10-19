import logging.config

# logging.debug() # BAD because it uses the root logger
logging.getLogger("my_app") # GOOD because it uses one of your loggers

logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {},
    "formatters": {},
    "handlers": {},
    "loggers": {},
}

def main():
    # logging.basicConfig(level=logging.DEBUG)
    logging.config.dictConfig(config=logging_config) # Use dictConfig()

    logging.debug("debug message")
    logging.info("info message")
    logging.warning("warning message")
    logging.error("error message")
    logging.critical("critical message")
    try:
        1/0
    except ZeroDivisionError:
        logging.exception("exception message")


if __name__ == "__main__":
    main()
