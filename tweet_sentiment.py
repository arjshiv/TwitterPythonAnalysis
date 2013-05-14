import sys
import json
import re

#This program runs my tweets through a dictionary of sentiments and computes the sentiment of the tweet

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def wordSplitForTweetText(tweetText):
    nonalpha = re.compile(r'[^a-z]+')
    tokens = nonalpha.split(tweetText.lower())
    return tokens
    

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)

    textString = "text"
    data = []
    with tweet_file as f:
        for line in f:
            if textString in json.loads(line).keys():
                data.append(json.loads(line)['text'])            

    #data is a list of tweet texts
    #print data[45]

    dataLength = len(data)

    #Code from the assignment help website
    afinnfile = sent_file
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        term = term.lower().decode('utf-8') #convert keys to lowercase and format in utf-8
        scores[term] = int(score)  # Convert the score to an integer.

    sentiments = [] #This will store our final sentiment values

    for counter in range (0, dataLength):
##        print "Tweet #", counter, ":", data[counter]
        score = 0
        if(wordSplitForTweetText(data[counter])):
            for word in wordSplitForTweetText(data[counter]):
                if word.lower().decode('utf-8') in scores.keys():
                    score += scores[word]
            

##        else: #else score defaults to zero
##            print "No English words in Tweet #", counter
            
    
        sentiments.append(score)



    for counter in range(0, dataLength):
        print sentiments[counter]


    #print type(scores)		
##    for score in scores:
##		print score,":",scores[score] # Print every (term, score) pair in the dictionary
    
    
    
if __name__ == '__main__':
    main()
        

