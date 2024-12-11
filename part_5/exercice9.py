class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def get_string(self):
        self.input_string = input("Ingresa una cadena: ")

    def print_string(self):
        print("Cadena en mayúsculas:", self.input_string.upper())

# Ejemplo de uso
manipulator = StringManipulator()
manipulator.get_string()
manipulator.print_string()
