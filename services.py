from database import get_connection

# Service class handles service database operations
class Service:
    def __init__(self, name="", description="", cost=0.0, serviceID=-1):
        """Initialize a Service object with service details"""
        self.name        = name
        self.description = description
        self.cost        = cost
        self.serviceID   = serviceID

    @staticmethod
    def getAllServices():
        """
        Returns a list of all services as dicts, ordered by name.
        """
        conn = get_connection()
        cursor = conn.cursor()

        try:
            # Query all service records
            cursor.execute('''
                SELECT Service_ID, name, description, cost
                FROM services
                ORDER BY name ASC
            ''')

            rows = cursor.fetchall()
            conn.close()

            # Convert rows into dictionaries for frontend use
            return [
                {
                    "serviceID":   row["Service_ID"],
                    "name":        row["name"],
                    "description": row["description"],
                    "cost":        row["cost"]
                }
                for row in rows
            ]

        except:
            conn.close()
            return []

    @staticmethod
    def getServiceByID(serviceID):
        """
        Returns a single service as a dict, or None if not found.
        """
        if serviceID == -1:
            return None

        conn = get_connection()
        cursor = conn.cursor()

        try:
            # Query database for matching service
            cursor.execute('''
                SELECT Service_ID, name, description, cost
                FROM services
                WHERE Service_ID = ?
            ''', (serviceID,))

            row = cursor.fetchone()
            conn.close()

            if row is None:
                return None

            # Convert row into dictionary for frontend use
            return {
                "serviceID":   row["Service_ID"],
                "name":        row["name"],
                "description": row["description"],
                "cost":        row["cost"]
            }

        except:
            conn.close()
            return None
