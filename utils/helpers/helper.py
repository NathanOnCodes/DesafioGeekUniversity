from datetime import date
from datetime import datetime

def date_to_str(date: date) -> str:
    """
        Converte uma data para uma string no formato dd/mm/aaaa
    """
    return date.strftime("%d/%m/%Y")

def str_to_date(date: str) -> date:
    """
        Converte uma string no formato dd/mm/aaaa para uma data
    """
    return datetime.strptime(date, "%d/%m/%Y").date()

def float_str_moeda(valor: float) -> str:
    """
        Converte um float para uma string formatada como moeda
    """
    return f'R$ {valor:.2f}'