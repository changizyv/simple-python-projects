import re
a= input("Please enter your number: ")
# حذف همه کاراکترهای غیر عددی
b= re.sub("^\+98","0",a)
# تبدیل "+98" در ابتدای رشته به "0"
c= re.sub("\D","",b)
# تبدیل "0098" در ابتدای رشته به "0"
d= re.sub("^0098","0",c)
print ("your number with true format is : " , d)

