# Circular Economy Repair Database

This project is a relational database application designed to support a local circular economy initiative. It connects individuals who have broken household items with skilled local repairers, aiming to reduce landfill waste and promote sustainability.

## Technologies Used
* **Database:** PostgreSQL
* **Language:** Python 3
* **Adapter:** psycopg2
* **Environment:** Windows Subsystem for Linux (WSL / Ubuntu)

## Project Structure
* `app.py`: The main database setup script. It establishes the connection, drops existing tables to ensure a clean state, creates the 7 required tables (Users, Categories, Repairers, RepairerSkills, ServiceRequests, Appointments, Reviews), and populates them with sample test data.
* `queries.py`: The query execution script. It runs specific SQL queries (like calculating the total KG of landfill saved and finding 5-star reviews) to demonstrate the database's analytical capabilities.
* `.gitignore`: Ensures local Python virtual environment files are not uploaded to the repository.

## Setup and Installation Instructions

### Prerequisites
Ensure you have PostgreSQL, Python 3, and `pip` installed on your Linux/WSL environment.

### 1. Database Configuration
Start the PostgreSQL service and create the required database, user, and permissions:

```bash
sudo service postgresql start
sudo -u postgres psql
```

Inside the PostgreSQL prompt (`postgres=#`), execute the following commands:

```sql
CREATE DATABASE circular_economy_db;
CREATE USER myuser WITH PASSWORD 'mypassword';
GRANT ALL ON SCHEMA public TO myuser;
\q
```
*(Note: The explicit schema grant is required for PostgreSQL v15+ to allow the user to create tables in the public schema).*

### 2. Python Environment Setup
Clone this repository, create a virtual environment to isolate dependencies, and install the PostgreSQL adapter:

```bash
python3 -m venv venv
source venv/bin/activate
pip install psycopg2-binary
```

## Running the Application

Ensure your virtual environment is activated (`source venv/bin/activate`) before running the scripts.

**1. Build the Database Schema and Insert Data:**
Run the setup script to create the tables and insert the sample records.
```bash
python3 app.py
```

**2. Execute the Analytical Queries:**
Run the queries script to view the database outputs for the specific project requirements (Total Landfill Saved and Average Hourly Rates).
```bash
python3 queries.py
```

## Future Enhancements
* Implement a Graphical User Interface (GUI) or Web Frontend (e.g., using Flask or Django) for easier user interaction.
* Expand the test dataset to simulate a full production environment.
* Add automated triggers for appointment status updates.