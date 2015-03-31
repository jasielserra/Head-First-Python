Python 3.4.0 (default, Apr 11 2014, 13:05:18) 
[GCC 4.8.2] on linux
Type "copyright", "credits" or "license()" for more information.
>>> man = []
>>> other = []
>>> import os
>>> os.getcwd()
'/home/serra'
>>> os.ch
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    os.ch
AttributeError: 'module' object has no attribute 'ch'
>>> os.chdir('/home/serra/Documentos/hfpy_code/chapter3')
>>> os.getcwd()
'/home/serra/Documentos/hfpy_code/chapter3'
>>> try:
	with open('sketch.txt') as data:
		for each_line in data:
			try:
				(role, line_spoken) = each_line.split(':',1)
				line_spoken = line_spoken.strip()
				if role == 'Man':
					man.append(line_spoken)
				elif role == 'Other Man':
					other.append(line_spoken)
			except ValueError:
				pass
except IOError:
	print("The datafile is missing")

	
>>> man
['Is this the right room for an argument?', "No you haven't!", 'When?', "No you didn't!", "You didn't!", 'You did not!', 'Ah! (taking out his wallet and paying) Just the five minutes.', 'You most certainly did not!', "Oh no you didn't!", "Oh no you didn't!", "Oh look, this isn't an argument!", "No it isn't!", "It's just contradiction!", 'It IS!', 'You just contradicted me!', 'You DID!', 'You did just then!', '(exasperated) Oh, this is futile!!', 'Yes it is!']
>>> other
["I've told you once.", 'Yes I have.', 'Just now.', 'Yes I did!', "I'm telling you, I did!", "Oh I'm sorry, is this a five minute argument, or the full half hour?", 'Just the five minutes. Thank you.', 'Anyway, I did.', "Now let's get one thing quite clear: I most definitely told you!", 'Oh yes I did!', 'Oh yes I did!', 'Yes it is!', "No it isn't!", 'It is NOT!', "No I didn't!", 'No no no!', 'Nonsense!', "No it isn't!"]
>>> try:
	with open('man_data.txt','w') as man_file, open('other_data.txt','w') as other_file:
		print(man, file=man_file)
		print(other, file=other_file)
except IOError as err:
	print("File error" + str(err))

	
>>> 
