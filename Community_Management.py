import mysql.connector
from datetime import timedelta
from datetime import datetime
from prettytable import PrettyTable
import pyfiglet
from termcolor import colored

con = mysql.connector.connect(host='localhost',user='root',password='podacomp##25',database='demo')
cursor = con.cursor()


# code for checking in visitors or helpers

def checkin():
ascii_art = pyfiglet.figlet_format("Check In Counter", font="standard")

# Color the ASCII art
colored_ascii_art = colored(ascii_art, 'cyan')

# Print the result
print(colored_ascii_art)

def visitor():
ID = int(input("Enter Visitor ID"))
Flat = int(input("Enter Flat Number the Visitor wishes to visit "))
query = "Select ApprovedVisitor_ID from Residents where Flat_no = %s"%(Flat)
cursor.execute(query)
data = cursor.fetchall()
for i in data:
for j in i:
if j == ID:
s = "Visitor Approved!! You May Enter"
s2 = colored(s,'green')
print(s2)
else:
# redirect to new visitor
print("Visitor not Approved.")
print("Visitor to be redirected to temporary unapproved visitation")
temporary_pass()

def helper():
ID=int(input("Enter Helper ID:"))
Name=input("Enter Helper Name:")
Flat_no=int(input("Enter Flat Number where the helper works:"))
query_1="select Helper_ID FROM Residents where Flat_no = %s"%(Flat_no)
cursor.execute(query_1)
data=cursor.fetchall()
helper_approved=0
for i in data:
if i[0]==ID:
helper_approved=1
break
if helper_approved:
s = "Helper Approved!! You May Enter"
s2 = colored(s,'green')
print(s2)
#print("Helper approved.You may enter!!")
else:
# redirect to new helper
print("Helper not approved")
print("Helper to be redirected to temporary unapproved visitation")
temporary_pass()

n = int(input("Enter 1 for Visitor Check In\nEnter 2 for Helper Check In"))
if n == 1:
visitor()
elif n == 2:
helper()

def temporary_pass():

ascii_art = pyfiglet.figlet_format("Temporary Pass Centre", font="standard")

# Color the ASCII art
colored_ascii_art = colored(ascii_art, 'cyan')

# Print the result
print(colored_ascii_art)

# Get user input
VID = int(input("Enter Visitor ID "))
name = input("Enter Name Please: ")
flat = int(input("Enter flat: "))
contact = input("Enter Primary Contact: ")
purpose = input("Enter purpose of visit")


# Prepare the SQL insert statement
insert_query = """
INSERT INTO Temporary_Visitors (Flat_no, Visitor_Name, Contact, Purpose)
VALUES (%s, %s, %s, %s)
"""
# Execute the query
cursor.execute(insert_query, (flat, name, contact, purpose))

# Commit the transaction
con.commit()
print("Visitor record inserted successfully.")
s ="Temporary Pass Granted.You May Enter"
s2 = colored(s,'green')
print(s2)


def addition():
ascii_art = pyfiglet.figlet_format("Addition Counter", font="standard")

# Color the ASCII art
colored_ascii_art = colored(ascii_art, 'cyan')

# Print the result
print(colored_ascii_art)

def resident():
Flat= int(input("Enter flat"))
Name = input("Enter Name Please")
No = int(input("Enter Family Members"))
No2 = int(input("Enter number of Vehicles"))
V_NO = input("Enter Primary Vehicle Number")
Contact = input("Enter Primary Contact")
H_ID = int(input("Enter Approved Helper ID (Only One)"))
H_NAME = input("Enter Helper Name")
NoH= int(input("Enter Number of Total Helpers assisting you"))
V_ID = int(input("Enter ID of approved regular visitor"))
Fees = float(input("Enter Salary or Fees paid to maintainance"))
Status = input("Paid Status as of Now? (Paid/Unpaid)")

insert_query = """
INSERT INTO Residents VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# Data tuple
data = (Flat, Name, No, No2, V_NO, Contact, H_ID, H_NAME, NoH, V_ID, Fees, Status)

# Execute the query
cursor.execute(insert_query, data)

s="Record inserted successfully!"
s2 = colored(s,'green')
print(s2)

cursor.execute("Select * from Residents")
table = PrettyTable()

# Add column names
table.field_names = [description[0] for description in cursor.description]
data = cursor.fetchall()
# Add rows
for i in data:
table.add_row(i)

# Print the table
print(table)

# Commit the transaction
con.commit()

def helper():
ID= int(input("Enter Assigned Helper_ID"))
Name = input("Enter Name Please")
Contact = input("Enter Primary Contact")
Flat = int(input("Enter Flat Number to work in"))
Service = input("Enter the type of service provided (Cooking/Cleaning/Tutor/Coach)")
Salary = float(input("Enter Monthly Salary"))
B = float(input("Enter discussed bonus in case of overtime"))
Total_Salary = input("Enter Salary expected in case of overtime (salary+bonus)")
Leaves = int(input("Enter Leaves Permitted"))
Taken = int(input("Enter Leaves Taken"))
Entry = input("Enter entry time")
Exit = input("Enter exit time")
Hours = int(input("Enter daily working hours"))
entry_time = datetime.strptime(Entry, '%H:%M:%S').time()
exit_time = datetime.strptime(Exit, '%H:%M:%S').time()

# Parameterized SQL INSERT statement
insert_query = """
INSERT INTO helper (Helper_ID, Name, contact, Flat_No, Service_provided, Salary, Bonus, Total_Salary, Leaves_Permitted, Leaves_Taken, Entry_Time,Exit_Time,Total_working_hours)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s, %s, %s)"""

# Data tuple
data = (ID, Name, Contact, Flat, Service, Salary, B, Total_Salary, Leaves, Taken,Entry,Exit, Hours)

# Execute the query
cursor.execute(insert_query, data)

# Commit the transaction
con.commit()
s="Record inserted successfully!"
s2 = colored(s,'green')
print(s2)

cursor.execute("Select * from helper")
table = PrettyTable()

# Add column names
table.field_names = [description[0] for description in cursor.description]
data = cursor.fetchall()
# Add rows
for i in data:
table.add_row(i)

# Print the table
print(table)

# Commit the transaction
con.commit()

n = int(input("Enter 1 for Resident Addition\nEnter 2 for Helper Addition\nEnter 3 for Visitor Addition"))

if n == 1:
resident()

if n == 2:
helper()

# updating details of residents and helpers
def update():

ascii_art = pyfiglet.figlet_format("Updation Centre", font="standard")

# Color the ASCII art
colored_ascii_art = colored(ascii_art, 'cyan')

# Print the result
print(colored_ascii_art)

#updating details of residents
def up_resident_info():
flat = int(input("Enter Flat number of the resident to update: "))
while True:
print("Choose an option to update:")
print("1. Update Number of Family Members")
print("2. Update Number of Vehicles")
print("3. Update Primary Vehicle Number")
print("4. Update Primary Contact Number")
print("5. Update Name of the Helper")
print("6. Update Paid Status of Maintenance (Paid/Unpaid)")
print("7. Exit")

choice = input("Choose an option (1-7): ")

if choice == '1':
no_of_residents = int(input("Enter new number of family members: "))
update_query = "UPDATE Residents SET NumberofResidents = %s WHERE Flat_no = %s"
cursor.execute(update_query, (no_of_residents, flat))
elif choice == '2':
no_of_vehicles = int(input("Enter new number of vehicles: "))
update_query = "UPDATE Residents SET NumberofVehicles = %s WHERE Flat_no = %s"
cursor.execute(update_query, (no_of_vehicles, flat))
elif choice == '3':
vehicle_no = input("Enter updated primary vehicle number: ")
update_query = "UPDATE Residents SET Vehicle_Number = %s WHERE Flat_no = %s"
cursor.execute(update_query, (vehicle_no, flat))
elif choice == '4':
contact = input("Enter updated primary contact number: ")
update_query = "UPDATE Residents SET Contact = %s WHERE Flat_no = %s"
cursor.execute(update_query, (contact, flat))
elif choice == '5':
helper_name = input("Enter updated name of the helper: ")
update_query = "UPDATE Residents SET Helper_Name = %s WHERE Flat_no = %s"
cursor.execute(update_query, (helper_name, flat))
elif choice == '6':
paid_status = input("Enter updated paid status of maintenance (Paid/Unpaid): ")
update_query = "UPDATE Residents SET Paid_Status = %s WHERE Flat_no = %s"
cursor.execute(update_query, (paid_status, flat))
elif choice == '7':
print("Exiting the update menu.")
break
else:
s="Invalid choice. Please try again."
s2 = colored(s,'red')
print(s2)

con.commit()
s="Resident information updated successfully!"
s2 = colored(s,'green')
print(s2)

cursor.execute("SELECT * FROM Residents WHERE Flat_no = %s", (flat,))
updated_data = cursor.fetchall()
for row in updated_data:
print(row)

#updating details of helpers
def up_helper_info():
helper_id = int(input("Enter Helper ID of the record to update: "))
while True:
print("Choose an option to update:")
print("1. Update Salary")
print("2. Update Type of Service")
print("3. Update Primary Contact Number")
print("4. Update Bonus")
print("5. Update Leaves Permitted")
print("6. Exit")

choice = input("Choose an option (1-6): ")
if choice == '1':
s_type = input("Do you want to increment or decrement the salary? (Enter 'increment' or 'decrement'): ")
if s_type not in ['increment', 'decrement']:
print("Invalid option for salary update.")
continue
salary_change = int(input("Enter the amount to change the salary by: "))
if s_type == 'increment':
salary_update_query = "UPDATE helper SET Salary = Salary + %s WHERE Helper_ID = %s"
else: # decrement
salary_update_query = "UPDATE helper SET Salary = Salary - %s WHERE Helper_ID = %s"
cursor.execute(salary_update_query, (salary_change, helper_id))
print("Salary updated successfully!")

elif choice == '2':
type_of_service = input("Enter updated type of service: ")
update_query = "UPDATE helper SET Service_Provided = %s WHERE Helper_ID = %s"
cursor.execute(update_query, (type_of_service, helper_id))
print("Type of service updated successfully!")

elif choice == '3':
contact = input("Enter updated primary contact number: ")
update_query = "UPDATE helper SET Contact = %s WHERE Helper_ID = %s"
cursor.execute(update_query, (contact, helper_id))
print("Contact number updated successfully!")

elif choice == '4':
bonus = int(input("Enter updated bonus: "))
update_query = "UPDATE helper SET Bonus = %s WHERE Helper_ID = %s"
cursor.execute(update_query, (bonus, helper_id))
print("Bonus updated successfully!")

elif choice == '5':
leaves_permitted = int(input("Enter updated leaves permitted: "))
update_query = "UPDATE helper SET Leaves_Permitted = %s WHERE Helper_ID = %s"
cursor.execute(update_query, (leaves_permitted, helper_id))
print("Leaves permitted updated successfully!")

elif choice == '6':
print("Exiting the update menu.")
break
else:
s="Invalid choice. Please try again."
s2 = colored(s,'red')
print(s2)

con.commit()
s="Helper information updated successfully!"
s2 = colored(s,'green')
print(s2)

cursor.execute("SELECT * FROM helper WHERE Helper_ID = %s", (helper_id,))
updated_data = cursor.fetchall()
for row in updated_data:
print("-"*20)
print(row)
print("-"*20)


n = int(input("Enter 1 for Resident updation\nEnter 2 for Helper updation"))
if n == 1:
up_resident_info()
if n == 2:
up_helper_info()

def delete():
ascii_art = pyfiglet.figlet_format("Record Removal Centre", font="standard")

# Color the ASCII art
colored_ascii_art = colored(ascii_art, 'cyan')

# Print the result
print(colored_ascii_art)

def record_resident():
flat = int(input("Enter Flat number of the resident to delete: "))
cursor.execute("DELETE FROM Residents WHERE Flat_no = %s", (flat,))


s="Record Deleted Successfully!"
s2 = colored(s,'green')
print(s2)

print("New Record")
cursor.execute("SELECT * FROM Residents")
table = PrettyTable()

# Add column names
table.field_names = [description[0] for description in cursor.description]
data = cursor.fetchall()
# Add rows
for i in data:
table.add_row(i)

# Print the table
print(table)

con.commit()
def record_helper():
helper_id = int(input("Enter Helper ID of the record to delete: "))
cursor.execute("DELETE FROM helper WHERE Helper_id = %s", (helper_id,))

s="Record Deleted Successfully!"
s2 = colored(s,'green')
print(s2)

print("New Record")
cursor.execute("SELECT * FROM helper")
table = PrettyTable()

# Add column names
table.field_names = [description[0] for description in cursor.description]
data = cursor.fetchall()
# Add rows
for i in data:
table.add_row(i)

# Print the table
print(table)
con.commit()
n = int(input("Enter 1 for Resident Deletion\nEnter 2 for Helper Deletion"))
if n == 1:
record_resident()
if n == 2:
record_helper()


# searching in residents and helpers table

def search():
ascii_art = pyfiglet.figlet_format("Search Centre", font="standard")

# Color the ASCII art
colored_ascii_art = colored(ascii_art, 'cyan')

# Print the result
print(colored_ascii_art)


while True:
print("Search Menu:")
print("1.Search for Unpaid Maintenance Fees")
print("2.Check Helpers with Extra Leaves")
print("3.Check Working Hours and Apply Bonus")
print("4.Exit")

choice=input("Choose an option (1-4):")

if choice == '1':
search_fee()

elif choice == '2':
helper_leaves()

elif choice == '3':
working_hours()

elif choice == '4':
print("Exiting the search menu.")
break

else:
s="Invalid choice. Please try again."
s2 = colored(s,'red')
print(s2)


def search_fee():
se_query = "SELECT * FROM Residents WHERE Paid_Status='Unpaid'"
cursor.execute(se_query)

unpaid_data = cursor.fetchall()
if unpaid_data:
for i in unpaid_data:
print(i)
else:
s="No unpaid maintenance fees found."
s2 = colored(s,'green')
print(s2)

def helper_leaves():
le_query = "SELECT * FROM helper WHERE Leaves_Taken > Leaves_Permitted"
cursor.execute(le_query)

leave_data = cursor.fetchall()
if leave_data:
table = PrettyTable()

# Add column names
table.field_names = [description[0] for description in cursor.description]
data = cursor.fetchall()
# Add rows
for i in data:
table.add_row(i)

# Print the table
print(table)

else:
s="No helpers have taken extra leaves."
s2 = colored(s,'green')
print(s2)


def working_hours():
query = "SELECT Helper_ID, Entry_Time, Exit_Time, Salary, Bonus FROM helper"
cursor.execute(query)
data = cursor.fetchall()

for row in data:
helper_id, entry_time, exit_time, salary, bonus = row
hours_worked = exit_time - entry_time # assuming MySQL TIME or DATETIME format

if hours_worked > timedelta(hours=1):
print(f"Helper ID {helper_id} worked {hours_worked}. Applying 5% bonus.")
bonus_query = "UPDATE helper SET Bonus = Bonus + (Salary * 0.05) WHERE Helper_ID = %s"
Tsalary = "UPDATE helper SET Total_Salary = Salary+Bonus WHERE Helper_ID = %s"
cursor.execute(bonus_query, (helper_id,))
cursor.execute(Tsalary, (helper_id,))
con.commit()


ascii_art = pyfiglet.figlet_format(" Welcome to Community Management System")
print(ascii_art)

while True:
print("System Menu:")
print("Hello User, select a number to address your query below")
print("1 TO Check In At Gate")
print("2 TO ADD Record for New Resident/Helper")
print("3 TO UPDATE any incorrect or outdated information")
print("4 TO Remove a Resident/Helper Record")
print("5 TO Search for Unapid Fees/ Exceeding Leaves / Pending Bonus")
print("6 TO Exit from MENU")

choice=input("Choose an option (1-6):")

if choice == '1':
checkin()

elif choice == '2':
addition()

elif choice == '3':
update()

elif choice == '4':
delete()
elif choice == '5':
search()

elif choice == '6':

ascii_art = pyfiglet.figlet_format(" Thank you For Using Community Management System",font="standard")
print(ascii_art)
print("Exiting the search menu.")
break

else:
s="Invalid choice. Please try again."
s2 = colored(s,'red')
print(s2)
