# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.awstats_cache.testing import COLLECTIVE_AWSTATS_CACHE_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.awstats_cache is properly installed."""

    layer = COLLECTIVE_AWSTATS_CACHE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.awstats_cache is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.awstats_cache'))

    def test_browserlayer(self):
        """Test that ICollectiveAwstatsCacheLayer is registered."""
        from collective.awstats_cache.interfaces import (
            ICollectiveAwstatsCacheLayer)
        from plone.browserlayer import utils
        self.assertIn(ICollectiveAwstatsCacheLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_AWSTATS_CACHE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['collective.awstats_cache'])

    def test_product_uninstalled(self):
        """Test if collective.awstats_cache is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.awstats_cache'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveAwstatsCacheLayer is removed."""
        from collective.awstats_cache.interfaces import ICollectiveAwstatsCacheLayer
        from plone.browserlayer import utils
        self.assertNotIn(ICollectiveAwstatsCacheLayer, utils.registered_layers())
