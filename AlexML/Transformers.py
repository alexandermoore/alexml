import numpy as np
from sklearn import preprocessing
import pandas as pd

# All operate on Pandas Dataframes


class TransformerHelpers:
	def __init__(self):
		pass

	def apply_transformers(self, df, transformers):
		for transformer in transformers:
			transformer.transform(df)

class BaseTransformer(object):
	def __init__(self, colnames):
		self.transformcolnames = colnames

	def transform(self, df):
		pass

class BasicFuncTransformer(BaseTransformer):
	def __init__(self, colnames, func):
		super(BasicFuncTransformer, self).__init__(colnames)
		self.transformfunc = func

	def transform(self, df):
		transformcols = self.transformcolnames
		df[transformcols] = df[transformcols].applymap(self.transformfunc)

class CategoricalTransformer(BaseTransformer):
	def __init__(self, colnames, deleteoriginal=True):
		super(CategoricalTransformer, self).__init__(colnames)
		self.deleteoriginal = deleteoriginal 

	def transform(self, df):
		transformcols = self.transformcolnames
		for c in transformcols:
			uniquevals = df[c].unique()
			for v in uniquevals:
				newcol = c + "_" + str(v)
				df[newcol] = pd.Series(df[c] == v, dtype=np.double)
			if self.deleteoriginal:
				df.drop(c, axis=1, inplace=True)

class MissingValueTransformer(BaseTransformer):
	def __init__(self, colnames, newdefault=0.0, missingfunc=pd.isnull):
		super(MissingValueTransformer, self).__init__(colnames)
		self.newdefault = newdefault
		self.missingfunc = missingfunc

	def transform(self, df):
		for c in colnames:
			newcol = c + "_missing"
			df[newcol] = pd.Series(df[c] == self.missinvalue, dtype=np.double)
			df[c][missingfunc(df[c])] = self.newdefault
			df.drop('c', axis=1, inplace=True)