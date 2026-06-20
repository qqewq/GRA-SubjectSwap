class Policy:
    def __init__(self, mapping):
        # mapping: id -> {subjectivity, role, allowed, forbidden, required}
        self.mapping = mapping

    def get_subjectivity(self, id):
        return self.mapping[id]["subjectivity"]

    def allowed(self, id):
        return self.mapping[id].get("allowed", [])

    def forbidden(self, id):
        return self.mapping[id].get("forbidden", [])

    def required(self, id):
        return self.mapping[id].get("required", [])

    def swap(self):
        new_mapping = {}
        for id, props in self.mapping.items():
            new_props = props.copy()
            new_props["subjectivity"] = "instrument" if props["subjectivity"] == "subject" else "subject"
            new_props["role"] = "previous_instrument" if props["role"] == "leader" else "leader"  # пример
            new_mapping[id] = new_props
        return Policy(new_mapping)
