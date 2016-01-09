import numpy as np
from sklearn.metrics import accuracy_score, roc_auc_score

class PredictionStatistics:
	def __init__(self):
		pass

	def get_thresholded_predictions(self, predicted_probs, threshold, yesval=1.0, noval=0.0):
		threshfunc = np.vectorize(lambda x: yesval if x >= threshold else noval)
		return threshfunc(predicted_probs)

	def get_accuracy(self, true, predicted):
		return accuracy_score(true, predicted)

	def get_auc(self, true, predicted):
		return roc_auc_score(true, predicted)
