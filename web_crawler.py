'''Web Crawler:

This script takes a site URL as an argument
and creates a map of that domain as a Python dictionary.
Script will work properly with exemplary site:

URL: http://0.0.0.0:8000'''


import requests, bs4


dict = {}


def site_map(url):
    '''This function takes url (http://0.0.0.0:8000) as parameter
    and creates a python dictionary. Dictionaries contain
    URL, title and links within every site.'''
    res = requests.get(url)     # create response object
    try:                        # check if the page does exist
        res.raise_for_status()
    except Exception as exc:
        print('Error has occured:\t %s' % (exc))

    siteSoup = bs4.BeautifulSoup(res.text, features='html.parser')      # create Beautiful soup object
    titleSoup = siteSoup.select('title')                                # search for website title
    title = titleSoup[0].getText()
    linksSoup = siteSoup.find_all('a')                                  # search for links
    links = set()
    url_split = url.split('/',3)                                        # get index site url from url parameter
    index_url = url_split[0] + '//' + url_split[2]

    for item in linksSoup:                      # iterate trough found links

        if item in links:
            continue                            # skip if link already in set
        elif index_url in item.attrs['href']:
            links.add(item.attrs['href'])       # add link if it contains index site url
        elif item.attrs['href'].startswith('/'):
            links.add(index_url + item.attrs['href'])      # add link to subpage
        else:
            continue                            # skip if its link to external site

    dict[url] = {'title': title,                # create new item in dictionary
                'links': links}

    for link in links:          # iterate trough links found on website

        if link in dict:
            continue            # skip if link is already a key in dictionary
        else:
            site_map(link)      # perform recursion trough the rest of links
                                # in links set.
    return dict                 # return complete dictionary


site_map('http://0.0.0.0:8000')
print(dict)