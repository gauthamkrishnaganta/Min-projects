# every python file -> is a module -> import keyword -> __name__ ->
'''
import day4_revision
print(dir(day4_revision)) #dir -> directory will return all available methods,attributes
#print(type(day4_revision.cricket))
#print(type(day4_revision.details))
day4_revision.cricket(
    "India", "Australia",
    rohit=57, kohli=154, gill=34)
#print(day4_revision.details.keys())
#print(day4_revision.details['team'])
day4_revision.details.update({'players':["virat","Ms Dhoni","rohit","bumrah"],
                              'indian_players': 16

})
print(day4_revision.details)

#from - keyword
import day4_revision
from day4_revision import cricket,details
details.update({'players':["virat","Ms Dhoni","rohit","bumrah"],
                              'indian_players': 16})

print(day4_revision.__doc__)# returns doc string from the given module
#Built-in-Modules -> math, random, os, time, datetime
#download modules -> pypi(The Python Package Index)
# build a qr code scanner using python -> linkdin URL
'''
import pyqrcode
import png
#create a QRcode by giving a Github link
git_link = "https://github.com/gauthamkrishnaganta"
qr = pyqrcode.create(git_link)
qr.png("Git.png",scale = 10)



