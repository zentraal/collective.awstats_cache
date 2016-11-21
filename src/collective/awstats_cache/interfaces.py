# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""
try:
    from collective.awstats_hitcounter.interfaces import ICollectiveAwstatsHitcounterLayer as IDefaultBrowserLayer
except:
    from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class ICollectiveAwstatsCacheLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""
