#Exercise 5: More Variables and Printing

my_name = 'Zed A. Shaw'
my_age = 35
my_height = 74    #inches
my_weight = 180    #lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")

my_height = my_height * 2.54    #changing inches to centimetres
my_weight = my_weight * 0.453    #changing pounds to kilograms

print(f"His height in centimetres is {my_height}.")
print(f"His weight in kilograms is {my_weight}.")
