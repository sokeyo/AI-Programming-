import re

from urllib.request import urlopen

hyperlink = input("Please Enter web url ")

openlink = urlopen(hyperlink)

page = openlink.read().decode()

links = re.findall('"((http|ftp)s?://.*?)"', page)

#print(links)
#method for removing html markup
def remove_html_markup(s):
    tag = False
    quote = False
    out = ""

    for c in s:
        if c == '<' and not quote:
            tag = True
        elif c == '>' and not quote:
            tag = False
        elif (c == '"' or c == "'") and tag:
            quote = not quote
        elif not tag:
            out = out + c

    return out

#counting the frequency of words
def wordfrequency():
    data = remove_html_markup(page)

    wordcount = {}

    for word in data.split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

    for u, w in wordcount.items():
        order = (u, w)
        return order

#method for returning links
def returnlinks(hyperlink):
    openlink = urlopen(hyperlink)

    page = openlink.read().decode()

    links = re.findall('"((http|ftp)s?://.*?)"', page)

    return links





print(returnlinks(hyperlink))


for i in range(3):
    links1 = returnlinks(hyperlink)
    visitedlink = links1[3]
    visitedlink_n = (', '.join(visitedlink))
    visited_link_to_str = (visitedlink_n[:-7])
    print(visited_link_to_str)


    for i, link in enumerate(links1):
        newlink = (', '.join(link))
        strlink = (newlink[:-7])
        print('#%d: %s' % (i + 1, strlink))
    i = +1

#method for removing html markup
def remove_html_markup(s):
    tag = False
    quote = False
    out = ""

    for c in s:
        if c == '<' and not quote:
            tag = True
        elif c == '>' and not quote:
            tag = False
        elif (c == '"' or c == "'") and tag:
            quote = not quote
        elif not tag:
            out = out + c

    return out

#counting the frequency of words
data = remove_html_markup(page)

wordcount = {}

for word in data.split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

for u, w in wordcount.items():
        order = (u, w)
        print(order)
