import logging

# logging.c
logger = logging.getLogger(__name__)
subscribers = dict()

def subscribe(event: str, action: callable) -> None:
    """
    adds event handler for event
    """
    if not event in subscribers:
        logger.info(f'creating new list for event {event}')
        subscribers[event] = list()
    else:
        logger.info(f'{event=} already present')
    logger.info(f'appending action={action.__name__} to {event=}')
    subscribers[event].append(action)

def post_event(event: str, data: str) -> None:
    if event in subscribers:
        logger.info(f'{event=} found')
        for action in subscribers[event]:
            if action :
                logger.info(f'running {action.__name__}({data})')
                action(data)
            else:
                logger.error(f'cannot run {action=}')
    else:
        logger.warn(f'{event=} not found')

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO, 
        format="[%(levelname)s | %(filename)s - %(funcName)s() ] %(message)s"
    )

    def action(data) -> None:
        print(f'action: {data=}')
    subscribe('test', action)
    subscribe('test', action)
    post_event('test', 'data')