import urllib
from plone.app.layout.viewlets.common import ViewletBase
from collective.awstats_cache import Session
from zope.component import getMultiAdapter
COLUMNS = ['id', 'entry', 'bandwidth', 'exit', 'pages', 'last_changes']


class AwstatsStatisticsViewlet(ViewletBase):

    def get_statistics(self):
        """ get statistics for context url
        """
        statistics = {
            'entry': 0,
            'bandwidth': 0,
            'exit': 0,
            'pages': 0
        }
        portal_state = getMultiAdapter(
            (self.context, self.request), name=u'plone_portal_state'
        )
        site = portal_state.portal()
        url = self.context.absolute_url().replace(site.absolute_url(), '')
        if url == '':
           url = '/'
        quoted_url = urllib.quote(url)

        results = Session.execute(
            'SELECT * FROM statistics WHERE url="%s"' % quoted_url).fetchone()
        if results:
            statistics = dict(zip(COLUMNS, results))
        if statistics and self.context.portal_type == "File":
            results_dw = Session.execute(
                'SELECT * FROM statistics WHERE url="%s"' % quoted_url).fetchone()
            if results_dw:
                downloads = dict(zip(COLUMNS, results_dw))
                statistics['downloads'] = downloads['pages']
        return statistics
