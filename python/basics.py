#!/bin/python3

#STRINGS
print("hello world")
print("hello winnie")
print("""this string runs
multiple lines""")
print('\n')
print("hey kali")

print('\n') 

#MATHS

print(50+50) #add
print(50-50) #subtract
print(50*50) #multiple
print(50%50) #modulas 
print(50/6) #divide
print(50//6) #no remainder
print(50+50-50*50/50) #PEMDAS ( PLEASE EXCUSE MY DEAR AUNT SALLY)
print(50**2)
#P - PARENTHESES 
#E - EXPONENT
#M - MULTIPLY 
#D - DIVIDE 
#A = ADDITION 
#S SUBTRACT
 
print('\n')

#VARIABLES AND METHODS	

quote = "everything is fair in love and war "  #quote is variable here
print (quote) #printing variable 
print('\n')

print (quote.upper()) #upper case function 
print (quote.lower()) #lower case function
print (quote.title()) #title case function

print(len(quote)) #counts characters including space. 
print('\n')


name = "bluesniffer" #string 
age = 33 #int
gpa = 3.7 #float

print (name)
print (int(age))
print (int(30.1))
print (int(30.9)) #will it round ? NO .

print("my name is " + name + " and i am " + str(age) + " years old")

age+=1
print (age)

birthday = 1
age += birthday 
print(age)

print('\n')

#FUNCTIONS

def whoami():   # function without parameters 
	name = "bluesniffer" #local variable 
	age = 33
	print("my name is " + name + " i am " + str(age) + " years old ")
whoami()	  
			


def add(num):
	print(num + 100)
add(60)	


def multiply (x,y):
	return x*y
multiply(7,7)	
print(multiply(7,7)) #multiplication using return statement 

def add(x,y):
 	print(x+y)
add(7,7)	#addition 

def newline():
	print('\n') #function to print new line
newline()
print("hello")

#BOOLEAN EXPRESSIONS (TRUE OR FALSE)

bool1 = True 
bool2 = 3*3 == 9 
bool3 = False 
bool4 = 3*3 != 9

print(bool1,bool2,bool3,bool4)
print(type(bool1)) #bool
bool5 = "True"
print(type(bool5)) #string
newline()

#RELATIONAL AND BOOLEAN OPERATORS
greater_than = 7 > 5
lesser_than = 5 < 7
 
test_and = (7 > 5 ) and (5 < 7) #True 
test_and2 = (7 > 5 ) and (5 > 7) #False
test_or = (7 > 5 ) or ( 5 < 7 ) #True 
test_or = (7 > 5 ) or (5 > 7 ) # True 
test_not = not True #False

newline()

#CONDITION STATEMENTS if/else

def drink(money):
	if money >=2:  #indentation is very important 
		return "you can buy a drink"
	else:
		return "not enough money"

print (drink(5))
print (drink(1))	
newline()

def alchohol(money,age):
	if (money >=5) and (age > 21):
		return "you can buy urself a drink"
	elif (money >=5) and (age < 21):
		return "you dont match age criteria"
	elif (money < 5) and (age >=21):
		return "not enough money"
	else:
		return "get lost "
		
		
print(alchohol(6,22))
print(alchohol(6,18))
print(alchohol(2,22))
print(alchohol(2,18))

newline()

#LISTS - HAVE SQUARE  BRACKETS [] lists are changeable
movies = ["harry potter", "pirates of carribean", "ddlj","the nun"]
print(movies[3])
print(movies[1:3]) # it will print index number 1,2 but not 3rd .
print(movies[1:]) # it will print all the names starting from 1 to end 
print(movies[:1]) # it will only print index number 0 that is all the items before 1 
print(movies[-1]) # it will print last item in the list  #positive index start from 0 and negative from -1 & from backwards
print(len(movies)) # will print count of items in the list
movies.append("mr robot") # appends/add  item at the end of the list
print(movies)
print(movies[4]) #index number 4 
movies.insert(2,"money heist") #will add item at second position/index 
print(movies)
movies.pop() #removes the last time 
print(movies)
movies.pop(0) #it will remove item with index number 0 	
print(movies)	

#we can also combine 2 lists

webseries = ["dark","vikings", "game of thrones"]

movies.extend(webseries)
print(movies) 
#creating a new list with combination of both movies and webseries 
favorite_shows = movies + webseries #movies are already extended with webseries so we will get webseries twice 
print(favorite_shows)


#creating 2 dimensional list 

grades = [["bob",82],["lydia", 90],["alice", 40]]   # 2 dimensional index
bob_grade= grades[0][1] #it is saying that we want to pull item from index number 0 that is bob and from index number 0 we want item number 1 that is 82 . so here bob is index 0  , lydia is index 1 and alice is index 2
print (bob_grade)  
#we can also edit bobs grade like this 
grades[0][1] = 83
print(grades)
bob_grade = grades[0][1]
print(bob_grade)

newline()

#TUPLES - have round brackets ()  tuples cant be changed 
coordinates = ("23","47","78") #immutable :- means cant be changed _
print(coordinates[1])

newline()
#LOOPINHG 

# FOR LOOPS - START TO FINISH OF AN ITERATE 

vegetables = ["tomato" , " onion" " cucumber"]
for x in vegetables :
	print(x) #it will print all 3 vegetables 
	
# WHILE LOOP - execute as long as True 

i=1 
while i<10 :
	print(i)
	i += 1
	
newline()

# ADVANCED STRINGS  #Strings are immutable 

my_name = "bluesniffer"
print(my_name[0])  #PRINTS FIRST LETTER
print(my_name[-1]) #PRINTS LAST LETTER 

sentence = "this is a sentence "
print (sentence[:4]) # here we know the sentence so it is easy for us 

print(sentence.split()) # Delimeter -  default delimeter is a space 

sentence_split = sentence.split()
sentence_join = ' ' .join(sentence_split)
print (sentence_join)

too_much_space = "                    hello      "
print(too_much_space)
print(too_much_space.strip()) # it will not print space 


print ( "A" in "Apple ") #True 
print ( "a" in "Apple " ) # False 

letter = "A"
word = "Apple"
print (letter.lower() in word.lower()) # true and improved way to not be case sensitive 

movie = "the nun"
print ("my favorite movie is {}. " .format(movie)) #format strings 
print ("my favorite movie is " + movie + ".")  #string concatenation 
print ("my favorite movie is %s ." %movie ) #percent formatting 
print (f"my favorite movie is {movie}.") # f string 

# Dictonaries - key/value pairs with {} braces 

drinks = {"black label": 7 , "soda": 4 , "coke": 7 } #drink is the key and price is the value 
print(drinks)

employees = {"Accounts": ["alex", "smriti" , "bir" ], "IT":["krish" , "rahul" , "rohan "] , "HR": ["ramesh" , "lydia "]} # department is key and people inside it are values 
print (employees)
employees ["legal"] = ["jeevan"]  # adds new key value pair 
print(employees)
employees.update({"sales": ["king" , "sania", "rani"]}) #adds new key:value pair 
print(employees)

drinks ["black label"] = 8  #updating values in dictionary 
print (drinks)

print(drinks.get("black label"))













	
