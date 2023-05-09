from datetime import datetime
import statistics


class SimpleReport:
    @classmethod
    def generate(cls, products):
        manufacture_date = min([
            products["data_de_fabricacao"]
            for products in products
        ])

        current_date = datetime.today().strftime("%Y-%m-%d")

        expired_dates = min([
            date["data_de_validade"]
            for date in products
            if date["data_de_validade"] > current_date
        ])

        enterprise = [firm["nome_da_empresa"] for firm in products]

        return (
            f"Data de fabricação mais antiga: {manufacture_date}\n"
            f"Data de validade mais próxima: {expired_dates}\n"
            f"Empresa com mais produtos: {statistics.mode(enterprise)}"
        )
