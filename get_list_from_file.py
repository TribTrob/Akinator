def get_list_from_file(file_name):

    with open(file_name, "r") as file:
        lines = file.readlines()
    list_of_ppl = [element.replace("\n", "").split(",") for element in lines]
    return list_of_ppl


def get_names(table):
    names = []
    for i in table:
        print(i)
    print(names)


# print(get_list_from_file("emberek.txt"))

get_names(get_list_from_file("emberek.txt"))
