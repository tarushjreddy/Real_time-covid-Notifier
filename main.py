# import plyer
import requests
import os
from bs4 import BeautifulSoup

# additional link https://www.covid19india.org
# def notify(title, text, app_icon):
#     os.system("""
#               osascript -e 'display notification "{}" with title "{}"'
#               """.format(text, title, app_icon))

import plyer
from plyer import notification
# https://upload.wikimedia.org/wikipedia/commons/8/82/SARS-CoV-2_without_background.png
# https://www.mohfw.gov.in


def notifyme(title, message):
    plyer.notification.notify(
        title=title,
        message=message,
        app_icon="SARS-CoV-2_without_background.ico",
        timeout=2
    )


def getData(url):
    r = requests.get(url)
    print(r)
    return r.text


if __name__ == "__main__":
    # notify("Title", "Heres an alert",
    #        "SARS-CoV-2_without_background.ico")

    # notify("Sunnyleone", "this is my way my life")
    myhtml = getData("https://www.mohfw.gov.in/")
    soup = BeautifulSoup(myhtml)

    # print(soup.prettify)
    # for tbody in soup.findAll("tbody"):
    # print("this is the example", tbody.get_text)
    print(soup(text="tbody"))

    abc = soup(text=lambda t: "<td>" in t)
    efg = str(abc)
    dec = BeautifulSoup(efg)

    # print(abc)
# print(c)
    result = dec.find_all("tr")
    resultt = BeautifulSoup(str(result))
    # print(resultt.get_text())
    myDataStr = ""
    # for items in resultt:
myDataStr += resultt.get_text()
print(type(myDataStr))
npm = myDataStr.split("\\n\\t")
pnp = str(npm)
car = pnp.replace("'", '')
ls = ['']
od = car.replace(", , ,", "\n")
lis = ls.append(od)
print(lis)


one = od.replace("[[,", "")

# one = od.replace("]]", "")


# print(type(od))
# for item in od:
#     print(item)


# print(myDataStr.split("\n"))
# for items in omsairam:

# print(items.split("\t"))

# print(dec.find_all("tbody"))
# print(abc.split("</td>\n\t<td>4"))
# print(c.split(""))

# https: // my-json-server.typicode.com/developerking9/indiacovid/IndiaCaseReport/1
while True:
    myHtmlData = getData("https://www.mohfw.gov.in/")
    soup = BeautifulSoup(myHtmlData, "html.parser")
    abc = ""
    for tr in soup.find_all('tbody')[1].find_all('tr'):
        abc += tr.get_text()
    abc = abc[1:]
    itemlist = abc.split("\n\n")
    states = ['karnataka', 'Telangana']
    for item in itemlist[0:22]:
        datalist = item.split('\n')
        if datalist[1] in states:
            ntitle = "cases"
            ntext = f"{datalist[1]}"
            notifyme(ntitle, ntext)
            time.sleep(2)
    time.sleep(3600)
