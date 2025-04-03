# Write a Python function to reverses a string if its length is a multiple of 4. 

# multiple of 4 means : 4,8,12,16,.....

def rev(s):
    
    if len(s) % 4 == 0:
        return s[::-1] 
    return s  

print(rev("Python"))      
print(rev("Code"))       
print(rev("HelloWorld"))  