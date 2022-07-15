# Greg_Abacaxi ~ 15/07/22
# Versão 1.1

# Declaração de variáveis 
cpf = 'a'
n1 = 0
n2 = 0
j = 0

# Input e correção de edgecase
print('-=*=' * 14 + '-')
cpf = str(input('>> Digite os 9 primeiros números do CPF: '))
cpf = cpf.replace('.', '')
cpf = cpf.replace('-', '')
cpf = cpf.replace(' ', '')

# Operações para determinar o primeiro dígito verificador
for i in range(10, 1, -1):
    n1 += int(cpf[j]) * i
    j += 1

if (n1 % 11 >= 2):
    n1 = 11 - (n1 % 11)
else: 
    n1 = 0

cpf = cpf + str(n1)

# Reset da variável de controle j
j = 0

# Operações para determinar o segundo dígito verificador
for i in range(11, 1, -1):
    n2 += int(cpf[j]) * i
    j += 1

if (n2 % 11 >= 2):
    n2 = 11 - (n2 % 11)
else: 
    n2 = 0

cpf = cpf + str(n2)

# Formatação do CPF para o modelo padrão
cpf1 = str(cpf[0] + cpf[1] + cpf[2])
cpf2 = str(cpf[3] + cpf[4] + cpf[5])
cpf3 = str(cpf[6] + cpf[7] + cpf[8])
cpf4 = str(cpf[9] + cpf[10])
cpf = str(cpf1 + '.' + cpf2 + '.' + cpf3 + '-' + cpf4)

# Retorno do CPF com os dígitos verificadores
print('-=*=' * 14 + '-')
print('>> CPF com dígitos de verificação: \033[1;32m{}\033[0;0m'.format(cpf))
print('-=*=' * 14 + '-')

#Teste