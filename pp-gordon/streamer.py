#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy 
import json
import sys
from datetime import date
import codecs


class MyStreamListener(tweepy.StreamListener):

        def __init__(self, file_name):
                self.write_file = file_name
                self.count = 0
                self.max = 1000

        

	def on_data(self, data):
		tweet = json.loads(data)
                try:
                        if self.count > self.max:
                                return False
                        elif "RT" not in tweet["text"] and "https://t.co" not in tweet["text"]:
                                self.count += 1
                                print self.count
                                with codecs.open(self.write_file, 'a', 'utf-8') as write_out:
                                        json.dump(tweet, write_out)
                                        write_out.write("\n")
                except KeyError:
                        print 'key errrrrrr'
                        

	def on_error(self, status):
		print (status)

def main():
	CONSUMER_KEY = 'SE5gaC6dWv4gWLOv9kNavyvz2'
	CONSUMER_SECRET = 'iCuXVKtvKa3L3mKfWznAv1YV7IRLa8CmAmWZ5Iudvx9yavJE1p'
	ACCESS_KEY = '755408587200102400-X4i55C0tGRR1KBTC9ZNBfC7hjk4X24o'
	ACCESS_SECRET = 'IQqrlRfw9JZhi0WkKL0OcQECOxbdZ9eNBNYJQzpY0PQUs'

	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	api = tweepy.API(auth)

        #these are what we're filtering for
        to_filter = ['Hillary', 'Trump']

        #creates a file with the filter terms and the date
        output_filename = '_'.join(to_filter)+'_'
        d = date.today()
        #not proud of this, could have been more elegant
        output_filename = output_filename + str(d.timetuple()[2]) + '_' + str(d.timetuple()[1]) + '_' + str(d.timetuple()[0]) + '.dat'

        #create the file to write the things to
        with open(output_filename, 'w') as to_write:
                pass

	myStreamListener = MyStreamListener(output_filename)
	myStream = tweepy.Stream(auth, myStreamListener)


	myStream.filter(track=to_filter)

if __name__ == "__main__":
	main()
