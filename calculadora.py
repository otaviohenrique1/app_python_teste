from typing import List


class Calculadora:
    @staticmethod
    def calcula_medida(a: float, b: float, c: float) -> float:
        return (b * c) / a

    @staticmethod
    def to_fixed(numero: float, casas_decimais: int) -> str:
        return f"{numero:.{casas_decimais}f}"

    @staticmethod
    def calcula_medida_formatada(resultado: float) -> str:
        return Calculadora.to_fixed(resultado, 2)

    @staticmethod
    def formata_calculo(valor: List[str]) -> str:
        return " -> ".join(valor)

    @staticmethod
    def formatador_final(valor: float, resultado: float, nome_medida: str):
        return Calculadora.formata_calculo(
            [nome_medida, str(resultado), str(round(valor))]
        )





