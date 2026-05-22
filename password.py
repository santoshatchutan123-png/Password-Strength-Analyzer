import re
password=input("enter the password")
st=""
score=0
if len(password)>=12:
    score=+2
elif len(password)>=8:
    score=+1
if re.search(r"[a-z]",password):
    score=+1
if re.search(r"[A-Z]",password):
    score=+1
if re.search(r"/d",password):
    score=+1
if re.search(r"[@#$%^&*]",password):
    score=+1
if score <=2:
    st = "weak"
elif score <=5:
    st = "medium"
else :
    st = "strong"
print("strength :",st)
if st == "weak":
    suggestion=password.capitalize()+"@2408"
print("suggested password :",suggestion)

