## Menu de Opções

1. Cadastrar Funcionário

2. Consultar Funcionário <br>
   2.a Consultar Todos<br>
   2.b Consultar por Id<br>
   2.c Consultar por Setor<br>
   2.d Retornar ao Menu<br>

3. Remover Funcionário

4. Encerrar Programa

## Requisitos

**A.** Implementa o print com o nome da sua empresa.

**B.** Implementa uma lista com o nome `lista_funcionarios` e a variável `id_global` com valor inicial.

**C.** Implementa uma função chamada `cadastrar_funcionario(id)` em que:<br>
&nbsp;&nbsp;&nbsp;&nbsp;   **a.** Pergunta nome, setor e salário do funcionário.<br>
&nbsp;&nbsp;&nbsp;&nbsp;   **b.** Armazena o id (fornecido via parâmetro da função), nome, setor e salário dentro de um dicionário.<br>
&nbsp;&nbsp;&nbsp;&nbsp;   **c.** Copia o dicionário para dentro da `lista_funcionarios`.

**D.** Implementa uma função chamada `consultar_funcionarios()` em que:<br>
 &nbsp;&nbsp;&nbsp;&nbsp;  **a.** Pergunta qual opção deseja (1. Consultar Todos / 2. Consultar por Id / 3. Consultar por Setor / 4. Retornar ao menu).<br>
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     **i.** Se Consultar Todos, apresenta todos os funcionários com todos os seus dados cadastrados.<br>
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     **ii.** Se Consultar por Id, solicita ao usuário que informe um id e apresenta o funcionário específico com todos os seus dados cadastrados.<br>
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     **iii.** Se Consultar por Setor, solicita ao usuário que informe o setor e apresenta o(s) funcionário(s) do setor com todos os seus dados cadastrados.<br>
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     **iv.** Se Retornar ao menu, retorna ao menu principal.<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    **v.** Se entrar com um valor diferente de 1, 2, 3 ou 4, printa `"Opção inválida"` e repete a pergunta D.a.<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    **vi.** Enquanto o usuário não escolher a opção 4, o menu consultar funcionários deve se repetir.

**E.** Implementa uma função chamada `remover_funcionario()` em que:<br>
&nbsp;&nbsp;&nbsp;&nbsp;   **a.** Pergunta pelo id do funcionário a ser removido.<br>
&nbsp;&nbsp;&nbsp;&nbsp;   **b.** Remove o funcionário da `lista_funcionarios`.<br>
&nbsp;&nbsp;&nbsp;&nbsp;   **c.** Se o id fornecido não for de um funcionário da lista, printa `"Id inválido"` e repete a pergunta E.a.
