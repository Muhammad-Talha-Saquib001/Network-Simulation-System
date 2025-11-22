# src/main.py

from core.router import Router
from core.packet import Packet


def demo_simulation():
    # Create routers
    r1 = Router("A")
    r2 = Router("B")
    r3 = Router("C")

    # Connect routers
    r1.add_connection(r2, delay=0.2)
    r2.add_connection(r3, delay=0.2)

    # Routing tables
    r1.add_route("C", "B")
    r2.add_route("C", "C")
    r2.add_route("A", "A")
    r3.add_route("A", "B")

    # Create packet
    packet = Packet(source="A", destination="C", payload="Hello Cloud!")

    # Forward packet
    current = r1
    while current:
        print(f"Router {current.router_id} forwarding packet {packet.id}")
        current = current.forward_packet(packet)

    print("Packet delivered successfully.")
    print("Path:", " -> ".join(packet.path))


if __name__ == "__main__":
    demo_simulation()
