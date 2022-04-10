class Gate:
    def __init__(self,gate_id) -> None:
        self.gate_id = gate_id


class Entrance(Gate):
    def __init__(self, gate_id) -> None:
        super().__init__(gate_id)

class Exit(Gate):
    def __init__(self, gate_id) -> None:
        super().__init__(gate_id)