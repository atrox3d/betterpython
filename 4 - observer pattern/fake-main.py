import logging

from api_v3.listeners import slack
from api_v3.listeners import email

logging.basicConfig(
    level=logging.INFO, 
    format="[%(levelname)s | %(filename)12s | %(funcName)15s() ] %(message)s"
)

slack.setup_handlers()
email.setup_handlers()
