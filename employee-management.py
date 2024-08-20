print ('Bem vindo à empresa do Leon Santiago')

idglobal = 4851208 #RU
lista_funcionarios = []
funcionario = {}


#funções
def cadastrar_funcionario(id):
    nome = input('Qual o nome do funcionário?')
    setor = input('Qual o setor do funcionário?')
    salario = float(input('Qual o salário do funcionário?'))
    
    #dicionário, chave e valor (string)
    funcionario = {'id': id, 'nome': nome, 'setor': setor, 'salario': salario}

    lista_funcionarios.append(funcionario.copy())
    
def consultar_funcionario():
    while True:
        print ('Opções:')
        print ('1. Consultar todos')
        print ('2. Consultar por ID')
        print ('3. Consultar por setor')
        print ('4. Retornar ao menu')
        
        try:
            escolha = int(input('Qual opção deseja?'))
            
            while escolha not in [1, 2, 3, 4]: #se é um número, mas nao 1 2 ou 3
                print ('Por favor, escolha um número válido.')
        
        except ValueError: #se não é número
            print ('Por favor, escolha um número válido.')
            continue

        #escolhas do menu
        if escolha == 1:
            print (lista_funcionarios)

        elif escolha == 2:
            id = int(input('Por favor, insira o ID do funcionário:'))

            #loop for percorre cada 'funcionário' na lista de funcionários
            for funcionarios in lista_funcionarios:
                if funcionarios ['id'] == id:
                    print (funcionarios)  
                    break #termina aqui se encontrado, se n vai continuar buscando
            else:
                print (f'Funcionário com ID {id} não encontrado.')

        elif escolha == 3:
            setor = (input('Por favor, insira o setor do funcionário:'))
            find = False

            #loop for percorre cada 'funcionário' na lista de funcionários
            for funcionarios in lista_funcionarios:
                if funcionarios ['setor'] == setor:
                    print (funcionarios) #printa o dicionario 'funcionario' 
                    find = True
                    
            if not find:
                print (f'Funcionário com setor {setor} não encontrado.')

        elif escolha == 4:
            return
    
        else:
            print ('Tente de novo.')

def remover_funcionario():
    id = int(input('Qual a ID do funcionário a ser removido?'))

    find = False
    for funcionario_a_ser_removido in lista_funcionarios:
        
        if funcionario_a_ser_removido ['id'] == id:
            lista_funcionarios.remove(funcionario_a_ser_removido)
            print (f'Funcionário com ID {id} removido com sucesso.') 
            find = True

            break #sai do loop apos encontrar funcionario pelo id e remover
    if not find:
        print (f'Funcionário com o ID {id} não foi encontrado.')

#main
while True:
    print ('Empresa Leonidas')
    print (' ')
    print ('1. Cadastrar funcionários')
    print ('2. Consultar funcionários')
    print ('3. Remover funcionário')
    print ('4. Sair')
    
    try:
        escolha = int(input('Qual opção deseja?'))
    
        while escolha not in [1, 2, 3, 4]: #se nao for numero valido
            print ('Escolha uma opção válida.')
        
    except ValueError:  #se nao for numero
            print ('Escolha uma opção válida.')
            continue

    if escolha == 1:
        idglobal += 1
        cadastrar_funcionario(idglobal)
    
    elif escolha == 2:
        consultar_funcionario()

    elif escolha == 3:
        remover_funcionario()

    elif escolha == 4:
        print ('Encerrando o programa...')
        break
