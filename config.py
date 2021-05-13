class DevConfig(object):
    DEBUG = True
    THREADS_PER_PAGE = 2

class ProdConfig(object):
    DEBUG = False
    THREADS_PER_PAGE = 2
