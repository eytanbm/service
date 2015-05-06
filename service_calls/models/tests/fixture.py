'''
Created on Apr 23, 2015

@author: eytan
'''
from django.contrib.auth.models import User
import random

from service_calls.content import TICKET_ROLE, TICKET_TYPE
from service_calls.models.fault import Fault
from service_calls.models.ticket import Ticket
from service_calls.models.ticket_role import TicketRole


class ModelTestFixture(object):
    
    def __init__(self):
        self.users = [User.objects.create_user("test_user%d" % i, password="test_user%i") for i in xrange(20)]
        def create_roles():
            role_choices = [x[0] for x in TICKET_ROLE.to_choices()]
            roles = [TicketRole(role=random.choice(role_choices), user=random.choice(self.users))]
            TicketRole.objects.bulk_create(roles)
        def create_faults():
            faults = [Fault(name="Test Fault number %d" % i) for i in xrange(10)]
            Fault.objects.bulk_create(faults)
        def create_tickets():
            owner = TicketRole.objects.get_or_create(role=TICKET_ROLE.Manager, user=self.users[0])[0]
            tickets = [Ticket(owner=owner, type=random.choice([x[0] for x in TICKET_TYPE.to_choices()]), fault=random.choice(Fault.objects.all())) for i in xrange(100)]
            Ticket.objects.bulk_create(tickets)
        create_roles()
        create_faults()
        create_tickets()
        
    def random_role(self):
        return random.choice(TicketRole.objects.all())
        
    def random_ticket(self):
        return random.choice(Ticket.objects.all())
        
