# -*- coding: utf-8 -*-

from sqlalchemy import schema, types
from sqlalchemy import Table
from collective.awstats_cache import ORMBase


metadata = ORMBase.metadata


class Statistics(ORMBase):

    __tablename__ = 'statistics'

    id = schema.Column(types.Integer, primary_key=True)
    url = schema.Column(types.String())
    entry = schema.Column(types.String())
    bandwidth = schema.Column(types.String(20))
    exit = schema.Column(types.String(20))
    pages = schema.Column(types.String(20))
    last_changes = schema.Column(types.String(20))

    def __init__(self, url, entry, bandwidth, exit, pages, last_changes):

        self.url = url
        self.entry = entry
        self.bandwidth = bandwidth
        self.exit = exit
        self.pages = pages
        self.last_changes = last_changes


statistics = Table('statistics', metadata)
