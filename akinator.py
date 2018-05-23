from get_list_from_file import get_list_from_file
import random


def list_handling(people, attribute):
    new_people = []
    for person in people:
        if attribute in person:
            new_people.append(person)
    people = new_people
    return people


def main():
    list_handling(get_list_from_file("emberek.txt"), "man")


if __name__ == '__main__':
    main()
