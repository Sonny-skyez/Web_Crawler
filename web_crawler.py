#!/usr/bin/env python

'''
Web Crawler:

This script takes a site URL as an argument
and creates a map of that domain as a Python dictionary.
'''


import requests, bs4


dict = {}


def site_map(url):

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

            # if str(url).endswith('.html'):
            #
            #     split_url = url.split('/', 3)
            #     links.add(split_url[0] + '//' + split_url[2] + item.attrs['href'])
            #
            # else:
            #
            #     links.add(url + item.attrs['href'])


        else:
            continue


    if dict[url] not in dict:

    dict[url] = {'title': title,
             'links': links}





    # site_map('http://0.0.0.0:8000/example.html')
    # for link in links:
    #
    #
    #     site_map(link)


    return print(dict)


site_map('http://0.0.0.0:8000')