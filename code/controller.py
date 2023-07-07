# imports
from code.utils import is_integer

from typing import List, Tuple
from statistics import mean


class Gerenciador:

    def __set_data(self, data: List[Tuple[int, int]]) -> None:

        """
            seta a lista válida p/
            posterior cálculos de
            de dias bons e dias consecutivos;
        """

        self.__data = data

    def le_dados(self) -> List[Tuple[int, int]]:

        """
            recebe a quantidade de dias e a
            quantidade de vendas p/ cada um
            desses dias, faz a validação e 
            retorna uma lista válida sem
            valores corrompidos;

            returns:

                lista no formato (dia, vendas)
                >>> [(1, 5), (2, 18), (5, 13)]
        """ 

        # recebe entrada de dias e faz validação;
        n = input("Número de dias: ")
        while (not n.isdigit() or int(n) <= 1):
            n = input("Número de dias: ")

        # constrói uma lista com os dias numerados;
        days = range(1, int(n) + 1)
        
        sales = list()
        
        # recebe a entrada de vendas por dia;
        for day in days:
            
            sale = input(f"Quantidade vendida no dia {day}: ")

            # valida a entrada;
            while not is_integer(sale):
                sale = input(f"Quantidade vendida no dia {day}: ")

            sales.append(int(sale))

        # junta as duas listas de dias e vendas;
        raw_data = zip(days, sales)

        # filtra os valores de venda p/ obter apenas os não corrompidos;
        data = list(filter(lambda y:  0 <= y[1] <= 1000, raw_data))
        self.__set_data(data)

        return data


    def dias_bons(self) -> List[int]:

        """
            valida a quantidade de dias cujas
            vendas foram superiores do que a média
            da soma das vendas dos dias anteriores;

            returns:

                lista com dias bons;
                >>> [2, 5]
        """

        good_days = list()

        for n, data in enumerate(self.__data, start = 0):

            # desconsidera o 1o dia;
            if (n == 0):
                continue

            # calcula a média das vendas dos dias anteriores;
            total_sales = mean([data[1] for data in self.__data[:n]])

            # se a venda do dia em questão for maior que a média, adiciona à lista de dias bons;
            day, sale = data

            if (sale > total_sales):
                good_days.append(day)                

        return good_days

    def pares_consecutivos(self) -> int:

        """
            retorna a quantidade de
            vezes em que d2 > d1;
        """

        # contrói uma lista com as valores de vendas;
        sales = [data[1] for data in self.__data]
        y = 0

        for index, sale in enumerate(sales):

            # ignorar o valor da primeira venda, afinal não há vendas anteriores;
            if (index == 0):
                continue 
        
            # se a venda em questão for maior que a venda do dia anterior, contabiliza o par;
            if sale > sales[index - 1]:
                y += 1

        return y

    def exibe_resultados(self) -> None:

        """
            printa a lista pós validação,
            os dias bons e os pares consecutivos;
        """

        good_days = self.dias_bons()
        consecutives = self.pares_consecutivos()

        print("Lista válida: ", self.__data)
        print("Dias bons: ", good_days)
        print("Pares consecutivos: ", consecutives)


            