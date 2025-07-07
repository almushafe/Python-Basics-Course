# variable hota ha data store karna ka lya
# aur value data khlata ha khwa woh kisi bhi qisam ka ho

#  phla variable ata ha phir = eis sign  ka baad valu ko likha

var = 10 # yahan var variable ka name ha aur 10 value ha 10 store ho gya var ka ander ab var ka ander 10 ki power ha
bahi = 'hello'
list = [1,2,3,4,5]
liststring = ['hello', 'world', 'python']
Mix_list = ['hello', 1,3.0,{'name':'ali','age':20}]

tuple = (1,2,3,4,5)

dict = {'name':'ali','age':20}

set = {1,2,3,4,5}
bool = True
float = 10.0
int = 10

print(var)
print(bahi)
print(list)
print(liststring)
print(Mix_list)
print(tuple)
print(dict)





# variable ka kuch aur bhi types han


# single variable 

a = 10
print("single variable",a)

# multiple variable aur multiple value

a,b,c = 10,"string",[234,"error"]
print("multiple variable aur multiple value",a,b,c)

# multiple variable aur single value | chained assignment

a = b = c = 10
print("multiple variable aur single value | chained assignment",a,b,c) 


#  local variable aur global variable
# 1. local variable

def local_variable():
    a = 20
    print(a)

local_variable()
print(a)

# 2. global variable



a = 32415
def local_variable():
    global a # yahan global keyword ka use kiya ha toh a ko global variable banaya ha
    a = 20
    print(a)

local_variable()
print(a)
