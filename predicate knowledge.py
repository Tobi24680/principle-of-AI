
class KnowledgeBase:
    def __init__(self):
            self.facts = []
    def add_fact(self, fact):
            self.facts.append(fact)
    def remove_fact(self, fact):
            self.facts.remove(fact)
    def check_fact(self, fact):
            return fact in self.facts
    def display_facts(self):
            print('Facts in Knowledge Base:')
            for fact in self.facts:
                print(fact)
    def to_first_order_logic(self):
            first_order_logic_facts = []
            for fact in self.facts:
                words = fact.split()
                if len(words) >= 3 and words[1] in ['is', 'are']:
                    subject = words[0]
                    predicate = words[1]
                    objects = words[2:]
                    if len(objects) == 1:
                        first_order_logic = f"{predicate}({subject} {objects[0]})"
                    else:
                        first_order_logic = f"{predicate}({subject} {''.join(objects)})"
                    first_order_logic_facts.append(first_order_logic)
            return first_order_logic_facts

kb = KnowledgeBase()
print('Enter facts line by line:')
while True:
    fact_str = input('Enter a fact: ')
    if fact_str.lower() == 'q':
        break
    kb.add_fact(fact_str)

check_fact_str = input('Enter fact to check: ')
if kb.check_fact(check_fact_str):
    print(f"'{check_fact_str}' is a fact in Knowledge Base")
else:
    print('Not found')
kb.display_facts()
first_order_logic_facts = kb.to_first_order_logic()
print('\nFacts in First Order Logic:')
for fact in first_order_logic_facts:
    print(fact)