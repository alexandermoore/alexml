from sklearn.ensemble import RandomForestClassifier as sklearn_RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn import cross_validation
from sklearn.externals import joblib

class BaseMLClassifier(object):
		def __init__(self):
			self.model = None

		def train(self, db, specific_indices=None):
			pass

		def test(self, db, specific_indices=None):
			pass

		def save(self, filename):
			joblib.dump(self.model, filename)

		def load(self, filename):
			self.model = joblib.load(filename)


class RandomForestClassifier(BaseMLClassifier):
	def __init__(self, n_trees=100):
		super(RandomForestClassifier, self).__init__()
		self.model = sklearn_RandomForestClassifier(n_estimators=n_trees)

	def train(self, db, specific_indices=None):
		if not specific_indices:
			data = db.data
			target = db.target
		else:
			data = db.data[specific_indices]
			target = db.target[specific_indices]
		self.model.fit(data, target)

	def test(self, db, specific_indices=None):
		if not specific_indices:
			data = db.data
		else:
			data = db.data[specific_indices]
		prediction_probs = self.model.predict_proba(data)
		return prediction_probs

class NeuralNetworkClassifier(BaseMLClassifier):
	def __init__(self, hidden_layer_sizes=(5,), activation='relu', l2reg=1e-3):
		super(NeuralNetworkClassifier, self).__init__()
		self.model = MLPClassifier(activation=activation, algorithm='l-bfgs', alpha=l2reg, hidden_layer_sizes=hidden_layer_sizes, random_state=1)

	def train(self, db, specific_indices=None):
		if not specific_indices:
			data = db.data
			target = db.target
		else:
			data = db.data[specific_indices]
			target = db.target[specific_indices]
		self.model.fit(data, target)

	def test(self, db, specific_indices=None):
		if not specific_indices:
			data = db.data
		else:
			data = db.data[specific_indices]
		prediction_probs = self.model.predict_proba(data)
		return prediction_probs

	def get_coefficients(self):
		return self.model.coefs_

	def run_backwards(output):
		coefs = self.get_coefficients()

class CrossValidationHandler():
	def __init__(self):
		pass

	def generate_folds(self, db, n_folds):
		n_data = db.data.shape[0]
		folds = cross_validation.KFold(n_data, n_folds)
		return folds

	# Evaluates each function in eval_functions on each fold.
	# Useful for computing multiple metrics.
	def score_cross_validation(self, db, model, folds, eval_functions):
		scores = []
		for trainfold, testfold in folds:
			model.train(db, specific_indices=trainfold)
			target = db.target[testfold]
			predicted = model.test(db, specific_indices=testfold)
			scores.append( [evalfunc(target, predicted) for evalfunc in eval_functions] )
		return scores



