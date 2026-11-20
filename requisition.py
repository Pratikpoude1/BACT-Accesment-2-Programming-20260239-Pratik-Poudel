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
