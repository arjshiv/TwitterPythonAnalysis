import sys
import json
import re

#This code identifies the sentiment of words which are not already in our repositories by computing them from the sentiment of each tweet

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

    sentiments = {}

    for counter in range (0, dataLength):
##        print "Tweet #", counter, ":", data[counter]
        score = 0
        if(wordSplitForTweetText(data[counter])):
            for word in wordSplitForTweetText(data[counter]):
                if scores.has_key(word.lower().decode('utf-8')):
                    score += scores[word]
            

        sentiments[data[counter]] = score

        #sentiments is now a dictionary with the tweet
        #as key and its score as value

        newSentiments = {}
        frequency = {}

    for counter in range (0, dataLength):
        score = 0
        if(wordSplitForTweetText(data[counter])):
            for word in wordSplitForTweetText(data[counter]):
                if (word): #make sure you dont have blank strings
                    #I'm updating the frequency of each word first
                    if frequency.has_key(word.lower().decode('utf-8')):
                        frequency[word] += 1
                    else:
                        frequency[word] = 1
                    #Now check for the word in the tweet    
                    if not scores.has_key(word.lower().decode('utf-8')):
                        if not newSentiments.has_key(word.lower().decode('utf-8')):
                            newSentiments[word] = 0 #Now the dictionary has keys of all the words not in the sentiment file

	#Research paper used : O'Connor, B., Balasubramanyan, R., Routedge, B., & Smith, N. From Tweets to 
	#Polls: Linking Text Sentiment to Public Opinion Time Series. (ICWSM), May 2010.
    #From the paper, sentiment score of a word = #positive tweets/#negative tweets
    #Loop through each tweet which has the word, and add positive tweets and negative tweets

    for key in newSentiments.keys():
        pos_tweets = 0.0
        neg_tweets = 1.0 #To avoid division by zero
        #Now loop through each tweet
        for tweet in sentiments.keys():
            if key in tweet: #Check for substring - the word is present in the tweet text
                if sentiments[tweet] < 0:
                    neg_tweets += 1.0
                else:
                    pos_tweets +=1.0

        newSentiments[key] = pos_tweets/neg_tweets



    for key in newSentiments.keys():
        print key, round(newSentiments[key],2) #round to two digits
    


##############main#######################

    
if __name__ == '__main__':
    main()
