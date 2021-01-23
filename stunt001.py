import os
import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger("log")


def log_dehcec(func):
    def worjf