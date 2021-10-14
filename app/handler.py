import sys


class DataExtractor:

    @staticmethod
    def get_data(*args):
        cmd = args or sys.argv[1:]
        data, is_path = DataExtractor.this_is_the_way(*cmd)
        prep_data = DataExtractor.get_file_data(data) if is_path else data
        return prep_data

    @staticmethod
    def get_file_data(path):
        data = ""
        try:
            with open(path) as f:
                data = f.read()
        except FileNotFoundError:
            error_messages = """
            If you are trying to check a file make sure that the path is correct. 
            The calculation will be done on this data as a line."""
            print(error_messages)
        return data or path

    @staticmethod
    def this_is_the_way(path='', *args):
        is_path = False
        if not isinstance(path, str):
            return "", None
        if path:
            str_path = str(path)
            is_path = str_path.find('/') != -1 and str_path[-4:].find('.') != -1
            is_path = is_path or (len(str_path) < 20 and str_path[-4:].find('.') != -1) or False
        return path, is_path
