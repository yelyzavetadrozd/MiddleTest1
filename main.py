def parse_line(line: str) -> tuple:
    items = line.split()
    if len(items) < 3:
        raise ValueError(f'Not enough values to unpack (expected at least 4, got {len(items)})')
    country, area, population = items
    return country, area, population

def main(file_name):
    pass


if __name__ == '__main__':
    main('population.txt')

