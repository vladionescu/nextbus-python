#!/usr/bin/env python2
import requests
import xml.etree.ElementTree as XML
import logging

class Nextbus(object):

    base = 'http://webservices.nextbus.com/service/publicXMLFeed?command=predictions'
    
    def __init__(self, agency='sf-muni', route=None, stop=None):
	self.log = logging.getLogger('nextbus-python')
	self.log.setLevel(logging.INFO)
	stdout = logging.StreamHandler()
	stdout.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
	self.log.addHandler(stdout)

	self.agency = agency
	self.route = route
	self.stop = stop

    def nextbus(self, agency=None, route=None, stop=None):
	if agency is None:
	    agency = self.agency

	if route is None:
	    route = self.route

	if stop is None:
	    stop = self.stop

	for param in [agency, route, stop]:
	    if param is None:
		raise ValueError('Need an agency, a bus route, and a bus stop to get predictions')
	
	url = '{base}&a={agency}&r={route}&s={stop}'.format(base=self.base,
		agency=agency, route=route, stop=stop)

	self.log.debug('URL: %s', url)

	# Fetch the data from NextBus
	xml = self.query(url)

	# Look for a prediction in the returned data
	predictions = []

	if xml.iter('prediction'):
	    for prediction in xml.iter('prediction'):
		mins = prediction.get('minutes')
		predictions.append(mins)
		self.log.debug('%s in %s minutes', route, mins)
	else:
	    self.log.debug('No predictions at this time.')

	return predictions

    def query(self, url=None):
	if url is None:
	    e = 'Need a URL to query to API'
	    self.log.error(e)
	    raise ValueError(e)

	try:
	    response = requests.get(url).text
	    xml = XML.fromstring(response)
	except requests.exceptions.ConnectionError:
	    e = 'Cannot connect to NextBus XML API'
	    self.log.error(e)
	    raise SystemExit(e) # a/k/a quit()
	except XML.ParseError:
	    e = 'Cannot decode NextBus API response. Expecting valid XML.'
	    self.log.error(e)
	    raise SystemExit(e) # a/k/a quit()

	return xml
