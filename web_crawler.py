'''
Web Crawler:

This script takes a site URL as an argument
and creates a map of that domain as a Python dictionary.
Script will work properly with exemplary site:
url: http://0.0.0.0:8000
'''


import requests, bs4


dict = {}


def site_map(url):

    '''This function takes url (http://0.0.0.0:8000) as parameter
    and creates a python dictionary. Dictionaries contain
    URL, title and links within every site.'''

    res = requests.get(url)     # create response object

    try:
        # check if the page does exist
        res.raise_for_status()

    except Exception as exc:
        print('Error has occured:\t %s' % (exc))

    # create Beautiful soup object
    siteSoup = bs4.BeautifulSoup(res.text, features='html.parser')

    titleSoup = siteSoup.select('title')    # search for website title
    title = titleSoup[0].getText()

    linksSoup = siteSoup.find_all('a')      # search for links

    links = set()

    url_split = url.split('/',3)    # get index site url from url parameter
    index_url = url_split[0] + '//' + url_split[2]


    # iterate trough found links
    for item in linksSoup:

        if item in links:
            # skip if link already in set
            continue

        elif index_url in item.attrs['href']:
            # add link if it contains index site url
            links.add(item.attrs['href'])

        elif item.attrs['href'].startswith('/'):
            # add link to subpage
            links.add(index_url + item.attrs['href'])

        else:
            # skip if its link to external site
            continue


    # create new item in dictionary
    dict[url] = {'title': title,
                'links': links}


    # iterate trough links found on website
    for link in links:

        if link in dict:
            # skip if link is already a key in dictionary
            continue

        else:
            # perform recursion trough the rest of links
            # in links set.
            site_map(link)

    return dict     # return complete dictionary


site_map('http://0.0.0.0:8000')

print(dict)