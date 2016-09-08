import sys
import codecs
import json

"""
This goes through the annotated folder and deletes the duplicates
"""


def main():
    unique_tweets = {}
    with codecs.open("annotated_for_entities.dat", 'r', 'utf-8') as file_open:
        for line in file_open:
            tweet = json.loads(line)
            if tweet['id'] not in unique_tweets:
                unique_tweets[tweet['id']] = tweet
    print len(unique_tweets)

    with codecs.open("annotated_for_entities_new.dat", 'w', 'utf-8') as out_file:
        for thing in unique_tweets:
            json.dump(unique_tweets[thing], out_file)
            out_file.write("\n")
                


if __name__ == '__main__':
    main()
