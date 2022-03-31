# import re

# article = '''['#content', '#python-network', '/', '/psf-landing/', 'https://docs.python.org', 'https://pypi.org/', '/jobs/', '/community-landing/', '#top', '/', 'https://psfmember.org/civicrm/contribute/transact?reset=1&id=2', '#site-map', '#', 'javascript:;', 'javascript:;', 'javascript:;', '#', 'https://www.facebook.com/pythonlang?fref=ts', 'https://twitter.com/ThePSF', '/community/irc/', '/about/', '/about/apps/', '/about/quotes/', '/about/gettingstarted/', '/about/help/', 'http://brochure.getpython.info/', '/downloads/', '/downloads/', '/downloads/source/', '/downloads/windows/', '/downloads/macos/', '/download/other/', 'https://docs.python.org/3/license.html', '/download/alternatives', '/doc/', '/doc/', '/doc/av', 'https://wiki.python.org/moin/BeginnersGuide', 'https://devguide.python.org/', 'https://docs.python.org/faq/', 'http://wiki.python.org/moin/Languages', 'http://python.org/dev/peps/', 'https://wiki.python.org/moin/PythonBooks', '/doc/essays/', '/community/', '/community/diversity/', '/community/lists/', '/community/irc/', '/community/forums/', '/psf/annual-report/2021/', '/community/workshops/', '/community/sigs/', '/community/logos/', 'https://wiki.python.org/moin/', '/community/merchandise/', '/community/awards', '/psf/conduct/', '/psf/get-involved/', '/psf/community-stories/', '/success-stories/', '/success-stories/category/arts/', '/success-stories/category/business/', '/success-stories/category/education/', '/success-stories/category/engineering/', '/success-stories/category/government/', '/success-stories/category/scientific/', '/success-stories/category/software-development/', '/blogs/', '/blogs/', '/psf/newsletter/', 'http://planetpython.org/', 'http://pyfound.blogspot.com/', 'http://pycon.blogspot.com/', '/events/', '/events/python-events/', '/events/python-user-group/', '/events/python-events/past/', '/events/python-user-group/past/', 'https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event', '/shell/', '//docs.python.org/3/tutorial/controlflow.html#defining-functions', '//docs.python.org/3/tutorial/introduction.html#lists', 'http://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator', '//docs.python.org/3/tutorial/', '//docs.python.org/3/tutorial/controlflow.html', '/doc/', 'https://psfmember.org/civicrm/contribute/transact?reset=1&id=37', '/about/gettingstarted/', '/downloads/release/python-3104/', 'https://docs.python.org', '//jobs.python.org', 'https://blog.python.org', 'https://pythoninsider.blogspot.com/2022/03/python-3104-and-3912-are-now-available.html', 'http://pyfound.blogspot.com/2022/03/meta-deepens-its-investment-in-python.html', 'https://pythoninsider.blogspot.com/2022/03/python-3103-3911-3813-and-3713-are-now.html', 'http://pyfound.blogspot.com/2022/03/the-pi-thon-2022-psf-spring-fundraiser.html', 'https://pythoninsider.blogspot.com/2022/03/python-3110a6-is-available.html', '/events/calendars/', '/events/python-user-group/1212/', '/events/python-events/1211/', '/events/python-events/1206/', '/events/python-events/1196/', '/events/python-events/1146/', '/success-stories/', '/success-stories/python-seo-link-analyzer/', '/success-stories/python-seo-link-analyzer/', '/about/apps', 'http://www.djangoproject.com/', 'http://www.pylonsproject.org/', 'http://bottlepy.org', 'http://tornadoweb.org', 'http://flask.pocoo.org/', 'http://www.web2py.com/', 'http://wiki.python.org/moin/TkInter', 'https://wiki.gnome.org/Projects/PyGObject', 'http://www.riverbankcomputing.co.uk/software/pyqt/intro', 'https://wiki.qt.io/PySide', 'https://kivy.org/', 'http://www.wxpython.org/', 'http://www.scipy.org', 'http://pandas.pydata.org/', 'http://ipython.org', 'http://buildbot.net/', 'http://trac.edgewall.org/', 'http://roundup.sourceforge.net/', 'http://www.ansible.com', 'https://saltproject.io', 'https://www.openstack.org', 'https://xon.sh', '/dev/peps/', '/dev/peps/peps.rss', '/psf/', '/psf/', '/users/membership/', '/psf/donations/', '#python-network', '/about/', '/about/apps/', '/about/quotes/', '/about/gettingstarted/', '/about/help/', 'http://brochure.getpython.info/', '/downloads/', '/downloads/', '/downloads/source/', '/downloads/windows/', '/downloads/macos/', '/download/other/', 'https://docs.python.org/3/license.html', '/download/alternatives', '/doc/', '/doc/', '/doc/av', 'https://wiki.python.org/moin/BeginnersGuide', 'https://devguide.python.org/', 'https://docs.python.org/faq/', 'http://wiki.python.org/moin/Languages', 'http://python.org/dev/peps/', 'https://wiki.python.org/moin/PythonBooks', '/doc/essays/', '/community/', '/community/diversity/', '/community/lists/', '/community/irc/', '/community/forums/', '/psf/annual-report/2021/', '/community/workshops/', '/community/sigs/', '/community/logos/', 'https://wiki.python.org/moin/', '/community/merchandise/', '/community/awards', '/psf/conduct/', '/psf/get-involved/', '/psf/community-stories/', '/success-stories/', '/success-stories/category/arts/', '/success-stories/category/business/', '/success-stories/category/education/', '/success-stories/category/engineering/', '/success-stories/category/government/', '/success-stories/category/scientific/', '/success-stories/category/software-development/', '/blogs/', '/blogs/', '/psf/newsletter/', 'http://planetpython.org/', 'http://pyfound.blogspot.com/', 'http://pycon.blogspot.com/', '/events/', '/events/python-events/', '/events/python-user-group/', '/events/python-events/past/', '/events/python-user-group/past/', 'https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event', '/dev/', 'https://devguide.python.org/', 'https://bugs.python.org/', 'https://mail.python.org/mailman/listinfo/python-dev', '/dev/core-mentorship/', '/dev/security/', '#python-network', '/about/help/', '/community/diversity/', 'https://github.com/python/pythondotorg/issues', 'https://status.python.org/', '/psf-landing/', '/about/legal/', '/privacy/', '/psf/sponsorship/sponsors/#heroku']'''
# stale_links = re.findall('http://[a-z0-9_.\-]+\.[a-z0-9_\-/]+', article)
# print(stale_links)
