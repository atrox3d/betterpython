import logging

from lib.log import log
from ..event import subscribe

logger = logging.getLogger(__name__)

def handle_user_registered_event(user):
    log(f"User registered with email address {user.email}")

def handle_user_password_forgotten_event(user):
    log(f"User with email address {user.email} requested a password reset")

def handle_user_upgrade_plan_event(user):
    log(f"User with email address {user.email} has upgraded their plan")

def setup_handlers():
    logger.info('log: subscribing user events')
    subscribe("user-registered", handle_user_registered_event)
    subscribe("user-password-forgotten", handle_user_password_forgotten_event)
    subscribe("user-upgrade", handle_user_upgrade_plan_event)