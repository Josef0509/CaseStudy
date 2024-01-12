import os
from users import User
from tinydb import TinyDB, Query
from datetime import datetime
from serializer import serializer


class Device():
    # Class variable that is shared between all instances of the class
    db_connector = TinyDB(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.json'), storage=serializer).table('devices')

    # Constructor
    def __init__(self, device_name : str, article_number_dev : str, device_description_dev : str, managed_by_user_id : str, acquisition_date_dev: datetime, change_date_dev: datetime):
        self.device_name = device_name
        self.article_number = article_number_dev
        self.acquisition_date = acquisition_date_dev
        self.change_date = change_date_dev
        self.device_description = device_description_dev
        self.managed_by_user_id = managed_by_user_id
        self.is_active = True
        
    # String representation of the class
    def __str__(self):
        return f'Device {self.device_name} ({self.managed_by_user_id})'

    # String representation of the class
    def __repr__(self):
        return self.__str__()
    
    def store_data(self):
        print("Storing data...")
        # Check if the device already exists in the database
        DeviceQuery = Query()
        result = self.db_connector.search(DeviceQuery.device_name == self.device_name)
        if result:
            # Update the existing record with the current instance's data
            result = self.db_connector.update(self.__dict__, doc_ids=[result[0].doc_id])
            print("Data updated.")
        else:
            # If the device doesn't exist, insert a new record
            self.db_connector.insert(self.__dict__)
            print("Data inserted.")
            
    # Class method that can be called without an instance of the class to construct an instance of the class
    @classmethod
    def load_data_by_device_name(cls, device_name):
        # Load data from the database and create an instance of the Device class
        DeviceQuery = Query()
        result = cls.db_connector.search(DeviceQuery.device_name == device_name)

        if result:
            data = result[0]
            return cls(data['device_name'], data['article_number'], data['device_description'], data['managed_by_user_id'], data['acquisition_date'], data['change_date'])
        else:
            return None



    