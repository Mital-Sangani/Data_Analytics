# What is File function in python? What are keywords to create and write file. 

"""
defination : 

Python me file function wo built-in functions hote hain jo file ke saath kaam karne 
(open, read, write, close) ke liye use hote hain. Ye functions hume system me stored 
files se interact karne ki permission dete hain.

----------------------------------------------------------------------------------------------------------

🔹 Common file functions:

open() - File ko open karta hai.

read() - File ka content read karta hai.

write() - File me naya data likhta hai aur purana data delete ho jata he.

append() - Purani file ka data delete kiye bina naya content add karta hai.

close() - Kaam hone ke baad file close karta hai.

with open() - jo automatically file close kar deta hai.

------------------------------------------------------------------------------------------------------

keyword : "x"

Exclusive Mode - Nayi file create karta hai. Agar file pehle se exist karti hai, to error dega.

keyword : "w"

Write Mode - File me likhne ke liye. Agar file exist karti hai, to pura purana data delete ho jayega.

keyword : "a"

append Mode - File me likhne ke liye. Agar file exist karti hai, to purana data delete nahi hota he new content
add ho jata he


"""