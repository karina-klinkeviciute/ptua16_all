def calculate_bmi(height, weight):
    return weight / (height**2)

height = float(input("Įveskite ūgį metrais: "))
weight = float(input("Įveskite svorį kilogramais: "))
bmi = calculate_bmi(height, weight)
print(f"KMI yra {bmi:.2f}.")

# Github