from sklearn.metrics import recall_score

pred = [1, 1, 1, 0, 0, 2]
real = [0, 1, 0, 1, 0, 1]
print(recall_score(real, pred, average="macro"))


