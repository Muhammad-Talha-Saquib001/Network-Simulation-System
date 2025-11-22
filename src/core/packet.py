# src/core/packet.py

import time
import uuid


class Packet:
    """
    Represents a network packet in the simulation.
    """

    def __init__(self, source, destination, size=1, payload=""):
        self.id = uuid.uuid4().hex[:8]  # Unique packet identifier
        self.source = source  # Source router ID
        self.destination = destination  # Destination router ID
        self.size = size  # Size in arbitrary units
        self.payload = payload  # Packet data
        self.timestamp = time.time()  # Creation time
        self.path = []  # Routers visited (for visualization)

    def add_hop(self, router_id):
        self.path.append(router_id)

    def __repr__(self):
        return f"<Packet {self.id} {self.source}->{self.destination} size={self.size}>"
