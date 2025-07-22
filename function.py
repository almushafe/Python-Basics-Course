# Python Function Tutorial
"""
https://www.geeksforgeeks.org/python/advanced-python-tutorials/

https://ipython.ai/advanced-guide-python-functions-scope-beyond/

https://www.geeksforgeeks.org/python/python-variables/
"""

# Python ma Function kya hota ha
#  python ma fucntion eik code block hota hai jo kisi khas kam karna ka lya banya jata hai

# aur koi kam ham na bar bar karna ho to ham function ka istemal karte hain

# function ka istemal karne se hamara code chota aur asan ho jata hai

# function ki basics 
def function_name():
    # yahan par ham function ka code likhte hain
    print("Hello, World!")

#  def eik keyword ha aur ya function define karna ka lya istemal hota hai
#  aur def keyword likhna ka baad function ka naam likhte hain
#  function ka naam likhne ka baad parentheses () lagate hain 
# aur parenthse ka ander jo likhta han eis ko khta han input lana  ya argumant value (optional)
#  colon : (:) lagana na bhoolna 
# aur colon ka matlab hota hai ke ab function ka body shuru ho raha hai
# return output ka lya ya wapis karna ka lya istaml hota hai


def greet(name):
    """
    function ka name greet hai aur yeh eik argument name leta hai
    """
    print(f"Hello, {name}!")  # Function body: prints a greeting message printing the name

# Function call karna ka traiqa bohat simple ha ap us function ka naam likho aur parentheses () lagao

# eik argumant dain kyon ka apna function bana ta howa argument dya tha name ka nam sa eis lya ab ap yahan eis argument ma eik string  pass YA KUCH BHI  karin agin

greet('Alice')  # Function call: passing 'Alice' as an argument to the function
# Function call with a different argument
greet(4+5)    # Function call: passing 'Bob' as an argument to the

# hum multiple bhi perameter da saktainhain

# jaisa ka function ka naam multiple hai aur yeh eik argument name leta hai
def multiple(a,b):
    """
    function ka name multiple hai aur yeh do arguments leta hai a aur b
    """
    print(f"The sum of {a} and {b} is {a + b}")  # Function body: prints the sum of a and b

# Function call with two arguments
multiple(10, 20)  # Function call: passing 10 and 20 as arguments to the function

# eik aur khasyat dikr karta hon function i varable lenght premeter
# jsia ka "*args"
def greet(*args): # eis o bolta han arbitrary eis ka matlab man caha ap kuch bhi da sakta han leken argument eik tuple ki sorat ma ander ata han
    print(args)

greet(1,2,3,4,56,120)

# ya bhi eik keyword ha function permeter ma istaml karna ka **kwargs
def naya(**kwargs):
    '''eis ka matlab ha ka function ko  keyword arguments jitna chhain da sakta han
    leken ya sub eik ditonry ki sorat ma ander jata han
    '''
    print(kwargs)

naya(name='Muhamamd',Age=20,profasion='I am Student')

# Eik Zarori baat yaad rkhain ka function ka bracket ka ander jo ham likhta hain woh hota variable hi han liken eis ko function sath khas kya gya ha eis lya eis ka name varible ka perameter kha gya ha aur variable ki value ko yahn argument khta han






def greet(name):  # ← یہاں 'name' ایک **parameter** ہے
    print("Hello", name)

greet("Ali")       # ← یہاں "Ali" ایک **argument** ہے




def show_info(*args, **kwargs):  # ← parameters
    print(args)
    print(kwargs)

show_info(1, 2, name='Ahmed', age=23)  # ← arguments






# return woh keyword ha jo function sa output da a ha function ki traf sa resut wapis la na ka lya 

# print aur function ma farq ya ha print sirf console pa out put dhka ta ha aur tempory hota aur ya function ka out put data ha aur sath ath ya value wapis karta ha 

def check():
    print("Hello")    # ← صرف دکھا رہا ہے
    return "Bye"      # ← value واپس دے رہا ہے

result = check()
print("Returned:", result)



# default perameter 

def nice(name='Muhamamd'):
    print("Aslam U alikm", name)

nice()
nice("Saad") 


#  Keyword Arguments

# jasa ka mana permeter dya us ma key argument da dya
def wah(name,Age):
    print(f'Mera Name {name} ', f' {Age} sal umer ha', sep=' ha ma Alhamduliilah meri')

wah(name='Muhamamd', Age=20)


# Ab sab sa main topicha aur muskil bhi aur zarori bhi us ka name ha recursion

# recursion eik function ko kAI BAR CALL kar sakta ha

# jsa ka




# recursion topic descuse coming soon



























# lambda function ya bara maza ka ha
# ya ei anonums function hoa ha

show =lambda x : print(x) # x ya permeter ha colon sa function shro hota ah

show(20)

(lambda name:print(name))("Muhamamd")
# eis funcion ko baqyda name nahi dya gya



#  Advanced Concepts (صرف سمجھنے کے لیے ابھی):


