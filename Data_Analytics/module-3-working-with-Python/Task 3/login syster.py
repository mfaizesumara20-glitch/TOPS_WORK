# w.a.p to authentications of password if user input correct password its authanticated login sussesfully outher wise incorrect password if users continue enter three attemps password fail your accout will be blocked

# for i in range (1,4):
#     email = input('Enter your email')
#     password = input('Enter your password')
#     i = i+1

#     if email == 'admin@gmail.com' and password == 'admin@123':
#         print('you have loged in successfully')
#     else:
#         print('something is wrong try again')
# else:
#     print('you are out of attempts your account is')


for i in range(1, 4):
    email = input('Enter your email: ')
    password = input('Enter your password: ')

    if email == 'admin@gmail.com' and password == 'admin@123':
        print('You have logged in successfully')
        break
    else:
        print('Something is wrong, try again')
else:
    print('You are out of attempts. Your account is locked.')