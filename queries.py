import psycopg2

def run_project_queries():
    try:
        conn = psycopg2.connect(
            dbname="circular_economy_db",
            user="myuser",
            password="mypassword",
            host="localhost"
        )
        cursor = conn.cursor()
        print("--- Running Circular Economy Database Queries ---\n")

        # Query 1: Total Kg of Landfill Saved
        print(">> Query 1: Total Kg of Landfill Saved")
        cursor.execute('''
            SELECT Categories.CategoryName, Sum(Categories.AvgLandfillSaved_KG) AS TotalKGSaved
            FROM Categories
            INNER JOIN ServiceRequests ON Categories.CategoryID = ServiceRequests.CategoryID
            WHERE ServiceRequests.RequestStatus = 'Completed'
            GROUP BY Categories.CategoryName;
        ''')
        for row in cursor.fetchall():
            print(f"   Category: {row[0]} | Total KG Saved: {row[1]}")
        print("-" * 50)

        # Query 2: Users Who Left a 5-Star Review
        print(">> Query 2: Users Who Left a 5-Star Review")
        cursor.execute('''
            SELECT Users.FullName, ServiceRequests.ItemDescription, Reviews.Rating
            FROM Users
            INNER JOIN ServiceRequests ON Users.UserID = ServiceRequests.UserID
            INNER JOIN Appointments ON ServiceRequests.RequestID = Appointments.RequestID
            INNER JOIN Reviews ON Appointments.ApptID = Reviews.ApptID
            WHERE Reviews.Rating = 5;
        ''')
        for row in cursor.fetchall():
            print(f"   User: {row[0]} | Item: {row[1]} | Rating: {row[2]} Stars")
        print("-" * 50)

        # Query 3: Average Hourly Rate per Category
        print(">> Query 3: Average Hourly Rate per Category")
        cursor.execute('''
            SELECT Categories.CategoryName, AVG(RepairerSkills.HourlyRate) AS AverageCostPerHr
            FROM Categories
            INNER JOIN RepairerSkills ON Categories.CategoryID = RepairerSkills.CategoryID
            GROUP BY Categories.CategoryName;
        ''')
        for row in cursor.fetchall():
            print(f"   Category: {row[0]} | Avg Hourly Rate: ${row[1]:.2f}")
        print("-" * 50)

        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_project_queries()