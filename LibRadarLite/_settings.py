# -*- coding: utf-8 -*-

#   Copyright 2017 Zachary Marv (马子昂)
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

#   LibRadar settings.py

#   Settings about python scripts in LibRadar folder.
#   All the scripts in LibRadar need import this file.


import logging.config
import os

"""
    whether clean the workspace after work
        0 : Clean nothing
        1 : Clean res files
        2 : Clean smali files
        3 : Clean everything
"""
CLEAN_WORKSPACE = 3

"""
IGNORE ZERO API FILES

    If there's no API in a class file, just ignore it.
    If there's no API in a package, just ignore it.
"""
IGNORE_ZERO_API_FILES = True

"""
Config Files
"""

SCRIPT_PATH = os.path.split(os.path.realpath(__file__))[0]
if not os.path.exists(os.path.join(SCRIPT_PATH, 'Data')):
    os.mkdir(os.path.join(SCRIPT_PATH, 'Data'))
FILE_LOGGING = os.path.join(SCRIPT_PATH, 'Data', 'logging.conf')
FILE_RULE = os.path.join(SCRIPT_PATH, 'Data', 'tag_rules.csv')
LITE_DATASET_10 = os.path.join(SCRIPT_PATH, 'Data', 'lite_dataset_10.csv')

"""
    Logs
"""

logging.config.fileConfig(FILE_LOGGING)
# create logger
logger = logging.getLogger('radar')
