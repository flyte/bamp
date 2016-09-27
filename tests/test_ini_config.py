from six import StringIO
from six.moves import configparser

from bamp.config.ini import config_dump


def make_config(content):
    config = configparser.ConfigParser()
    input_file = StringIO(content)
    config.readfp(input_file)
    return config


def test_empty_config():
    config = make_config('')
    assert {} == config_dump(config)


def test_one_section_no_values():
    config = make_config('[test_section]')
    assert {'test_section': {}} == config_dump(config)


def test_one_section_simple_value():
    config = make_config('[market]\n' 'cheese = cheddar')
    assert {'market': {'cheese': 'cheddar'}} == config_dump(config)


def test_one_section_multiline_value():
    config = make_config('[market]\n' 'files=\n' '  leicester\n' '  cheddar')
    assert {'market':
            {'files': ('leicester', 'cheddar')}} == config_dump(config)


def test_two_sections_one_empty():
    config = make_config('[empty]\n'
                         '[market]\n'
                         'files=\n'
                         '  leicester\n'
                         '  cheddar')
    assert {'empty': {},
            'market':
            {'files': ('leicester', 'cheddar')}} == config_dump(config)
