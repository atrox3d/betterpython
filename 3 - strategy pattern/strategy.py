import string
import random
from typing import List
from abc import ABC, abstractmethod
from dataclasses import dataclass, field


def generate_id(length=8):
    # helper function for generating an id
    return ''.join(random.choices(string.ascii_uppercase, k=length))


@dataclass
class SupportTicket:
    customer: str
    issue: str
    id: str = field(default_factory=generate_id)


class TicketOrderingStrategy(ABC):
    @abstractmethod
    def create_ordering(self, _list: List[SupportTicket]) -> List[SupportTicket]:
        pass

class FIFOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, _list: List[SupportTicket]) -> List[SupportTicket]:
        return _list.copy()

class LIFOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, _list: List[SupportTicket]) -> List[SupportTicket]:
        lifo = _list.copy()
        lifo.reverse()
        return lifo
    
class RandomOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, _list: List[SupportTicket]) -> List[SupportTicket]:
        rnd = _list.copy()
        random.shuffle(rnd)
        return rnd

class CustomerSupport:

    def __init__(self):
        self.tickets: List[SupportTicket] = []

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self, processing_strategy: TicketOrderingStrategy):

        ticket_list = processing_strategy.create_ordering(self.tickets)

        # if it's empty, don't do anything
        if len(ticket_list) == 0:
            print("There are no tickets to process. Well done!")
            return

        for ticket in ticket_list:
            self.process_ticket(ticket)

    def process_ticket(self, ticket: SupportTicket):
        print("==================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("==================================")


# create the application
app = CustomerSupport()

# register a few tickets
app.create_ticket("John Smith", "My computer makes strange sounds!")
app.create_ticket("Linus Sebastian", "I can't upload any videos, please help.")
app.create_ticket("Arjan Egges", "VSCode doesn't automatically solve my bugs.")

# process the tickets
app.process_tickets(RandomOrderingStrategy())
