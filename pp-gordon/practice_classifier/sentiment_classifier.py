#!/usr/bin/env python
# -*-encoding: utf-8 -*-

"""
This is a script that, in the end, should be able to classify a tweet
into positive, negative or neutral
"""
import sys
# editing path to import modules
# just the folder above
sys.path.append('../')
import tokenizer
import codecs
import json
from os import path

def read_tweets(file_name):
	tweets = {}
	with codecs.open(file_name, 'r', 'utf-8') as tweets_to_read:
		for line in tweets_to_read:
			try:
				tweet = json.loads(line)
				tweets[tweet['id']]= tweet
			except:
				continue
	return tweets

def tweet_tokenizer(to_tokenize):
	tok = tokenizer.Tokenizer(preserve_case=False)
	return(tuple(tok.tokenize(to_tokenize)))

def lexicon_extractor(list_of_lexicons):
	final_polar_words = []
	file_path = path.relpath("../lexicons/")
	for lexicon in list_of_lexicons:
		lexicon_path = file_path + '/' + lexicon
		with codecs.open(lexicon_path, 'r', 'utf-8') as read_lexicon:
			polar_words = [line for line in read_lexicon if line.startswith(';') == False]
			final_polar_words += polar_words

	return set(final_polar_words)

def neutrality_tester():
	print 'test'


def main():
	# importing the tweets to be annotated
	tweets = read_tweets("hilary_trump_23_07_2016.dat")

	positive_lexicons = ["positive-words-Bing.txt"]
	negative_lexicons = ["negative-words-Bing.txt"]
	positive_lexicon = lexicon_extractor(positive_lexicons)
	negative_lexicon = lexicon_extractor(negative_lexicons)

	for tweet in tweets:

		print tweets[tweet]['text']
		tokenized_tweet = tweet_tokenizer(tweets[tweet]['text'])
		
		#neutrality_tester()
		answer = raw_input('press s to stop')
		if answer == 's':
			break

if __name__ == "__main__":
	main()
