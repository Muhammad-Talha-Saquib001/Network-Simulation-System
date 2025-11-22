# src/protocols/protocol_base.py


class ProtocolBase:
    """
    Base class for all protocols in the simulation.
    Each protocol must define how it sends and receives packets.
    """

    def __init__(self, node):
        """
        node: The router or host running this protocol.
        """
        self.node = node

    def send(self, *args, **kwargs):
        raise NotImplementedError("Protocol must implement send().")

    def receive(self, packet):
        raise NotImplementedError("Protocol must implement receive().")
