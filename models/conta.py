from models.cliente import Cliente
from utils.helper import float_str_moeda

class Conta:

    """
        Essa classe representa uma conta bancária.

        Temos os seguintes métodos e propriedades:
            Sacar,
            Depositar,
            Transferir,
            Extrato,
            Limite,
            Saldo Total.
    """

    codigo: int = 1001

    def __init__(self: object, cliente: Cliente) -> None:
        self.__codigo: int = Conta.codigo
        self.__cliente: Cliente = cliente
        self.__saldo: float = 0.0
        self.__limite: float = 100.0
        self.__saldo_total : float = self._calcula_saldo_total
        Conta.codigo += 1

    def __str__(self: object) -> str:
        return f'Código: {self.__codigo}\nCliente: {self.__cliente}\nSaldo: \
        {float_str_moeda(self.__saldo)}\nLimite: \
          {float_str_moeda(self.__limite)}\nSaldo Total: \
        {float_str_moeda(self.__saldo_total)}'

    @property
    def numero(self: object) -> int: 
        return self.__numero
    
    @property
    def cliente(self: object) -> Cliente:
        return self.__cliente
    
    @property
    def saldo(self: object) -> float:
        return self.__saldo
    
    @saldo.setter
    def saldo(self: object, valor: float) -> None:
        self.__saldo = valor

    @property
    def limite(self: object) -> float:
        return self.__limite
    
    @limite.setter
    def limite(self: object, valor: float) -> None:
        self.__limite = valor
    @property
    def saldo_total(self: object) -> float:
        return self.__saldo_total

    @property
    def _calcula_saldo_total(self: object) -> float:
        return self.__saldo + self.__limite
    
    def depositar(self: object, valor: float) -> None:
        pass
    
    def sacar(self: object, valor: float) -> None:
        pass

    def transferir(self: object, conta_destino: object, valor: float) -> None:
        pass

    def extrato(self: object) -> None:
        pass