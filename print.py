import urllib
import json

#Print all tweets corresponding to a specific search query

query = raw_input('What is your search query ?:')

nPageString = input('How many pages of results would you like ?:')

nPages = int(nPageString) + 1

for pageNumber in range(1,nPages):

	print "\n*--Page Number ", pageNumber, "---------*\n"
	urlString = "http://search.twitter.com/search.json?q="+query+"&page="+str(pageNumber)
	response = urllib.urlopen(urlString)

	pyresponse = json.load(response) #Dictionary of JSON responses
	#The key "results" stores the results of the Twitter search

	#This dictionary contains lists of dictionaries, for whom the key #"text" is the content of the tweet itself.

	results = pyresponse["results"] #List of results (list of dictionaries)

	i = 0
	for data in results: 
	####
	#loop through each element of the list and print out the text
	####
		print "\n Page", pageNumber, ", Tweet ", i+1, "---------\n"
		i = i+1
		print data["text"]
		
