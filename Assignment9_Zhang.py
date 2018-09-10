'''
Huiyu Zhang
Assignment#9
TA:Vipra Gupta
'''

#code testing
def main():
	print CalcNewPopulation(307357870)	
	BreakoutTime(70000)
	humanDNA="CGCAAATTTGCCGGATTTCCTTTGCTGTTCCTGCATGTAGTTTAAACGAGATTGCCAGCACCGGGTATCATTCACCATTTTTCTTTTCGTTAACTTGCCGTCAGCCTTTTCTTTGACCTCTTCTTTCTGTTCATGTGTATTTGCTGTCTCTTAGCCCAGACTTCCCGTGTCCTTTCCACCGGGCCTTTGAGAGGTCACAGGGTCTTGATGCTGTGGTCTTCATCTGCAGGTGTCTGACTTCCAGCAACTGCTGGCCTGTGCCAGGGTGCAGCTGAGCACTGGAGTGGAGTTTTCCTGTGGAGAGGAGCCATGCCTAGAGTGGGATGGGCCATTGTTCATG"
	ListCodonPositions("CCG",humanDNA) 
	print
	answer=raw_input("Do you want to play a game? (y) or (n):")
	if (answer=="y"):
		number=input("Which story do you want to play?(between 1-5):")
		MadLib(number)
	else:
		print "good bye"
		return 0
	answer2=raw_input("Do you want play it again? (y) or (n):")
	while(answer2=="y"):
		number=input("Which story do you want to play?(between 1-5):")
		MadLib(number)
		answer2=raw_input("Do you want play it again? (y) or (n):")


#Problem1   
#calculate the next year's population given a current population 
def CalcNewPopulation(initialPop):
	birthRate=7 #rate of birth is 7 seconds/person
	deathRate=13 # rate of death
	immigrate=35 #rate of immigrate
	secYear=365*24*60*60#calculate the total seconds in a year
	birthPerYear=secYear/birthRate#calculate the total birth per year
	deathPerYear=secYear/deathRate#total death per year
	immigratePerYear=secYear/immigrate#total immigrate per year
	return (initialPop+birthPerYear-deathPerYear+immigratePerYear) #return the new population

#Problmen2	
#prints the number of days,hours,minutes, and seconds given a number of seconds
def BreakoutTime(numSec):
	day=numSec/86400 #number of days
	sec=numSec%86400 #remaining seconds
	hour=sec/3600 #number of hours 
	sec=sec%3600 #remaining seconds
	minute=sec/60 #number of minutes
	sec=sec%60 # remaining seconds
	print "Days:",day
	print "Hours:",hour
	print "Minutes:",minute 
	print "Seconds:",sec
	
#Problem3
#prints the position where a sequence match was found
def ListCodonPositions(codon,humanDNA):
	for i in range(0,len(humanDNA)):
		if (humanDNA[i]==codon[0] and humanDNA[i+1]==codon[1] and humanDNA[i+2]==codon[2]): #find the matching conditions
			print (i+1), #print out the position of the sequence

#Problem4
#asks for parts of speech and those words are plugged into a template to generate a funny story
def MadLib(number):
	if (number==1):
		story="Be kind to your <noun>-footed <plural noun>, or a duck may be somebody's <noun>."
		replace1=raw_input("Enter noun1:") #ask user to input a string for noun1
		replace2=raw_input("Enter a plural noun:")#ask user to input a string for plural noun
		replace3=raw_input("Enter noun2:") #ask user to input a string for noun2
		newStory=replace(story,replace1)#replace the noun1 with the string entered by user
		newStory=replace(newStory,replace2)#replace the plural noun with the string entered by user
		newStory=replace(newStory,replace3)#replace noun2 with the string entered by user
	elif (number==2):
		story="It was the <adjective1> of <noun1>, it was the <adjective2> of <noun2>."
		replace1=raw_input("Enter adjective1:")
		replace2=raw_input("Enter noun1:")
		replace3=raw_input("Enter adjective2:")
		replace4=raw_input("Enter noun2:")
		newStory=replace(story,replace1)
		newStory=replace(newStory,replace2)
		newStory=replace(newStory,replace3)
		newStory=replace(newStory,replace4)	
	elif (number==3):
		story="<plural noun>? I don't have to show you any <adjective> <plural noun>!"
		replace1=raw_input("Enter plural noun1:")
		replace2=raw_input("Enter adjective:")
		replace3=raw_input("Enter plural noun2:")
		newStory=replace(story,replace1)
		newStory=replace(newStory,replace2)
		newStory=replace(newStory,replace3)	
	elif (number==4):
		story="My <relative> always said <noun> was like a box of <noun>. You never know what you're gonna get."
		replace1=raw_input("Enter relative:")
		replace2=raw_input("Enter noun1:")
		replace3=raw_input("Enter noun2:")
		newStory=replace(story,replace1)
		newStory=replace(newStory,replace2)
		newStory=replace(newStory,replace3)	
	elif (number==5):
		story="One <time of Day>, I <verb> a <noun> in my pajamas. How he got in my pajamas, I don't know."
		replace1=raw_input("Enter time of Day:")
		replace2=raw_input("Enter verb:")
		replace3=raw_input("Enter noun:")
		newStory=replace(story,replace1)
		newStory=replace(newStory,replace2)
		newStory=replace(newStory,replace3)	
			

	print newStory
	
#This is a helper function
#aims to replace the small elements in the story
def replace(story,replace):
	for i in range(0,len(story)):
		index1=story.find("<",0,len(story)) #find the postion of first "<" in the string
		index2=story.find(">",0,len(story)) #find the postion of first ">" in the string
		newStory=story[:index1]+replace+story[index2+1:] #make up the new story by combing elements after replacement
	return newStory


main()















