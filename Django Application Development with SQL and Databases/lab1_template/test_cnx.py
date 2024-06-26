"""
test_cnx.py
-----------
A script to test the connection to a PostgreSQL database from a WSL environment.

Purpose:
--------
This script was created to verify that a Python application running in Windows Subsystem for Linux (WSL)
can connect to a PostgreSQL database running on a Windows machine. The connection was initially failing
due to firewall settings and configuration issues.

Steps Taken:
------------

1. **Finding the IP Address:**
    - Opened Command Prompt on the Windows machine.
    - Ran the `ipconfig` command to display the network configuration.
    - Located the `IPv4 Address` for the active network adapter, which was `192.168.0.12`.

2. **PostgreSQL Configuration:**
    - Ensured that PostgreSQL was listening on all addresses by setting `listen_addresses = '*'` in the `postgresql.conf` file.
    - Added an entry for the WSL IP address (`192.168.0.12/32`) to the `pg_hba.conf` file to allow connections.
    - Restart postgres with `net stop postgresql-x64-13` and `net start postgresql-x64-13`.

3. **Firewall Settings:**
    - Temporarily disabled the Windows Firewall to test the connection with `netsh advfirewall set allprofiles state off`.
    - Upon successful connection, created a new inbound rule in the Windows Firewall to allow traffic on port 5432.
    - Firewall can be turn on with `netsh advfirewall set allprofiles state on`.

Usage:
------
Run the script in a Python environment within WSL to test the connection to the PostgreSQL database.

Dependencies:
-------------
- psycopg2

To install psycopg2, run:
    pip install psycopg2-binary

Example:
--------
    $ python3 test_cnx.py
"""

import psycopg2
import traceback

try:
    connection = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="postgres",
        host="192.168.0.12",  # Use the IP address of the Windows machine
        port="5432"
    )
    print("Connection successful")
except Exception as e:
    print(f"Error: {e}")
    traceback.print_exc()
