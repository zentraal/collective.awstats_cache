import urllib
from plone.app.layout.viewlets.common import ViewletBase
from collective.awstats_cache import Session
from zope.component import getMultiAdapter


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
        downloads = statistics.copy()
        
        portal_state = getMultiAdapter(
            (self.context, self.request), name=u'plone_portal_state'
        )
        site = portal_state.portal()
        
        url = self.context.absolute_url().replace(site.absolute_url(), '')
        urls = []
        if url == '':
           url = '/'
        quoted_url = urllib.quote(url)
        
        urls.append(quoted_url)
        urls.append(quoted_url + '/view')
        canonical_url = urllib.quote(context_state.canonical_object_url())
        if canonical_url not in urls:
           urls.append(canonical_url)
           urls.append(canonical_url + '/view')

        query = 'SELECT * FROM statistics WHERE url IN %s' % str(tuple(urls))
        results = Session.execute(query).fetchall()
        if results:
            for row in rows_stat:
                for key in statistics.keys():
                    statistics[key] = statistics[key] + int(row[key])

            results_dw = Session.execute(
                'SELECT * FROM statistics WHERE url="%s/at_download%%"' % quoted_url).fetchall()
            if results_dw:
                downloads = statistics.copy
                for row in rows_stat:
                    for key in statistics.keys():
                        downloads[key] = downloads[key] + int(row[key])
                statistics['downloads'] = downloads['pages']
        return statistics
