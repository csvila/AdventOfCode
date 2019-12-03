from math import floor

def  fuel_rocket_calc():
    f = open('../input/input_dia1.txt')
    fuel_by_module = []
    for mass in f:
        fuel = calc_fuel(mass)
        fuel_by_module.append(fuel)
    return fuel_by_module

def fuel4fuelmass(rocket_fuel):
    sum_fuel = 0
    for fuel in rocket_fuel:
        new_fuel = fuel
        while True:
            new_fuel = calc_fuel(new_fuel)
            if new_fuel > 0:
                sum_fuel += new_fuel
            else:
                break
    return sum_fuel


def calc_fuel(mass):
    return floor(int(mass)/3) - 2

fuel_array = fuel_rocket_calc()
rocket_fuel = sum(fuel_array)
fuel_fuel = fuel4fuelmass(fuel_array)

print(f"Fuel 4 Modules: {rocket_fuel} \nFuel 4 Fuel: {fuel_fuel}\nFULL: {rocket_fuel + fuel_fuel}")