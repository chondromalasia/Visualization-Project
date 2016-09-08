import json
import sys

file_name = sys.argv[1]

tweets_data = []
tweets_file = open(file_name, "r")
count = 0
for line in tweets_file:
	count += 1
	
	try:
		tweet = json.loads(line)
		tweets_data.append(tweet)
	except:
		continue

print len(tweets_data)
print count
