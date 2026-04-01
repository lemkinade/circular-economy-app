# Repair Matchmaker Database

A PostgreSQL database schema designed for a local repair matchmaking service. The database handles users, repairers, item categories, and service requests. Its core function is to use relational data structures to accurately map a user's broken item to a repairer who has the specific skills to fix it.

## Technologies Used
* **Database:** PostgreSQL
* **Language:** Python 3
* **Adapter:** psycopg2
* **Environment:** Windows Subsystem for Linux (WSL / Ubuntu)

## Project Structure
* `app.py`: The main database setup script. It establishes the connection, drops existing tables to ensure a clean state, creates the 7 required tables (Users, Categories, Repairers, RepairerSkills, ServiceRequests, Appointments, Reviews), and populates them with sample test data.
* `queries.py`: The query execution script. It runs specific SQL queries (like calculating the total KG of landfill saved and finding 5-star reviews) to demonstrate the database's analytical capabilities.

## Entity-Relationship Diagram

![Repair Matchmaker ER Diagram](assets/erd.png)

## Installation & Setup

To explore or run this database project locally, you will need Python 3 installed on your machine. The database operations and connections are handled via the `psycopg2` adapter.

**1. Clone the repository and navigate to the directory:**
```bash
git clone <https://github.com/lemkinade/repair_matchmaker_db.git>
cd repair_matchmaker_db
```

**2. Create and activate a Python virtual environment:**
This ensures the database dependencies do not interfere with your system's global Python installation.
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

**3. Install the required dependencies:**
```bash
pip install -r requirements.txt
```

**4. Initialize the database schema and seed data:**
Run the initialization script to connect to PostgreSQL, build the tables, establish foreign key constraints, and insert the sample data.
```bash
python3 app.py
```

## Future Enhancements
* Implement a Graphical User Interface for easier user interaction.
* Expand the test dataset to simulate a full production environment.