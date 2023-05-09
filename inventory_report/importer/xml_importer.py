from .importer import Importer
import xmltodict


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if path.endswith(".xml"):
            with open(path) as file:
                xml_dict = xmltodict.parse(file.read())

            return xml_dict.get("dataset", {}).get("record", [])

        raise ValueError("Error!!")
