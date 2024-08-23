import re
email_regex = r'^[a-zA-Z]+\.[a-zA-Z]+@fpmoz\.sum\.ba$'

eduId_regex = r'^[a-zA-Z][a-zA-Z]+@sum\.ba$'

email=input("Unesite e-mail: ")
eduId=input("Unesite eduId: ")

if re.match(email_regex, email):
    print("e-mail je ispravan!")
else:
    print("e-mail nije ispravan!")

if re.match(eduId_regex, eduId):
    print("eduId je ispravan!")
else:
    print("eduId nije ispravan!")
