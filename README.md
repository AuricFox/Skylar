# Skylar
Programming practice for coding assessments and interviews. Focuses on SQL queries and databases.

## Getting Started

To get started with Skylar, follow these steps:

1. **Clone the Repository:**
    ```
    git clone https://github.com/AuricFox/Skylar.git
    ```

2. **Navigate to the Project Directory:**
    ```
    cd Skylar
    ```

3. **Setup Environment:**
    ```
    pip install virtualenv  
    virtualenv env

    .\env\Scripts\activate      # Windows
    source env/bin/activate     # Mac OS
    ```

4. **Install Dependencies:**
    ```
    (env) pip install flask
    (env) pip install tabulate
    ```

5. **Run Server:**
    ```
    (env) python app.py
    ```

    The server will start running, and you can access the application by navigating to `http://localhost:5000` in your web browser.

## Database Schema

Below is the schema of the SQLite3 database used for Skylar:

### Customer

|**cid**|cname|address|city|state|

- **PK**: cid

### ContactInfo

|**cid**|type|value|

- **PK**: cid, type, value
- **FK**: ContactInfo.cid TO Customer.cid
- **type examples**: cell, home, email

### Restaurant

|**rid**|rname|city|state|rating|ownerID|

- **PK**: rid
- **FK**: Restaurant.ownerID TO Owner.oid

### Reservation

|**cid**|rid|date|num_adults|num_child|

- **PK**: cid, rid
- **FK**: Reservation.cid TO Customer.cid
- **FK**: Reservation.rid TO Restaurant.rid

### Owner

|**Oid**|oname|

- **PK**: Oid

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT) - see the [LICENSE](LICENSE) file for details.
