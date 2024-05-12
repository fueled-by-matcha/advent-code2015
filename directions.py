# this function translates coordinates into directions
def directions(coordinates):
    # variable to track the floor Santa goes to
    counter = 0

    # iterate through coordinates to either add or subtract a floor.  Skips any invalid characters
    for step in range(0, len(coordinates)):
        if coordinates[step] == '(':
            counter += 1
        elif coordinates[step] == ')':
            counter -= 1
        else:
            continue

    # return the floor Santa is on    
    return counter

# collect coordinates from user
coordinates = input("Please enter coordinates for Santa (must be in the form of ( or )): ")

# check to make sure that coordinates are being passed and not blank characters
if len(coordinates) <= 0:
    check  = False
    while not check:
        print("Please enter valid coordinates for Santa.")
        coordinates = input("Please enter coordinates for Santa: ")
        if len(coordinates) >= 1:
            break

# call directions function to translate coordinates        
santaFloor = directions(coordinates)

# print results for user
print(f"Santa went to floor {santaFloor} to deliver food")