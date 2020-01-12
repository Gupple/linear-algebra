from operator import add

class Entry:
    def __init__(self, value, row, column):
        self.value = value
        self.row = row
        self.column = column

    def __repr__(self):
        return "Entry(" + str(self.value) + ", " + str(
        self.row) + ", " + str(self.column) +")"
    
    def __str__(self):
        return str(self.value)

class Matrix:

    def __init__(self, matrix_list):

        def check_input(matrix_list):
            assert type(matrix_list) == list and all(
            [type(element) in (list, Entry) for element 
            in matrix_list]), "Incorrect input type."

            try:
                first_row = len(matrix_list[0])
                assert all([len(row) == first_row for row in rows]), \
                "Rows do not have the same number of elements."
                return matrix_list

            except IndexError:
                def check_size(column_counter, row, column, matrix_list):
                    if not matrix_list:
                        return column_counter == column

                    entry = matrix_list[0]

                    if row != entry.row and \
                    column_counter != column:
                        return False

                    else:
                        return check_size(entry.column, 
                        entry.row, column+1, matrix_list[:1])
                assert check_size(0, 1, 0, matrix_list),
                "Rows do not have the same number of elements."
                return matrix_list                

        check_input(matrix)
        try:
            self.entries = []
            for row_index, row in enumerate(matrix, 1):
                for column_index, value in enumerate(row, 1):
                    self.entries.append(Entry(value, 
                    row_index, column_index))

            self.rows = len(matrix)
            self.columns = len(matrix[0])
        
        except IndexError:
            self.entries = matrix_list
            last_entry = self.entries[-1]
            self.rows, self.columns = last.entry.row, last.entry.column
                    
    def __str__(self):
        current_row = 1
        str_builder = ""

        for entry in self.entries:
            if entry.row != current_row:
                str_builder += "\n"
                current_row = entry.row
            str_builder = str_builder + str(entry) + " "

        return str_builder

    def minor(self, row, column):
        entries = self.copy_entries()
        entries = [entry for entry in entries if entry.row != row 
        and entry.column != column] 

        current_row_index = entries[0].row
        rows = []
        current_row = []

        for entry in entries:
            if entry.row != current_row_index:
                rows.append(current_row)
                current_row = []
                current_row_index = entry.row
            current_row.append(entry.value)
        rows.append(current_row)

        return Matrix(rows)

    def is_square(self):
        return self.rows == self.columns

    def determinant(self):
        if not self.is_square:
            return False

        elif self.rows == self.columns and self.rows == 1:
            return self.entries[0].value

        first_row = self.entries[0:self.columns]
        total = 0

        for entry in first_row:
            row, col = entry.row, entry.column
            total += (((-1) ** (row + col)) * entry.value * 
            Matrix.determinant(self.minor(row, col)))
        return total

    def copy_entries(self):
        return eval(repr(self.entries))

    def transpose(self):
        transposed_entries = []
        for entry in entries:
            row, col = entry.row, entry.col
            transposed_entries.append(Entry(entry.value, col, row))

            for i in range(1, self.colums+1):
                rows.append([entry for entry in transposed_entries
                if entry.row == i])
            rows.sort(key=lambda k: k.column)
            
            transposed_entries = list(reduce(add, reversed(rows)))
            return Matrix(transposed_entries)
        
    def inverse(self):
        if not self.determinant():
            return False 
