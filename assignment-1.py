# Node class definition
class Node:
    def __init__(self, node_type, value=None):  # Corrected constructor
        self.type = node_type  # 'operator' or 'operand'
        self.left = None
        self.right = None
        self.value = value  # value like 'age > 30' if it's an operand

# Function to create the rule tree (AST)
def create_rule(rule_string):
    tokens = rule_string.replace('(', '').replace(')', '').split()
    root = None
    current_node = None
    
    for token in tokens:
        if token in ['AND', 'OR']:
            operator_node = Node('operator', token)
            if root is None:
                root = operator_node
                current_node = root
            else:
                operator_node.left = current_node
                current_node = operator_node
        else:
            operand_node = Node('operand', token)
            if current_node is not None:
                current_node.right = operand_node
            else:
                current_node = operand_node
    
    return root  # Make sure this is outside the loop


def evaluate_rule(node, data):
    if node is None:  # Check if the node exists
        return False  # Or handle this case as you prefer
    
    if node.type == 'operand':
        field, operator, value = node.value.split()
        value = int(value) if value.isdigit() else value.strip("'")
        return eval(f"{data[field]} {operator} {value}")

    elif node.type == 'operator':
        if node.value == 'AND':
            return evaluate_rule(node.left, data) and evaluate_rule(node.right, data)
        elif node.value == 'OR':
            return evaluate_rule(node.left, data) or evaluate_rule(node.right, data)
        
# Test Case
rule_string = "age > 30 AND department = 'Sales'"
sample_data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}

# Build the rule tree
rule_tree = create_rule(rule_string)

print(f"Rule Tree Root: {rule_tree}")

# Evaluate the rule
result = evaluate_rule(rule_tree, sample_data)
print("Evaluation Result:", result)  # Should print True if the rule matches the data