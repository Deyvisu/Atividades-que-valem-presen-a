import json

class Funcionario:
    def __init__(self, id, nome, salario):
        self._id = id
        self._nome = nome
        self._salario = salario

with open('banco.json') as b:
    banco = json.load(b)

funcionarios = []

for funcionario in banco:
    funcionarios.append(Funcionario(funcionario["ID"], funcionario["Nome"], funcionario["Salario"]))

for i in range(len(funcionarios)):
    print(f"{funcionarios[i]._id} - {funcionarios[i]._nome}")

op = int(input("Digite o número do funcionário que deseja ver o salário:"))

print(f"O salario de {funcionarios[op-1]._nome} é RS: {funcionarios[op-1]._salario}")


