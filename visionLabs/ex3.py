"""
Самый простой способ - написать декоратор, который будет замерять время работы функции и логировать это
"""
import logging
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig(
    level=logging.INFO, format='#%(asctime)s# %(name)s %(levelname)s: %(message)s'
)


def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            return func(*args, **kwargs)
        except:
            pass
        finally:
            logger.info('Process time of %s is  %s', func.__name__, time.time() - start_time)

    return wrapper


@time_it
def do_smth(a: int, b: int):
    print('Do smth', a, b)


do_smth(12, 500)
