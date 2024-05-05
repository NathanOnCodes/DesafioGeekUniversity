from datetime import date
from utils.helpers import date_to_str, str_to_date

class Cliente:
    contador = 101

    def __init__(self: object, nome: str, email: str, cpf: str, data_nascimento: str) -> None:
        self.__codigo: int = Cliente.contador
        self.__nome: str = nome
        self.__email: str = email
        self.__cpf: str = cpf
        self.__data_nascimento: date = str_to_date(data_nascimento)
        self.__data_cadastro: date = date.today()
        Cliente.contador += 1

    @property
    def codigo(self: object) -> int:
        return self.__codigo
    
    @property
    def nome(self: object) -> str:
        return self.__nome
    
    @property
    def email(self: object) -> str:
        return self.__email
    
    @property
    def cpf(self: object) -> str:
        return self.__cpf
    
    @property
    def data_nascimento(self: object) -> str:
        return date_to_str(self.__data_nascimento)
    
    @property
    def data_cadastro(self: object) -> str:
        return date_to_str(self.__data_cadastro)
    
    def __str__(self) -> str:
        return f'Código: {self.__codigo}\nNome: {self.__nome}\nEmail: {self.__email}\nCPF: {self.__cpf}\nData de nascimento: {self.__data_nascimento}\nData de cadastro: {self.__data_cadastro}'