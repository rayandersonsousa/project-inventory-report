from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path, type):
        file_data = CsvImporter.import_data(path)

        if type == "simples":
            return SimpleReport.generate(file_data)
        if type == "completo":
            return CompleteReport.generate(file_data)

        raise ValueError("Error!!!")
