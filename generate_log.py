from datetime import datetime

from lib.generate_log import generate_log as _generate_log

__all__ = ["generate_log"]

def generate_log(log_data):
    return _generate_log(log_data)
