import os
from dotenv import load_dotenv
import logging

load_dotenv()

# api_key = os.getenv("API_KEY", "stadart_key")
# password = os.getenv("PASSWORD", "qwe123")

# print(api_key)
# print(password)

# logging.basicConfig(
#     level=logging.INFO,
#     filename="my_log.log",
#     format="%(asctime)s %(filename)s %(levelname)s %(message)s"
# )
# logging.debug("debug")
# logging.info("info")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")

"""
Debug - отладка
Info - информационный уровень
Warning - предупреждения
Error - уровень ошибок
Critical - критический уровень
"""

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