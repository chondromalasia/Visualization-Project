#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Annotates tweets into either hillary, trump, both or neither

saves to annotated_for_entities.dat

automatically checks to see if tweet has already been annotated
automatically writes to .dat if end of file is reached
"""

import sys
import codecs
import json

def tweet_generator():
        """
        Creates generator object for tweets in file
        """
	with codecs.open(sys.argv[1], 'r', 'utf-8') as tweets_file:
		for line in tweets_file:
			try:
				yield json.loads(line)
			except:
				continue

def test_tweet(to_test, ids):

        if "RT" in to_test["text"]:
                return False
        elif to_test["id"] in ids:
                return False
        elif "https://t.co" in to_test["text"]:
                return False
        else:
                return True

def ask():
        return raw_input("h = clinton; t = trump; b = both; n = neither; d = done: ")

def annotate_tweet(to_annotate):
        print to_annotate["text"] + '\n'
        answer_good = False
        answer = ''

        while answer_good == False:
                answer = ask()
                print "\n"
                if answer == 'd':
                        return False
                elif answer not in ['h', 't', 'b', 'n']:
                        print 'Try Again'
                else:
                        answer_good = True

        to_annotate["entity"] = answer

        return to_annotate
                

def main():
	keep_going = True
	new_tweet_generator = tweet_generator()
        annotated_tweets = []
        all_ids = []

        with codecs.open("annotated_for_entities.dat", "r", "utf-8") as read_ids:
                for line in read_ids:
                        try:
                                line = json.loads(line)
                                all_ids.append(line["id"])
                        except:
                                continue
        print "There are %d already done." % len(all_ids)

	while keep_going:
                try:
		        tweet = next(new_tweet_generator)
                        
                        # make sure it's not an RT or a previously used tweet
                        # or a link
                        if test_tweet(tweet, all_ids):
                                annotate = annotate_tweet(tweet)
                                if annotate == False:
                                        keep_going = False
                                else:
                                        annotated_tweets.append(tweet)

                        print "There are %d annotated tweets." % len(annotated_tweets)
                except:
                        keep_going = False
                finally:
                        if len(annotated_tweets) > 0:
                                with codecs.open("annotated_for_entities.dat", 'a', 'utf-8') as write_file:
                                        for tweet in annotated_tweets:
                                                json.dump(tweet, write_file)
                                                write_file.write("\n")
                        



if __name__ == "__main__":
	main()
