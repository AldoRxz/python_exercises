class PowerCalculator:
    def calculate_power(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n

        result = 1.0
        current_power = x

        while n > 0:
            if n % 2 == 1:
                result *= current_power
            current_power *= current_power
            n //= 2

        return result


power_calculator = PowerCalculator()

# Casos de prueba
input_x1, input_n1 = 2, -3
output_result1 = power_calculator.calculate_power(input_x1, input_n1)

input_x2, input_n2 = 3, 5
output_result2 = power_calculator.calculate_power(input_x2, input_n2)

print(f"Entrada: pow({input_x1}, {input_n1})")
print(f"Salida: {output_result1}")

print(f"Entrada: pow({input_x2}, {input_n2})")
print(f"Salida: {output_result2}")
