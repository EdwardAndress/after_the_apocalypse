__author__ = 'jimnarey'


def parse_file(filename):

    my_table = []

    with open(filename, 'r') as file:

        for line in file:
            my_line = line.replace('\n', '')
            my_list = my_line.split(',')

            my_name = my_list[0].strip(" ")
            my_formula = my_list[2].strip(" ")

            if len(my_list) != 4:
                print(my_list[0], 'has', len(my_list), 'values')
            else:

                if len(my_list[1].split(';')) < 2:
                    my_foundin = my_list[1].strip(" ")
                else:
                    my_foundin = my_list[1].split(';')

                    i = 0
                    while i < len(my_foundin):
                        my_foundin[i] = my_foundin[i].strip(" ")
                        i += 1


                if len(my_list[3].split(';')) < 2:
                    my_foundwhere = my_list[3].strip(" ")
                else:
                    my_foundwhere = my_list[3].split(';')

                    i = 0
                    while i < len(my_foundwhere):
                        my_foundwhere[i] = my_foundwhere[i].strip(" ")
                        i += 1

                my_dict = {
                    'name': my_name,
                    'foundin': my_foundin,
                    'formula': my_formula,
                    'foundwhere': my_foundwhere
                }

                my_table.append(my_dict)

                print(my_list[0], 'success')

    return my_table


def csv_to_lists(filename):

    my_table = []

    with open(filename, 'r') as file:

        for line in file:  # Loop through all rows

            line_string = line.replace('\n', '')  # Remove carriage return characters from each line
            row_list = line_string.split(',')  # Split each line into a list with comma as the separator

            for i in range(len(row_list)):  # Loop through each cell in one row
                row_list[i] = row_list[i].split(';')  # Convert each cell to a list (even if one item long)

                for k in range(len(row_list[i])):  # Loop through each list/cell
                    row_list[i][k] = row_list[i][k].strip(' ')  # Remove any spaces at ends of strings

                    while row_list[i][k] != row_list[i][k].replace('  ', ' '):  # Remove multiple spaces
                        row_list[i][k] = row_list[i][k].replace('  ', ' ')

            my_table.append(row_list)  # Add each row to the table list
            print(row_list[0], 'success')

    return my_table


def sort_unique(table, column):

    my_list = []

    for i in range(len(table)):  # Loop through rows in table

        for k in range(len(table[i][column])):  # Loop through list at row i, in provided column

            if table[i][column][k] not in my_list:

                if table[i][column][k] != '':
                    my_list.append(table[i][column][k])

    return my_list


def list_to_file(a_list, filename):

    with open(filename, 'r') as file:
        file.writelines(a_list)
