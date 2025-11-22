# src/core/router.py

from .connection import Connection
from .packet import Packet


class Router:
    """
    Simulates a router with a routing table and connected links.
    """

    def __init__(self, router_id):
        self.router_id = router_id
        self.routing_table = {}  # destination -> next_hop_router_id
        self.connections = {}  # neighbor_id -> Connection object

    # ----------------------------- #
    #   CONNECTION MANAGEMENT        #
    # ----------------------------- #

    def add_connection(self, other_router, bandwidth=1, delay=0.1):
        """
        Connects this router to another router with a simulated link.
        """
        connection = Connection(self, other_router, bandwidth, delay)
        self.connections[other_router.router_id] = connection
        other_router.connections[self.router_id] = connection

    # ----------------------------- #
    #       ROUTING TABLE            #
    # ----------------------------- #

    def add_route(self, destination, next_hop):
        """Add or update a routing entry."""
        self.routing_table[destination] = next_hop

    # ----------------------------- #
    #       PACKET FORWARDING        #
    # ----------------------------- #

    def forward_packet(self, packet):
        """
        Forwards packet based on the routing table.
        Returns the next router, or None if destination reached.
        """
        packet.add_hop(self.router_id)

        if packet.destination == self.router_id:
            return None  # Packet has arrived

        if packet.destination not in self.routing_table:
            raise Exception(f"No route from {self.router_id} to {packet.destination}")

        next_hop = self.routing_table[packet.destination]

        connection = self.connections.get(next_hop)
        if not connection:
            raise Exception(f"No connection from {self.router_id} to {next_hop}")

        next_router = connection.transmit(packet, self.router_id)
        return next_router

    # ---- Phase 3: Routing Table Integration ----

    def set_routing_table(self, table):
        self.routing_table = table

    def forward(self, packet):
        dest = packet.destination

        if dest in self.routing_table:
            next_hop = self.routing_table[dest]["next_hop"]
            print(f"[Router {self.name}] Forwarding packet to next hop {next_hop}")
            return next_hop
        else:
            print(f"[Router {self.name}] No route to destination {dest}")
            return None
