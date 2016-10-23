#!/usr/bin/env python2
import requests
import xml.etree.ElementTree as XML
import logging

base = 'http://webservices.nextbus.com/service/publicXMLFeed?command=predictions'
agency = 'sf-muni'
route = '2'
stop = '6608' # Sutter x Scott

def main():
    log = logging.getLogger('nextbus-python')
    log.setLevel(logging.INFO)
    stdout = logging.StreamHandler()
    stdout.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    log.addHandler(stdout)

    url = '{base}&a={agency}&r={route}&s={stop}'.format(base=base,
	    agency=agency, route=route, stop=stop)

    log.debug('URL: %s', url)

    # Fetch the data from NextBus
    try:
	response = requests.get(url).text
	xml = XML.fromstring(response)
    except requests.exceptions.ConnectionError:
	log.error('Cannot connect to NextBus XML API')
	raise SystemExit # a/k/a quit()
    except XML.ParseError:
	log.error('Cannot decode NextBus API response. Expecting valid XML.')
	raise SystemExit # a/k/a quit()

    # Look for a prediction in the returned data
    if xml.iter('prediction'):
	for prediction in xml.iter('prediction'):
	    mins = prediction.get('minutes')
	    log.info('%s in %s minutes', route, mins)
    else:
	log.info('No predictions at this time.')

if __name__ == '__main__':
    main()
