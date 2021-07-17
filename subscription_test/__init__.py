import logging

try:
    from gevent import monkey

    monkey.patch_all()
except ImportError:
    logging.warning("gevent not installed - async unavailable")

from .app import app

__all__ = ["app"]
