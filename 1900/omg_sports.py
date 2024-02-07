def find_mode(x):
	freq = {}
	for item in x:
		if item in freq:
			freq[item] += 1
		else:
			freq[item] = 1
			max_freq = 0
	for index, (value, count) in enumerate(freq.items()):
		if count > max_freq:
			max_freq = count
			ret = []	
	for index, (value, count) in enumerate(freq.items()):
		if count == max_freq:
			ret.append(value)
	return ret


def find_player_mode(scores, p):
	return find_mode(scores[p])


def find_game_mode(scores, g):
	game_scores = []
	for i in range(len(scores)):
		game_scores.append(scores[i][g])
	return find_mode(game_scores)

if __name__ == '__main__':
	scores = [

	[20, 27, 16, 23, 20, 27, 18],
	[8, 18, 11, 17, 9, 12, 0],
	[34, 19, 25, 22, 19, 25, 31],
	[17, 8, 11, 34, 15, 0, 9],
	[2, 0, 3, 0, 10, 2, 0]

	]

print(find_player_mode(scores, 0))

print(find_player_mode(scores, 3))

print(find_player_mode(scores, 4))

print(find_game_mode(scores, 0))

print(find_game_mode(scores, 2))
