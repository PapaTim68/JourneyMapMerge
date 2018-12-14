# -*- coding: utf-8 -*-
"""
Created on 14.12.2018

@author: 
"""
# External Moduls
import logging

# Own Imports/Moduls


logger = logging.getLogger().getChild(__name__)
if not logger.hasHandlers():
    logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

if __name__ == '__main__':
    pass
