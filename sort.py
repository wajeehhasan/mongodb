import random
my_lit=[]

for x in range(10):
	my_lit.append(random.randint(1,50))

temp=None



def sor_ted(my_lit):
	if my_lit==sorted(my_lit):
		print("here you go")
		return(my_lit)
	else:
		for x in range(len(my_lit)):
			for x in range(len(my_lit)-1):
				temp=my_lit[x]
				if my_lit[x]<my_lit[x+1]:
					my_lit[x]=my_lit[x+1]

				my_lit[x+1]=temp
		return sor_ted(my_lit)


print(my_lit)