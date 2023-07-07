def is_integer(
    n: str
) -> bool:

    """
        valida se o valor
        é um número;
    """

    # se for negativo, desconsidera o sinal;
    if n.startswith("-"):
        n = n[1:]

    return n.isdigit()