from sklearn.metrics import f1_score, log_loss
import numpy as np

def evaluate_model(true_y, y_pred, y_pred_proba):
    score = f1_score(true_y, y_pred, average = 'weighted')
    logLoss = log_loss(true_y, y_pred_proba, eps = 1e-15)
    tmp_y=np.asarray(true_y)
    print("f1_score precision : (version sklearn)", score)
    print("La log-loss est de : ", logLoss)
    print("evaluation (version Sam) : ")
    print(tmp_y[tmp_y==y_pred].shape[0], "/", y_pred.shape[0])
    print("Precision : %f" % (tmp_y[tmp_y==y_pred].shape[0] / y_pred.shape[0]))

def evaluate_model_Acc(true_y, y_pred):
    score = f1_score(true_y, y_pred, average = 'weighted')
    tmp_y=np.asarray(true_y)
    print("f1_score precision : (version sklearn)", score)
    print("evaluation (version Sam) : ")
    print(tmp_y[tmp_y==y_pred].shape[0], "/", y_pred.shape[0])
    print("Precision : %f" % (tmp_y[tmp_y==y_pred].shape[0] / y_pred.shape[0]))

def evaluate_model_prob(true_y, y_pred_proba):
    logLoss = log_loss(true_y, y_pred_proba, eps = 1e-15)
    print("La log-loss est de : ", logLoss)
