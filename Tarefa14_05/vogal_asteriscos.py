
f = input('Digite uma frase: ')

for l in f:
  f1 = l.replace('a','*')
  f2 = f1.replace('e','*')
  f3 = f2.replace('i','*')
  f4 = f3.replace('o','*')
  f5 = f4.replace('u','*')
  print(f5)