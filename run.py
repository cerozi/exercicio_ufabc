# imports
from code.controller import Gerenciador


def main() -> None:

    """
        executa o programa;
    """

    gerenciador = Gerenciador()

    gerenciador.le_dados()
    gerenciador.exibe_resultados()


if __name__ == "__main__":

    main()

