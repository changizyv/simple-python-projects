import re
a= input("Please enter your number: ")
# delete space or string characters
b= re.sub("^\+98","0",a)
# convert "Phone country code" to "0"
c= re.sub("\D","",b)
# convert "0098" to "0"
d= re.sub("^0098","0",c)
print ("your number with true format is : " , d)

