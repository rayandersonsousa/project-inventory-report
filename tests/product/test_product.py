from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        id=1,
        nome_do_produto="Relâmpago Marquinhos",
        nome_da_empresa="Copa Pistão",
        data_de_fabricacao="25/04/2023",
        data_de_validade="25/04/2033",
        numero_de_serie="RM95",
        instrucoes_de_armazenamento="LOCAL SECO E AREJADO",
    )

    assert product.id == 1
    assert product.nome_do_produto == "Relâmpago Marquinhos"
    assert product.nome_da_empresa == "Copa Pistão"
    assert product.data_de_fabricacao == "25/04/2023"
    assert product.data_de_validade == "25/04/2033"
    assert product.numero_de_serie == "RM95"
    assert product.instrucoes_de_armazenamento == "LOCAL SECO E AREJADO"
