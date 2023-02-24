def check_speed(velocity):
    if velocity <= 50:
        print("Speed allowed")
    else:
        print("Not allowed speed")

if __name__ == "__main__":
    vel = float(input("Current speed: "))
    check_speed(vel)