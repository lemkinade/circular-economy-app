import psycopg2

def setup_database():
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        dbname="circular_economy_db",
        user="myuser",
        password="mypassword",
        host="localhost"
    )
    cursor = conn.cursor()

    print("Connected to database. Setting up tables...")

    # Drop tables if they exist to avoid conflicts when re-running the script
    cursor.execute('''
        DROP TABLE IF EXISTS Reviews, Appointments, ServiceRequests, RepairerSkills, Repairers, Categories, Users CASCADE;
    ''')

    # Create Tables based on project specification
    cursor.execute('''
        CREATE TABLE Users (
            UserID SERIAL PRIMARY KEY,
            FullName VARCHAR(100) NOT NULL,
            Email VARCHAR(100) NOT NULL UNIQUE,
            City VARCHAR(50) NOT NULL,
            ZipCode VARCHAR(10) NOT NULL,
            DateJoined TIMESTAMP NOT NULL
        );

        CREATE TABLE Categories (
            CategoryID SERIAL PRIMARY KEY,
            CategoryName VARCHAR(50) NOT NULL UNIQUE,
            AvgLandfillSaved_KG DOUBLE PRECISION NOT NULL
        );

        CREATE TABLE Repairers (
            RepairerID SERIAL PRIMARY KEY,
            BusinessName VARCHAR(100) NOT NULL,
            ContactEmail VARCHAR(100) NOT NULL UNIQUE,
            City VARCHAR(50) NOT NULL,
            Bio TEXT NOT NULL
        );

        CREATE TABLE RepairerSkills (
            SkillID SERIAL PRIMARY KEY,
            RepairerID INTEGER NOT NULL REFERENCES Repairers(RepairerID),
            CategoryID INTEGER NOT NULL REFERENCES Categories(CategoryID),
            HourlyRate NUMERIC(10,2) NOT NULL
        );

        CREATE TABLE ServiceRequests (
            RequestID SERIAL PRIMARY KEY,
            UserID INTEGER NOT NULL REFERENCES Users(UserID),
            CategoryID INTEGER NOT NULL REFERENCES Categories(CategoryID),
            ItemDescription TEXT NOT NULL,
            RequestStatus VARCHAR(50) NOT NULL,
            RequestDate TIMESTAMP NOT NULL,
            WarrantyEnd TIMESTAMP
        );

        CREATE TABLE Appointments (
            ApptID SERIAL PRIMARY KEY,
            RequestID INTEGER NOT NULL REFERENCES ServiceRequests(RequestID),
            RepairerID INTEGER NOT NULL REFERENCES Repairers(RepairerID),
            ApptDate TIMESTAMP NOT NULL,
            ApptStatus VARCHAR(50) NOT NULL
        );

        CREATE TABLE Reviews (
            ReviewID SERIAL PRIMARY KEY,
            ApptID INTEGER NOT NULL REFERENCES Appointments(ApptID),
            Rating SMALLINT NOT NULL,
            Comment TEXT,
            ReviewDate TIMESTAMP NOT NULL
        );
    ''')

# Insert complete sample data to test with
    cursor.execute('''
        -- 1. Insert Users
        INSERT INTO Users (FullName, Email, City, ZipCode, DateJoined) 
        VALUES ('Alice Johnson', 'alice.j@email.com', 'Springfield', '62704', '2023-01-15'),
               ('Bob Smith', 'bob.smith@email.com', 'Shelbyville', '62565', '2023-02-10');
               
        -- 2. Insert Categories
        INSERT INTO Categories (CategoryName, AvgLandfillSaved_KG) 
        VALUES ('Electronics', 0.5),
               ('Furniture', 15.0);
               
        -- 3. Insert Repairers
        INSERT INTO Repairers (BusinessName, ContactEmail, City, Bio) 
        VALUES ('Tech Fix Pro', 'contact@techfix.com', 'Springfield', 'Specializing in laptops and phones.'),
               ('Woodwork Wizards', 'info@woodwizards.com', 'Shelbyville', 'Restoring antique furniture.');

        -- 4. Insert Repairer Skills (Linking Repairers to Categories with Hourly Rates)
        INSERT INTO RepairerSkills (RepairerID, CategoryID, HourlyRate)
        VALUES (1, 1, 45.00), -- Tech Fix Pro fixes Electronics for $45/hr
               (2, 2, 60.00); -- Woodwork Wizards fixes Furniture for $60/hr

        -- 5. Insert Service Requests (Broken items reported by users)
        INSERT INTO ServiceRequests (UserID, CategoryID, ItemDescription, RequestStatus, RequestDate)
        VALUES (1, 1, 'Laptop screen flickering', 'Completed', '2023-03-01 10:00:00'),
               (2, 2, 'Antique dining chair broken leg', 'Completed', '2023-03-05 14:30:00'),
               (1, 1, 'Smartphone battery won''t hold charge', 'Pending', '2023-04-10 09:15:00');

        -- 6. Insert Appointments 
        INSERT INTO Appointments (RequestID, RepairerID, ApptDate, ApptStatus)
        VALUES (1, 1, '2023-03-02 11:00:00', 'Completed'),
               (2, 2, '2023-03-06 15:00:00', 'Completed');

        -- 7. Insert Reviews (Alice leaves a 5-star review, Bob leaves a 4-star)
        INSERT INTO Reviews (ApptID, Rating, Comment, ReviewDate)
        VALUES (1, 5, 'Fast and incredibly helpful! Screen looks brand new.', '2023-03-03 09:00:00'),
               (2, 4, 'Solid woodwork, but took a bit longer than expected.', '2023-03-08 10:00:00');
    ''')

    # Query to verify data was inserted
    cursor.execute("SELECT * FROM Users;")
    users = cursor.fetchall()
    
    print("\n--- Registered Users in Database ---")
    for user in users:
        print(f"ID: {user[0]}, Name: {user[1]}, City: {user[3]}")

    # Commit the changes and close connections
    conn.commit()
    cursor.close()
    conn.close()
    print("\nDatabase setup completed successfully!")

if __name__ == "__main__":
    setup_database()