import urllib
from urllib import request
import urllib.parse
import re
import tkinter as tk
import random
#from crawler_seed_url2 import *


window = tk.Tk()
window.title("My APP")

# ------window size
window.geometry("1000x600")

# ------label
title = tk.Label(text="Welcome to my web crawler GUI", font=("Times New Roman", 20))
title.grid(column=2, row=0)

# ------entry field
entry_field1 = tk.Entry()
entry_field1.grid(column=2, row=1)
url = str(entry_field1.get())

#def phrase_generator():
    #phrases =["Hello ", "How are you? ", "What are you looking for ", "Have a good Day  "]
    #url  = str(entry_field1.get())
    #return phrases[random.randint(0, 4)] + name


# ----THE CRAWLER---

def test_method(url):
    #url = 'http://www.dndi.org'
    values = {'s': 'basics', 'submit': 'search'}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

        # print (respData)
    paragraphs = re.findall(r'<.*?>', str(respData))
    str_result = ""

    for eachP in paragraphs:
        str_result += str(eachP)+"\n"
        print(eachP)
# ---END OF CRAWLER---
    return str_result

def phrase_display():
    url = str(entry_field1.get())
    str_result = test_method(url)
    #greeting = [test_method()]

    # creates the text field
    greeting_display = tk.Text(master=window, height=30, width=120)
    greeting_display.grid(column=2, row=3)

    greeting_display.insert(tk.END, str_result)

# button
button1 = tk.Button(text="Search", bg="green", font=("Times New Roman", 15), command=phrase_display)
button1.grid(column=2, row=2)


window.mainloop()

