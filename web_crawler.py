#!/usr/bin/env python

'''
Web Crawler:

This script takes a site URL as an argument
and creates a map of that domain as a Python dictionary.
Script will work properly wit exemplary site
url: http://0.0.0.0:8000
'''


import requests, bs4


dict = {}


def site_map(url):

    '''This function takes url (http://0.0.0.0:8000) as parameter
    and creates a python dictionary. Dictionaries contain
    URL, title and links within every site.'''

    # create response object
    res = requests.get(url)

    # check if the page exist
    try:
        res.raise_for_status()

    except Exception as exc:
        print('Error has occured:\t %s' % (exc))

    # create Beautiful soup object
    siteSoup = bs4.BeautifulSoup(res.text, features='html.parser')


    titleSoup = siteSoup.select('title')    # search for website title
    title = titleSoup[0].getText()

    linksSoup = siteSoup.find_all('a')      # search for links

    links = set()       # create a set of links

    url_split = url.split('/',3)
    index_url = url_split[0] + '//' + url_split[2]


    for item in linksSoup:

        if item in links:
            continue

        elif index_url in item.attrs['href']:
            links.add(item.attrs['href'])

        elif item.attrs['href'].startswith('/'):

            links.add(index_url + item.attrs['href'])

        else:
            continue



    dict[url] = {'title': title,
                'links': links}




    for link in links:

        if link in dict:

            continue

        # elif link in dict:
        #
        #     continue



        else:
            site_map(link)

    return dict


site_map('http://0.0.0.0:8000')

print(dict)