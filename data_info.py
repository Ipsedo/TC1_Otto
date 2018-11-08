import matplotlib.pyplot as plt
import pylab


def mk_dict_labels(all_y):
    values = []
    count_labels = {}
    for row in all_y.values:
        values.append(row)
    for l in values:
        if l in count_labels:
            count_labels[l] += 1
        else:
            count_labels[l] = 1
    return count_labels


def plot_hist(labels, data):
    labels = [(k,v) for k, v in labels.items()]
    labels.sort(key=lambda k: k[0])
    x = [i for i in range(len(labels))]
    x_name = [k for k,_ in labels]
    y = [v for _,v in labels]
    if data == "all_data":
        plt.title("Nombre d'exemples par classe sur toutes les données")
        colorBar = "blue"
    if data == "train_data":
        plt.title("Nombre d'exemples par classe sur les données d'entrainement")
        colorBar = "green"
    if data == "valid_data":
        plt.title("Nombre d'exemples par classe sur les données de validation")
        colorBar = "purple"
    plt.bar(x, y, 0.5, color=colorBar)
    pylab.xticks(x, x_name, rotation=40)
    plt.show()
