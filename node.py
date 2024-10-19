class Node:
    def __init__(self, type, operator=None, left=None, right=None, value=None):
        self.type = type          # "operator" or "operand"
        self.operator = operator  # "AND", "OR", ">", "<", "==", "!="
        self.left = left          # Left child Node
        self.right = right        # Right child Node
        self.value = value        # (attribute_name, value)

    def __repr__(self):
        return f"Node(type='{self.type}', operator='{self.operator}', value={self.value})"