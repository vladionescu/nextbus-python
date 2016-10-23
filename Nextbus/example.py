#!/usr/bin/env python2
#import Nextbus # use when running outside Nextbus dir
from __init__ import Nextbus # use when running within Nextbus dir
import requests
import xml.etree.ElementTree as XML
import logging

agency = 'sf-muni'
route = '2'
stop = '6608' # Sutter x Scott

def main():
    api = Nextbus(agency=agency, route=route, stop=stop)
    predictions = api.nextbus()

    if predictions:
	for prediction in predictions:
	    print 'Next {} in {} minutes'.format(route, prediction)
    else:
	print 'No predictions'

if __name__ == '__main__':
    main()
