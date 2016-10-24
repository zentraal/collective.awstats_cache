# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.awstats_cache


class CollectiveAwstatsCacheLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=collective.awstats_cache)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.awstats_cache:default')


COLLECTIVE_AWSTATS_CACHE_FIXTURE = CollectiveAwstatsCacheLayer()


COLLECTIVE_AWSTATS_CACHE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_AWSTATS_CACHE_FIXTURE,),
    name='CollectiveAwstatsCacheLayer:IntegrationTesting'
)


COLLECTIVE_AWSTATS_CACHE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_AWSTATS_CACHE_FIXTURE,),
    name='CollectiveAwstatsCacheLayer:FunctionalTesting'
)


COLLECTIVE_AWSTATS_CACHE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_AWSTATS_CACHE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveAwstatsCacheLayer:AcceptanceTesting'
)
