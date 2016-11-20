#!/usr/bin/env python2
#import libnextbus # use when running outside Nextbus dir
from __init__ import Nextbus # use when running within Nextbus dir
import requests

agency = 'sf-muni'
route = '38'
stop = '4294' # Divisadero x Geary

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
