from .base import *  # noqa

DEBUG = False
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split()
