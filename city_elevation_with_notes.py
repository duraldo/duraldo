# define a basic city class
class City:
	name = ""
	country = ""
	elevation = 0 
	population = 0

# create a new instance of the City class and
# define each attribute
city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

# create a new instance of the City class and
# define each attribute
city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

# create a new instance of the City class and
# define each attribute
city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"    #dot notation we can add .attribute, this is like going another level deeper then dictionary...?
city3.elevation = 38
city3.population = 9733509

def max_elevation_city(min_population):
	# Initialize the variable that will hold (like math, attributes are variables)
# the information of the city with (look at"return_city" and and a return_elevation as parameters? what is the word for this, someone said to call it a placeholdher, that makes sense to me)
# the highest elevation 
	return_city = City()

	# Evaluate the 1st instance to meet the requirements:
	# does city #1 have at least min_population and
	# is its elevation the highest evaluated so far?
	if city1.population >= min_population and city1.elevation > return_city.elevation:    #I created 'return_elevation', it's not needed to created another return value.
		return_city = city1
	# Evaluate the 2nd instance to meet the requirements:
	# does city #2 have at least min_population and
	# is its elevation the highest evaluated so far?
	if city2.population >= min_population and city2.elevation > return_city.elevation:    #if city2 meets the requriments z greater than equal to a and b > return value
		return_city = city2
	# Evaluate the 3rd instance to meet the requirements:
	# does city #3 have at least min_population and
	# is its elevation the highest evaluated so far?
	if city1.population >= min_population and city3.elevation > return_city.elevation:    #why did i put return city here? pay more attention
		return_city = city3

	#Format the return string (we tried the {}{}.format, lets try the f-string way, rather then format method, but both SHOULD work...says the book.
	if return_city.name:
		return f"{return_city.name}, {return_city.country}"    #is the f-string needed? Yes! But it's printing out city not country lol
	else:    #I was getting an intendention error, because i used tabs at one point, stick with .
		return ""    #city3 will return blank because it doesn't match it

print(max_elevation_city(100000)) # Should print "Cusco, Peru"
print(max_elevation_city(1000000)) # Should print "Sofia, Bulgaria"
print(max_elevation_city(10000000)) # Should print ""

### Extra notes, this was a tough one for me. I think I had it right originally, but STICK WITH TABS OR SPACES, lol.
### I am remembering that episode of Silicon Valley heh.
### Code is nearly complete for the quiz, i hope this helps someone figure it out, because I had to use a book to understand the f-string and return function
### As well as, you don't need to always right it like .format (f-string can be used for that!) 
### Yes, this one question took me a day, and reading various websites that explain python, incluiding the manual found at:
    ### https://docs.python.org/3/tutorial/classes.html
    ### https://peps.python.org/pep-0498/#how-to-denote-f-strings
