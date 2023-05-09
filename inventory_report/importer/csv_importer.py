from .importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        if path.endswith(".csv"):
            with open(path, newline='') as file:
                data = csv.DictReader(file)
                return [item for item in data]

        raise ValueError("Error!!!")
