"""
The long and short of it is that this just counts tweets about each one
of these jackals
Right now it's just one file, but the plan is that it goes through
every .dat and starts to do its thing
"""
import os
import codecs
import json
import sys
sys.path.append('../')
import tokenizer

def tweet_generator(to_read):
	"""
	Creates generator object for tweets in file
	"""
	with codecs.open(to_read, 'r', 'utf-8') as tweets:
		for line in tweets:
			try:
				yield json.loads(line)
			except:
				continue

def hillary_or_trump(tweet, tokenizer_thing):
	to_test = tokenizer_thing.tokenize(tweet['text'])
	print to_test
	# if hilary is mentioned in a tweet
	for word in to_test:
		if u'hillary' in word:
			if u"trump" in word:
				return 'b'
			else:
				return 'h'
		elif u"trump" in word:
			return 't'
	return 'n'
		

def main ():
	new_tweet_generator = tweet_generator("../Hillary_Trump_24_8_2016.dat")
	keep_going = True
	count = 0
	tok = tokenizer.Tokenizer(preserve_case=False)
	#order: hilary, trump, both, neither
	names_count = [0, 0, 0, 0]
	while keep_going:
		try:
			count += 1
			whois = hillary_or_trump(next(new_tweet_generator),tok)
			print type(whois)
			if whois == 'h':
				names_count[0] += 1
			elif whois == 't':
				names_count[1] += 1
			elif whois == 'b':
				names_count[2] += 1
			else:
				names_count[3] +=1
			print names_count
		except StopIteration:
			print 'looks like the end of file'
			keep_going = False
		except Exception,e:
			print str(e)

	
	

if __name__ == "__main__":
	main()
