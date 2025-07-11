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



