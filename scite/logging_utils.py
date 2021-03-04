# -*- coding: utf-8 -*-
import logging


def set_logger(name: str) -> logging.Logger:
    """ Enable custom logger `name`"""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    sh = logging.StreamHandler()
    sh.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(message)s")
    sh.setFormatter(formatter)
    logger.addHandler(sh)
    return logger
