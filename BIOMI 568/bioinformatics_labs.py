#------------------------------------------------------------
# Python Lab 1: Intro
#------------------------------------------------------------
"""

Instructions: Read the information and try the examples in the interpreter.
Once you understand the concepts, answer the EXERCISES using variables and
the print statement. (See example answer for EXERCISE 1).

To test your answers, save the file and run it (F5 key) in IDLE.

For this lab, we will ONLY grade the answers for the EXERCISE portions.

"""
print("A. PYTHON AS A CALCULATOR")
#
#There are four different mathematical operators to
#add, subtract, multiply and divide: +, -, *, and /.
#Here are a few examples to try in the interpreter.
#
#>>> 2+2	#addition
#>>> 4*4	#multiplication
#>>> 16/4	#division
#>>> 2-2	#subtraction

#Python has 2 other operation symbols:
#Exponentiation: **
#5 ** 2 == 25
#and
#Remainder: %
#14 % 3 == 2

#
print('EXERCISE 1: Calculations \n')
#"""
#A1.   Add 17 and 383
A1 = 17 + 383
print('A1.', A1, '\n')


#A2.   Divide 222 by 11
A2 = 222/11
print('A2.', A2, '\n')

#A3.   Multiply 20 by 0.5
A3 = 20 * 0.5
print('A3.', A3, '\n')

print("B. USING PARENTHESES ( ) FOR CALCULATIONS\n")

#When parentheses are used in calculations, they tell python what to calculate first
#just like in math class. Python works on the calculation in ( ) before it does anything else. 
#
#>>> 5*(3+2) 	#First Python adds 3 and 2, then multiplies this by 5
#25
#>>> (5*3) +2	#First Python multiplies 5 and 3 then adds 2
#17
#
#Try the following:
#
B1 = 5*3+2
B2 = 3+2*5
#
#Can you see the difference?
print('B1. ',B1, '\nB2. ', B2)
print('\nWithout parentheses python will perform the multiplication first and then the addition. \nWhen I add parentheses around the addition I can make the answers equal.')
b1 = 5*(3+2)
b2 = (3+2)*5
print('b1. ', b1, '\nb2. ', b2, '\n')


#
print('C. ASSIGNING VALUES TO VARIABLES\n')
#The equal sign ("=") is used to assign a value to a variable.
#The value of an assignment is not written: 

width = 20
height = 5*9
area = width * height
#
#EXERCISE
#
#C1. Assign a new variable named area that is equal to width multiplied by height.
#then print the value of area:
print('C1. Area: ', area, '\n')

print('D. PRINTING\n')

#Now here is a more complicated program. Save and run the following printing programs
#in a file called YourName.py, where YourName is your first and last name like this: ScottKelley.py

#NOTE: Parts D and E are for PRACTICE ONLY.
#You do not need to turn in this file, only the Lab file.
#
print("Jack and Jill went up a hill")
print("to fetch a pail of water;")
print("Jack fell down, and broke his crown,")
print("and Jill came tumbling after.\n")
#
#When you run this program it prints out: 
#
#Jack and Jill went up a hill
#to fetch a pail of water;
#Jack fell down, and broke his crown,
#and Jill came tumbling after.
#
print('E. ORDER OF OPERATIONS\n')
#
#Expressions 
#
#Here is another program. Add this to the end of the previous Jack and Jill printing program. 
#
sum_this=2+2
multiply_that=3*4
#
print ("2 + 2 is", sum_this)
print ("3 * 4 is", multiply_that)
print (100 - 1, " = 100 - 1")
print ("(33 + 2) / 5 + 11.5 = ",(33 + 2) / 5 + 11.5)
#
#And here is the output when the program is run: 
#
#2 + 2 is 4
#3 * 4 is 12
#99 = 100 - 1
#(33 + 2) / 5 + 11.5 = 18.5
#
print('\nF. VARIABLES IN PYTHON\n')
#
#Learning to use variables is one of the most important parts of programming.
#Fortunately, Python makes using variables very easy. In math class, variables
#represent numbers or values and the same can be true in python. They can also
#represent numbers or letters, or even more complex things that we will get to later.
#
print('1. Numbers\n')
#
#Variables are like expandable boxes that can hold values of all sizes.
#Begin by setting variables to different number values.
#In Python, variable names are always letters or words that you set equal to something else:
#
x=5 	#Here I set a variable called x equal to the number 5
print('x=',x)		#Entering x at the prompt, Python tells me x equals 5
#5
x=10	#Here I changed the value of x to 10.
print('x=',x)
#10
y=200	#Now I made a new variable, y, equal to 200
print('y=', y)
#
#Once you create variables, you can start to play with them in different ways.
#For instance you can add, multiply, divide or subtract them just like numbers.
#Here are a few examples to try out. Set the variables to the values above.
#See what answers you get:
#
print('y + x:', y+x)		
print('x * y:', x*y)		
print('x * (x + y) :',x*(x+y))		
print('x * (y + y):',x*(y+y))
z = x+y           #You can assign a variable equal to other variables.
print('z is :', z)

print('\nEXERCISES\n')
#F1a. What is x after the following operation?
x=x+1

print('F1a. x is now 11: ', x)
#F1b. And again
x=x+1

print('F1b. x is now 12: ', x)
#F1c. What about this?
x+=1
print('F1c. x+=1 is the same as saying x = x+1, so x is now 13: ', x)

#But x, y and z are really boring variable names.
#In fact, you can make variable names as long and complicated as you like! 
#
width = 200
jorge_is_terrific = 3000
small_one = 0.000003
BIG_ONE = 40000000000
#
#Names to Avoid:
#Never use the characters 'l' (lowercase letter el), 'O' (uppercase letter oh),
#or 'I' (uppercase letter eye) as single character variable names.
#In some fonts, these characters are indistinguishable from the numerals one and zero.
#When tempted to use 'l', use 'L' instead.

print('\nMORE EXERCISES\n')	
#F1d. What happens when you do this?
#BIG_ONE == big_one

print('F1d. When you type, BIG_ONE == big_one, An error occurs because you have not defined the variable, big_one.')


#
#Python does not like spaces in the names, which is why I use the underscore _ character to connect words.  If you put a space in there you will get a SyntaxError like this:
#
#>>> small one = 003
#  File "<string>", line 1
#     small one = 003
#             ^
# SyntaxError: invalid syntax
#
#Python also does not like funny characters like percentage signs (%) and asterisks (*). 
#
#>>> big% = 90
#  File "<string>", line 1
#     big% = 90
#          ^
# SyntaxError: invalid syntax
#>>> big*=90
#  File "<string>", line 1
#     big*=90
#         ^
# SyntaxError: invalid syntax
#
print('\nMORE EXERCISES\n')

#F1d. Set x to a value of 2000. Set y to a value of 0.25. Multiply x and y.    
#F1e. Make the variable SPAM equal to x minus y. 
#F1f. Divide SPAM by x and then add y.

x = 2000
y = 0.25
z = x * y
print('F1d. x is {}, y is {}, x*y is {}\n'.format(x,y,z))

SPAM = x - y
Eq = (SPAM / x) + y

print('F1e. SPAM is {} \nF1f. (SPAM / x) + y is {:.8f}\n'.format(SPAM, Eq))

#
#One more thing you should know about variable names is that Python really cares about uppercase
#and lowercase letters in names.
#For instance, the variable names SPAM, spam, Spam, and SpaM are all different variables to Python
#even though they are spelled the same. This is why I like to keep all my variable names in lower
#case letters so I do not get mixed up.
#
#HELPFUL HINT: A value can be assigned to several variables simultaneously: 
#
#>>> x = y = z = 0  # Zero x, y and z
#
print('2. Strings (Letters and Words)\n')
#
#Python also has many ways to manipulate and play with letters and words. In Python, words are
#called Strings because you can string letters together to form words.
#
#For example, my name is "Scott", but you can also think of this word as a bunch of letter
#strung together:
#			S C O T T
#
#Of course, Scott could also be a very nice name for a variable:
#
#>>> Scott = 31
#>>> Scott
#31
#
#So we have to distinguish strings from variable names using quotation marks ("").
#
name = "Scott" 	#Here is a string of my name
#"Scott"
what = 'does not'
#'does not'
okay = 'like'
#'like'
food = 'spam'		#And here is a food I dislike
#'spam'
#
#Just like with numbers, we can make variables hold strings as values.
#Here are a few examples you can try out at the prompt:
#
name = 'scott'	     #Here I set a variable name 
## equal the string 'scott'
food = 'spam!'
emotion = 'hates'
#>>> emotion
#'hate'
print(name, emotion, food)
    
print('\nG. MANIPULATING STRINGS\n')
#
print('1. Concatenation and Multiplication of Strings\n')
#
#In Python, you can concatenate strings with the + operator.
#Concatenation is the process of tying or gluing strings together to make longer strings. 
#
#Here are a few examples to try: 
#
#>>> 'CATTACG' + 'AATGC'
#>>> 'CATTACG' + ' ' + 'AATGC'	#Notice the empty ' ' space character
#>>> 'CATTACG' + 'AATGC' + ' '
#
#You can also concatenate variables together if they hold strings as values:
#
DNA1 = 'AGAGAGAG'
DNA2 = 'GATGGACT'
#>>> DNA1 + DNA2
#
#You can also print out very long strings:
#
#>>> long_string = 'Can you help me find the cat?\n I think she ran out of the house!'
#>>> print (long_string)
#Can you help me find the cat?
# I think she ran out of the house!


#EXCERCISES
#G1a. Create a new variable called new_DNA that equals the concatenation of DNA1 and DNA2. ?????
new_DNA = DNA1 + DNA2
print('G1a. new_DNA:', new_DNA)
#G1b. Add the string '\n' to new_DNA and print new_DNA. What happens when you do this? ?????
print('G1b.', new_DNA +'\n')
print('By adding the string \\n it returns anthing after it to a new line.\n')
#
#By now you have probably noticed that the \n character is an enter character and returns to the
#next line. This is an example of a hidden character you do not see them when you print the string
#out, but they are there anyway. Another hidden character is \t, which is a tab character.
#
#Not only can you concatenate (or add) strings together, you can also multiply (or repeat)
#strings with the * operator. Try a few examples to see what this does:
#
#>>> DNA1*2
#>>> DNA2*7
#>>> new_DNA*10
# 
#Strings can be concatenated (glued together) with the + operator, and repeated with *: 
#
#>>> word = 'Help' + ' Me'
#>>> word
#'Help Me'
#>>> '<' + word*5 + '>'
#'<Help MeHelp MeHelp MeHelp MeHelp Me>'
#
print('2. Cool Python Trick #1: SLICING')
#
#MORE EXERCISES

#G2a. Can you figure out what the following code is doing?????
word='HelpMe'
print('\nG2a.', word[4])
print(word[0:2])
print(word[2:4])
my_word=word[4:6]
print(my_word)

print('word[4] is printing the character in the 4th position in the string.')
print('word[0:2] is printing the characters at positions 0,1 but not 2.')
print('word[2:4] is printing the characters at positions 2,3 but not 4.')
print('my_word = word[4:6] is creating a new variable with the characters at positions 4,5 there is no character in the 6th position.')

#G2b. What happens if you do word[0:8]
print('\nG2b.', word[0:8])
print('word[0:8] prints the entire string')

#G2c. What about word[8]
print('\nG2c. word[8] returns an error because there is no 8th position in the string')

#G2d. What about word[:-1]
print('\nG2d.', word[:-1])
print('word[:-1] prints the characters starting at the beginning position, since no specific position is entered, up to the last position.')
print('The -1 position is also the last position in the string because the \'-\' reads the string backwards.')

#G2e. What about word[:-2]
print('\nG2e.', word[:-2])
print('word[:-2] is similar to question G2d except it ends before second to last position. -2 means the second position reading backwards.')

#Try out the following string slices:
#
#>>> word[:2]    # The first two characters
#'He'
#>>> word[2:]    # All but the first two characters
#'lpA'
#
#NOTE: Strings are immutable. They cannot be changed!
#
#Assigning to an indexed position in the string results in an error: 
#
#>>> word[0] = 'x'
#Traceback (most recent call last):
#  File "<stdin>", line 1, in ?
#TypeError: object doesn't support item assignment
#
#>>> word[:1] = 'Splat'
#Traceback (most recent call last):
#  File "<stdin>", line 1, in ?
#TypeError: object doesn't support slice assignment
#
#However, creating a new string with the combined content is easy and efficient: 
#
#>>> 'x' + word[1:]
#'xelpA'
#>>> 'Splat' + word[4]
#'SplatA'
#
#Here's a useful invariant of slice operations: s[:i] + s[i:] equals s. 
#
#>>> word[:2] + word[2:]
#'HelpMe'
#>>> word[:3] + word[3:]
#'HelpMe'
#
#Degenerate slice indices are handled gracefully: an index that is too large
#is replaced by the string size, an upper bound smaller than the lower bound returns an empty string. 
#
#>>> word[1:100]
#'elpAMe'
#>>> word[10:]
#''
#>>> word[2:1]
#''
#3. Going Backwards
#
#Indices may be negative numbers, to start counting from the right. For example: 
#
#>>> word[-1]     # The last character
#'A'
#>>> word[-2]     # The last-but-one character
#'p'
#>>> word[-2:]    # The last two characters
#'pA'
#>>> word[:-2]    # All but the last two characters
#'Hel'
#
#But note that -0 is really the same as 0, so it does not count from the right! 
#
#>>> word[-0]     # (since -0 equals 0)
#'H'
#
#Out-of-range negative slice indices are truncated, but don't try this for single-element
#(non-slice) indices: 
#
#>>> word[-100:]
#'HelpA'
#>>> word[-10]    # error
#Traceback (most recent call last):
#  File "<stdin>", line 1, in ?
#IndexError: string index out of range
#
#
print('\nFINAL EXERCISES\n')
#G3a. Make a new variable Total_DNA that concatenates DNA1 and DNA2 and multiplies them 10 times.
Total_DNA = (DNA1 + DNA2) * 10
print('G3a.\n', Total_DNA)

#G3b. Make a new variable called Microsat that equals a slice of Total_DNA that includes the first copy of DNA1 (see Cool Python Trick #1: SLICING).
Microsat = Total_DNA[:8]
print('\nG3b.\n', Microsat)
#G3c. Make a new variable called PrimeEnd equal to a slice of the last 10 bases of Total_DNA.
PrimeEnd = Total_DNA[-10:]
print('\nG3c.\n', PrimeEnd)
#


#----------------------------------------------------------------------------
# PYTHON LAB 2: Conditionals
#----------------------------------------------------------------------------

#- Read the instructions for each part CAREFULLY.
#- IN THE EXERCISES, USE THE VARIABLE NAMES INDICATED

#----------------------------------------------------------------------------
#== PART 1 ==
"""
Write a script below using if/elif/else that compares two variables, fx and fy.
If the fx is greater than fy print "fx is da bomb."
Else if fy is greater than fx print "No dude, fy is da bomb."
Else print "They are both losers."
"""

#Test different values of fx and fy
#fx=9
#fy=2
fx=0.9
fy=2.8
#fx=fy=0

#== PART 1 Answer ==

if fx > fy:
    print('fx is da bomb.')
elif fy > fx:
    print('No dude, fy is da bomb.')
else:
    print("They are both losers.")

#---------------------------------------------------------------------------

#== PART 2 ==
"""
Write some code to test wether the length of the variable dna1
is greater or equal to 10 bases (characters) long or less than 10 long.
If greater or equal, print the sequence.
Else print Too Short!
"""
          
#Try it with different values of dna1:

#dna1='GTAACAG'
          
#dna1="CAGATTAGGA"
dna1="GGACAACCGATTACAGGATGCCG"

#== PART 2 Answer ==
if len(dna1) >= 10:
    print(dna1)
else:
    print("Too Short!")

#----------------------------------------------------------------------------

#== PART 3 ==
"""
Using the double equals sign!
Write an if/then statement to check if the string seq  is a perfect match to
EITHER of two sequences of human DNA: "GAATTC" or "CTTAAG"
If it is a perfect match, print "MATCH". Else print ("FAIL")
"""

#Test with different values of seq
#seq="GAATTC"
seq="CTTAAG"
#seq="ACACACAC"

#== PART 3 Answer ==

if seq == 'GAATTC' or seq == 'CTTAAG':
    print("MATCH")
else:
    print("FAIL")


#-------------------------------------------------------------------------
#== PART 4 ==

"""
Write a script that does the following:

(1) Take in a sequence (mrna) as an argument and converts it to UPPER CASE.
(2) Extracts the first three letters from the sequence.
(3) Check if the first three letters is a start codon "AUG".
      If the sequence has a start codon print "Protein Sequence Found."
         and also print the sequence. print(mrna)
      Else if the start codon is NOT found, print "Protein Sequence not found."
"""
#Test the function with different values of mrna:
#mrna="AUGGGAAAUUU"
#mrna="GGGaaaAAG"

#This has a lowercase 'aug' and should also print "Protein Sequence Found."
mrna="augggaaauuu"


#== PART 4 Answer ==

mrna = mrna.upper()

if mrna[0:3] == "AUG":
    print('Protein Sequence FOUND.')
    print(mrna)

else:
    print('Protein Sequence NOT FOUND.')


#-------------------------------------------------------------------------------
# PYTHON LAB 3: Loops
#-------------------------------------------------------------------------------
import random
outfile=open('Armstrong03Lab.txt','w')

print("\n########## PART 1 ##########\n")
outfile.write("\n########## PART 1 ##########\n")
#PART 1 - STRING LOOPING & COUNTING

#(1) Use a "for" loop to iterate through the DNA sequence.
#(2) Count the number of G's and C's in the DNA sequence.
#(3) Print the number of G's and C's in the DNA sequence.

#DATASET FOR PART 1: try each of thes options
#test_dna="GACCTTTAC"
test_dna="GATCCTGGCTCAGGACGAACGCTGGCGGCGTGCTTAACACATGCAAGTCGAGCGGTAAGGCCCTTCGGGGTACACGAGCGGCGAACGGGTGAGTAACACGTGGGTGATCTGGGGCCCCATCTA"

#== PART 1 ==
G_count = 0
C_count = 0

for base in test_dna:
    if base == "G":
        G_count+=1
    elif base == "C":
        C_count+=1
    else:
        continue

print("number of G\'s:", G_count)
out=str(G_count)+"\n"
outfile.write(out)

print("number of C\'s:", C_count)
out=str(C_count)+"\n"
outfile.write(out)

#-------------------------------------------------------------------------------
print("\n########## PART 2 ##########\n")
outfile.write("\n########## PART 2 ##########\n")
#PART 2 - CLEAN the Sequence first then calculate the percentage of G and Cs 

nasty_dna="\n AgGctgTtgC \t\n"

# (1) Clean the DNA sequence.
# (2) Use a "for" loop to iterate through the DNA sequence.
# (3) Count the number of G's and C's in the DNA sequence.
# (4) Calculate the proportion of G and C nucleotides in the DNA sequence.
#       For example this proportion in DNA sequence "GACT" is 0.5. 
# (5) Print the percentage of G and C in the DNA sequence.

#To get percentage divide the count of G and C by the total length of the DNA
#Then multiply by 100. 0.5 becomes 50.0
#For example: len(clean_dna)


#== PART 2 ==
nasty_dna= nasty_dna.strip()
nasty_dna= nasty_dna.upper()
clean_dna = nasty_dna

print(clean_dna)
out=str(clean_dna)+"\n"
outfile.write(out)

G_C_count=0

for base in clean_dna:
    if base == "G" or base == "C":
        G_C_count+=1
    else:
        continue

percent_GC = G_C_count/len(clean_dna)*100
print("percentage of G\'s and C's:{:.2f}%".format(percent_GC))
out=str(percent_GC)+"\n"
outfile.write(out)



#-------------------------------------------------------------------------------
print("\n########## PART 3 ##########\n")
outfile.write("\n########## PART 3 ##########\n")
#PART 3 - CHARACTER CLASSIFICATION

dna="AAGGTTCCCCG"*10

# (1) Count the number of each type of base in the DNA sequence.
# (2) Return the counts of each type of base in the DNA sequence.
# (3) Also print out a table of the counts as shown below.

#== PART 3 ==
count_A = 0
count_T = 0
count_G = 0
count_C = 0

for base in test_dna:
    if base == "G":
        count_G+=1
        
    elif base == "C":
        count_C+=1

    elif base == "A":
        count_A+=1
        
    elif base == "T":
        count_T+=1
        
    else:
        continue

print("\tA\t{}".format(count_A))
out= "\tA\t" + str(count_A) + "\n"
outfile.write(out)

print("\tT\t{}".format(count_T))
out= "\tT\t" + str(count_T) + "\n"
outfile.write(out)

print("\tG\t{}".format(count_G))
out= "\tG\t" + str(count_G) + "\n"
outfile.write(out)

print("\tC\t{}".format(count_C))
out= "\tC\t" + str(count_C) + "\n"
outfile.write(out)


#The table should look like this:
#   A   9
#   T	10
#   G	12
#   C	7

#-------------------------------------------------------------------------------
print("\n########## PART 4 ##########\n")
outfile.write("\n########## PART 4 ##########\n")
#PART 4 - Using range and random


#Use the random.shuffle function to make and print 10 random lists of names.

names=['Tara','Merkel','Bob','Dwight','Chrysanthemum','Tiny Tim','Boba Fett','Lando','Sgt. Rock','Beyonce']
print("Original List: ",names) #prints the unshuffled names

out="Original List: " + str(names) + "\n"
outfile.write(out)


#== PART 4 ==

for i in range(10):
    random.shuffle(names)
    print(i+1,".\t", names)
    out=str(names) + "\n"
    outfile.write(out)

#-------------------------------------------------------------------------------
print("\n########## PART 5 ##########\n")
outfile.write("\n########## PART 5 ##########\n")
#PART 5 - Write everthing to a file!!

"""
For this last part, write all your results (PARTS 1 to 4) to a file called: YourName03Lab.txt
YourName should be changed to your name of course.

How to do this? It's easy!

(1) Put this code at the top of the file:
outfile=open('YourName03Lab.txt','w')

(2) After each print statement, add a line to write data to a file, for example:

print(names)
out=str(names) # You can only write strings to a file!
outfile.write(out)

(3) At the end of this file put this code:

outfile.close()

----------------------------------------------------------------------------------------------------------------------------------------
NOTE: For this assignment, you will be submitting your finished YourName03Lab.py file AND the YourName03Lab.txt file you just generated.
----------------------------------------------------------------------------------------------------------------------------------------

"""
outfile.close()


#----------------------------------------------------------------------------
#PYTHON LAB 4: LISTS
#----------------------------------------------------------------------------

print("\n########## PART 1 ##########\n")

#PART 1 - Append substrings to a list

#(1) Use a for loop to iterate through a sequence.
#(2) Divide the sequence into sections of 3 DNA bases with NO OVERLAP.
#(3) Append the 3-base codons to a list.
#[NOTE: If a group is not 3 bases long, do not include it in the list.]
#(4) Print the final list. 

#== PART 1 ==

#seq="AUGGGAAGC"   #This should print  ["AUG","GGA","AGC"]
seq="AUGGGAAGCGCGG"  #This should print  ["AUG","GGA","AGC","GCG"]

#Here is a little snippet of code that should help.
#It uses a for loop to 'break up' a string into groups of 3 characters
# like with codons. Question - how do you then append then to a list?
part1_list=[]

for i in range(0,len(seq),3):
    codon=seq[i:i+3]
    print(codon)
    if len(codon) == 3:
        part1_list.append(codon)

print(part1_list)

#-------------------------------------------------------------------------------
print("\n########## PART 2 ##########\n")

#PART 2 - Change the length of the substrings

# Exactly the same as part 1 EXCEPT instead of 3-characters
#    it can be of length x, where x is an integer.
# For example if x=4, then if seq='AAAAGGGGCCCC' the loop would print
# ['AAAA','GGGG','CCCC']
# Feel free to copy paste and modify the loop from part 1

#== PART 2 ==

#Try it out with two different values of x and two different sequences
x=4
#x=5 

#seq="AAAAGGGGCCCC"
seq="AUGUAUGUCUGUCUGAUC"

part2_list=[]

for i in range(0,len(seq),x):
    codon=seq[i:i+x]
    print(codon)
    if len(codon) == x:
        part2_list.append(codon)

print(part2_list)


#------------------------------------------------------------------------------
print("\n########## PART 3 ##########\n")

#PART 3 -  Iterate through a list of strings, calculate value, write to file


#(1) Iterate through the list of sequences
#(2) Count G's and C's for each sequence nmer in a list.
#(3) Calculate the GC Percentage for the sequence nmer.
#(4) Write the sequence and its GC percentage (separated by a "Tab")
#    to a file named:
#       gc_output.txt

###A counting shortcut for string data:
#seq="AGGT"
#g_count=seq.count("G")
#print(g_count)

#For example if given the following sequence list
#seq_list=["AAUG","AGCG","GCUA"]

#The loop would write the following to the file gc_output.txt
#AAUG    25.0
#AGCG    75.0
#GCUA    50.0

#== PART 3 ==
print("Answer in txt file")

outfile=open('gc_output.txt','w')


#seq_list=["AAUG","AGCG","GCUA"]
seq_list=["AAUGGAGACU","AGCGCCCC","GCUAAAAAAU"]

for i in range(0,len(seq_list)):
    x = seq_list[i]
    gc_count = x.count("G")+x.count("C")
    percent_gc = gc_count/len(x)*100
    out = str(percent_gc)
    outfile.write(x+"\t"+out+"\n")

outfile.close()


#----------------------------------------------------------------------------
#PYTHON LAB 5: Functions
#----------------------------------------------------------------------------

import random
import re

"""
In this assignment, you will go back to your working code from 
previous assignments and converts your scripts to functions.

To begin, you can literally copy and paste the old code to this 
file then turn it into a working function. 

Test the functions with the values indicated and make sure
you get the results you expect to get.
"""

print("\n########## PART 1 ##########\n")

#PART 1 - Convert 03Lab part 2 to a function

#FUNCTION NAME: fractionGC
#PARAMETERS: 1 (A DNA sequence)
#PURPOSE: The function should:
#           (1) Clean the DNA sequence.
#	    (2) Use a "for" loop to iterate through the DNA sequence.
#	    (3) Count the number of G's and C's in the DNA sequence.
#           (4) Calculate the fraction (NOT PERCENT) of G's and C's in the DNA sequence. 
#	    (5) Return the fraction of G's and C's in the DNA sequence.
#RETURN VALUES: The fraction of G's and C's in the DNA sequence. (A float)

#== FUNCTION 1 ==

def fractionGC(dna):
    dna = dna.upper().strip().replace(" ","")
    count = 0
    for base in dna:
        if base == "G" or base == "C":
            count += 1
        else:
            continue

    gc_content = count/len(dna)
        
    return gc_content

#EXAMPLE: 
gc_content = fractionGC("\n AgGctgTtgC \t\n")
print(gc_content)

#The function would return:
#   0.6

test_seq1="GACCTTTAC"
test_seq2="GATCCTGGCTCAGGACGAACGCTGGCGGCGTGCTTAACACATGCAAGTCGAGCGGTAAGGCCCTTCGGGGTACACGAGCGGCGAACGGGTGAGTAACACGTGGGTGATCTGGGGCCCCATCTA"

gc_content = fractionGC(test_seq1)
print("test_seq1:", gc_content)

gc_content = fractionGC(test_seq2)
print("test_seq2:", gc_content)


#Test the function with the sequence from EXAMPLE and verify your result.
#Test the function again with "test_seq1" and test_seq2".
#Return the "GC" content of "test_seq1" to "gc_content". 
#Test it again with "test_seq2".


print("\n########## PART 2 ##########\n")

#PART 2 - Convert 03Lab part 3 to a function

#FUNCTION NAME: count_DNA_bases
#PARAMETERS: 1 (A DNA sequence)
#PURPOSE: The function should:
#           (1) Count the number of each type of base in the DNA sequence.
#           (2) Return the counts of each type of base in the DNA sequence.
#           (3) Also print out a table as shown below.
#RETURN VALUES: The counts of each type of base in the DNA sequence. (A tuple)
#                   [NOTE: Return the counts EXACTLY in this order: A's, T's, G's and C's.]
# Example tuples: my_tuple1=(x,y,z)  my_tuple2=(1,2,3,4)


#== FUNCTION 2 ==
def count_DNA_bases(dna):
    count_A = 0
    count_T = 0
    count_G = 0
    count_C = 0
    
    for base in dna:
        if base == "A":
            count_A += 1
        elif base == "T":
            count_T += 1
        elif base == "G":
            count_G += 1
        elif base == "C":
            count_C += 1
        else:
            continue
        
    count_tuple = (count_A, count_T, count_G, count_C)
    print(" A   ", count_A, "\n","T   ", count_T, "\n","G   ", count_G, "\n","C   ", count_C, "\n")

    return count_tuple


#TEST DATA FOR PART 2:
test_dna1="AAGCTACGTGGGTGACTTTGCCGATTTAAGCCTGGGAA"

#EXAMPLE:
DNAcounts=count_DNA_bases(test_dna1)
print (DNAcounts)

#The function would print a table:
#   A   9
#   T	10
#   G	12
#   C	7

#The function would return:
#   (9, 10, 12, 7)


print("\n########## PART 3 ##########\n")

#PART 3 - Convert 03Lab part 4 to a function

#Use the random.shuffle function to make and print 10 random lists of names.



#== FUNCTION 3 ==
def shuffle_list(names):
    for i in range(10):
        random.shuffle(names)
        print(names)

    return


names=['Tara','Merkel','Bob','Dwight','Chrysanthemum','Tiny Tim','Boba Fett','Lando','Sgt. Rock','Beyonce']
print(names) #prints the unshuffled names
shuffle_list(names)


print("\n########## PART 4 ##########\n")

#PART 4 -  Convert 04Lab part 2 to a function

#FUNCTION NAME: codon_list
#PARAMETERS: 1 (A sequence)
#PURPOSE: The function should:
#   (1) Iterate through the sequence.
#   (2) Divide the sequence into sections of 3-base codons with NO OVERLAPPING.
#   (3) Add the codons to a list.
#   [NOTE: If a group is not 3 bases long, do not include it in the list.]
#   (4) Return the list.
#RETURN VALUES: A list of codons. (A list)

#== FUNCTION 4 ==

def codon_list(seq):
    x = 3
    codon_list=[]

    for i in range(0,len(seq),x):
        codon=seq[i:i+x]
        if len(codon) == x:
            codon_list.append(codon)

    return codon_list


#EXAMPLE:
dna1="AUGGGAAGC"
codons=codon_list(dna1)
print(codons)

#The function would return:
#   ["AUG","GGA","AGC"]


#----------------------------------------------------------------------------
#PYTHON LAB 6: Dictionaries
#----------------------------------------------------------------------------

#------------------------------------------------------------------------------------------
# - PART 1 -
#------------------------------------------------------------------------------------------

#FUNCTION NAME: rna2protein
#PARAMETERS: 1 (An RNA sequence)
#PURPOSE: The function should:
#           (1) Divide the RNA sequence into a list of 3-base codons.
#HINT: You could use CodonList inside this function from previous lecture.
#           (2) Create a new protein string.
#           (3) Use the "standard_code" dictionary to find the amino acid for each codon in the list.
#           (4) Return the new protein string.
#RETURN VALUES: A protein sequence. (A string)

#Hint: When building the protein you are trying to return, add the dictionary values below (the letters
#      of the amino acids to an empty string (e.g., prot="").

standard_code = {
     "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L", "UCU": "S",
     "UCC": "S", "UCA": "S", "UCG": "S", "UAU": "Y", "UAC": "Y",
     "UAA": "*", "UAG": "*", "UGA": "*", "UGU": "C", "UGC": "C",
     "UGG": "W", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
     "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P", "CAU": "H",
     "CAC": "H", "CAA": "Q", "CAG": "Q", "CGU": "R", "CGC": "R",
     "CGA": "R", "CGG": "R", "AUU": "I", "AUC": "I", "AUA": "I",
     "AUG": "M", "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
     "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K", "AGU": "S",
     "AGC": "S", "AGA": "R", "AGG": "R", "GUU": "V", "GUC": "V",
     "GUA": "V", "GUG": "V", "GCU": "A", "GCC": "A", "GCA": "A",
     "GCG": "A", "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
     "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}

#== FUNCTION 1 ==
def rna2protein(seq):
    protein = ""
    
    for i in range(0,len(seq),3):
        codon = seq[i:i+3]
        if len(codon) == 3:
            try:
                aa = standard_code[codon]
            except:
                aa = "X"
            protein += aa
        else:
            break
            
    return protein

#EXAMPLE:
protein=rna2protein("GCGAGGGUCUGA")
print(protein)

#This should print:
#ARV*



#------------------------------------------------------------------------------------------
# - PART 2 -
#------------------------------------------------------------------------------------------

#FUNCTION NAME: dna2protein
#PARAMETERS: 1 (A DNA sequence)
#PURPOSE: The function should:
#           (1) Clean the DNA sequence and convert it to RNA. Just change T's to U's (don't reverse compliment)
#           (2) Divide the RNA sequence into a list of 3-base codons.
#           (3) Create a new protein string.
#           (4) Use the "standard_code" dictionary to find the amino acid for each codon.
#                   [NOTE: Stop translating after "Stop" codons.]
#           (5) Return the new protein string.
#RETURN VALUES: A protein sequence. (A string)

#== FUNCTION 2 ==
def dna2protein(seq):
    seq = seq.upper().strip()
    seq = seq.replace(" ","")
    seq = seq.replace("T","U")
    protein = ""
    for i in range(0,len(seq),3):
        codon = seq[i:i+3]
        if len(codon) == 3:
            try:
                aa = standard_code[codon]
            except:
                aa = "?"
            protein += aa
            if aa == "*": break
        else:
            break
    return protein


#EXAMPLE:
protein=dna2protein("\n   ATGCaaaGAGacTGAgCC  \n\t\n")
print(protein)

#The function would return:
#   MQRD*

############# Extra Practice ##############
# Modify your dna2protein function
# Use a try/except loop with your dictionary so that if the key is NOT in the dictionary,
#  It adds a "?" instead to the protein sequence.

#EXAMPLE:
protein2=dna2protein("\n   ATGC-aaGAGacTGAgCC  \n\t\n")
print (protein2)
###
#Should print:
#   M?RD*



#------------------------------------------------------------------------------------------
# - PART 3 -
#------------------------------------------------------------------------------------------

#FUNCTION NAME: EC_translate
#PARAMETERS: 2 (A sequence, and a default integer parameter set equal to "0")  
#PURPOSE: The function should:
#           (1) Clean the sequence.
#           (2) Check to see if the sequence is RNA or DNA. If it is DNA, convert it to RNA.
#           (3) Divide the RNA sequence into a list of 3-base codons.
#           (4) Create a new protein string.
#           (5) Based on the second parameter, use the appropriate dictionary 
#                   (if 0 use "standard_code", else use "mitochondrial_code")

#           (6) Return the new protein string.

#RETURN VALUES: A protein sequence. (A string)


mitochondrial_code = {
     "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L", "UCU": "S",
     "UCC": "S", "UCA": "S", "UCG": "S", "UAU": "Y", "UAC": "Y",
     "UAA": "*", "UAG": "*", "UGU": "C", "UGC": "C", "UGA": "W",
     "UGG": "W", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
     "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P", "CAU": "H",
     "CAC": "H", "CAA": "Q", "CAG": "Q", "CGU": "R", "CGC": "R",
     "CGA": "R", "CGG": "R", "AUU": "I", "AUC": "I", "AUA": "M",
     "AUG": "M", "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
     "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K", "AGU": "S",
     "AGC": "S", "AGA": "*", "AGG": "*", "GUU": "V", "GUC": "V",
     "GUA": "V", "GUG": "V", "GCU": "A", "GCC": "A", "GCA": "A",
     "GCG": "A", "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
     "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}

#== FUNCTION 3 ==
def EC_translate(fseq, fcode=0):    #fcode is set to a default of 0 (see above)
    fseq = fseq.upper().strip()
    fseq = fseq.replace(" ","")
    protein = ""
    
    if "T" in fseq:
        fseq = fseq.replace("T","U")
        
        
    protein = ""
    for i in range(0,len(fseq),3):
        codon = fseq[i:i+3]
        if len(codon) == 3:
            try:
                if fcode == 0:
                    aa = standard_code[codon]
                else:
                    aa = mitochondrial_code[codon]
            except:
                aa = "?"
                
            protein += aa
            if aa == "*": break
        else:
            break
        
    return protein


#HINT(1):
#   If NO second parameter is passed to the function (the default is not changed),
#       the function should use the "standard_code".

#EXAMPLE(1):
protein1=EC_translate("\n  AUGccaaGAGActGAgCC \t\n")
print("standard:",protein1)

#The function would return:
#   MPRD*
 
#HINT(2):
#   If a second parameter is passed to the function (the default is changed),
#       the function should use the "mitochondrial_code".

#EXAMPLE(2):
protein2=EC_translate("\n  AUGccaaGAGActGAgCC \t\n", 1)
print ("mitochondrial:",protein2)

#The function would return:
#   MP*

#Test the function with the following sequences using both "standard" and "mitochondrial" codes:
rna1=" \n \tAUGcaaGCAGuuACAUGAGagguAGGCAAGCACGCAGGAAC   \n\t"
prot1 = EC_translate(rna1)
prot2 = EC_translate(rna1, 1)

print("RNA")
print(" standard:", prot1, "\n", "mitochndrial:", prot2)

dna1=" \n atGTTCAtagTCATTATagTTacagTATTATtCTGa \n\t"
prot3 = EC_translate(dna1)
prot4 = EC_translate(dna1,1)

print("DNA")
print(" standard:", prot3, "\n", "mitochndrial:", prot4)
