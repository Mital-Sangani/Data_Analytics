# How memory is managed in Python? 

"""
Python me memory do main parts me divide hoti hai:

1️⃣ Heap Memory = Yeh dynamically allocated objects (like lists, dictionaries, objects) ko store karti hai. 
Yeh globally accessible hoti hai.

Example: Lists, dictionaries, class objects, etc.

x = [1, 2, 3]  # Heap memory me store hota hai

2️⃣ Stack Memory = Yeh function calls aur local variables ko store karti hai. Jab function execute hota hai, 
tab iska stack frame banta hai, aur function complete hone par delete ho jata hai.

Example: Local variables, function calls

def func():
    a = 10  # Stack memory me store hota hai
    print(a)

func()


"""