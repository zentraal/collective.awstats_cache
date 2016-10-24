# -*- coding: utf-8 -*-


def prepare(engine):
    from collective.awstats_cache import ORMBase
    import collective.awstats_cache.models
    ORMBase.metadata.create_all(engine)
