"""Quick script to pull data from NYTimes"""

import json
import os
import sys
import urllib
import urllib2

import api_keys

def main(api_key, category, label):
    content = []

    for i in range(0, 5):
        url = 'http://api.nytimes.com/svc/search/v1/article?query=classifiers_facet={0}&api-key={1}&offset={2}'.format(category, api_key, i)
        h = urllib.urlopen(url)
        data = json.loads(h.read())

        for results in data['results']:
            content.append(result['body'])

    f = open(label, 'w')

    for line in content:
        try:
            f.write(u'{0}\n'.format(line))
        except UnicodeEncodeError:
            pass

    f.close()

if __name__ == '__main__':
    main(api_keys.article_api_key, '[Top/Features/Arts]', 'arts')
    main(api_keys.article_api_key, '[Top/News/Sports]', 'sports')

