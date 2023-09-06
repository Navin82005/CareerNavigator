from organization_api.models import *

class EventSerializer:
    def __init__(self, id = None):
        if id != None:
            self.user = User.objects.get(id=id)
        self.models = Events.objects.all()
        self.organization = Organization.objects.all()

    def getEvents(self):
        data = {}
        if self.organization != None:
            for i in self.organization:
                data[i] = []
                for j in i.events.all():
                    data[i] += [j]

        return data