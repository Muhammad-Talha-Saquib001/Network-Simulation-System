# src/main.py
from core.router import Router
from protocols.smtp import SMTPProtocol
from routing.vector_routing import DistanceVectorRouting  # <-- Phase 3 import


def build_simple_topology():
    # Create routers
    rA = Router("A")
    rB = Router("B")
    rC = Router("C")

    # Connect routers (bidirectional via Router.add_connection)
    rA.add_connection(rB, delay=0.1)
    rB.add_connection(rC, delay=0.1)

    # ---------------------------------------------------------
    # PHASE 3: Automatic Routing Table Creation (Distance Vector)
    # ---------------------------------------------------------
    dvr = DistanceVectorRouting()

    # Initialize neighbor cost tables
    dvr.initialize_router("A", {"B": 1})
    dvr.initialize_router("B", {"A": 1, "C": 1})
    dvr.initialize_router("C", {"B": 1})

    # Simulate routing table exchanges (lightweight DV process)
    dvr.update("A", "B", dvr.get_table("B"))
    dvr.update("B", "A", dvr.get_table("A"))
    dvr.update("B", "C", dvr.get_table("C"))
    dvr.update("C", "B", dvr.get_table("B"))

    # -------------------------------
    # Convert DV table → Router table
    # -------------------------------
    def convert_table(dv_table):
        """
        Convert DV entries such as:
            "C": {"next_hop": "B", "cost": 1}
        into:
            "C": "B"
        because Router.forward_packet expects next-hop strings.
        """
        return {dest: dv_table[dest]["next_hop"] for dest in dv_table}

    # Assign converted routing tables to routers
    rA.set_routing_table(convert_table(dvr.get_table("A")))
    rB.set_routing_table(convert_table(dvr.get_table("B")))
    rC.set_routing_table(convert_table(dvr.get_table("C")))

    # ---------------------------------------------------------
    # END PHASE 3
    # ---------------------------------------------------------

    return rA, rB, rC


def demo_smtp():
    rA, rB, rC = build_simple_topology()

    # Attach SMTP protocol instances to routers (A and C)
    smtp_A = SMTPProtocol(node=rA)
    smtp_C = SMTPProtocol(node=rC)

    # Initiate SMTP send from A to C
    smtp_A.send("Hello C, this is A via SMTP", destination="C")


if __name__ == "__main__":
    demo_smtp()
