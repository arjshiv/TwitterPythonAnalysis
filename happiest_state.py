import sys
import json
import re

#Finds the happiest state in the US based on a set of results

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


    #Dictionary of states in the US
    ## {{{ http://code.activestate.com/recipes/577305/ (r1)
    stateDictionary = {
            'AK': 'Alaska',
            'AL': 'Alabama',
            'AR': 'Arkansas',
            'AS': 'American Samoa',
            'AZ': 'Arizona',
            'CA': 'California',
            'CO': 'Colorado',
            'CT': 'Connecticut',
            'DC': 'District of Columbia',
            'DE': 'Delaware',
            'FL': 'Florida',
            'GA': 'Georgia',
            'GU': 'Guam',
            'HI': 'Hawaii',
            'IA': 'Iowa',
            'ID': 'Idaho',
            'IL': 'Illinois',
            'IN': 'Indiana',
            'KS': 'Kansas',
            'KY': 'Kentucky',
            'LA': 'Louisiana',
            'MA': 'Massachusetts',
            'MD': 'Maryland',
            'ME': 'Maine',
            'MI': 'Michigan',
            'MN': 'Minnesota',
            'MO': 'Missouri',
            'MP': 'Northern Mariana Islands',
            'MS': 'Mississippi',
            'MT': 'Montana',
            'NA': 'National',
            'NC': 'North Carolina',
            'ND': 'North Dakota',
            'NE': 'Nebraska',
            'NH': 'New Hampshire',
            'NJ': 'New Jersey',
            'NM': 'New Mexico',
            'NV': 'Nevada',
            'NY': 'New York',
            'OH': 'Ohio',
            'OK': 'Oklahoma',
            'OR': 'Oregon',
            'PA': 'Pennsylvania',
            'PR': 'Puerto Rico',
            'RI': 'Rhode Island',
            'SC': 'South Carolina',
            'SD': 'South Dakota',
            'TN': 'Tennessee',
            'TX': 'Texas',
            'UT': 'Utah',
            'VA': 'Virginia',
            'VI': 'Virgin Islands',
            'VT': 'Vermont',
            'WA': 'Washington',
            'WI': 'Wisconsin',
            'WV': 'West Virginia',
            'WY': 'Wyoming'
    }

    #Set each sentiment to zero



    textString = "text"
    countryString = "United States"

    #I'm preserving the code from problem 2 so that I can re-use it
    data = [] #Array of the text in each tweet
    state = [] #Array of the state from which each tweet was made, same order as data
    
    with tweet_file as f:
        for line in f:
            if json.loads(line).has_key(textString): #Confine to tweets with text & location data
                if (json.loads(line)['place']):
                    if(json.loads(line)['place']['country'].lower() == countryString.lower()):
                        if json.loads(line)['place']['full_name'].split()[1] in stateDictionary:
                            data.append(json.loads(line)['text'])
                            state.append(json.loads(line)['place']['full_name'].split()[1])
                            #The previous line takes the state name and puts it into state


    #data is a list of tweet texts
##    for count in range(0, len(state)):
##        print state[count]


    dataLength = len(data)

    #Code from the assignment help website
    afinnfile = sent_file
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        term = term.lower().decode('utf-8') #convert keys to lowercase and format in utf-8
        scores[term] = int(score)  # Convert the score to an integer.

    stateSentiments = {} #Make a dictionary with State name as key and sentiment as values

#Code from problem 2, modified for our purposes
    for counter in range (0, dataLength):
        score = 0
        if(wordSplitForTweetText(data[counter])):
            for word in wordSplitForTweetText(data[counter]):
                if word.lower().decode('utf-8') in scores.keys():
                    score += scores[word]
        
            
        if (stateSentiments.has_key(state[counter])):
            stateSentiments[state[counter]] += score
        else:
            stateSentiments[state[counter]] = score

    #List of the keysSort in descending order of happiness, eg. (AZ, NY, UT)        
    stateSentimentsList = sorted(stateSentiments, key = stateSentiments.get, reverse = True)
    
    print stateSentimentsList[0] #Print the first key - i.e. the happiest state
    
if __name__ == '__main__':
    main()
        

