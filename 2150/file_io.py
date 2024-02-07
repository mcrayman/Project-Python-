'''
Does some simple analysis on the "title.basics" data file from IMDb:
https://www.imdb.com/interfaces/

If you'd like to run this on your own, download and unzip the title.basics
data, then rename the data file to imdb_titles.tsv

This is a tab-separated values (TSV) text file.  The website above has a
description of how the file is formatted.
'''

try:
	# Open the data file for reading, and another file for writing
	# The encoding argument is needed on the first file since the IMDb files
	#  use UTF-8 encoding
	f = open('imdb_titles.tsv', 'r', encoding='UTF-8')
	f_out = open('results.txt', 'w')

	# Using readlines() reads the whole file into a single list of strings
	# lines = f.readlines()

	count = 0

	# Using the loop below reads only one line at a time (more RAM-friendly!)
	for line in f:
		# Split the current line around tabs
		fields = line.split('\t')

		# Store the individual fields into separate variables
		id_num, media_type, title_primary, title_original, is_adult, year_start, year_end, runtime, genres = fields

		try:
			# year_start and runtime (along with all the other variables from
			#  line 30) are strings, so we need to convert them to int before
			#  doing numerical comparisons.  The try-except block lets us do
			#  this without crashing the program if the conversion fails.
			year_start = int(year_start)
			runtime = int(runtime)

			# Look for all movies made between 1939-1965 that are at least 2
			#  hours in length
			if media_type == 'movie' and 1939 <= year_start <= 1965 and runtime >= 120:
				count += 1

				# Write this movie's info to f_out
				f_out.write(f'{media_type} {title_primary} {year_start} {runtime} {genres}\n')

		except ValueError:
			pass

	# Always close files when you're done working with them!
	f.close()
	f_out.close()

	# Show how many items matched our criteria after the loop finishes
	print(count)

# This exception handler runs if the file open operation fails
except FileNotFoundError:
	print('Invalid file name, try something else.')
