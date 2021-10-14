# **Bracket Checker**

This utility checks the code for the correct use of **brackets**.

If your data has an **incorrect** use of **brackets**, the program will return a false operand object (*False*).

If all is **well**, you get a true operand object. (*True*)

# **How to use?**

## **Like a library.**
Add this line to the block of imports in your code:
```
import bracket_check
```
### **For strings:**
```
bracket_check("You string object.") 
```


### **For files:**
```
bracket_check("you/path/file.py")
```


## **Like a utility.**
### **For text:**
```
$ python3 -m bracket_check "your text"
```
or
```
$ python3 -m bracket_check 'your text'
```
or
```
$ python3 -m bracket_check your_text
```


### **For files:**
```
$ python3 -m bracket_check you/path/file.py
```


# **Testing**

This program has a number of tests of its own, if you want to run them use the code below:
```
$ pytest bracket_check
```


# **Info**
*This product is incomplete and will be further refined.*
