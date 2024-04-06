import re

#FUNÇÃO VALIDA PLACA MERCOSUL
def validar_placas(placas):
    #regex (explicar)
    padrao_placa = r'^[A-Za-z]{3}\d[A-Za-z]\d{2}$'
    
    #ESTRUTURA DE DADOS PARA PLACA VALIDAS E INVALIDAS (ARRAYS)
    placas_validas = []
    placas_invalidas = []

#FAZENDO VALIDÇÃO DAS PLACAS A PARTIR DA REGEX E PACKAGE "RE"
    for placa in placas:
        if re.match(padrao_placa, placa):
            placas_validas.append(placa)
        else:
            placas_invalidas.append(placa)

    return placas_validas, placas_invalidas

#CRIANDO DICIONARIO (COM SET PARA ARMAZENAR MULTIPLOS OBJETOS)
placas_crud = {
    'placas': set()
}

#adiconar placa (function)
def adicionar_placa(placa):
    placas_crud['placas'].add(placa)
    
#remover placa (function)
def remover_placa(placa):
    placas_crud['placas'].discard(placa)

#consultar placa (function)
def consultar_placas():
    return list(placas_crud['placas'])

#validação de cadastro function
def validar_cadastro():
    placas = consultar_placas()
    placas_validas, placas_invalidas = validar_placas(placas)

#usnado função de remoção de placa (remover do vetor)
    for placa in placas_invalidas:
        remover_placa(placa)
    
    return placas_validas, placas_invalidas


#while para imprimir menu e interargir com usuário (interface)
def menu():
    while True:
        print("\nMenu de Gerenciamento de Placas:")
        print("1 - Adicionar placa")
        print("2 - Remover placa")
        print("3 - Consultar placas")
        print("4 - Validar placas cadastradas")
        print("5 - Sair")

#captando input do usuário
        escolha = input("Escolha uma opção: ")

#estrutura de decisão para menu
        if escolha == '1':
            placa = input("Digite a placa para adicionar: ").strip()
            adicionar_placa(placa)
            print("Placa adicionada.")

        elif escolha == '2':
            placa = input("Digite a placa para remover: ").strip()
            if placa in placas_crud['placas']:
                remover_placa(placa)
                print("Placa removida.")
            else:
                print("Placa não encontrada.")

        elif escolha == '3':
            print("Placas cadastradas:")
            for placa in consultar_placas():
                print(placa)

        elif escolha == '4':
            placas_validas, placas_invalidas = validar_cadastro()
            print("Placas válidas:")
            for placa in placas_validas:
                print(placa)
            print("\nPlacas inválidas foram removidas do cadastro.")

        elif escolha == '5':
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")

#bloco de execução do programa (pep-8: boas práticas)
if __name__ == '__main__':
    menu()
