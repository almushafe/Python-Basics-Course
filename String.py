# string khta han text ko jo do string ka dermyan ai "" or ''.abs
# single qoutes or double qoutes dono use kar sakta han
hello = "hello world" # string ko declare karna ha toh uska dermyan use karna ha 
#  multi line string ko declare karna ha toh uska dermyan use karna ha
hello = '''
lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quos.
lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quos.
'''

#  ab string ka mazeed functionality hai

# specal cracters ko string ma kasia likhan 

a = "hello \"World\""
print(a)

# repetion matlab eik string bar bar

a = "hello" * 10
print(a)

# text indexing matlab jo likha howa ha us ka har word kon sa number per ha ya find karta ha. 

# index 0 se start hota ha aur find karta han phla string phir us ka sath [0] P

a = "python"[4]
print(a)
# print(a[0])
# print(a[-1])


#  string slicing matlab eik string ko do string ma divide karta ha
# eis ko istam karna ha to eis tarah  :   string[start:stop]

variable1 = "Python"[1:5] # 1 wala word ko print kara ga aur : 5 wala ko print nahi kara ga
variable2 = "Python"[2:3] # 2 wala word ko print kara ga aur : 3 wala ko print nahi kara ga
variable3 = "Python"[2:-3] # 2 wala word ko print kara ga mager se -3 wala ko print nahi kara ga
print(variable1)
print(variable2)
print(variable3)
# print(variable[0:4])



# String methods

# Upper case matlab har word ko capital kar deta ha
Captial = "hello".upper()
print(Captial)
# print(Captial.upper())

# capitaize ya shro ka word ko capital kart ha 

captial = "hello".capitalize()
print(captial)
# print(captial.capitalize())



# replace string matlaqb badlna chnge karna ha

ReplaceOne = "World"
replace = "hello".replace("hello","python")
print(replace)
print(ReplaceOne.replace("World", "Hello"))


# String lenght maloom karin 

StringLenght = len("Python")
print(StringLenght)
# print(len(StringLenght))



#  f string eis ine ka nader hamain aur mazeed power mil jata han

f = "World!"
fString = f"Hellow {f} "
print(fString)



# String check  

text = "hello world, python"
print("python" in text) # in use hota ha ka batata ha ka eis string ma ya ha ya nahi agr na ho to false return kara ha

# cheik nahi karo 
txt = "World Python"
print('python'not in txt)


# String split matlab eik string ko do string ma divide karta ha

