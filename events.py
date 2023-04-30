# events.py
class Event:
    def __init__(self, event_name, description, creator, participants=None):
        self.event_name = event_name
        self.description = description
        self.creator = creator
        if participants is None:
            self.participants = []
        else:
            self.participants = participants

    def set_event_name(self, event_name):
        self.event_name = event_name

    def set_description(self, description):
        self.description = description

    def set_creator(self, creator):
        self.creator = creator

    def add_participant(self, participant):
        self.participants.append(participant)

    def remove_participant(self, participant):
        self.participants.remove(participant)

    def get_event_name(self):
        return self.event_name

    def get_description(self):
        return self.description

    def get_creator(self):
        return self.creator

    def get_participants(self):
        return self.participants
