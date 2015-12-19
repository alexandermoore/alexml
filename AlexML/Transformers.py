import numpy as np
from sklearn import preprocessing

# All operate on Pandas Dataframes


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
		for c in transformcols:
			df[c].apply(self.transformfunc)

class CategoricalTransformer(BaseTransformer):
	def __init__(self, colnames):
		super(CategoricalTransformer, self).__init__(colnames)


class MissingValueTransformer(BaseTransformer):
	pass

