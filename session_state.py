# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 15:43:45 2024

@author: nm.acuna
"""

# session_state.py
class SessionState(object):
    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

def get(**kwargs):
    if not hasattr(get, '_session_state'):
        get._session_state = SessionState(**kwargs)

    return get._session_state
