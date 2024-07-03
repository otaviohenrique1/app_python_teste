from calculadora import Calculadora


def calcula_medida_amx_10rc(valor_c: float):
    valor_imagem = valor_c
    resultado_imagem1 = Calculadora.calcula_medida(137, 300, valor_imagem)
    print(
        Calculadora.formata_calculo(
            [
                "amx-10rc",
                str(valor_imagem),
                Calculadora.to_fixed(resultado_imagem1, 2),
                str(round(resultado_imagem1)),
            ]
        )
    )
