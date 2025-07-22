"""
https://wiki.python.org/moin/ForLoop
https://www.programiz.com/python-programming/for-loop
https://www.geeksforgeeks.org/python/python-for-loops/
https://realpython.com/python-for-loop/#iterating-over-multiple-iterables-sequentially  # advanced
"""

# for loop
# ____________________________________________________________________________________________________

# forloop python ka ander eik khasiyat hai jo kisi code block ko bar bar chalane ka lya istemal hota hai
# foorloop ko ham list ma ya dictionary ma istemal karte hain aur wagirah.

#  for loop ka istemal karne se hamara code chota aur asan ho jata hai
# for loop ki basics

# for loop shroh hota ha ( for) name ka keywords aur phir eik variable ka naam likhte hain us ka baad in keyword ko likhta han jis ka matlab ha ka ap list ya kisi cheez ko ander sa items nikal raha han .

for item in [1,2,3,4,5]:
    print(item)  # Function body: prints each item in the list . ya loop ka ander ka code ha


#  for loop ka istemal karne ka traiqa bohat simple ha ap us for loop ka naam likho aur in keyword lagao aur phir eik variable ka naam likho aur phir list ya kisi cheez ko ander sa items nikal raha han .


# jaisa eik range class ki misal da ta han

# range eik class ha jisa aam tor per for loop ma istaml kya jata hai
# range ka 3 premeter hota han jis ma eik deafault hota ha agr apistaml kari 
# woh stop ha stop ka matlab ha ka loop kab tak chalega
# aur start ka matlab ha ka loop kahan se shroh hoga aur step ka matlab
# aur step ka matlab ha ka loop kitne kitne bar chalega

# range(start, stop, step)

for i in range(1, 10, 2):  # Loop from 1 to 9 with a step of 2
    print(i)  # Function body: prints each number in the range


# kuch asa key words jo loop ka ander istaml kya jata han jaisa ka .
#  break | continue | pass

#  break
# break ka istemal karte hain jab ap chahte hain ka loop ko band karna hai
# matlab loop ko chlata howa rook don

# jaisa ka

for i in range(1, 10):
    if i == 5:  # Condition to break the loop
        break  # Breaks the loop when i is equal to 5
    print(i)  # Function body: prints each number until the loop is broken

# -------------------------------------------------------------------------------

# continue
# continue ka istemal karte hain jab ap chahte hain ka loop ko agla iteration par jana hai
#  matlab bahi sedh sadh ignor skip karna code ko chal dana

for i in range(1, 10):
    if i == 5:  # Condition to skip the current iteration
        continue  # Skips the rest of the loop body when i is equal to 5
    print(i)  # Function body: prints each number except when i is equal to 5


# ----------------------------------------------------------------------------------------------

# pass

#  pass ka faidh ya hai ka program ma error na aaye aur loop ko chalayen ya jab likhta han jab loop ka ander kuch nahi likh rha

for i in range(1, 10):
    pass # pass ka matlab ha ka ap kuch nahi karna chahte hain lekin loop ko chalana chahte hain 



# ___________________________________________________________________________________________________



