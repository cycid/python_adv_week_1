"""
 A 10x10 matrix of integers is given. A number is entered. Find out which rows and
columns of the matrix contain the given number. (either random or reading from a file (input.txt))
"""




from import_table import main as values
from import_table import income_values as value_input
def main():
    matrix=values()
    value=value_input("digit")
    if value<10 or value>50:
        return print("please choose correct range")
    else:
        rows=[]
        columns=[]
        for row in range(len(matrix)):
            r=matrix[row]
            for column in range(len(r)):
                if matrix[row][column]==value:
                    rows.append(row)
                    columns.append(column)
                else:
                    pass

        return print("row indexes",rows,"\n","column indexes",columns)

main()
