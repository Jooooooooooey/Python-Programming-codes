'''
Huiyu Zhang
Assignment#10
TA:Vipra Gupta
'''
#In this assignment, I am writing a program that converts common testing
#abbreviations to English words.


#This function aims to read a given file and generate a dictionary
def CreateDictionary(filename):
	Dict={}
	f=open(filename)              # f refers to file
	for line in f:
		index=line.find(",")
		key=line[:index]
		value=line[index+1:]
		Dict[key]=value
	return Dict

#This function aims to return a deslanged string which is translated 
#from a given slang
def Deslang(slang, wordDictionary):
	splitSlang=slang.split()      #split the string
	for i in range(0,len(splitSlang)):
		if splitSlang[i] in wordDictionary:
			splitSlang[i]=wordDictionary[splitSlang[i]][:-1]
	new=' '.join(splitSlang)      #connect every element in the list
	return new
	
def main():
	#test a
	wordDictionary=CreateDictionary("textToEnglish.txt")
	#test b
	abbre=raw_input("Enter a text abbreviation:")  #abbre refers to abbreviation
	if abbre in wordDictionary:
		print wordDictionary[abbre][:-1]
	else:
		print "Not Found"
	answer=raw_input("Do you still want to enter a text abbreviation(yes or quit): ")
	while answer=="yes":
		abbre=raw_input("Enter a text abbreviation:")
		if abbre in wordDictionary:
			print wordDictionary[abbre][:-1]
		else:
			print "Not Found"
		answer=raw_input("Do you still want to enter a text abbreviation(yes or quit): ")

	#test c
	slang=raw_input("Enter an arbitrary number of text abbreviations, separated by a space: ")
	newSentence=Deslang(slang,wordDictionary)
	print newSentence
	answer2=raw_input("Do you still want to play this games? (yes or quit): ")
	while answer2=="yes":
		slang=raw_input("Enter an arbitrary number of text abbreviations, separated by a space: ")
		newSentence=Deslang(slang,wordDictionary)
		print newSentence
		answer2=raw_input("Do you still want to play this games? (yes or quit): ")
		
	

main()
		
		

