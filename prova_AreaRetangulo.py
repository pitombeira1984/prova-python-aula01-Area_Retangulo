def area_retangulo(base, altura):
    area = base * altura
    return area

# Get user input
b = float(input('Informe a base do Retangulo: '))
h = float(input('Informe a altura do Retangulo: '))

# Calculate the area by calling the function
resultado = area_retangulo(b, h)

# Print the result
print(f'A area do Retangulo = {resultado} m²')
