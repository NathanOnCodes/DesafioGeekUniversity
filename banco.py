from typing import List
from time import sleep

from models.cliente import Cliente
from models.conta import Conta

contas: List = []

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
    pass


def efetuar_saque() -> None:
    pass


def efetuar_deposito() -> None:
    pass


def efetuar_transferencia() -> None:
    pass


def listar_contas() -> None:
    pass


def buscar_conta_por_numero() -> None:
    pass


if __name__ == '__main__':
    main()

