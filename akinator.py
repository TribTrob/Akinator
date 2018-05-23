from get_list_from_file import get_table_from_file
import random

def list_handling(people, attribute):
    print(people)
    for person in people:
        if attribute not in person:
            print(person)
            people.remove(person)
    print(people)
            










def main():
    list_handling(get_table_from_file("emberek.txt"), "Brad Pitt")

if __name__ == '__main__':
    main()