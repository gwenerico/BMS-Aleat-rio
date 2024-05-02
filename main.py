import random
import os

def sorteio():
    
    s1 = ""
    s2 = 0
    s3 = 0
    s4 = 0
    s5 = 0
    s6 = 0
    s7 = 0
    s8 = 0
    rand = []


    Quant_sort = ""

    while True:

        Quant_sort = input('''Digite quantas coisas deseja sortear.
entre 2 a 8
''')

        if Quant_sort not in ["2", "3", "4", "5", "6", "7", "8"]:
            pass
        else: 
            break

    if Quant_sort == "2":
        s1 = input('''
Digite deseja sortear
''')
        s2 = input('''
Digite deseja sortear
''')
        rand = [s1, s2]
        random.shuffle(rand)
        
        print('''
Entre aqueles 2 itens o sorteado foi
''')
        print(random.choice(rand))

        repetir()

    elif Quant_sort == "3":
        s1 = input('''
Digite oque deseja sortear
''')
        s2 = input('''
Digite oque deseja sortear
''')
        s3 = input('''
Digite oque deseja sortear
''')
        rand = [s1, s2, s3]
        random.shuffle(rand)
        
        print('''
Entre aqueles 3 itens o sorteado foi
''')
        print(random.choice(rand))

        repetir()
    
    elif Quant_sort == "4":
        s1 = input('''
Digite oque deseja sortear
''')
        s2 = input('''
Digite oque deseja sortear
''')
        s3 = input('''
Digite oque deseja sortear
''')
        s4 = input('''
Digite oque deseja sortear
''')
        rand = [s1, s2, s3, s4]
        random.shuffle(rand)
        
        print('''
Entre aqueles 4 itens o sorteado foi
''')
        print(random.choice(rand))

        repetir()

    elif Quant_sort == "5":
        s1 = input('''
Digite oque deseja sortear
''')
        s2 = input('''
Digite oque deseja sortear
''')
        s3 = input('''
Digite oque deseja sortear
''')
        s4 = input('''
Digite oque deseja sortear
''')
        s5 = input('''
Digite oque deseja sortear
''')
        rand = [s1, s2, s3, s4, s5]
        
        print('''
Entre aqueles 5 itens o sorteado foi
''')
        print(random.choice(rand))

        repetir()

    elif Quant_sort == "6":
        s1 = input('''
Digite oque deseja sortear
''')
        s2 = input('''
Digite oque deseja sortear
''')
        s3 = input('''
Digite oque deseja sortear
''')
        s4 = input('''
Digite oque deseja sortear
''')
        s5 = input('''
Digite oque deseja sortear
''')
        s6 = input('''
Digite oque deseja sortear
''')
        rand = [s1, s2, s3, s4, s5, s6]
        random.shuffle(rand)
        
        print('''
Entre aqueles 6 itens o sorteado foi
''')
        print(random.choice(rand))

        repetir()

    elif Quant_sort == "7":
        s1 = input('''
Digite oque deseja sortear
''')
        s2 = input('''
Digite oque deseja sortear
''')
        s3 = input('''
Digite oque deseja sortear
''')
        s4 = input('''
Digite oque deseja sortear
''')
        s5 = input('''
Digite oque deseja sortear
''')
        s6 = input('''
Digite oque deseja sortear
''')
        s7 = input('''
Digite oque deseja sortear
''')
        rand = [s1, s2, s3, s4, s5, s6, s7]
        random.shuffle(rand)
        
        print('''
Entre aqueles 7 itens o sorteado foi
''')
        print(random.choice(rand))

        repetir()

    elif Quant_sort == "8":
        s1 = input('''
Digite oque deseja sortear
''')
        s2 = input('''
Digite oque deseja sortear
''')
        s3 = input('''
Digite oque deseja sortear
''')
        s4 = input('''
Digite oque deseja sortear
''')
        s5 = input('''
Digite oque deseja sortear
''')
        s6 = input('''
Digite oque deseja sortear
''')
        s7 = input('''
Digite oque deseja sortear
''')
        s8 = input('''
Digite oque deseja sortear
''')
        rand = [s1, s2, s3, s4, s5, s6, s7, s8]
        random.shuffle(rand)
        
        print('''
Entre aqueles 8 itens o sorteado foi
''')
        print(random.choice(rand))
        repetir()

def repetir():
    vr = input('''Quer fazer outro
se sim, digite S
se não, digite N
''').upper()
    
    if vr == "S":
        limpar_his()
        sorteio()
    else:
        print('''
Sorteio aleatório finalizado.
''')
        
    


def limpar_his():

    if os.name == "ponix":
        os.system("clear")
    else:
        os.system("cls")

sorteio()