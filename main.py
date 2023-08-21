import argparse
import importlib


def main():
    """Parses command line arguments and passes them to an instantiation
    of a database management class. Different methods of the class are called
    depending on what the user wants to do with a database.
    """
    # Create argument parser
    parser = argparse.ArgumentParser(description="Access database")

    # Define command line arguments
    parser.add_argument("host", help="Host name")
    parser.add_argument("user", help="MySQL server username")
    parser.add_argument("password", help="Password associated with username")
    parser.add_argument("database", help="User-defined database")
    parser.add_argument("table", help="User-defined table")
    parser.add_argument("filename", help="Name of file from which to load data")
    parser.add_argument("class_name", help="Database class")

    # Parse command line arguments
    args = parser.parse_args()

    # Load class
    try:
        module = importlib.import_module(f"database_classes.{args.class_name.lower()}")
        database_class = getattr(module, args.class_name)

        # Instantiate class
        database_instance = database_class(
            host=args.host,
            user=args.user,
            password=args.password,
            database=args.database,
            table=args.table,
            filename=args.filename,
        )

        # Execute database class methods
        database_instance.delete_db()
        database_instance.create_db()
        database_instance.create_table()
        database_instance.populate_table()
        database_instance.query_data()
        database_instance.plot_data()
        database_instance.close_connection()

    except (ImportError, AttributeError) as e:
        print(e)


if __name__ == "__main__":
    main()
