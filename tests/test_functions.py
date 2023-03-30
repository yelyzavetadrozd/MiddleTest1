import pytest
from main import parse_line, sort_by_area, sort_by_population, main
import os

@pytest.fixture(autouse=True)
def prepare_text_file(tmp_path):
    target_file = os.path.join(tmp_path, 'test.txt')
    with open(target_file, 'w') as file:
        lines = ['Ukraine 603549 40997699\n',
                 'Poland 322575 38244000\n',
                 'Bulgaria 110993 6520314\n',
                 'Italy 301338 60588306\n',
                 'Croatia 56594 4291000\n',
                 'Spain 504645 47500000\n',
                 'Portugal 92225 10347892\n']
        file.writelines(lines)
    return target_file

def test_sort_by_area(prepare_text_file):
    expected = {'Croatia': 56594,
                'Portugal': 92225,
                'Bulgaria': 110993,
                'Italy': 301338,
                'Poland': 322575,
                'Spain': 504645,
                'Ukraine': 603549
                }
    result = total_expenses_by_categories(prepare_text_file)

    assert set(expected.keys()) == set(result.keys())
    assert all([expected[key] == item for key, item in result.items()])