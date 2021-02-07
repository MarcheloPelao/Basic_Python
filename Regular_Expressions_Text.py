texto='''"Ethics are build right into the idals and objetives of the United 
Nation" #USNG @ NY Society for Ethical Culture bit.ly/2guVerg  @UN
@UN_WOMEN'''

texto1=texto.split(' ')
print(texto1)

#finding specific words
# HASGTAG

[print(i) for i in texto1 if i.startswith('#')]

'''
match something after '@' 
alphabet, numbers,special symbols '_'
'''
import re

[print(i) for i in texto1 if re.search('@[A-Za-z0-9_]+',i)]

[print(i) for i in texto1 if re.search('@\w+',i)] #lo mismos que arriba, con
#meta caracteres

''' finding specific characters'''

text2='ouagadougou'
#find all vowel
print(re.findall(r'[aeiou]',text2))
#not a vowel
print(re.findall(r'[^aeiou]',text2))

#Regular expression for dates

datestr='23-10-2002\n23/10/2002\n23/10/02\n10/23/2002\n23 Oct 2002\n23 '\
        'October 2002\nOct 23, 2002\nOctober 23, 2002\n'
print(re.findall(r'\d{2}[/-]\d{2}[/-]\d{4}',datestr))

print(re.findall(r'\d{2}[/-]\d{2}[/-]\d{2,4}',datestr)) #2 o 4 digit year

#1 o 2 ; 2 o 4 digit in date
print(re.findall(r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}',datestr))

print(re.findall(r'\d{2}\s(?:Jan|Feb|Mar|Apr|May|'
                 r'Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{4}',datestr))

print(re.findall(r'\d{2}\s(?:Jan|Feb|Mar|Apr|May|'
                 r'Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s\d{2,4}',datestr))

print(re.findall(r'(?:\d{2}\s)?(?:Jan|Feb|Mar|Apr|May|'
                 r'Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s(?:\d{2},\s)?\d{4}'
                 ,datestr))

print(re.findall(r'(?:\d{1,2}\s)?(?:Jan|Feb|Mar|Apr|May|'
                 r'Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s(?:\d{1,2},\s)?\d{2,4}'
                 ,datestr))

