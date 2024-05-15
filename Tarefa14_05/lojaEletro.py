i = ['computador','celular','fone de ouvido']
v = [2719,1666,210]
tp = sum(v)
print(f'Olá, seja bem vindo(a)!Sua lista de eletronicos,{i},deu um total parcial de {tp} reais.')
print('')
if tp > 500:
  tt = tp * 0.9
  print(f'Sua compra por atigir um valor mínimo de 500 reais,recebeu um desconto de 10%')
  print(f'O valor total é de {tt} reais.')
else:
  print('Sua compra não atingiu o valor mínimo de 500 reais,por isso não recebeu nenhum desconto')
  print(f'O valor total é de {tp} reais.')