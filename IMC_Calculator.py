def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal (IMC) utilizando la fórmula:
    IMC = peso / (altura^2)
    """
    imc = peso / (altura ** 2)
    return imc

def clasificar_imc(imc):
    """
    Clasifica el IMC en diferentes categorías según la OMS.
    """
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidad grado I"
    elif 35 <= imc < 39.9:
        return "Obesidad grado II"
    else:
        return "Obesidad grado III"

def main():
    print("Calculadora de Índice de Masa Corporal (IMC)")
    
    # Solicitar al usuario su peso y altura
    try:
        peso = float(input("Ingresa tu peso en kilogramos: "))
        altura = float(input("Ingresa tu altura en metros: "))
        
        # Calcular el IMC
        imc = calcular_imc(peso, altura)
        
        # Clasificar el IMC
        clasificacion = clasificar_imc(imc)
        
        # Mostrar el resultado
        print(f"\nTu IMC es: {imc:.2f}")
        print(f"Clasificación: {clasificacion}")
    
    except ValueError:
        print("Por favor, ingresa valores numéricos válidos.")

if __name__ == "__main__":
    main()