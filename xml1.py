import xml.etree.ElementTree as ET 
data = '''<person>
        <name>Subash</name>
        <phone types= "initl"> 9860533921</phone>
        <email hide = "Yes"/>
        </person>'''
        
tree = ET.fromstring(data)
print('Name: ', tree.find('name').text)
print('Attr: ', tree.find('email').get('hide'))
