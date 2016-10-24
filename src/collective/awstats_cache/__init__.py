# -*- coding: utf-8 -*-
"""Init and utils."""
import logging
from sqlalchemy.ext import declarative
from z3c.saconfig import named_scoped_session
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('collective.awstats_cache')

logger = logging.getLogger('collective.awstats_cache')

ORMBase = declarative.declarative_base()
Session = named_scoped_session('awstats_statistics')
