def parse_line(line: str) -> tuple:
    items = line.split()
    if len(items) < 3:
        raise ValueError(f'Not enough values to unpack (expected at least 3, got {len(items)})')
    country, area, population = items
    return country, area, population

def sort_by_area(file_name):
    items = {}
    with open(file_name) as file:
        for line in file:
            country, area, _ = parse_line(line)
            items[country] = int(area)
    sorted_items_by_area = sorted(items.items(), key=lambda x: x[1])
    return sorted_items_by_area

def sort_by_population(file_name):
    items = {}
    with open(file_name) as file:
        for line in file:
            country, _, population = parse_line(line)
            items[country] = int(population)
    sorted_items_by_population = sorted(items.items(), key=lambda x: x[1])
    return sorted_items_by_population

def main(file_name):
    print (sort_by_area(file_name))
    print(sort_by_population(file_name))


if __name__ == '__main__':
    main('population.txt')

