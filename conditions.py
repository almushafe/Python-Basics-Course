"""
https://mimo.org/glossary/python/conditions
https://realpython.com/python-conditional-statements/
https://www.geeksforgeeks.org/python/conditional-statements-in-python/
https://www.w3schools.com/python/python_conditions.asp
"""

#  Python Conditions and If statements

#  condition ka matlab shrtain python main shart wala kam jaisa ka ka agr magr agr ya ho ga to ya nahi ho ga eis trah ki shartin hoti python main inhain if  
# sa repesnt kya jata hai

# if matlab agr matlb shart hai aur jawab shart if ka block ander likh ta han colon ka baad jaisa ka.

if 19 > 1: # main  na bola ka agr (if) 19 bara hai 1 sa 
    print("hellow world") # to helow world print ho 

# esi trah if ka sath ata hai else else ka matlab agr na how ato ya ho ga magr ka mana main jaisa ka.abs

if 19 < 1: # main na kha ka agr (if) 19 1 sa chota ha agr chota hai to  to hello world print ho ja agr 9 1 sa chot nahi hai to phoir ya galt ho jaiga else ho jaiga phir else ka colon ka baad kuch code block likh sakt a ho .
    print('hello woeld')
else:
    print('19 chota nahi 1 muqabla main')


x = 10
if x > 5:
    print("x bara hai 5 se")


x = 2
if x > 5:
    print("x bara hai 5 se")
else:
    print("x chota hai 5 se ya barabar")


# ab ham prh ta hain ifelse matlab agr magr agr jaisa ka 

x = 5
if x > 5:# mana ka ka x agr bara hai 5 sa to mera block cahli agr nahi to agala block ma jao whan phir shat ai gi kya x barabr hai hai 5 sa agr ya sahi howa to eis ka block jchali ga agr eis ka block bhi galt howa to woh defalt main end main chal jai ga.
    print("x bara hai 5 se")
elif x == 5:
    print("x barabar hai 5 ke")
else:
    print("x chota hai 5 se")




