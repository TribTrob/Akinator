from get_list_from_file import get_list_from_file
import random

def list_handling(people, attribute):
    for person in people:
        if attribute not in person:
            print(person)
            people.remove(person)









def main():
    list_handling(get_list_from_file("emberek.txt"), "woman")

if __name__ == '__main__':
    main()