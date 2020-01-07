
u=['111','222','333','444']
p=[111,222,333,444]
while True:
    us=input('enter your username \n')
    r=us in u
    if(r==1):
       print('username is available')
       pwd=input('enter your password')
       ind=u.index(us)
       if(pwd==p[ind]):
          print('pasword is matched')
       else:
          print('pasword is matched')                                                
    else:
       print('incorrect username')
