import csv
from beautifultable import BeautifulTable


def read_csv(filename: str, delimiter: str = ';') -> tuple[list, list]:
    with open(filename) as file:
        database = csv.reader(file, delimiter=delimiter)
        film_header = next(database)
        films = [film for film in database]
        return film_header, films


def print_csv(header, films) -> None:
    table = BeautifulTable()
    table.columns.header = header
    for row in films:
        if row:
            table.rows.append(row)
    print(table)


def add_to_csv(filename: str, delimiter: str, note: list) -> None:
    with open(filename, 'a') as file:
        writer = csv.writer(file, delimiter=delimiter)
        writer.writerow(note)
    print(f'Added note: ', *note)
    input('Press Enter to continue...')


def remove_from_csv(filename: str, film_id: str, delimiter=';') -> None:
    film_header, films = read_csv(filename)
    result = [film_header]
    is_find = False

    for film in films:
        if film:
            if not film[0] == film_id:
                result.append(film)
            else:
                is_find = True

    if is_find:
        with open(filename, 'w'):
            pass

        for note in result:
            with open(filename, 'a') as file:
                writer = csv.writer(file, delimiter=delimiter)
                writer.writerow(note)
        print(f'Removed note with id {film_id}')
    else:
        print(f'Film with id {film_id} not found')
    input('Press Enter to continue...')


def print_films_with_rating(header, films, rating):
    result = [film for film in films if film and film[3] == rating]
    print_csv(header, result)
    input('Press Enter to continue...')
