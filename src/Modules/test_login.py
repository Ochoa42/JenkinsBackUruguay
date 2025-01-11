import os
import json
import time
import pytest
import traceback

from helpers.auth_token_helper import get_auth_token
from helpers.runtime_tools import RunTimeTools

def pytest_configure(config):
    pytest.env = configure_env(config)

    try:
        os.makedirs(os.getcwd() + os.sep + "Reports")
    except:
        pass

    current_time = time.strftime("%Y%m%d-%H%M%S")

    config.option.htmlpath = os.getcwd() + os.sep + "Reports" + \
        os.sep + "Report-" + \
        str(pytest.env['env']).upper() + '-' + current_time + '.html'

    try:
        pytest.auth_token = get_auth_token(pytest.env['username'],pytest.env['password'],pytest.env['base_url'])
    except Exception as e:
        raise Exception(traceback.format_exc() + '\n' 'Unable to get auth token: ' + str(e))
    
    try:
        pytest.runtime_tools = RunTimeTools()
    except Exception as e:
        raise Exception(traceback.format_exc() + '\n' 'Unable to get auth token: ' + str(e))

def pytest_addoption(parser):
    parser.addoption('--env',dest='env', action='store', required=True)
    parser.addoption('--username',dest='username', action='store')
    parser.addoption('--password',dest='password', action='store')
    parser.addoption('--base_url',dest='base_url', action='store')

def configure_env(config):
    env = None
    with open(os.getcwd() + os.sep + 'environment.json','r+') as json_file:
        env = json.load(json_file)

        env['env'] = str(config.option.env).lower()

        if config.option.username is not None:
            env['username'] = config.option.username
        
        if config.option.password is not None:
            env['password'] = config.option.password
        
        if config.option.base_url is not None:
            env['base_url'] = str(config.option.base_url).lower()
        
        json_file.seek(0)
        json.dump(env,json_file,indent=4)
        json_file.truncate()
        json_file.close()
    
    return env
#https://docs.google.com/spreadsheets/d/10d4GV3ORzKqEEVQyzHUPqYvv88LKllyyZBQkyUI0x40/edit?gid=0#gid=0