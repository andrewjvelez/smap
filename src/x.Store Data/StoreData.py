import json

class StoreData():
	def __init__(self, filename = ''):
		if filename == '':
			self.filename = 'data.json'
		else:
			self.filename = filename
	
	def get_data_dictionary(self):		
		try:
			with open(self.filename) as f_obj:
				data = json.load(f_obj)
		except IOError:
			data = {}
		
		return data

	def get_data(self, tag):
		data = self.get_data_dictionary()
		if tag in data:
			return data[tag]
		else:
			return ''

	def set_data(self, tag, value):
		data = self.get_data_dictionary()
		data[tag] = value
		with open(self.filename,'w') as f_obj:
			json.dump(data,f_obj)

