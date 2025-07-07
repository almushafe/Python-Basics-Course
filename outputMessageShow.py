# phli baat ab jo hum parh raha han ya khlta ha eik function jo kam karta ha ka ap ka code ko output ma show karta ha matlab output ki screen ma ap ka code show hota ha.

# eis ka function kuch yon ha : print()  ya function ka name  ha (print) aur () esa bracet khta han aur ya python ka shtx ha name ka sath agr ya ai to shmjah jain ka ya eik function ha .

print() # ya print function ha aur function bracet ma kuch permeter khas hota han us function sa jo built karta han to print ka ander bhi kuch permeter han woh kitna han : eis ka ander 5 permeter han.

# Syntax

# print(object(s), sep=separator, end=end, file=file, flush=flush) 

# 1. phla permeter ha object(s) ha jo kisi bhi cheez ko string ma convert karta ha .
# 2. ya premeter sep=separotor eik sa zyadh string han to yah ein ko suprate karta ha liken ya optional ha na bhi karo phir bhi theek ha.
# 3. ya premeter end=end  ya do line ko eik line ma hi karta ha jaisa ka dono line ma string han ya dono ko eik line ma karda ga liken ya bhi otional ha.

# 4. ya perameter file=file jis ma file ka ander data save karta han ya string ya bhi otional ha.

# 5. ya perameter flash=flash ya bata ta ha ka ap ka output flash aya ya buffer ya bhi optional.

# ab ein sub ka bara ma bata ta hain eik eik kar ka ka kaisa use hota han

# 1 ----------- Object(s)

# > ya eis ka basic use ha
print("Hello World!") # one argument

# > ya multiple argument da bhi sakta han kaisa
print("Hello World !", "Wellcome", 123) #multiple argument

# 2 -------------------------- sep

print("Hello","world", sep=" ") # blank space
print("Hello","world", sep="-") # use dash -
print("Hello","world", sep=",") # use comma ,
print("Hello","world", sep=".") # use dot , eg.

# 3 -------------- end

print("hello",end=" ") # dono line eik line ho gai ap end sa hi agli line add ho kjai gi
print("world")

# 4 ------------- file

# > ya asal ma file banata han us ka ander data stroe karta han abhi pershan nahon sirf stucture dhkaihn ka yah bhi se ho ga.abs

with open("demo.txt",'w') as f:
    print("Hello World!", file=f)

# dosra logic

import sys

print("Hello", file=sys.stdout)


# 5 --------------------- flush 

# > ya bhi code abhi shmjah nahi ai ga aga ai ga eis lya eis ko shmjain sirf ya flush agr true ho ga to who line print ho jai gi gar false ho ga to dono line print ho jai gi.


import time

print("Loading...", end='', flush=True)
time.sleep(2)
print(" Done")

# dosra logic

for i in range(5):
    print(i, end=" ", flush=True)
    time.sleep(1)
print('Done')








#  f- string

print(f"Hello {10 + 20}")






