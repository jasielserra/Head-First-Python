#import os
#os.chdir('/home/serra/Documentos/hfpy_code/chapter5')

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


print(sorted(james))
print(sorted(julie))
print(sorted(mikey))
print(sorted(sarah))
