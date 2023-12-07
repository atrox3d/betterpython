import logging

from api_v3.listeners import slack

logging.basicConfig(
    level=logging.INFO, 
    format="[%(levelname)s | %(filename)12s | %(funcName)15s() ] %(message)s"
)

slack.setup_handlers()