import os
from tinydb import TinyDB, Query
from datetime import datetime
from serializer import serializer


class User():
	# Class variable that is shared between all instances of the class
	db_connector = TinyDB(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.json'), storage=serializer).table('users')

	# Constructor
	def __init__(self, user_name : str, user_email : str):
		self.name = user_name
		self.email = user_email
		self.is_active = False

	# String representation of the class
	def __str__(self):
		return f'User {self.name} ({self.email})'

	# String representation of the class
	def __repr__(self):
		return self.__str__()

	def store_data(self):
		print("Storing data...")
		# Check if the device already exists in the database
		user_query = Query()
		result = self.db_connector.search(user_query.name == self.name)
		if result:
			# Update the existing record with the current instance's data
			result = self.db_connector.update(self.__dict__, doc_ids=[result[0].doc_id])
			print("Data updated.")
		else:
			# If the device doesn't exist, insert a new record
			self.db_connector.insert(self.__dict__)
			print("Data inserted.")

	def delete_data(self, doc_id):
		print("Deleting data...")
		# Check if the device already exists in the database
		user_query = Query()
		result = self.db_connector.search(user_query.name == self.name)
		if result:
			# Delete the existing record
			result = self.db_connector.remove(doc_ids=[result[0].doc_id])
			print("Data deleted.")
		else:
			print("Data not found.")

	# Class method that can be called without an instance of the class to construct an instance of the class
	@classmethod
	def load_data_by_user_name(cls, user_name):
		# Load data from the database and create an instance of the Device class
		user_query = Query()
		result = cls.db_connector.search(user_query.name == user_name)

		if result:
			data = result[0]
			return [cls(data['name'], data['email']), data.doc_id]
		else:
			return None
	
	def delete_data_by_doc_id(cls, doc_id):
		# Load data from the database and create an instance of the Device class
		result = cls.db_connector.remove(doc_ids=[doc_id])

		if result:
			return True
		else:
			return False
