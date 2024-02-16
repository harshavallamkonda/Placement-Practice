O = 6.34 # Global Variable
def p(): #Defining a Function
    O = "PQR" # This is Local Variable
    print(" This is a Sample " + O) # Printing of Local Variable
p() #This means in line 2 you have defined a function but after defining you need to close the function right
print (O) # Printing of Global Variable

########################################

#Using Global Variable Inside a Function

def Q():
    global R #Here global is a python keyword where we used this 'R' keyword globally
    R = "Vallamkonda"
    print(R)
Q() #closing of a function
print ("Hello this is family of " + R)
    
