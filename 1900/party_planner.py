# this program automates calculations done for party planning 

#f = friends
#c = cans
#p = packs 

def plan_party(f, c, p): #defines the function of plan_party
	f += 1 #adding self
	total_drinks = f * c
	packs = total_drinks // p
	if packs * p - total_drinks < 0:
		packs += 1
	extra = packs * p - total_drinks
	print(packs, p,'\b-pack(s) needed')
	print(extra, 'extra can(s)')

packs = plan_party(2,2,2)



def plan_party2(f, c, p):
	f += 1
	total_drinks = f * c
	packs = total_drinks // p
	if packs * p - total_drinks < 0:
		packs += 1
	return packs

#takes user input for the plan_party function

plan_party(int(input('How many friends are you throwing this party for? ')),int(input('How many cans will each person drink? ')),int(input('How many cans are in each pack? ')))
print('Return value from plan_party2 ',plan_party2(9,14,6))