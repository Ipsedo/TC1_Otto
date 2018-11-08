import pandas


def open_otto_csv(file):
    return pandas.read_csv(file, sep=',')


def get_x_y(pandas_data_frame):
    y = pandas_data_frame["target"]
    x = pandas_data_frame.drop(columns=["id", "target"])
    return x, y
