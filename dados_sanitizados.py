#import os
#os.chdir('/home/serra/Documentos/hfpy_code/chapter5')
from sanitize import sanitize

with open('james.txt') as james_file:
    james_data = james_file.readline()
    james = james_data.strip().split(',')

with open('julie.txt') as julie_file:
    julie_data = julie_file.readline()
    julie= julie_data.strip().split(',')

with open('mikey.txt') as mikey_file:
    mikey_data = mikey_file.readline()
    mikey = mikey_data.strip().split(',')

with open('sarah.txt') as sarah_file:
    sarah_data = sarah_file.readline()
    sarah = sarah_data.strip().split(',')

clean_james = []
clean_julie = []
clean_mikey = []
clean_sarah = []

for each_t in james:
    clean_james.append(sanitize(each_t))

for each_t in julie:
    clean_julie.append(sanitize(each_t))

for each_t in mikey:
    clean_mikey.append(sanitize(each_t))

for each_t in sarah:
    clean_sarah.append(sanitize(each_t))

print(sorted(clean_james))
print(sorted(clean_julie))
print(sorted(clean_mikey))
print(sorted(clean_sarah))
