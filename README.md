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

## Future Enhancements
* Implement a Graphical User Interface for easier user interaction.
* Expand the test dataset to simulate a full production environment.