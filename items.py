# items.py
class Item:
    def __init__(self, item_name, item_description, item_holder):
        self.item_name = item_name
        self.item_description = item_description
        self.item_holder = item_holder

    def set_item_name(self, item_name):
        self.item_name = item_name

    def set_item_description(self, item_description):
        self.item_description = item_description

    def set_item_holder(self, item_holder):
        self.item_holder = item_holder

    def get_item_name(self):
        return self.item_name

    def get_item_description(self):
        return self.item_description

    def get_item_holder(self):
        return self.item_holder
