# assignment-1
# Rule Engine with AST

## 📜 Overview
This project is a 3-tier rule engine application that determines user eligibility based on attributes like age, department, income, etc. The rule engine uses an *Abstract Syntax Tree (AST)* to represent and evaluate conditional rules.

## 🛠️ Features
- *Dynamic Rule Creation:* Convert rule strings into an AST structure.
- *Rule Evaluation:* Evaluate user data against complex conditions using logical operators like AND/OR.
- *Data Flexibility:* Supports dynamic attributes like age, department, and more.

## 📦 Project Structure
- Node: Class definition to represent the nodes in the AST.
- create_rule(rule_string): Function to build the rule tree from a rule string.
- evaluate_rule(node, data): Function to evaluate the AST against user data.
- *Test Cases*: Sample rule and data to test the functionality.

## 🚀 Getting Started

### Prerequisites
- *Python 3.x* installed on your system.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/sadiyarajgoli/assignments.git
   cd assignments

2. Install any dependencies (none required for basic functionality).



🔧 Usage

1. Create a Rule Tree: The create_rule(rule_string) function builds an Abstract Syntax Tree (AST) from the given rule. Example:

rule_string = "age > 30 AND department = 'Sales'"
rule_tree = create_rule(rule_string)


2. Evaluate a Rule: Use the evaluate_rule(node, data) function to check if user data matches the conditions of the rule:

sample_data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
result = evaluate_rule(rule_tree, sample_data)
print("Evaluation Result:", result)



🧪 Test Cases

The code includes a basic test case to validate the functionality of the rule engine:

rule_string = "age > 30 AND department = 'Sales'"
sample_data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}

rule_tree = create_rule(rule_string)
result = evaluate_rule(rule_tree, sample_data)
print("Evaluation Result:", result)  # Expected output: True



⚙️ Functions Explained

1. Node Class: Represents a node in the AST, which can be an operator or operand.


2. create_rule(rule_string): Converts rule strings into a structured AST.


3. evaluate_rule(node, data): Recursively evaluates the AST against the user data.

