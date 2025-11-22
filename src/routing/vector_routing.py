# src/routing/vector_routing.py


class DistanceVectorRouting:
    def __init__(self):
        self.tables = {}

    def initialize_router(self, router_name, neighbors):
        # neighbors = {neighbor_name: cost}
        self.tables[router_name] = {
            dest: {"cost": cost, "next_hop": dest} for dest, cost in neighbors.items()
        }
        self.tables[router_name][router_name] = {"cost": 0, "next_hop": router_name}

    def update(self, router_name, neighbor_name, neighbor_table):
        updated = False
        my_table = self.tables[router_name]

        for dest, entry in neighbor_table.items():
            new_cost = entry["cost"] + 1  # assume cost 1 per hop
            if (dest not in my_table) or (new_cost < my_table[dest]["cost"]):
                my_table[dest] = {"cost": new_cost, "next_hop": neighbor_name}
                updated = True

        return updated

    def get_table(self, router_name):
        return self.tables[router_name]
