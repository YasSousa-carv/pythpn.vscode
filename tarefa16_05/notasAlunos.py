lp= [78,45,90,100,85,20,75,66,98,0]

for n in lp:
    if n >= 90:
        print(f'O aluno(a) de {n} pontos recebeu a nota A')
    elif n >=80 and n<90:
        print(f'O aluno(a) de {n} pontos recebeu a nota B')
    elif n >=70 and n<80:
        print(f'O aluno(a) de {n} pontos recebeu a nota C')
    elif n >=60 and n<70:
        print(f'O aluno(a) de {n} pontos recebeu a nota D')
    elif n<60:
        print(f'O aluno(a) de {n} pontos recebeu nota F')
    else:
        print('Erro!')