import pytest
from main import parse_line, sort_by_area, sort_by_population, main
import os

@pytest.fixture(autouse=True)
def prepare_text_file(tmp_path):
    target_file = os.path.join(tmp_path, 'test.txt')
    with open(target_file, 'w') as file:
        lines = ['Ukraine 603549(km^2) 40997699\n',
                 'Poland 322575(km^2) 38244000\n',
                 'Bulgaria 110993(km^2) 6520314\n',
                 'Italy 301338(km^2) 60588306\n',
                 'Croatia 56594(km^2) 4291000\n',
                 'Spain 504645(km^2) 47500000\n',
                 'Portugal 92225(km^2) 10347892\n']
        file.writelines(lines)
    return target_file


