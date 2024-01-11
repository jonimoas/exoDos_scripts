import xml.etree.ElementTree as ET 
import requests
from dict2xml import dict2xml
import os

imagePriorities = [{'prio':1,'type':'Box - Front'},{'prio':2,'type':'Clear Logo'},{'prio':3,'type':'Box - 3D'}]

tree = ET.parse("MS-DOS.xml") 
metatree = ET.parse("Metadata.xml") 

f = open("gamelist.xml", "a")
f.write('<gameList>\n')
f.close()

emugames = []
root = tree.getroot()
metaroot = metatree.getroot()

imagePriorities.sort(key=lambda x: x['prio'])

for game in root.findall('./Game'):
    emustationgame = {}
    try:
        emustationgame['name'] = game.find('Title').text
        images = []
        for xmlimages in metaroot.iter('GameImage'):
            try:
                if xmlimages.find('DatabaseID').text == game.find('DatabaseID').text:
                    images.append(xmlimages)
            except:
                None
        filename = None
        for prio in imagePriorities:
            for image in images:
                if image.find('Type').text == prio['type']:
                    filename = image.find('FileName').text
                    break
            if filename is not None:
                break
        if filename == None and len(images) > 0:
            filename = images[0].find('FileName').text
        if filename is not None:
            finalFilename = game.find('Title').text.replace(':','-').replace('?','-').replace('>','-').replace('<','-').replace('*','-') + "-image." + filename.split('.')[-1]
            if not os.path.isfile('images/' + finalFilename):
                response = requests.get('https://images.launchbox-app.com/' + filename)
                open('images\\' + finalFilename, "wb").write(response.content)
            emustationgame['image'] = './images/' + finalFilename
    except Exception as e:
        print(e)
    emustationgame['path'] = './' + game.find('ApplicationPath').text.split('\\')[-1]
    emustationgame['desc'] = game.find('Notes').text
    emustationgame['developer'] = game.find('Developer').text
    try:
        emustationgame['genre'] = game.find('Genre').text.split(';')[0]
    except:
        None
    print(dict2xml({'game':emustationgame}))
    f = open("gamelist.xml", "a", encoding="utf-8")
    f.write(dict2xml({'game':emustationgame}) + '\n')
    f.close()

f = open("gamelist.xml", "a")
f.write('</gameList>')
f.close()



