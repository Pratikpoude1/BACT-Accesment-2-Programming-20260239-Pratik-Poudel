# BACT7501 Assessment 2 - Purchase Requisition System


class Requisition:
    def __init__(self, requisition_id):
        # Set starting values for one requisition
        self.requisition_id = requisition_id
        self.date = ""
        self.staff_id = ""
        self.staff_name = ""
        self.items = []
        self.total = 0
        self.status = "Pending"
        self.approval_reference = "Not available"

    def staff_info(self):
        # Ask for staff details
        print("Enter staff information:")

        self.date = input("Date (DD-MM-YYYY): ")
        while self.date == "":
            print("Date cannot be empty.")
            self.date = input("Date (DD-MM-YYYY): ")

        self.staff_id = input("Staff ID: ")
        while self.staff_id == "":
            print("Staff ID cannot be empty.")
            self.staff_id = input("Staff ID: ")

        self.staff_name = input("Staff Name: ")
        while self.staff_name == "":
            print("Staff Name cannot be empty.")
            self.staff_name = input("Staff Name: ")

    def requisitions_details(self):
        # Ask for items and prices, then calculate the total
        print("Enter requisition items:")

        while True:
            item_name = input("Item name: ")
            while item_name == "":
                print("Item name cannot be empty.")
                item_name = input("Item name: ")

            while True:
                try:
                    item_price = float(input("Item price: $"))
                    if item_price <= 0:
                        print("Price must be greater than 0.")
                    else:
                        break
                except ValueError:
                    print("Invalid price. Please enter a number.")

            self.items.append([item_name, item_price])

            another_item = input("Add another item? (yes/no): ").lower()
            while another_item != "yes" and another_item != "no":
                print("Please enter yes or no.")
                another_item = input("Add another item? (yes/no): ").lower()

            if another_item == "no":
                break

        self.total = 0
        for item in self.items:
            self.total += item[1]

    def requisition_approval(self):
        # Approve automatically if total is below $500
        if self.total < 500:
            self.status = "Approved"
            self.approval_reference = self.staff_id + str(self.requisition_id)[-3:]
        else:
            self.status = "Pending"
            self.approval_reference = "Not available"

    def respond_requisition(self):
        # Let a manager approve, reject, or leave a pending requisition pending
        if self.status == "Pending":
            print("")
            print(f"Requisition ID: {self.requisition_id} | Staff: {self.staff_name} | Total: ${self.total}")
            decision = input("Manager decision (approve/reject/pending): ").lower()

            while decision != "approve" and decision != "reject" and decision != "pending":
                print("Please enter approve, reject, or pending.")
                decision = input("Manager decision (approve/reject/pending): ").lower()

            if decision == "approve":
                self.status = "Approved"
                self.approval_reference = self.staff_id + str(self.requisition_id)[-3:]
            elif decision == "reject":
                self.status = "Not approved"
                self.approval_reference = "Not available"

    def display_requisition(self):
        # Show all details of this requisition
        print("")
        print("Requisition Summary")
        print(f"Date: {self.date}")
        print(f"Requisition ID: {self.requisition_id}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Staff Name: {self.staff_name}")
        print("Items:")
        for item in self.items:
            print(f"  - {item[0]}: ${item[1]}")
        print(f"Total: ${self.total}")
        print(f"Status: {self.status}")
        print(f"Approval Reference Number: {self.approval_reference}")
