#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Just seeing the ratio of retweets
"""

import json
import sys
import codecs

def main():
	file_name = sys.argv[1]

	with codecs.open(file_name, 'r', 'utf-8') as tweets_file:
		count = 0
		for line in tweets_file:
			try:
				tweet = json.loads(line)
				if "RT" not in tweet["text"]:
					count += 1
			except:
				continue
		print count


if __name__ == "__main__":
	main()
