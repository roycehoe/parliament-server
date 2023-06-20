from dotenv import dotenv_values

IS_DEV = False if dotenv_values(".env").get("IS_DEV") is None else True
DEFAULT_REDIS_PORT = 6379
REDIS_HOST = "localhost"

HANSARD_BASE_URL = "https://sprs.parl.gov.sg/search/getHansardReport/"
FIRST_PARLIAMENT_SITTING = (1955, 4, 22)
HANSARD_API_MAX_RETRIES = 5

DEFAULT_DATETIME_FORMAT = "%d-%m-%Y"
PATH_TO_PARLIAMENT_SITTING_DATES = "./data/parliament_sitting_dates.json"
PATH_TO_PARLIAMENT_DATA_DIR = "./data/parliament_data/"
