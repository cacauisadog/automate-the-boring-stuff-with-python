def print_table(table_data):
    # initiates col_width to contain the same number of 0 values as the number
    # of inner lists in the table
    table_len = len(table_data)
    col_width = [0] * table_len

    # each position in col_width holds the value of the len of the longest
    # string in each inner list
    for i in range(table_len):
        for list_item in table_data[i]:
            if len(list_item) > col_width[i]:
                col_width[i] = len(list_item)

    # since we can assume that all inner lists will contain the same number of
    # strings, we use the first inner list as parameter to print everything
    for i in range(len(table_data[0])):
        for j in range(len(col_width)):
            print(table_data[j][i].rjust(col_width[j]), end=' ')
        print()

table_data1 = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

table_data2 = [['batata', 'feijão', 'arroz', 'câncer'],
              ['rsrs', 'rsrsrs', 'creme de maracujá', 'wabba']]

print_table(table_data1)
print()
print_table(table_data2)
