import pandas


def find_min_max_mean(column):
    minimum = maximum = column[0]
    sum_column = 0
    for j in column:
        if j < minimum:
            minimum = j
        elif j > maximum:
            maximum = j
        sum_data = sum_column + j
    mean = sum_column / len(column)
    out = [minimum, maximum, mean]
    return out

data = pandas.read_csv('student - Sheet1.csv')

data_int = data.select_dtypes(include=['int64', 'float64'])

for i in data_int:
    min_max_mean = find_min_max_mean(data_int[i])
    print(f"{i}\n"
          f"\tMinimum = {min_max_mean[0]}\n"
          f"\tMaximum = {min_max_mean[1]}\n"
          f"\tMean = {round(min_max_mean[2], 3)}\n")

