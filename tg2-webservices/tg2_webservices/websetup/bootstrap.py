# -*- coding: utf-8 -*-
"""Setup the tg2-webservices application"""

import logging
from tg import config
from tg2_webservices import model

import transaction


def bootstrap(command, conf, vars):
    """Place any commands to setup tg2_webservices here"""

    # <websetup.bootstrap.before.auth

    # <websetup.bootstrap.after.auth>
