def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        
        bmi = calculate_bmi(weight, height)
        print(f"Your BMI is: {bmi:.2f}")
        
        category = get_bmi_category(bmi)
        print(f"You are in the category of: {category}")
    
    except ValueError:
        print("Invalid input. Please enter valid numerical values for weight and height.")

if __name__ == "__main__":
    main()