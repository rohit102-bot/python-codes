user_dict={'rk':'s123','nk':'k872','ok':'h123'}
#print(user_dict['rk'])
uname=input("enter name:")
if uname in user_dict:
    pwd=input("enter the password:")
    p=user_dict[uname]
    if pwd==p:
        print(f"welcome {uname}")
    else:
        print("password incorrect")
else:
    print("unknown user")