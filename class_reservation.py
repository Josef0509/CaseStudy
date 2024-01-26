import os
from users import User
from tinydb import TinyDB, Query
from datetime import datetime
from serializer import serializer

class Reservation():
	# Class variable that is shared between all instances of the class
	db_connector = TinyDB(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.json'), storage=serializer).table('reservations')

	# Constructor
	def __init__(self, device_name : str, reserver_dev : str, times : datetime, timee : datetime):
		self.device_name = device_name
		self.reserver = reserver_dev
		self.start_time = times
		self.end_time = timee
		self.is_active = False

	# String representation of the class
	def __str__(self):
		return f'Reseration {self.device_name} ({self.reserver})'

	# String representation of the class
	def __repr__(self):
		return self.__str__()

	def store_data(self):
		print("Storing data...")
		# Check if the reservation already exists in the database
		reservation_query = Query()
		result = self.db_connector.search(reservation_query.device_name == self.device_name)

		if result:
			# Check if the reservation already exists in the database
			sum_of_blocks  = len(result)
			# Raise an error if the reservation already exists
			error = False
			#Chek if the time is already taken
			for i in range(sum_of_blocks):
				if (result[i]['start_time'] <= self.start_time <= result[i]['end_time'] and result[i]['start_time'] <= self.end_time <= result[i]['end_time']):
					error = True
				if (self.start_time <= result[i]['start_time'] <= self.end_time and self.start_time <= result[i]['end_time'] <= self.end_time):
					error = True
				if (self.start_time <= result[i]['start_time'] <= self.end_time and result[i]['start_time'] <= self.end_time <= result[i]['end_time']):
					error = True
				if (result[i]['start_time'] <= self.start_time <= result[i]['end_time'] and self.start_time <= result[i]['end_time'] <= self.end_time):
					error = True
			# If the reservation already exists, raise an error
			if error:
				raise LookupError("Zeit ist schon vergeben")
			# If the reservation does not exist, insert a new record
			else:
				# Insert a new record
				self.db_connector.insert(self.__dict__)
				print("Data inserted.")
				return None

		if not result:
			# Insert a new record
			self.db_connector.insert(self.__dict__)
			print("Data inserted.")
			return None

	# Class method that can be called without an instance of the class to construct an instance of the class
	@classmethod
	def load_data_by_device_name(cls, device_name):
		# Load data from the database and create an instance of the Device class
		reservation_query = Query()
		result = cls.db_connector.search(reservation_query.device_name == device_name)

		if result:
			data = result[0]
			return [[cls(data['device_name'], data['reserver'], data['start_time'], data['end_time']) for data in result], data.doc_id]
		else:
			raise LookupError("Keine Reservierungen gefunden")

	@classmethod
	def delete_data_by_doc_id(cls, doc_id):
		# Load data from the database and create an instance of the Device class
		result = cls.db_connector.remove(doc_ids=[doc_id])

		if result:
			return True
		else:
			return False
