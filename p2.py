import os
import statistics

while True:
  tipo=input("Qual média desejada?: \n[p]: para encerrar o programa\n[m]: para média normal \n[mp]: para média ponderada \n[md]: para moda \n[mdn]: para mediana \n:")
  os.system('clear')
  if tipo == "m" :
    m=input("Qual é a matéria?: ")
    i = 1
    x=int(input("Quantas notas?:"))
    l=[]
    while(i <= x):
      i=i+1
      n=float(input("Qual sua nota:"))
      l.append(n)
      soma=sum(l)
      media=soma/x
    if media >= 70:
      os.system('clear')
      print("Matéria: {} \n".format(m))
      print("A média das notas: {} É respectivamente: {}" .format(l,media))
      print("você alcançou a média \nParabéns! Você passou!! \n")
    elif media == 60 :
      os.system('clear')
      print("Matéria: {} \n".format(m))
      print("A média das notas: {} É respectivamente: {}" .format(l,media))
      print("Você passou! porém esta de dependência \n")
    else:
      os.system('clear')
      print("Matéria: {} \n".format(m))
      print("A média das notas: {} É respectivamente: {}" .format(l,media))
      print("você está reprovado! \n")

  
  elif tipo == "mp":
    m=input("Qual é a matéria?: ")
    i = 1
    y=int(input("Quantas notas?:"))
    l2=[]
    l3=[]
    while(i <= y):
      i=i+1
      n2=float(input("Qual sua nota:"))
      n3=int(input("Qual frequência:"))
      produto=(n2*n3)
      l2.append(produto)
      l3.append(n2)
      p2=sum(l3)
    p=sum(l2)
    produto2=(p/p2)
    if produto2 >= 70:
      os.system('clear')
      print("Matéria: {} \n".format(m))
      print("A média ponderada das notas: {} é respectivamente: {} " .format(l2,produto2))
      print("você alcançou a média \n Parabéns! Você passou!!")
    elif produto2 == 60:
      os.system('clear')
      print("Matéria: {} \n".format(m))
      print("A média ponderada das notas: {} é respectivamente: {} " .format(l2,produto2))
      print("Por pouco você nao consegui /nVocê passou! porém esta em dependência /n")
    else:
      os.system('clear')
      print("Matéria: {} \n".format(m))
      print("A média ponderada das notas: {} é respectivamente: {} " .format(l2,produto2))
      print("Você está reprovado! \n")
  elif tipo == "md":
    moda=input("[m]: para moda normal\n[pm]: pra polimodal\n:")
    if moda == "m":
        x0=input("Qual matéria?:")
        x=int(input("Quantas notas?:"))
        l1=[]
        i=1
        while i <=x :
            x1=float(input("Nota:"))
            i=i+1
            l1.append(x1)
        print("Matéria:",x0)
        print("O número com maior frequência é:", statistics.mode(l1))
    elif moda == "pm":
        x0=input("Qual matéria?:")
        x=int(input("Quantas notas?:"))
        l1=[]
        i=1
        while i <=x :
            x1=float(input("Nota:"))
            i=i+1
            l1.append(x1)
        print("Matéria:",x0)
        print("Os números com maior frequência são:", statistics.multimode(l1))
  elif tipo == "mdn":
    x0=input("Qual matéria?:")
    x=int(input("Quantas notas?:"))
    ln=[]
    i=1
    while i <= x:
      x1=float(input("Notas:"))
      i=i+1
      ln.append(x1)
    l=len(ln)
    ln.sort()
    if l % 2 ==0:
      md1=ln[l//2]
      md2=ln[l//2-1]
      mediana=((md1+md2)/2)
    else:
      mediana=ln[l//2]
    print("Matéria:", x0)
    print("A mediana é:"+ str(mediana))
  elif tipo == "p":
    break