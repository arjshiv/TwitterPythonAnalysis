import sys
import json
import re

#This file returns the frequencies of each word in a list of tweets
#we only need one command line argument - The tweet file
def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def wordSplitForTweetText(tweetText):
    nonalpha = re.compile(r'[^a-z]+')
    tokens = nonalpha.split(tweetText.lower())
    return tokens
    

def main():
    tweet_file = open(sys.argv[1])

    
    textString = "text"
    data = []
    with tweet_file as f:
        for line in f:
            if textString in json.loads(line).keys():
                data.append(json.loads(line)['text'])            

    #data is a list of tweet texts
    #print data[45]

    dataLength = len(data)

    frequency = {}

    for counter in range (0, dataLength):
        if(wordSplitForTweetText(data[counter])):
            for word in wordSplitForTweetText(data[counter]):
                if (word): #make sure you dont have blank strings
                    #I'm updating the frequency of each word first
                    if frequency.has_key(word.lower().decode('utf-8')):
                        frequency[word] += 1
                    else:
                        frequency[word] = 1


    #Frequency = #occurrences of the word/#occurrences of all words
    #Loop through each key, and divide by the sum of all values

    totalOccurrencesOfAllWords = 0

    for key in frequency:
        totalOccurrencesOfAllWords += frequency[key]

    totalOccurrencesOfAllWords *= 1.0 #make it a float
    
    for key in frequency:
        frequency[key] /= totalOccurrencesOfAllWords
        print key, round(frequency[key], 3)


##    


##############main#######################

    
if __name__ == '__main__':
    main()
