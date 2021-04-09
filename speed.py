# speed calculator, gabriel maurer, april 09, 2021, 1:43pm v0.0

keep_going = "yes"

while keep_going == "yes" or keep_going == "yes":

    distance = float(input("please enter the distance and press enter.\n"))
    time = float(input("please enterthe time and press enter.\n"))

    speed = distance / time

    print(f"using the distance of {distance} meters {time} the speed is {speed} m/s. \n")

    keep_going = input("want to go?")