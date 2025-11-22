# src/core/connection.py

import time


class Connection:
    """
    Represents a bidirectional link between two routers.
    Includes bandwidth and delay simulation.
    """

    def __init__(self, router_a, router_b, bandwidth=1, delay=0.1):
        self.router_a = router_a
        self.router_b = router_b
        self.bandwidth = bandwidth  # Not fully used yet, can expand later
        self.delay = delay  # Artificial delay (seconds)
        self.active = True

    def transmit(self, packet, sender_id):
        """
        Simulates sending a packet over the connection.
        Causes delay to emulate real network latency.
        """
        if not self.active:
            raise Exception("Connection is down")

        time.sleep(self.delay)

        # Determine the receiving router
        if sender_id == self.router_a.router_id:
            return self.router_b
        elif sender_id == self.router_b.router_id:
            return self.router_a
        else:
            raise ValueError("Invalid sender for this connection")
