# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 15:43:45 2024

@author: nm.acuna
"""

# session_state.py
from streamlit.report_thread import get_report_ctx
from streamlit.server.server import Server

class SessionState(object):
    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

def get(**kwargs):
    ctx = get_report_ctx()

    # We want to get the session object to store the page state
    this_session = None
    current_server = Server.get_current()
    if hasattr(current_server, '_session_infos'):
        # Streamlit < 1.9.0
        session_infos = current_server._session_infos.values()
    else:
        # Streamlit >= 1.9.0
        session_infos = current_server._session_info_by_id.values()

    for session_info in session_infos:
        s = session_info.session
        if (s._main_dg._uploaded_file_mgr._uploaded_files and
                s.request_id == ctx.request_id):
            this_session = s

    if this_session is None:
        raise RuntimeError("Couldn't get Streamlit session.")

    # Get or create the session state
    if not hasattr(this_session, '_custom_session_state'):
        this_session._custom_session_state = SessionState(**kwargs)

    return this_session._custom_session_state