import urllib
from plone.app.layout.viewlets.common import ViewletBase
from collective.awstats_cache import Session
from zope.component import getMultiAdapter


class AwstatsStatisticsViewlet(ViewletBase):

    def get_statistics(self):
        """ get statistics for context url
        """
        portal_state = getMultiAdapter(
            (self.context, self.request), name=u'plone_portal_state'
        )
        site = portal_state.portal()
        url = self.context.absolute_url().replace(site.absolute_url(), '')
        quoted_url = urllib.quote(url)

        results = Session.execute(
            'SELECT * FROM statistics WHERE url="%s"' % quoted_url)
        if len(results) > 0:
            return results[0]
        return {
            'entry': 0,
            'bandwidth': 0,
            'exit': 0,
            'pages': 0
        }
