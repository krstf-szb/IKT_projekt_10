import os
os.system('cls')

def gyertya(x):
    if (x==1):

        print(r"""

     |\
     |#\
     |#/
     \/
     %
  ___%____
 |  Béke  |
 |  .::.  |
 |  .::.  |
 |  .::.  |
 |  .::.  |
 |  .::.  |
 |  .::.  |
 |  .::.  |

""")

    elif (x==2):

        print(r"""

     |\             |\
     |#\            |#\
     |#/            |#/
     \/             \/
     %              %
  ___%____       ___%____
 |  Béke  |     |   Hit  |
 |  .::.  |     |  .::.  |
 |  .::.  |     |  .::.  |
 |  .::.  |     |  .::.  |
 |  .::.  |     |  .::.  |
 |  .::.  |     |  .::.  |
 |  .::.  |     |  .::.  |
 |  .::.  |     |  .::.  |

""")

    elif (x==3):

        print(r"""

     |\             |\              |\
     |#\            |#\             |#\
     |#/            |#/             |#/
     \/             \/              \/
     %              %               %
  ___%____       ___%____        ___%____ 
 |  Béke  |     |   Hit  |      |  Sze-  |
 |  .::.  |     |  .::.  |      | retet  |
 |  .::.  |     |  .::.  |      |  .::.  |
 |  .::.  |     |  .::.  |      |  .::.  |
 |  .::.  |     |  .::.  |      |  .::.  |
 |  .::.  |     |  .::.  |      |  .::.  |
 |  .::.  |     |  .::.  |      |  .::.  |
 |  .::.  |     |  .::.  |      |  .::.  |

""")


    elif (x==4):

        print(r"""

     |\             |\             |\             |\ 
     |#\            |#\            |#\            |#\
     |#/            |#/            |#/            |#/
     \/             \/             \/             \/
     %              %              %              %
  ___%____       ___%____       ___%____       ___%____ 
 |  Béke  |     |   Hit  |     |  Sze-  |     | Remény |
 |  .::.  |     |  .::.  |     | retet  |     |  .::.  |
 |  .::.  |     |  .::.  |     |  .::.  |     |  .::.  |
 |  .::.  |     |  .::.  |     |  .::.  |     |  .::.  |
 |  .::.  |     |  .::.  |     |  .::.  |     |  .::.  |
 |  .::.  |     |  .::.  |     |  .::.  |     |  .::.  |
 |  .::.  |     |  .::.  |     |  .::.  |     |  .::.  |
 |  .::.  |     |  .::.  |     |  .::.  |     |  .::.  |

""")

    else:
        print('Max 4 gyertya van!')

Date = int(input('December hanyadika van?: '))
Kari = 24-Date
print(f"{Kari} nap van még karácsonyig.")
input('Üss az enterre.')

if(Kari<6):
    gyertya(4)
elif(5<Kari<13):
    gyertya(3)
elif(12<Kari<20):
    gyertya(2)
elif(19<Kari<25):
    gyertya(1)

