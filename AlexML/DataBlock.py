"""
CHANGE THIS WHOLE THING TO CHANGE PANDAS DATAFRAMES TO NUMPY ARRAYS.
APPLY ALL THE TRANSFORMATIONS WHILE IN THE PANDAS DATAFRAME.
THEN, CAN CONVERT TO A DATABOX FOR USE IN ALL ML ALGORITHMS. DATABOX
WILL HAVE EVERYTHING IN NUMPY ARRAYS AND INCLUDE HEADER INFORMATION.

PROVIDE A PANDAS HELPER LIBRARY AND PLOT LIBRARY TO OPERATE 
ON THE DATAFRAMES. INCLUDE A CONVERT TO DATABOX FUNCTION IN THE
PANDAS LIBRARY.

DATABOXES WILL BE USED AS INPUT TO ALL THE ML STUFF, SINCE THE ML
STUFF DOESN'T LIKE STRINGS AND SUCH.
"""






class DataBox:
	def __init__(self, data, header=[]):
		if header == []:
			header = [str(i) for i in xrange(data.shape[1])]
		self.data = data
		self.header = header
	
	def __update_header_dict(self):
		self.headerdict = dict([(self.header[i], i) for i in xrange(len(self.header))])

	def set_header(self, header):
		self.header = header
		self.__update_header_dict()

	def get_column_nums(self, header_fields):
		hdct =  self.headerdict
		return [hdct[header_field] for header_field in header_fields]

class NPDataBox(DataBox):
	def __init__(self, data, header=[]):
		super(NPDataBox, self).__init__(data, header=header)

class MultiTypeDataBox(DataBox):
	def __init__(self, data, header=[]):
		super(MultiTypeDataBox, self).__init__(data, header=header)

	# Casts it to a numpy array
	def convert_to_npdatabox(self):
		return NPDataBox(np.array(self.data), self.header)