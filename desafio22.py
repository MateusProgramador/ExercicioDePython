nome= str (input('qual seu nome'))
print (f'seu nome todo maiusculo é {nome.upper()}')
print (f'seu nome todo minusculo é {nome.lower()}')
print (f'seu nome possui {len(nome.replace(' ',''))}')
dividido=nome.split()
print (f'o nome {dividido[0]} possui uma quantia de {len(dividido[0])}')