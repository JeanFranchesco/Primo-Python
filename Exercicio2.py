loop=True
while(loop):
  num = int(input("Digite o numero para verificar se e primo "))
  if num > 0 and num <=1000:
    loop=False
numero=0
if num > 1:
  for i in range(2, num):
    if (num % i) == 0:
      break
  else:
     numero = 1;
if numero== 1:
  print("O Numero ",num," Ele e Primo")
else:
  print("O Numero ",num," Ele Nao e Primo")
