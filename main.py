import logging

logging.getLogger("my_app")

def main():
    logging.basicConfig(level=logging.DEBUG)
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
