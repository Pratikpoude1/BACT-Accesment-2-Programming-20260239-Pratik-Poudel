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