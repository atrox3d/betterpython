import logging

# logging.c
logger = logging.getLogger(__name__)
subscribers = dict()

def subscribe(event: str, action: callable) -> None:
    if not event in subscribers:
        subscribers[event] = list()
    else:
        logger.info(f'{event=} already present')
    subscribers[event].append(action)

def post_event(event: str, data: str) -> None:
    if event in subscribers:
        for action in subscribers[event]:
            if action :
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