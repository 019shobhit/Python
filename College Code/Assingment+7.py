class Constant:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return self.name

class Variable:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return self.name

class Predicate:
    def __init__(self, name, *args):
        self.name = name
        self.arguments = args  # Arguments can be constants or variables
    
    def __repr__(self):
        args = ", ".join(map(str, self.arguments))
        return f"{self.name}({args})"

class Not:
    def __init__(self, operand):
        self.operand = operand

    def __repr__(self):
        return f"¬({self.operand})"

class And:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.left} ∧ {self.right})"

class Or:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.left} ∨ {self.right})"

class Implies:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.left} → {self.right})"

class ForAll:
    def __init__(self, variable, expression):
        self.variable = variable
        self.expression = expression

    def __repr__(self):
        return f"∀{self.variable}.({self.expression})"

class Exists:
    def __init__(self, variable, expression):
        self.variable = variable
        self.expression = expression

    def __repr__(self):
        return f"∃{self.variable}.({self.expression})"



class KnowledgeBase:
    def __init__(self):
        self.facts = []

    def add_fact(self, fact):
        self.facts.append(fact)
    
    def query(self, expr):
        return self.evaluate(expr)

    def evaluate(self, expr):
        if isinstance(expr, Predicate):
            return expr in self.facts
        elif isinstance(expr, Not):
            return not self.evaluate(expr.operand)
        elif isinstance(expr, And):
            return self.evaluate(expr.left) and self.evaluate(expr.right)
        elif isinstance(expr, Or):
            return self.evaluate(expr.left) or self.evaluate(expr.right)
        elif isinstance(expr, Implies):
            return not self.evaluate(expr.left) or self.evaluate(expr.right)
        elif isinstance(expr, ForAll) or isinstance(expr, Exists):
            # Naive handling for demonstration purposes
            # Real implementations need quantifier handling with variable bindings.
            return False  # Placeholder; quantifier evaluation is complex
        else:
            raise ValueError("Unknown expression type.")



# Create constants and predicates
john = Constant("John")
mary = Constant("Mary")
likes = Predicate("Likes", john, mary)

# Initialize knowledge base and add facts
kb = KnowledgeBase()
kb.add_fact(likes)  # John likes Mary

# Querying facts
print(kb.query(likes))           # Output: True
print(kb.query(Not(likes)))      # Output: False

# Complex expressions
expr1 = And(likes, Not(Predicate("Likes", mary, john)))
print(kb.query(expr1))           # Output: True

# Quantifiers would need a more advanced handling.
