user_prompt = input("What formula would you like to use? (Time, Velocity, Length) ")

def length_formula():
    time = float(input("Δt: "))
    velocity = float(input("v: "))
    length = time * velocity
    return f"Δx = {length}"


def time_formula():
    length = float(input("Δx: "))
    velocity = float(input("v: "))
    time = length / velocity
    return f"Δt = {time}"

def velocity_formula():
    time = float(input("Δt: "))
    length = float(input("Δx: ")) 
    velocity = length / time
    return f"v = {velocity}"

if user_prompt.lower() == 'time': print(time_formula())
elif user_prompt.lower() == 'velocity': print(velocity_formula())
elif user_prompt.lower() == 'length': print(length_formula())
else:
    while user_prompt.lower() not in ('time', 'velocity', 'length'):
        user_prompt = input("What..? We can't calculate this, Please Enter again: Time, Velocity or Length.")
        if user_prompt.lower() == 'time': print(time_formula())
        elif user_prompt.lower() == 'velocity': print(velocity_formula())
        elif user_prompt.lower() == 'length': print(length_formula())
