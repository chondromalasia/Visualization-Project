#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A script that I'll use to annotate whether or not they're the right Hillaries or not
appends _edit to the name of the file, or edits an already edited one
Todo:

needs to be able to check to see if it has already been annotated
do some comments
"""

import json
import sys
import codecs

def ask():
	return raw_input("[h] = clinton; [t] = trump; [b] = both; [n] = neither; [d] = done: ")

def annotate(tweet_to_anno):

	print tweet_to_anno["text"] + '\n'
	answer_good = False
	answer = ''
	while answer_good == False:
		answer = ask()
		if answer == 'd':
			return False
		elif answer not in ['h', 't', 'b', 'n']:
			print "Try Again"
		else:
			answer_good = True

	tweet_to_anno["entity"] = answer

	return tweet_to_anno

def main():
	list_of_tweets = []
	with codecs.open(sys.argv[1], 'r', 'utf-8') as tweets_loaded:
		for tweet in tweets_loaded:
			try:
				list_of_tweets.append(json.loads(tweet))
			except:
				continue


		
	for i in range(len(list_of_tweets)):
		new_tweet = annotate(list_of_tweets[i])
		if new_tweet == False:
			print 'donezo'
			break
		else:
			list_of_tweets[i] = new_tweet

	# done with classifying, writing it to new thing
	file_name = ''
	if "_edit" in sys.argv[1]:
		file_name = sys.argv[1]
	else:
		file_name = sys.argv[1][:-4] + "_edit" + ".txt"

	with codecs.open(file_name, 'w', 'utf-8') as write_file:
		for entry in list_of_tweets:
			json.dump(entry, write_file)
		write_file.write("\n")

if __name__ == "__main__":
	main()
