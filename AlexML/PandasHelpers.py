import math
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class PandasHelpers:
	def __init__(self):
		pass

	def load_csv(self, filename, delim=",", header=None, thousands=","):
		if header is None:
			df = pd.read_csv(filename, sep=delim, header=0)
		else:
			df = pd.read_csv(filename, sep=delim, names=header, header=None)
		return df

	def delete_column(self, df, colname):
		df.drop(colname, axis=1, inplace=True)

	def get_headers(self, df):
		return df.columns.values

	def get_types(self, df):
		return df.dtypes

	def convert_column_types(self, df, colnames, newtype):
		df[colnames] = df[colnames].as_type(newtype)

	def get_correlations(self, df, colnames):
		return df[colnames].corr()

	def get_sorted_correlations(self, df, colnames, comparetocol):
		correls = []
		for i in xrange(len(colnames)):
			correls.append( (colnames[i], df[colnames[i]].corr(df[comparetocol])) )
		correls.sort(key=lambda x: x[1], reverse=True)
		return correls

	def make_histograms(self, df, colnames):
		lel = np.ones(5)
		numrows = math.ceil(math.sqrt(len(colnames)))
		fig = None
		fig = plt.figure()
		for i in xrange(len(colnames)):
			plt.subplot(numrows, numrows, i+1)
			plt.hist(df[colnames[i]])
			plt.title(colnames[i])
		return fig

	def make_all_scatterplots(self, df, colnames):
		return self.make_scatterplots(df, colnames, colnames)

	def __scatter(self, df, xcol, ycol):
			plt.scatter(df[xcol], df[ycol])
			plt.title(ycol + " vs. " + xcol)
			plt.xlabel(xcol)
			plt.ylabel(ycol)

	def make_scatterplots(self, df, colnames, comparetocols):
		numrows = len(colnames)
		numcols = len(comparetocols)
		fig = None
		fig = plt.figure()
		for i in xrange(len(colnames)):
			for j in xrange(len(comparetocols)):
				plt.subplot(numrows, numcols, numcols * i + (j + 1))
				self.__scatter(df, colnames[i], comparetocols[j])
		return fig

	def show_plots(self):
		plt.show()

	# Randomly shuffles rows
	def shuffle(self, df):
		return df.iloc[np.random.permutation(xrange(df1.shape[0]))]
		# nrows = df.shape[0]
		# for i in xrange(nrows):
		# 	j = np.random.randint(i, nrows)
		# 	row_j = df.iloc[j].copy()
		# 	df.iloc[j] = df.iloc[i]
		# 	df.iloc[i] = row_j

		# return df


	def save(self, filename, sep='\t', include_header=True):
		df.to_csv(filename, sep=sep, header=include_header)