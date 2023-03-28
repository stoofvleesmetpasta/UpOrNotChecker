import platform
import subprocess
import json

#ping functie aanmaken

def ping(host):
    parameter = '-n' if platform.system().lower()=='windows' else '-c'

    command = ['ping', parameter, '1', host]
    response = subprocess.call(command)

    if response == 0:
        return True
    else:
        return False

#webstites importeren of toevoegen
adresslist = open("week6/adressen.json", "r")
adressen = json.load(adresslist)
test = adressen["urls"]

add = input("geef een adres in om te checken. ")
if add != "":
    adressen["urls"].append(add)
    adresslist = open("week6/adressen.json", "w")
    json.dump(adressen, adresslist, indent= 4)



#html in orde krijgen
def html(test):
    midden=""
    boven = '{"html": "<html><head><title>My Website</title></head><body><h1>Sitecheck</h1>'
    onder = '</body></html>"}'

    for a in test:
        if ping(a) == True:
            midden = midden + f"<h2>{a} is actief<h2>"
        else:
            midden = midden +f"<h2>{a} is niet actief<h2>"

    display = boven + midden + onder

    data = open("week6/data.json", "w")
    data.write(display)

    data = open("week6/data.json", "r")
    data = json.load(data)
    html = data['html']

    checkdisplay = open("week6/index.html", "w")
    checkdisplay.write(html)
    checkdisplay.close()

html(test)