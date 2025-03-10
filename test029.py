carspeed=float(input('Type your car´s speed '))
if carspeed >= 80:
    print('You´re getting a fine for speeding,the limit is 80km/h')
    print('The fine is {}$D'.format((carspeed-80)*7 ))
else:
    print('Have a nice trip')
