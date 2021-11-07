import requests
from bs4 import BeautifulSoup
import tkinter as tk
from PIL import ImageTk

def getHotMessage():
    url = 'http://www.baidu.com/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

    response = requests.get(url,headers = headers)

    soup = BeautifulSoup(response.text,'lxml')
    listResult = soup.select('span.title-content-title')

    messageList = []

    for i in listResult:
        messageList.append(str(i).split('<span class="title-content-title">')[1].split('</span>')[0])
    return messageList

def show():
    global window
    window = tk.Tk()
    window.title('热点获取')
    window.geometry('900x500')

    messages = getHotMessage()
    x = 50
    y = 50
    index = 1
    for m in messages:
        textLabel = tk.Label(window,text = str(index) + '、' + m,font = ('Arial',29),foreground = 'black',compound = 'center')
        textLabel.place(x = x,y = y)
        y += 60
        index += 1

    window.mainloop()

show()