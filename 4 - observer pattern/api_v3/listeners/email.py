import logging

from lib.email import send_email
from ..event import subscribe

logger = logging.getLogger(__name__)


def handle_user_registered_event(user):
    # send a welcome email
    send_email(user.name, user.email,
        "Welcome",
        f"Thanks for registering, {user.name}!\nRegards, The DevNotes team")

def handle_user_password_forgotten_event(user):
    # send a password reset message
    send_email(user.name, user.email, "Reset your password",
        f"To reset your password, use this very secure code: {user.reset_code}.\nRegards, The DevNotes team")

def handle_user_upgrade_plan_event(user):
    # send a thank you email
    send_email(user.name, user.email,
        "Thank you",
        f"Thanks for upgrading, {user.name}! You're gonna love it. \nRegards, The DevNotes team")


def setup_handlers():
    logger.info('email: subscribing user events')
    subscribe("user-registered", handle_user_registered_event)
    subscribe("user-password-forgotten", handle_user_password_forgotten_event)
    subscribe("user-upgrade", handle_user_upgrade_plan_event)