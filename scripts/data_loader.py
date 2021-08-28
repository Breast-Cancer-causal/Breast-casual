# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 08:11:35 2021

@author: Smegn
"""

import pandas as pd
#loading file function

def load_csv(path):
    """
     A simple function which takes file path
     and  load a dataframe from a specified .csv filename returning the loaded DataFrame
     """
    data = pd.read_csv(path,engine='python',error_bad_lines=False, na_values=['?', None,'-','--','undefined'])
    return data