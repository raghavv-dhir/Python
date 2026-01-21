#1. Singleton
#2. ABC
#3. Factory
#4. Composition

class DatabaseConnection: #An app should not open multiple db connections unnecessarily, only shared connection is used everywhere.
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print("Connecting to database...")
        return cls._instance

db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(db1 is db2)  # True - both variables point to the same instance
print(id(db1))
print(id(db2)) #same id for db1 and db2 instance