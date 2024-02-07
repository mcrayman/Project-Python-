




cand = {}
idnum = 1
while idnum > 0:
	idnum = int(input('Enter candidate’s ID number (1-10741, any integer less than 1 to exit):'))
	if idnum > 10741:
		print('Invalid ID number!')
	if idnum in cand:
		cand[idnum] += 1
	else:
		cand[idnum] = 1

print('Vote Counts \n-----------')

for i in cand:
	if i != 0:
		print(f'Candidate {i}: ',cand[idnum], 'votes')

print()
print('Election Winner(s)\n------------------')

