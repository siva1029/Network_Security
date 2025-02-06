import os #Why os grade out here?
import sys
import json

from dotenv import load_dotenv
load_dotenv()
MONGO_DB_URL=os.getenv('MONGO_DB_URL')
print(MONGO_DB_URL)

#What is the meaning of word color codings?

import certifi

ca=certifi.where()

import pandas as pd
import numpy as np
import pymongo #Why yellow line undersline?

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    def csv_to_json_converter(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    if __name__ == '__main__':
        pass