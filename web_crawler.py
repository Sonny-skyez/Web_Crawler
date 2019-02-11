#!/usr/bin/env python

'''
Web Crawler:

This script takes a site URL as an argument
and creates a map of that domain as a Python dictionary.
'''


import requests, bs4


dict = {}


def site_map(url):

    '''This function takes url (http://0.0.0.0:8000) as parameter
    and creates a python dictionary. Dictionaries '''
    res = requests.get(url)

    # check if the page exist
    try:
        res.raise_for_status()

    except Exception as exc:
        print('Error has occured:\t %s' % (exc))


    siteSoup = bs4.BeautifulSoup(res.text, features='html.parser')


    titleSoup = siteSoup.select('title')
    title = titleSoup[0].getText()


    linksSoup = siteSoup.find_all('a')


    links = set()

    index_url = 'http://0.0.0.0:8000'


    for item in linksSoup:

        if item in links:
            continue

        elif index_url in item.attrs['href']:
            links.add(item.attrs['href'])

        elif item.attrs['href'].startswith('/'):

            links.add(index_url + item.attrs['href'])




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