import string 

password="helloworlggd"

#GOING THROUGH ALL THE CHARACTER AND CHECKING IF THERE IS A UPPERCASE LETTER IF YES THEN 1 OTHERWISE 0
#using any that we know wheter its true or false 
upper_case =any( [ 1 if c in string.ascii_uppercase  else 0 for c in password ])
lower_case =any( [ 1 if c in string.ascii_lowercase  else 0 for c in password ])
special =any( [ 1 if c in string.punctuation else 0 for c in password ])
digits =any( [ 1 if c in string.digits  else 0 for c in password ])

#print(string.punctuation)
character = [upper_case, lower_case, special, digits]

length = len(password)

#print(upper_case)


score = 0 

with open('common.txt' , 'r') as f:
    common = f.read().splitlines()

if password in common:
    print("password is too common. score 0/8")
    exit()

#CRITERIA
if length > 8:
    score+=1
if length > 12:
    score +=1
if length >17:
    score +=1
if length >20:
    score +=1