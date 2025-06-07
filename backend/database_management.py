import pymysql.cursors
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

def create_user_table(connection):
    """Create the plateform users table.
    
    Args:
        connection: The sql connection where to deploy the database.
    """

    with connection:
        with connection.cursor() as cursor:
            sql="""CREATE TABLE Users(
                id INT PRIMARY KEY AUTO_INCREMENT,
                person VARCHAR(255) NOT NULL,
                mail_adress VARCHAR(255) NOT NULL UNIQUE,
                pwd VARCHAR(255) NOT NULL,
                nb_attemps  INT,
                nb_obtained INT,
                account_creation_date DATE NOT NULL
            );"""
            cursor.execute(sql)
        connection.commit()

def create_slots_table(connection):
    """Create the canipark slots table.
    
    Args:
        connection: The sql connection where to deploy the database.
    """

    with connection:
        with connection.cursor() as cursor:
            sql="""CREATE TABLE slots(
                id INT PRIMARY KEY AUTO_INCREMENT,
                week_day VARCHAR(15),
                slot_time TIME,
                available BOOLEAN
            );"""
            cursor.execute(sql)
        connection.commit()

def create_booking_table(connection):
    """Create the booking table.
    
    Args:
        connection: The sql connection where to deploy the database.
    """

    with connection:
        with connection.cursor() as cursor:
            sql="""CREATE TABLE booking(
                id_booking INT PRIMARY KEY AUTO_INCREMENT,
                id_user INT NOT NULL,
                pwd VARCHAR(255),
                id_slot INT NOT NULL,
                FOREIGN KEY (id_user) REFERENCES Users(id),
                FOREIGN KEY (id_slot) REFERENCES slots(id)
            );"""
            cursor.execute(sql)
        connection.commit()

def init_db(connection):
    """Initalize the database with the required tables.
    
    Args:
        connection: The sql connection where to deploy the database.
    """

    print("Creating the database...")
    create_user_table(connection)
    create_slots_table(connection)
    create_booking_table(connection)
    print("Database created")

def add_user(connection, name: str, email: str, password: str, creation_date: datetime | None, nb_attempts = 0, nb_obtained = 0):
    """Add a new user to the database when they subscribe on the webpage?

    Args:
        connection: The sql connection where to deploy the database.
        name: The name provided by the user.
        email: The user's email address.
        password: The user's password for connexion to his canipark account.
        creation_date: The date the of the account creation (can be set in case of an account update).
        nb_attempts: The number of time the user asked for a slot (can be set in case of an account update).
        nb_obtained: The number of time the user obtained a slot (can be set in case of an account update).
    """

    if not creation_date:
        creation_date = datetime.today().strftime("%Y-%m-%d")
    with connection:
        with connection.cursor() as cursor:
            sql="""INSERT INTO Users (person, mail_adress, pwd, nb_attemps, nb_obtained, account_creation_date)
                VALUES (
                    %s, %s, %s, %s, %s, %s
                );
                """
            cursor.execute(sql, (name, email, password, nb_attempts, nb_obtained, creation_date))
        connection.commit()


if __name__=='__main__':
    print("connecting to the database")
    connection = pymysql.connect(host=os.environ["sql_host"],
                             user=os.environ['sql_user'],
                             password=os.environ["sql_password"],
                             database= os.environ["db_name"],
                             cursorclass=pymysql.cursors.DictCursor)


    