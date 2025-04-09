from dotenv import load_dotenv
import logging

load_dotenv()

logger = logging.getLogger("Selenium")
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s %(message)s")
handler_file = logging.FileHandler("Selenium_log.log", mode="a")
handler_file.setLevel(logging.ERROR)
handler_console = logging.StreamHandler()

handler_file.setFormatter(formatter)
handler_console.setFormatter(formatter)

logger.addHandler(handler_file)
logger.addHandler(handler_console)

logger.info("yeppie, logger is working somewhere")
logger.error("ypsie, error is here")