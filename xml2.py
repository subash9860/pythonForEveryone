import xml.etree.ElementTree as et
input = '''<stuff>
            <users>
                <user x = "2">
                    <id> 002 </id>
                    <name> subash </name>
            </user>
            <user x = "3">
                <id> 03</id>
                <name> KC </name>
            </user>
            </users>
            </stuff>'''
stuff = et.fromstring(input)
lst = stuff.findall('users/user')
print('user count: ', len(lst))
for iteam in lst:
    print('Name:',iteam.find('name').text)
    print('Id:',iteam.find('id').text)
    print('Attridute:',iteam.get('x'))