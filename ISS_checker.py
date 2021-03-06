import urllib.request
from xml.etree import ElementTree
from datetime import datetime, date, time
today_beginning = datetime.combine(date.today(), time())
url = "https://spotthestation.nasa.gov/sightings/xml_files/Ireland_None_Dublin.xml"

sighting_list = []
with urllib.request.urlopen(url) as response:
    xml = response.read().decode()
    tree = ElementTree.fromstring(xml)[0]
    for node in tree:
        if node.tag == "item":
            sighting_list.append(node)


for event in reversed(sighting_list):
    title = event.find("title").text.split()
    event_time = datetime.strptime(title[0], '%Y-%m-%d')
    if today_beginning <= event_time:
        description = title[1] +" "+title[2]+"\n"
        description += "\n".join([line.strip() for line in event.find("description").text.split("<br/>")])
        print(description)
input()
