import os
from tinydb import TinyDB, Query
from serializer import serializer

def find_database(filename, key) -> list:
    """Find all devices in the database."""
    # Define the database connector
    db_connector = TinyDB(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.json'), storage=serializer).table(filename)
    # Create a query object
    DeviceQuery = Query()
    # Search the database for all devices that are active
    result = db_connector.all()

    # The result is a list of dictionaries, we only want the device names
    if result:
        result = [[x[key] for x in result], [x.doc_id for x in result]]

    return result
