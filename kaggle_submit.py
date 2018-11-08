import pandas
import numpy as np

def make_csv_soumission(model, test_x, fileName, nb_class):
    y = model.predict_proba(test_x)
    dt = pandas.DataFrame(data=y, \
                          index=np.arange(1, y.shape[0]+1), \
                          columns=["Class_1","Class_2","Class_3","Class_4", \
                                   "Class_5","Class_6","Class_7","Class_8","Class_9"])
    dt.to_csv(fileName, sep=",", index_label="id")


def make_csv_soumission2(y, fileName, nb_class):
    dt = pandas.DataFrame(data=y, \
                          index=np.arange(1, y.shape[0]+1), \
                          columns=["Class_1","Class_2","Class_3","Class_4", \
                                   "Class_5","Class_6","Class_7","Class_8","Class_9"])
    dt.to_csv(fileName, sep=",", index_label="id")
