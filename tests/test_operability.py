import bracket_check as app
from random import choice
from os import system as sys_cmd, getcwd as current_dir


class CommonTools:
    bracket_numbers = [40, 41, 91, 93, 123, 125]  # utf-8
    random_range = range(10000)
    types = (int, float, complex, bool, tuple, list, set, dict)
    start_temp = "python3 -m bracket_check {}"
    valid_for_random_path = (0, 512, 32512)

    @staticmethod
    def generate_brackets(length):
        return "".join([chr(choice(CommonTools.bracket_numbers)) for _ in range(length)])

    @staticmethod
    def generate_random_str(length):
        return "".join([chr(choice(CommonTools.random_range)) for _ in range(length)])


class TestAppAsLib:

    def test_empty_string(self):
        data = ""
        assert app(data)

    def test_correct_value(self):
        data = "{[()]}"
        assert app(data)

    def test_invalid_value(self):
        data = "{[(}])"
        assert not app(data)

    def test_empty_val(self):
        assert app()

    def test_any_type(self):
        for type_of_data in CommonTools.types:
            assert app(type_of_data)

    def test_any_type_called(self):
        for type_of_data in CommonTools.types:
            assert app(type_of_data())

    def test_for_path_true(self):
        assert app(f'{current_dir()}/training_set.py')

    # def test_for_path_false(self):
    #     assert app(f'{current_dir()}/training_set_broke.txt') is False

    def test_all_vars(self):
        cases = {CommonTools.generate_brackets(5) for _ in range(100000)}
        for case in cases:
            assert not app(case)


class TestAppAsUtil:

    def test_empty(self):
        assert sys_cmd(CommonTools.start_temp.format('')) != 256

    def test_compile(self):
        assert sys_cmd(CommonTools.start_temp.format('')) == 0

    def test_set_path(self):
        assert sys_cmd(CommonTools.start_temp.format(f'{current_dir()}/training_set.py')) == 0

    def test_set_string(self):
        assert sys_cmd(CommonTools.start_temp.format(f'"{CommonTools.generate_brackets(100)}"')) == 0

    def test_set_wrong_path(self):
        try:
            assert sys_cmd(
                CommonTools.start_temp.format(
                    f'{CommonTools.generate_random_str(10)}/training_set.py')) in CommonTools.valid_for_random_path
        except ValueError as e:  # class errors are acceptable at this point: ValueError: embedded null byte
            print(f"Error: {e}")

    def test_set_random_string(self):
        for _ in range(100):
            try:
                assert sys_cmd(
                    CommonTools.start_temp.format(
                        f'{CommonTools.generate_random_str(100)}"')) in CommonTools.valid_for_random_path
            except ValueError as e:  # class errors are acceptable at this point: ValueError: embedded null byte
                print(f"Error: {e}")
