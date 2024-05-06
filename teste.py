from models.cliente import Cliente
from models.conta import Conta

Arthur : Cliente = Cliente('Arthur', 'be@.com', '123.456.789-00', '01/01/2000')
Maria : Cliente = Cliente('Maria', 'a@.com', '123.456.789-00', '01/01/2001')


contaf: Conta = Conta(Arthur)
contag: Conta = Conta(Maria)


print(contaf)
print(contag)