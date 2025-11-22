# src/protocols/smtp.py
from core.packet import Packet
from protocols.protocol_base import ProtocolBase


class SMTPProtocol(ProtocolBase):
    """
    Minimal SMTP-like protocol that uses the Router.forward_packet() API.
    Assumes `node` is an instance of Router (src.core.router.Router).
    """

    def send(self, message: str, destination: str):
        """
        Build a Packet from this node to `destination` and hand it to the node's forwarding.
        destination: router_id of the target Router (string)
        """
        # Packet constructor from Phase 1: (source, destination, size=1, payload="")
        pkt = Packet(
            source=self.node.router_id,
            destination=destination,
            size=max(1, len(message)),
            payload=f"SMTP_DATA:{message}",
        )

        print(f"[SMTP] {self.node.router_id} sending message -> {destination}")
        # Let router forward hop-by-hop using existing Router.forward_packet
        current = self.node
        try:
            while current:
                print(f"[SMTP] at router {current.router_id}")
                current = current.forward_packet(pkt)
        except Exception as e:
            print(f"[SMTP] delivery failed: {e}")
            return

        # When forward_packet returns None, packet reached destination
        print(f"[SMTP] message delivered. Path: {' -> '.join(pkt.path)}")

    def receive(self, packet: Packet):
        """Process an incoming packet that reached this router."""
        if packet.payload.startswith("SMTP_DATA:"):
            msg = packet.payload.split("SMTP_DATA:", 1)[1]
            print(
                f"[SMTP] {self.node.router_id} received message: '{msg}' from {packet.source}"
            )
        else:
            print(f"[SMTP] {self.node.router_id} received non-SMTP packet")
