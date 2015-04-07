import time


def profile(func):
    def func_with_profile(*args, **kwargs):
        milli_seconds_now = lambda: int(round(time.time() * 1000))
        start_ts = milli_seconds_now()
        print '{}Program Started{}'.format('-' * 10, '-' * 10)
        result = func(*args, **kwargs)
        end_ts = milli_seconds_now()
        print '{}Program     End{}'.format('-' * 10, '-' * 10)
        print 'Time spent: {:.3f}s'.format((float(end_ts) - start_ts) / 1000)
        return result

    return func_with_profile
