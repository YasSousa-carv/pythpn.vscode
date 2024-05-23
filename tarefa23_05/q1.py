hmax = int(input("Digite uma altura máxima: "))
hmin = int(input("Digite uma altura mínima: "))

h_a = {
    'aluno1':165,
    'aluno2':190,
    'aluno3':175,
    'aluno4':145,
    'aluno5':164,
    'aluno6':176,
    'aluno7':150,
    'aluno8':168,
    'aluno9':173,
    'aluno10':182
}

for h,a in h_a.items():
    if a > hmax:
        print(f'{h} é a altura máxima')
    elif a < hmin:
        print(f'{h} é a altura mínima')