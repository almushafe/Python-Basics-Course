"""
https://www.w3schools.com/python/python_while_loops.asp
https://www.programiz.com/python-programming/while-loop
https://www.coursera.org/tutorials/python-while-loop
https://serveracademy.com/blog/python-while-loop-tutorial/
https://www.tutorialspoint.com/python/python_while_loops.htm
"""

#  While loop

# while loop Kya Hai?
# while loop aik aisi loop hai jo tab tak repeat hoti hai jab tak uska condition True rehta hai. Jab condition False ho jaye, loop ruk jata hai.

# while condition:
    # code block


i = 1  # Step 1: Variable i ki value 1 rakhi
while i <= 5:  # Step 2: Jab tak i ki value 5 se chhoti ya barabar hai, loop chalega
    print(i)   # Step 3: i ki current value print karo
    i += 1     # Step 4: i ki value mein 1 ka izafa karo (i = i + 1)




# Jee haan, aap while True: ka use kar sakte hain Python mein, lekin is tarah ka loop infinite loop hota hai, kyunki condition True hamesha true rehti hai.
while True:
    print('hello')
# Yeh code bina kisi rukawat ke lagataar 'hello' print karta rahega — jab tak aap manually program ko stop na karen (jaise terminal mein Ctrl+C dabakar).

# Iska use kab hota hai?
# while True: ka use tab kiya jata hai jab aapko:

# Continuously koi kaam repeat karna ho ( kisi user input ka intezaar karna).

# Jab aapko loop ko manually break karna ho kisi condition ke basis par, jaise:


while True:
    user_input = input("Type 'exit' to stop: ")
    if user_input == 'exit':
        break # Yeh example safe hai kyunki isme break ka use hai jo loop ko rok sakta hai.
    print("You typed:", user_input)

