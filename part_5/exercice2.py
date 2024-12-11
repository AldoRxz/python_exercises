class RomanToInteger:
    def __init__(self):
        self.numeral_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def to_integer(self, roman):
        if not isinstance(roman, str):
            raise ValueError("Input must be a Roman numeral string")

        result = 0
        prev_value = 0

        for numeral in reversed(roman):
            value = self.numeral_map.get(numeral, 0)

            if value >= prev_value:
                result += value
            else:
                result -= value

            prev_value = value

        return result


converter = RomanToInteger()
roman_numeral = "MCMLXXXIV"
integer_value = converter.to_integer(roman_numeral)

print(f"The integer value for the Roman numeral {roman_numeral} is: {integer_value}")
