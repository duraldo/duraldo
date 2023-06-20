### From Crash Course Python, pig_latin function, this was difficult for me. Hopefully my notes will help someone.

def pig_latin(text):
  say = ""

  # Separate the text into words (this is the easier part)
  words = text.split()     #text is seperated by words using the .split() method
  say = []                 #iterate a new list, 'say' is the new ist

##Starting the for loop is what confused me.

  for word in words:   #for loop in word in 'words', you are defining the words in the value word
    # This is where I went wrong, I kept trying to do words = word [:1], however, a new variable/value needs to be created and assigned, for the pig latin prhase

    pig_word = word [1:] + word[0] +'ay'   # pig_word is the new variable/value (I am still confused on the terminology), use slicing method to add to the index. 
                                           #[:1] kept giving me just the normal phrase without piglatin
    say.append(pig_word)                   # say.append, syntax is list.append(x), where x is the variable 'pig_word'

    # Turn the list back into a phrase this part was easier then it needed to be
    # you can use the .join method in combination with the ' ' (whitespace) to get the phrase to work. 
  return ' '.join(say)                     # However, the string must be the new list [say]
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

### This was a difficult one for me, if you have any suggetions on helping me understand how I got to this answer, please by all means, give me suggestions!
