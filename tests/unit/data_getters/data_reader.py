import json
from pathlib import Path


class DataReader:
    """ class for reading test data for unit tests """
    @staticmethod
    def read(file_name: str):
        test_data_dir = DataReader.get_test_data_directory()
        file_path = test_data_dir / file_name
        with open(file_path) as f:
            return json.load(f)

    @staticmethod
    def get_test_data_directory() -> Path:
        """ return the path of the test data direcotory """
        unit_test_root = Path(__file__).parent
        test_data_dir = unit_test_root / Path("data")
        return test_data_dir
