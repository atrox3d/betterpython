import logging

from lib.db import create_user, find_user
from lib.stringtools import get_random_string
from .event import post_event

logger = logging.getLogger(__name__)


def register_new_user(name: str, password: str, email: str):
    # create an entry in the database
    user = create_user(name, password, email)
    
    logger.info(f'posting event user-registered for {user=}')
    post_event('user-registered', user)

def password_forgotten(email: str):
    # retrieve the user
    user = find_user(email)

    # generate a password reset code
    user.reset_code = get_random_string(16)

    logger.info(f'posting event user-password-forgotten for {user=}')
    post_event('user-password-forgotten', user)
