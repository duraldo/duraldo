### I need help with this one, already submitted it, but I don't understand why it's wrong, it gave the right print out right?
### Are they both supposed to have 1 apple? then johanna is supposed to have 2 and martin 1? I don't get it.

# “If you have an apple and I have an apple and we exchange these apples then
# you and I will still each have one apple. But if you have an idea and I have
# an idea and we exchange these ideas, then each of us will have two ideas.”
# George Bernard Shaw
#I have no idea how to solve this, but the output is I got is:


class Person:
    apples = 0
    ideas = 0

johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1

### It's so simple! one function for apples, one for ideas! change variables/attributes...
### pay attention to functions (exchange_APPLES) vs(exchange_ideas). then it's a simple math problem. I think.
def exchange_apples(you, me):
#Here, despite G.B. Shaw's quote, our characters have started with       
#different amounts of apples so we can better observe the results. 
#We're going to have Martin and Johanna exchange ALL their apples with #one another.
#Hint: how would you switch values of variables, 
#so that "you" and "me" will exchange ALL their apples with one another?
#Do you need a temporary variable to store one of the values?
#You may need more than one line of code to do that, which is OK. 
    you.apples, me.apples = you.apples,me.apples    # a = b is just transitive properties, like exchange rate, so this works. I think.
    return you.apples, me.apples
    
def exchange_ideas(you, me):    
    #"you" and "me" will share our ideas with one another.
    #What operations need to be performed, so that each object receives
    #the shared number of ideas?
    #Hint: how would you assign the total number of ideas to 
    #each idea attribute? Do you need a temporary variable to store 
    #the sum of ideas, or can you find another way? 
    #Use as many lines of code as you need here. 
    temporary = you.ideas + me.ideas    ###one more shot, assining a new temporary value, I don't think the amove method will work, since we are now "sharing ideas"...
    you.ideas=me.apples                 ###erase and replace applies with .ideas... wrong dot notation. (please work)
    me.ideas=temporary                  ###calling the attribute for the second part.
    return you.ideas, me.ideas

exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))

### 3 hours reading various ways to solve this, you can copy both functions and edit them, that was the harder way
### but creating a temporary variable to exhange something the same in line 28, is a simpler way.
### crossing my fingers this is right, I believe they are both to have 2 ideas...
### I was wrong, output came out to:
### Johanna has 1 apples and Martin has 2 apples
### Johanna has 2 ideas and Martin has 2 ideas

### Still wrong, why? "Not quite. Did you properly add or equivalate the attributes
### of both instances of the Person() class?

#Feedback on this one? This is the only one I coouldn't figure out by reading and pen and paper.

