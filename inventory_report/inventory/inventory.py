from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.json_importer import JsonImporter


class Inventory:
    @staticmethod
    def import_data(path, type):
        file_data = Inventory.file_type(path)

        if type == "simples":
            return SimpleReport.generate(file_data)
        if type == "completo":
            return CompleteReport.generate(file_data)

        raise ValueError("Error!!!")

    @staticmethod
    def file_type(path):
        if path.endswith(".csv"):
            return CsvImporter.import_data(path)
        if path.endswith(".json"):
            return JsonImporter.import_data(path)
