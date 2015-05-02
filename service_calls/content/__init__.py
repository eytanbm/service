from service_calls.utils.enumeration import Enumeration
from django.utils.translation import ugettext_lazy as _

TICKET_TYPE = Enumeration(
                                (u'Problem',    _(u'Problem Report')),
                          )

TICKET_SOURCE = Enumeration(
                                (u'Guset',          _(u'Guest Complaint')),
                                (u'Maintenance',    _(u'Maintenance Personnel Report')),
                          )

TICKET_PRIORITY = Enumeration(
                                (u'Low',            _(u'Low')),
                                (u'Normal',         _(u'Normal')),
                                (u'High',           _(u'High')),
                                (u'Critical',       _(u'Critical')),
                              )

TICKET_STATUS = Enumeration(
                                (u'Reported',   _(u'Reported')),
                                (u'Created',    _(u'Created')),
                                (u'Dispatched', _(u'Dispatched')),
                                (u'Assigned',   _(u'Assigned')),
                                (u'Done',       _(u'Done')),
                                (u'Closed',     _(u'Closed')),
                            )

TICKET_ROLE = Enumeration(
                                (u'Manager',    _(u'Manager')),
                                (u'Dispatcher', _(u'Dispatcher')),
                                (u'Assignee',   _(u'Assignee')),
                          )  

__all__ = [
           'urls',
           'TICKET_TYPE',
           'TICKET_SOURCE',
           'TICKET_PRIORITY',
           'TICKET_STATUS',
           'TICKET_ROLE',
           ]

