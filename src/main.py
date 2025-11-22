# src/main.py
from core.router import Router
from protocols.smtp import SMTPProtocol


def build_simple_topology():
    # Create routers
    rA = Router("A")
    rB = Router("B")
    rC = Router("C")

    # Connect routers (bidirectional via Router.add_connection)
    rA.add_connection(rB, delay=0.1)
    rB.add_connection(rC, delay=0.1)

    # Populate routing tables (manual static routes for demo)
    # A -> C via B
    rA.add_route("C", "B")
    # B -> C direct
    rB.add_route("C", "C")
    # B -> A direct
    rB.add_route("A", "A")
    # C -> A via B
    rC.add_route("A", "B")

    return rA, rB, rC


def demo_smtp():
    rA, rB, rC = build_simple_topology()

    # Attach SMTP protocol instances to routers (A and C)
    smtp_A = SMTPProtocol(node=rA)
    smtp_C = SMTPProtocol(node=rC)

    # NOTE: router.forward_packet appends hops to Packet.path.
    # We want C to be able to "receive" and process the payload after arrival.
    # To keep things modular, SMTPProtocol.send uses Router.forward_packet to deliver to the destination.
    # After send completes, Packet.path will show the route, and the destination router can inspect payload.
    smtp_A.send("Hello C, this is A via SMTP", destination="C")


if __name__ == "__main__":
    demo_smtp()
