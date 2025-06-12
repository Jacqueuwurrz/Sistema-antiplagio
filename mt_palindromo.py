import time

class TuringMachinePython:
    def __init__(self, tape):
        self.tape = list(tape) + ['_']  # Cinta con blanco al final
        self.head_pos = 0
        self.state = 'q0'
        self.running = True

        # Reglas para detectar palíndromos sobre {a, b}
        self.rules = {
            # Buscar el primer símbolo
            ('q0', 'a'): ('q1', '_', 'R'),
            ('q0', 'b'): ('q2', '_', 'R'),
            ('q0', '_'): ('q_accept', '_', 'S'),

            # Estado q1: buscar la última 'a'
            ('q1', 'a'): ('q1', 'a', 'R'),
            ('q1', 'b'): ('q1', 'b', 'R'),
            ('q1', '_'): ('q3', '_', 'L'),

            # Estado q2: buscar la última 'b'
            ('q2', 'a'): ('q2', 'a', 'R'),
            ('q2', 'b'): ('q2', 'b', 'R'),
            ('q2', '_'): ('q4', '_', 'L'),

            # Estado q3: comprobación final de 'a'
            ('q3', 'a'): ('q5', '_', 'L'),
            ('q3', '_'): ('q_accept', '_', 'S'),  # palíndromo impar

            # Estado q4: comprobación final de 'b'
            ('q4', 'b'): ('q5', '_', 'L'),
            ('q4', '_'): ('q_accept', '_', 'S'),

            # Estado q5: volver al principio
            ('q5', 'a'): ('q5', 'a', 'L'),
            ('q5', 'b'): ('q5', 'b', 'L'),
            ('q5', '_'): ('q0', '_', 'R'),
        }

    def step(self):
        symbol = self.tape[self.head_pos]
        key = (self.state, symbol)

        if key in self.rules:
            new_state, new_symbol, direction = self.rules[key]
            self.tape[self.head_pos] = new_symbol
            self.state = new_state

            if direction == 'R':
                self.head_pos += 1
            elif direction == 'L':
                self.head_pos -= 1

            self.display()
            time.sleep(0.5)
        else:
            self.running = False
            print("❌ Máquina detenida sin transición válida.")

    def run(self):
        while self.running and self.state != 'q_accept':
            self.step()

        if self.state == 'q_accept':
            print("✅ ¡La cadena es un palíndromo!")
        else:
            print("❌ La cadena NO es un palíndromo.")

    def display(self):
        print("Estado:", self.state)
        print("Cinta :", ''.join(self.tape))
        print("        " + " " * self.head_pos + "^")  # Marca la cabeza
        print("-" * 40)


# 🔽 Cambia aquí tu cadena
entrada = input("Ingresa una cadena con a y b: ")
mt = TuringMachinePython(entrada)
mt.run()
