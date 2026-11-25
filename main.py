import csv

tickets = []

def create_tickets():
    name = input("Employee Name: ")
    issue = input("Issue Description: ")

    ticket = {
        "id" : len(tickets) + 1,
        "employee" : name,
        "issue" : issue,
        "status" : "Open"
    }

    tickets.append(ticket)
    print("Ticket created successfully!")

def view_tickets():
    for ticket in tickets:
        print(ticket)

while True: 
    print("\nHELP DESK TICKET TRACKER")
    print("1. Create Ticket")
    print("2. View Tickets")
    print("3. Exit")

    choice = input("Choose an option: ")
    
    if choice == "1":
        create_tickets()

    elif choice == "2":
        view_tickets()

    elif choice == "3":
        break

    else: 
        print("invalid choice.")