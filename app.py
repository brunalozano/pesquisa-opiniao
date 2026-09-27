# Programa de Pesquisa de Opinião

# Contadores
excelente = 0
ruim = 0

# Repetição para 50 entrevistados e entrada
for i in range(50):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    opiniao = int(input("Digite sua opinião sobre o atendimento prestado, sendo 1 (EXCELENTE), 2 (BOM), 3 (RUIM): ")) 

    if opiniao == 1:
        excelente += 1

    if opiniao == 3:
        ruim += 1

# Saída
print("Quantidade de respostas EXCELENTE:", excelente)
print("Quantidade de respostas RUIM:", ruim)