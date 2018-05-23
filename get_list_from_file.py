def get_list_from_file(file_name):

    with open(file_name, "r") as file:
        lines = file.readlines()
    list_of_ppl = [element.replace("\n", "").split(", ") for element in lines]
    return list_of_ppl


def get_attribute_lists(table):
    names = []
    for i in table:
        names.append(i[0])

    genders = []
    for i in table:
        if i not in genders:
            genders.append(i[1])

    races = []
    for i in table:
        if i not in races:
            races.append(i[2])

    hair_colors = []
    for i in table:
        if i not in hair_colors:
            hair_colors.append(i[3])

    eye_colors = []
    for i in table:
        if i not in eye_colors:
            eye_colors.append(i[4])

    spec_features = []
    for i in table:
        if i not in spec_features:
            spec_features.append(i[5])

    movies = []
    for i in table:
        if i not in movies:
            movies.append(i[6])

    attribute_list = []
    attribute_list.append(names)
    attribute_list.append(genders)
    attribute_list.append(races)
    attribute_list.append(hair_colors)
    attribute_list.append(eye_colors)
    attribute_list.append(spec_features)
    attribute_list.append(movies)
# print(get_list_from_file("emberek.txt"))


get_attribute_lists(get_list_from_file("emberek.txt"))
