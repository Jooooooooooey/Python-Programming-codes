# -*- coding: utf-8 -*-

'''
Huiyu Zhang
project#2
TA: Vipra Gupta
'''

class findLover: 
	firstnames=[] #first names of every people in the file 
	lastnames=[] #last names of every people in the file
	ages=[] #ages
	races=[] #races
	emails=[] #emails
	outdoors=[] #interests in outdoors
	movies=[] #interests in movies
	animals=[] #interests in animals
	musics=[] #interests in musics
	drinkings=[] #interests in drinkings
	
	def __init__(self): #initializing every data members
		self.firstname=''
		self.lasrname=''
		self.age=0
		self.race=''
		self.email=0
		self.outdoor=0
		self.movie=0
		self.animal=0
		self.music=0
		self.drinking=0
		
		
	#This method tends to list the names that fit the user's requirements
	def listNames(self,gender,largeage,smallage,race,outdoor,movie,animal,music,drinking):
		if gender=='male':
			try:
				f=open('50men.txt')
			except IOError:
				print "Error: can't find file"
		elif gender=='female':
			try:
				f=open('50women.txt')
			except IOError:
				print "Error: can't find file"
		for line in f:
			splitLine=line.split(',')		
			findLover.firstnames.append(splitLine[0])
			findLover.lastnames.append(splitLine[1])
			findLover.ages.append(int(splitLine[2]))
			findLover.races.append(splitLine[3])
			findLover.emails.append(splitLine[4])
			findLover.outdoors.append(int(splitLine[5]))
			findLover.movies.append(int(splitLine[6]))
			findLover.animals.append(int(splitLine[7]))
			findLover.musics.append(int(splitLine[8]))
			findLover.drinkings.append(int(splitLine[9]))
		for i in range(0,50):
			if findLover.races[i]==race and findLover.ages[i]<=largeage and findLover.ages[i]>=smallage:
				print 'Name:',findLover.firstnames[i],', matching score:', self.matchingScores(findLover.outdoors[i],findLover.movies[i],findLover.animals[i],findLover.musics[i],findLover.drinkings[i],outdoor,movie,animal,music,drinking)
	
	#This method is going to calculate the macthingScores between the user and the person he/she searched
	#More likely in interests, higher the score
	def matchingScores(self,A1,A2,A3,A4,A5,B1,B2,B3,B4,B5):
		score=0
		a=[]
		list1=[A1,A2,A3,A4,A5]
		list2=[B1,B2,B3,B4,B5]
		for i in range(0,5):
			for j in range(0,5):
				if i==j:
					if abs(list1[i]-list2[j])<=1:
						score+=1
		return score
		
		
	#This method is going to provide the information of the person that user searched		
	def searchInformation(self,name):
		if name in findLover.firstnames:
			i=findLover.firstnames.index(name)
			self.firstname=findLover.firstnames[i]
			self.lastname=findLover.lastnames[i]
			self.age=findLover.ages[i]
			self.race=findLover.races[i]
			self.email=findLover.emails[i]
			self.outdoor=findLover.outdoors[i]
			self.movie=findLover.movies[i]
			self.animal=findLover.animals[i]
			self.music=findLover.musics[i]
			self.drinking=findLover.drinkings[i]
			print 'Name:',findLover.firstnames[i], findLover.lastnames[i]
			print 'age:', findLover.ages[i]
			print 'race:', findLover.races[i]
			print 'email: ', findLover.emails[i]
			print 'interests in outdoors:',findLover.outdoors[i]
			print 'interests in movies:', findLover.movies[i]
			print 'interests in animals:', findLover.animals[i]
			print 'interests in musics:', findLover.musics[i]
			print 'interests in drinkings:', findLover.drinkings[i]

			
	#This method is going to print out the information that user wants into a text file	
	def printInformation(self):
		line=['Name: ',self.firstname,' ',self.lastname,'\n','Age: ',str(self.age),
		'\n','Race: ',self.race,'\n','email: ',self.email, '\n', 'Interest in outdoors: ',
		str(self.outdoor),'\n','Interest in movies: ',str(self.movie),'\n',
		'Interest in animals: ',str(self.animal),'\n','Interest in musics: ',
		str(self.music),'\n','Interest in drinkings: ',str(self.drinking)]
		fo=open('Information.txt',"wb")
		fo.writelines(line)

class findPlaceToDate:
	
	def __init__(self):#Initializing every data members
		self.choice='' #type of the restaurant
		self.RName='' #name of the restaurant
		self.RAddress='' #address of the restaurant
		self.list=[] 
	
	#This method created a dictionary that have different kinds of restaurants
	#It will provide the information of the restaurant to the user	
	def findRestaurant(self,choice):
		Dict={'American':['River and Woods','2328 Pearl St, Boulder, CO, 80302'],
		'Mexican':['La Choza','4457 Broadway St, Boulder, CO, 80301'],
		'Chinese':['Zoe Ma Ma','2010 10th St, Boulder, CO, 80302'],
		'Indian':['Curry n Kebob','3050 28th St, Boulder, CO, 80301'],
		'Thai':['Terra Thai','1121 Broadway,Boulder, CO, 80302'],
		'Spanish':['Ado’s Kitchen & Bar','1143 13th St, Boulder, CO, 80302']}
		self.choice=choice
		if  self.choice in Dict:
			self.list=Dict[self.choice]
			self.RName=self.list[0]
			self.RAddress=self.list[1]
			print 'Here is a restaurant you might like: '
			print 'Name of restaurant: ',self.RName
			print 'Address of restaurant: ',self.RAddress
		else:
			self.choice=raw_input('Wrong spelling, please enter again: ')
			if  self.choice in Dict:
				self.list=Dict[self.choice]
				self.RName=self.list[0]
				self.RAddress=self.list[1]
				print 'Here is a restaurant you might like: '
				print 'Name of restaurant: ',self.RName
				print 'Address of restaurant: ',self.RAddress
	
	#This method tends to print out the information of the restaurant into a text file
	def printRestaurant(self):
		line=['Name: ', self.RName,'\nType: ', self.choice, '\nAddress: ', self.RAddress]
		fo=open('Restaurant.txt',"wb")
		fo.writelines(line)
	
	#This method is going to print out three ending sentences for the dating website
	def endingWords(self):
		from colorama import init,Fore
		init(autoreset=True)
		print(Fore.RED+'Send him/her an email right now!')
		print(Fore.RED+'Do not hesitate to ask him/her our for a dinner!')
		print(Fore.CYAN+'Good Luck!')
		
		
		
		
		
	
		

		
def main():
	gender=raw_input("which gender are you interested in? (male or female): ")
	race=raw_input("Which race are you interested in? (White or Black or Latino or Asian): ")
	print "White: men's age range:21-31; women's age range:18-40"
	print "Black: men's age range:23-32; women's age range:19-25"
	print "Asian: men's age range:22-38; women's age range:21-28"
	print "Latino: men's age range:23-32; women's age range:21-30"
	largeage=int(raw_input("what is the largest age you are interested in?: "))
	smallage=int(raw_input("what is the smallest age you are interested in?: "))
	outdoor=int(raw_input("How much do you enjoy outdoors?(rate bewteen 0~5): "))
	movie=int(raw_input("How much do you enjoy movies?(rate between 0~5): "))
	animal=int(raw_input("How much do you enjoy animals?(rate between 0~5): "))
	music=int(raw_input("How much do you enjoy musics?(rate between 0~5): "))
	drinking=int(raw_input("How much do you enjoy drinkings?(rate between 0~5): "))	
	if gender=='male':
		m=findLover()
		m.listNames('male',largeage,smallage,race,outdoor,movie,animal,music,drinking)
		name=raw_input("Which person so you want more information about?: ")
		m.searchInformation(name)
		ans=raw_input("Would you like to print out his information?(y or n): ")
		if ans=='y':
			m.printInformation()
			print "His information has been saved into a text file sucessfully."
		repeat=raw_input("Would you like to search for other names?(y or n): ")
		while repeat=='y':
			name=raw_input("Which person so you want more information about?: ")
			m.searchInformation(name)
			ans=raw_input("Would you like to print out his information?(y or n): ")
			if ans=='y':
				m.printInformation()
				print "His information has been saved into a text file sucessfully."
			repeat=raw_input("Would you like to search for other names?(y or n): ")
			
		answer=raw_input("Do you want to find a restaurant to date?(y or n): ")
		if answer=='y':
			choice=raw_input("Which type of restaurant do you like?(American or Mexican or Chinese or Indian or Thai or Spanish): ")
			c=findPlaceToDate()
			c.findRestaurant(choice)
			answer2=raw_input("Do you want to print the information about the restaurant(y or n): ")
			if answer2=='y':
				c.printRestaurant()
				print "The information of this restaurant has been saved into a text file successfully"
		a=findPlaceToDate()
		a.endingWords()	

			
			
	elif gender=='female':
		f=findLover()
		f.listNames('female',largeage,smallage,race,outdoor,movie,animal,music,drinking)
		name=raw_input("Which person so you want more information about?: ")
		f.searchInformation(name)
		answ=raw_input("Would you like to print our her information?(y or n): ")
		if answ=='y':
			f.printInformation()
			print "Her information has been saved into a text file sucessfully."
		repeat=raw_input("Would you like to search for other names?(y or n): ")
		while repeat=='y':
			name=raw_input("Which person so you want more information about?: ")
			f.searchInformation(name)
			ans=raw_input("Would you like to print out her information?(y or n): ")
			if ans=='y':
				f.printInformation()
				print "Her information has been saved into a txt file sucessfully."
			repeat=raw_input("Would you like to search for other names?(y or n): ")
		answer=raw_input("Do you want to find a restaurant to date?(y or n): ")
		if answer=='y':
			choice=raw_input("Which type of restaurant do you like?(American or Mexican or Chinese or Indian or Thai or Spanish): ")
			b=findPlaceToDate()
			b.findRestaurant(choice)
			answer2=raw_input("Do you want to print the information about the restaurant(y or n): ")
			if answer2=='y':
				b.printRestaurant()	
				print "The information of this restaurant has been saved into a text file successfully"
		a=findPlaceToDate()
		a.endingWords()	



	
main()
