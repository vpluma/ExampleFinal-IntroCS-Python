# Example Semester 1 - Final Python Project
def openingBanner():
	print("+================+")
	print("+ Opening Banner +")
	print("+================+")

def closingBanner():
	print(" ")
	print("+================+")
	print("+ Closing Banner +")
	print("+================+")

def askBasic():
	name = input("Enter name: ")
	age = int(input("Enter age: "))
	gpa = float(input("Enter GPA: "))
	return name, age, gpa

def clubs(name):
	clubList = []
	print("Hi " + name + "!")
	numClubs = int(input("Enter number of clubs: "))
	for i in range(numClubs):
		club = input("Enter club name: ")
		clubList.append(club)
	return clubList

def isHonorStudent(name, gpa):
	if gpa >= 3.75:
		print(name + " has earned Highest Honors")
	elif gpa >= 3.5 and gpa < 3.75:
		print(name + " has earned High Honors")
	else:
		print(name + " has earned Honors")

def printResults(clubList, name, gpa):
	closingBanner()
	print("GPA: " + str(gpa) )
	isHonorStudent(name, gpa)
	printClubs(clubList)

def printClubs(clubList):
	print("Club List: ", end = " ")
	for eachClub in clubList:
		print(eachClub, end = ". ")

def main():
	openingBanner()
	name, age, gpa = askBasic()
	clubList = clubs(name)
	printResults(clubList, name, gpa)

main()













