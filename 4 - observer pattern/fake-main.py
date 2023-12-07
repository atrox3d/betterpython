import logging

from api_v3.listeners import slack
from api_v3.listeners import email
from api_v3.listeners import log

from api_v3.user import register_new_user, password_forgotten

logging.basicConfig(
    level=logging.INFO, 
    format="[%(levelname)s | %(filename)12s | %(funcName)15s() ] %(message)s"
)

logger = logging.getLogger(__name__)

logger.info('setting up event handlers')
slack.setup_handlers()
email.setup_handlers()
log.setup_handlers()

logger.info(f'registering user')
register_new_user('bob', 'pwd', 'bob@mail')

logger.info(f'resetting password')
password_forgotten('bob@mail')