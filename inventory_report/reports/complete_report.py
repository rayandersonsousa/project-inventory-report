from .simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(products):
        part_report = ""

        inventory = Counter(
            product["nome_da_empresa"]
            for product in products
        )

        for enterprise, quantity in inventory.items():
            part_report += f"- {enterprise}: {quantity}\n"

        return (
            f"{SimpleReport.generate(products)}\n"
            "Produtos estocados por empresa:\n"
            f"{part_report}"
        )
