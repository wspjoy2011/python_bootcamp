from csv_files_crud import core as csv_mod

filename = 'films_db.csv'
delimiter = ';'


def start_app():
    print('''
        ────╔═╗╔═╗─╔╗───╔╦╗     ╔═╗───────╔╗
        ╔╦╦╗║═╣║╬║─╠╣╔═╗║║║     ║╬║╔╦╗╔═╗╔╝║
        ║║║║╠═║║╔╝╔╝║║╬║╠╗║     ║╔╝║╔╝║╬║║╬║
        ╚══╝╚═╝╚╝─╚═╝╚═╝╚═╝     ╚╝─╚╝─╚═╝╚═╝
        Simple console app to work with csv files
        ''')
    input('Press Enter to start app...')


def print_menu():
    print('''
    
    Welcome to main menu:
    
    Choose next:
    
    1. List all films
    2. Add film to database
    3. Remove item from database
    4. Print average film rating
    5. List of films with the highest rating
    6. Get films with the lowest rating
    0. Exit
    
    ''')


def main():
    start_app()

    while True:
        print_menu()
        user_choice = input('Enter a menu number: ')
        film_headers, films = csv_mod.read_csv(filename, delimiter)

        max_id = max([int(id[0]) for id in films if id])

        average_rating = [int(rating[3]) for rating in films if rating]
        average_rating = round(sum(average_rating) / len(average_rating), 1)

        max_rating = str(max([int(rating[3]) for rating in films if rating]))
        min_rating = str(min([int(rating[3]) for rating in films if rating]))

        if user_choice == '1':
            csv_mod.print_csv(film_headers, films)
            input('Press Enter to continue...')
        elif user_choice == '2':
            print('\nAdd film into database\n')
            film_title = input('Enter a film title: ')
            film_note = input('Enter a film note: ')
            film_rating = input('Enter rating: ')
            note = [str(max_id+1), film_title, film_note, film_rating]
            csv_mod.add_to_csv(filename, delimiter, note)
        elif user_choice == '3':
            print('\nRemove film from database\n')
            film_id = input('Enter film id to remove it from database: ')
            csv_mod.remove_from_csv(filename, film_id)
        elif user_choice == '4':
            print(f'\nAverage film rating: {average_rating}\n')
            input('Press Enter to continue...')
        elif user_choice == '5':
            csv_mod.print_films_with_rating(film_headers, films, max_rating)
        elif user_choice == '6':
            csv_mod.print_films_with_rating(film_headers, films, min_rating)
        elif user_choice == '0':
            print('Bye!')
            exit()
        else:
            print('Incorrect menu item')
            input('Press Enter to continue...')


if __name__ == '__main__':
    main()
