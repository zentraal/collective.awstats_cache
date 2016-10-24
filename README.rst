==============================================================================
collective.awstats_cache
==============================================================================

Get statistics from db

.. contents:: **Table of contents**

Introduction
============

This Plone add-on is based on `z3c.saconfig`__ and `SQLAlchemy`__, and can't provide any new feature to Plone
without a proper configuration.

__ http://pypi.python.org/pypi/z3c.saconfig
__ http://sqlalchemy.org/

Keep reading for installation and configuration guide.

How to use
==========

After the installation, a viewlet is renderer with info picked form awstats:

* hits
* page_views
* exit

Multiple sites
--------------

If your buildout hosts multiple Plone sites, all of them will store data in a different db

Installation and configuration
==============================

You must configure an access to an external DBMS. The name of the engine used must be ``awstats_statistics``.

Follow an example based on `sqlite`__.

__ http://www.sqlite.org/

Add ``collective.awstats_cache`` to your buildout, then provide a SQLAlchemy connection string::

    [buildout]
    ...
    
    [instance]
    ...
    eggs=
       ...
       collective.awstats_cache
    
    zcml-additional =
        ...
        <configure xmlns="http://namespaces.zope.org/zope"
                  xmlns:db="http://namespaces.zope.org/db">
           <include package="z3c.saconfig" file="meta.zcml" />
           <db:engine name="awstats_statistics"
                      url="sqlite:///${buildout:directory}/var/filestorage/awstats_statistics.db"
                      setup="collective.awstats_cache.prepare_model.prepare"
                      />
           <db:session name="awstats_statistics" engine="awstats_statistics" />
       </configure>
