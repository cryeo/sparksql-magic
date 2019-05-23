__version__ = '0.0.2'

from .sparksql import SparkSql


def load_ipython_extension(ipython):
    ipython.register_magics(SparkSql)
