word='Deleveled'


my_list=[]
new_list=[]
wrd=''
for x in word:
	my_list.append(x.lower())

print(my_list[::-1])


new_list=my_list[::-1]

print(new_list)

for x in new_list:
	wrd+=x

print(word,'\n')
print(wrd)