# sql-basics-automated

# Database Management Tool

This tool provides a flexible way to manage databases using SQL. Users can define custom data management classes to perform operations on their desired database and automate the process.

## Introduction
This project is a database management tool that empowers users to interact with their databases through custom data management classes. The README serves as a guide on how to use this tool effectively.

## Getting Started
To get started with this project, follow these steps:

### Prerequisites
- Python (version X.X.X)
- MySQL
- Pandas
- NumPy
- mysql.connector
- Matplotlib

You can install Python packages like Pandas, NumPy, mysql.connector, and Matplotlib using pip:

```bash
pip install pandas numpy mysql-connector-python matplotlib

Usage

This tool is designed to streamline database management tasks. Below are key aspects of its usage.

Database Management Classes
The database management classes are stored in the database_classes folder. Users can create their custom data management class that utilizes SQL to interact with their chosen database. Customize the class methods, such as populate_table(), query_data(), and plot_data(), according to your specific data management needs.

Command Line Arguments
When executing main.py, the following command line arguments must be provided:

host: The hostname of your database server.
user: Your database username.
password: Your database password.
database: The name of your database.
table: The name of the database table.
filename: The name of the CSV or XLSX file containing data.
class_name: The name of your custom data management class.

python main.py host user password database table filename class_name


