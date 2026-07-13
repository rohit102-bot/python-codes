userdict={'naresh':'n123','suresh':'s321','ramesh':'r567'}
def login(uname,pwd):
    if uname in userdict and pwd:
        return True
    else:
        False