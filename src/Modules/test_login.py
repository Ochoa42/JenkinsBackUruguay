import os
import json
import time
import pytest
import traceback

def pytest_addoption(parser):
    parser.addoption('--env',dest='env', action='store')
#https://docs.google.com/spreadsheets/d/10d4GV3ORzKqEEVQyzHUPqYvv88LKllyyZBQkyUI0x40/edit?gid=0#gid=0