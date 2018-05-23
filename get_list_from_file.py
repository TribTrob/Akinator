def get_table_from_file(file_name):

    with open(file_name, "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(";") for element in lines]
    return table


get_table_from_file("emberek.txt")
