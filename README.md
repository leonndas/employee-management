Este software conta com o seguinte menu de opções:

1. Cadastrar Funcionário 
2. Consultar Funcionário
   2.a Consultar Todos 
   2.b Consultar por Id 
   2.c Consultar por setor 
   2.d Retornar ao menu 
3. Remover Funcionário 
4. Encerrar Programa 
        
A.	Implementa o print com o nome da sua empresa. 
B.	Implementa uma lista com o nome de lista_funcionarios e a variável id_global com valor inicial.
C.	Implementa uma função chamada cadastrar_funcionario(id) em que:
  a.	Pergunta nome, setor, salario do funcionário;
  b.	Armazena o id (este é fornecido via parâmetro da função), nome, setor, salário dentro de um dicionário;
  c.	Copia o dicionário para dentro da lista_funcionarios;
D.	Implementa uma função chamada consultar_funcionarios() em que:
  a. Pergunta qual opção deseja (1. Consultar Todos / 2. Consultar por Id / 3. Consultar por Setor / 4. Retornar ao menu):
    i.	Se Consultar Todos, apresenta todos os funcionários com todos os seus dados cadastrados;
    ii.	Se Consultar por Id, solicita ao usuário que informe um id, e apresenta o funcionário específico com todos os seus dados cadastrados;
    iii.	Se Consultar por Setor, solicita ao usuário que informe o setor, e apresenta o(s) funcionário(s) do setor com todos os seus dados cadastrados;
    iv.	Se Retornar ao menu, retorna ao menu principal;
    v.	Se entrar com um valor diferente de 1, 2, 3 ou 4, printa “Opção inválida" e repete a pergunta D.a.
    vi.	Enquanto o usuário não escolher a opção 4, o menu consultar funcionários deve se repetir.
E.	Implementa uma função chamada remover_funcionario() em que:
  a.	Pergunta pelo id do funcionário a ser removido;
  b.	Remove o funcionário da lista_funcionarios;
  c.	Se o id fornecido não for de um funcionário da lista, printa “Id inválido” e repete a pergunta E.a.
