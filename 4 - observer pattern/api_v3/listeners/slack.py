import logging

from ..event import subscribe
from lib.slack import post_slack_message

logger = logging.getLogger(__name__)

def handle_user_registered_event(user):
    post_slack_message("sales",
        f"{user.name} has registered with email address {user.email}. Please spam this person incessantly.")

def handle_user_upgrade_plan_event(user):
    post_slack_message("sales",
        f"{user.name} has upgraded their plan.")

def setup_handlers() -> None:
    logger.info('slack: subscribing user events')
    subscribe('user-registered', handle_user_registered_event)
    subscribe('user-upgrade', handle_user_upgrade_plan_event)
