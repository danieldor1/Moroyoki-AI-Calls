import time
from functools import wraps


def exception(logger):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except:
                issue = "exception in "+func.__name__+"\n"
                issue = issue+"=============\n"
                logger.exception(issue)
                raise
        return wrapper
    return decorator


def retry(ExceptionToCheck, TRIES=4, DELAY=3, BACKOFF=2, logger=None):
    """this is a decorator
    Args:
        ExceptionToCheck (_type_): _description_
        tries (int, optional): _description_. Defaults to 4.
        delay (int, optional): _description_. Defaults to 3.
        backoff (int, optional): _description_. Defaults to 2.
        logger (_type_, optional): _description_. Defaults to None.
    """
    def deco_retry(f):
        @wraps(f)
        def f_retry(*args, **kwargs):
            mtries, mdelay = TRIES, DELAY
            while mtries > 1:
                try:
                    return f(*args, **kwargs)
                except ExceptionToCheck as e:
                    msg = "%s, Retrying in %d seconds..." % (str(e), mdelay)
                    if logger:
                        logger.warning(msg)
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= BACKOFF
            return f(*args, **kwargs)
        return f_retry
    return deco_retry
