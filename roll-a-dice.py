import random

response = "Y"

continuar = True

while response == "Y":
    
    response = input("Pressione Y para jogar novamente e N para sair: ")

    no = random.randint(1,6)

    if no == 1:
      print("[-----]")
      print("[     ]")
      print("[  0  ]")
      print("[     ]")
      print("[-----]")

    if no == 2:
      print("[-----]")
      print("[0   0]")
      print("[     ]")
      print("[ 0 0 ]")
      print("[-----]")

    if no == 3:
      print("[-----]")
      print("[0   0]")
      print("[  0  ]")
      print("[ 0 0 ]")
      print("[-----]")

    if no == 4:
      print("[-----]")
      print("[0    ]")
      print("[    0]")
      print("[0    ]")
      print("[-----]")

    if no == 5:
      print("[-----]")
      print("[  0  ]")
      print("[ 0 0 ]")
      print("[0   0]")
      print("[-----]")

    if no == 6:
      print("[-----]")
      print("[0   0]")
      print("[ 0 0 ]")
      print("[  0  ]")
      print("[-----]")

response = input("Digite Y para continuar ou N para sair: ")
      
if response.lower() == 'N':
    continuar = False
