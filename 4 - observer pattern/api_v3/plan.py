import logging
# from lib.email import send_email
from lib.db import create_user, find_user
# from lib.log import log
# from lib.slack import post_slack_message
from .event import post_event

logger = logging.getLogger(__name__)

def upgrade_plan(email: str):
    # find the user
    user = find_user(email)

    # upgrade the plan
    user.plan = "paid"

    logger.info(f'posting eventi user-upgrade for {user=}')
    post_event('user-upgrade', user)

