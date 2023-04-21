import numpy as np
from sklearn.metrics import accuracy_score

def temp_softmax(X,T=1):
    X=np.array(X)
    X=X/T
    e = np.exp(X)
    return e / np.sum(e, axis=1, keepdims=True)

def mse_ensemble(model1,model2,model3,x_train , y_train , x_val ,y_val):
    model1 = modellist[0]
    model2 = modellist[1]
    model3 = modellist[2]
    X1_val = model1.predict(x_val)
    X1 = model1.predict(x_train)
    X2_val = model2.predict(x_val)
    X2 = model2.predict(x_train)
    X3_val = model3.predict(x_val)
    X3 = model3.predict(x_train)
    List = [[X1_val, X1], [X2_val, X2], [X3_val, X3]]
    y_train = y_train.astype(int)
    y_val = y_val.astype(int)
    finals = []
    for lists in List:
        mean=np.zeros((len(np.unique(y_train))),dtype=float),
        std=np.zeros((len(np.unique(y_train))),dtype=float)
        probs=[[] for i in range(len(np.unique(y_train)))]
        for i in range(len(lists[1])):
          probs[y_train[i]].append(lists[1][i][y_train[i]])
        mean=np.zeros((len(np.unique(y_train))),dtype=float)
        std=np.zeros((len(np.unique(y_train))),dtype=float)
        for i in range(len(probs)):
          mean[i]=np.mean(probs[i])
          std[i]= np.std(probs[i])
        mean_T = temp_softmax([mean], T=2)
        std_T = temp_softmax([std], T=2)
        b = mean_T-std_T
        a = [mean]/mean_T
        X_val_final = a*lists[0] + b
        finals.append(X_val_final)
    finals = np.array(finals)
    summed = np.sum(finals, axis=0)
    ensembled_pred = np.argmax(summed, axis=1)
    accuracy_ens = accuracy_score(ensembled_pred, y_val)
    print(f"The accuracy after ensembling on the{fold_no+1}th fold: ", accuracy_ens)
    return ensembled_pred
    
