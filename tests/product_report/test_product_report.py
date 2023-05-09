from inventory_report.inventory.product import Product

result = (
    "O produto Relâmpago Marquinhos "
    "fabricado em 25/04/2023 "
    "por Copa Pistão com validade "
    "até 25/04/2033 "
    "precisa ser armazenado LOCAL SECO E AREJADO."
)


def test_relatorio_produto():
    product = Product(
        id=1,
        nome_do_produto="Relâmpago Marquinhos",
        nome_da_empresa="Copa Pistão",
        data_de_fabricacao="25/04/2023",
        data_de_validade="25/04/2033",
        numero_de_serie="RM95",
        instrucoes_de_armazenamento="LOCAL SECO E AREJADO",
    )
    assert repr(product) == result
