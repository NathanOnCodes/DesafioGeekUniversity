from typing import List
from time import sleep

from models.cliente import Cliente
from models.conta import Conta

contas: List[Conta] = []

def main() -> None:
    menu()


def menu() -> None:
    print('====================================')
    print('=============== ATM ================')
    print('============ Geek Bank =============')

    print('\nSelecione uma opção no menu:')
    print('1 - Criar conta')
    print('2 - Efetuar saque')
    print('3 - Efetuar depósito')
    print('4 - Efetuar transferência')
    print('5 - Listar constas')
    print('6 - Sair do sistema')

    opcao: int = int(input())
    match opcao:
        case 1:
            criar_conta()
        case 2:
            efetuar_saque()
        case 3:
            efetuar_deposito()
        case 4:
            efetuar_transferencia()
        case 5:
            listar_contas()
        case 6:
            print('Volte sempre!')
            sleep(2)
            exit(0)
        case _:
            print('Opção inválida!')
            sleep(2)
            menu()
            
def criar_conta() -> None:
    print('Informe os dados do cliente: ')

    nome: str = str(input('Nome: '))
    email: str = str(input('Email: '))
    cpf: str = str(input('CPF: '))
    data_nascimento: str = str(input('Data de nascimento: '))

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)
    conta: Conta = Conta(cliente)

    contas.append(conta)

    print('Conta criada com sucesso!')
    print('Dados da conta: ')
    print('-----------------')
    print(conta)
    sleep(2)
    menu()

def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta: '))
        conta: Conta = buscar_conta_por_numero(numero)
        if conta:
            valor: float = float(input('Informe o valor do saque: '))

            conta.sacar(valor)
        else:
            print(f'Não foi encontrada a conta com o número {numero}')
    else:
        print('Ainda não existem contas cadastradas.')
    sleep(2)
    menu() 


def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número conta: '))
        conta: Conta = buscar_conta_por_numero(numero)
        if conta:
            valor: float = float(input('Informe o valor do depósito: '))

            conta.depositar(valor)
        else:
            print(f'Não foi encontrada a conta com o número {numero}')
    else:
        print('Ainda não existem contas cadastradas.')
    sleep(2)
    menu()


def efetuar_transferencia() -> None:
    if len(contas) > 0:
        numero_conta_origem = int(input('Informe o número da sua conta: '))
        conta_origem: Conta = buscar_conta_por_numero(numero_conta_origem)

        if conta_origem:
            numero_conta_destino: int = int(input('Informe o número da conta de destino: '))
            conta_destino: Conta = buscar_conta_por_numero(numero_conta_destino)

            if conta_destino:
                valor: float = float(input('Informe o valor da transferência: '))

                conta_origem.transferir(conta_destino, valor)
            else:
                print(f'A conta destino com o número {numero_conta_destino} não foi encontrada.')
        else:
            print(f'Conta de número {numero_conta_origem} não encontrada.')
    else:
        print('Ainda não existem contas cadastradas.')
        sleep(2)
        menu()


def listar_contas() -> None:
    if len(contas) > 0:
        print('Listagem de contas')

        for conta in contas:
            print(conta)
            print('-------------------')
            sleep(1)
    else:
        print('Não existem contas cadastradas.')
        sleep(2)
        menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c


if __name__ == '__main__':
    main()

