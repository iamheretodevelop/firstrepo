import matplotlib.pyplot as plt
import numpy as np
import math

# setting constant value for acceleration due to gravity
A = 9.81
# since air drag force F=C*velocity^2 where C is constant and for certain body setting it to below value
C = 0.00322


def main():
    # asking for user inputs
    n_projectile = input("Enter the no. of projectiles to launch(max.3).")
    while n_projectile != "3" and n_projectile != "1" and n_projectile != "2":
        print("Invalid input")
        n_projectile = input("Enter the no. of projectiles to launch(max.3). ")
    n_projectile = int(n_projectile)
    if n_projectile == 1:
        int_velocity = float(input("Enter the launch velocity. "))
        theta = float(input("Enter the launch angle in degrees. "))
        theta = (theta * math.pi) / 180
    elif n_projectile == 2 or n_projectile == 3:
        int_velocity = float(input("Enter the launch velocity for 1st projectile. "))
        theta = float(input("Enter the launch angle in degrees for 1st projectile. "))
        theta = (theta * math.pi) / 180
        int_velocity2 = float(input("Enter the launch velocity for 2nd projectile. "))
        theta2 = float(input("Enter the launch angle in degrees for 2nd projectile. "))
        theta2 = (theta2 * math.pi) / 180
        if n_projectile == 3:
            int_velocity3 = float(input("Enter the launch velocity for 3rd projectile. "))
            theta3 = float(input("Enter the launch angle in degrees for 3rd projectile. "))
            theta3 = (theta3 * math.pi) / 180
    # the above commands takes input as per requirement.

    # getting coordinate list for plotting
    if n_projectile == 1:
        x, y, t = show_ideal_curve(int_velocity, theta)
        x_co, y_co, td = show_curve_under_drag(int_velocity, theta)
    elif n_projectile == 2 or n_projectile == 3:
        x, y, t = show_ideal_curve(int_velocity, theta)
        x_co, y_co, td = show_curve_under_drag(int_velocity, theta)
        x2, y2, t2 = show_ideal_curve(int_velocity2, theta2)
        x_co2, y_co2, td2 = show_curve_under_drag(int_velocity2, theta2)
        if n_projectile == 3:
            x3, y3, t3 = show_ideal_curve(int_velocity3, theta3)
            x_co3, y_co3, td3 = show_curve_under_drag(int_velocity3, theta3)
    # the above commands get list of coordinates from the function below

    # the command below prints the details of projectile including time of flight, horizontal range and max. vertical
    # height
    if n_projectile == 1:
        print("Under ideal condition: ")
        print(" Horizontal range= ", max(x))
        print(" Max. Vertical height= ", max(y))
        print(" Time of flight= ", t)
        print("Under effect of air drag:")
        print(" Horizontal range= ", max(x_co))
        print(" Max. Vertical height= ", max(y_co))
        print(" Time of flight= ", td)
    elif n_projectile == 2 or n_projectile == 3:
        print("For 1st projectile:")
        print(" Under ideal condition: ")
        print("     Horizontal range= ", max(x))
        print("     Max. Vertical height= ", max(y))
        print("     Time of flight= ", t)
        print("Under effect of air drag: ")
        print("     Horizontal range= ", max(x_co))
        print("     Max. Vertical height= ", max(y_co))
        print("     Time of flight= ", td)
        print("For 2nd projectile:")
        print(" Under ideal condition: ")
        print("     Horizontal range= ", max(x2))
        print("     Max. Vertical height= ", max(y2))
        print("     Time of flight= ", t2)
        print(" Under effect of air drag: ")
        print("     Horizontal range= ", max(x_co2))
        print("     Max. Vertical height= ", max(y_co2))
        print("     Time of flight= ", td2)
        if n_projectile == 3:
            print("For 3rd projectile:")
            print(" Under ideal condition: ")
            print("     Horizontal range= ", max(x3))
            print("     Max. Vertical height= ", max(y3))
            print("     Time of flight= ", t3)
            print(" Under effect of air drag: ")
            print("     Horizontal range= ", max(x_co3))
            print("     Max. Vertical height= ", max(y_co3))
            print("     Time of flight= ", td3)

    # plotting the obtained coordinate list
    if n_projectile == 1:
        plt.plot(x, y, 'b-', label='Ideal Trajectory')
        plt.plot(x_co, y_co, 'b:', label="Drag Trajectory")
    elif n_projectile == 2 or n_projectile == 3:
        plt.plot(x, y, 'b-', label='Ideal Trajectory(1st Projectile)')
        plt.plot(x_co, y_co, 'b:', label="Drag Trajectory(1st Projectile)")
        plt.plot(x2, y2, 'r-', label='Ideal Trajectory(2nd Projectile)')
        plt.plot(x_co2, y_co2, 'r:', label="Drag Trajectory(2nd Projectile)")
        if n_projectile == 3:
            plt.plot(x3, y3, 'g-', label='Ideal Trajectory(3rd Projectile)')
            plt.plot(x_co3, y_co3, 'g:', label="Drag Trajectory(3rd Projectile)")
    plt.title('Projectile Trajectory')
    plt.xlabel('X-displacement(in meters)')
    plt.ylabel('Y- displacement(in meters)')
    plt.legend()
    plt.show()
    # the above command plots the graph


def show_curve_under_drag(int_velocity, theta):
    # time reference
    time = np.linspace(0, 100, 1000000)
    dt = time[1] - time[0]
    # resolving velocity into horizontal velocity
    v_x = int_velocity * math.cos(theta)
    # resolving velocity into vertical velocity
    v_y = int_velocity * math.sin(theta)
    # creating list of horizontal coordinates
    x_co_list = []
    y_co_list = []
    x = v_x * dt
    y = v_y * dt
    x_co_list.append(x)
    y_co_list.append(y)
    t = dt
    while y > 0:
        v_x = v_x - C * (v_x ** 2) * dt
        x = x + v_x * dt
        x_co_list.append(x)
        v_y = v_y - C * (v_y ** 2) * dt - A * dt
        y = y + v_y * dt
        y_co_list.append(y)
        t = t + dt
    return x_co_list, y_co_list, t


def show_ideal_curve(int_velocity, theta):
    # time reference
    time = np.linspace(0, 1000, 1000000)
    dt = time[1] - time[0]
    # resolving velocity into horizontal velocity
    v_x = int_velocity * math.cos(theta)
    # resolving velocity into vertical velocity
    v_y = int_velocity * math.sin(theta)
    # creating list of horizontal coordinates
    x_co_list = []
    y_co_list = []
    x = v_x * dt
    y = v_y * dt
    x_co_list.append(x)
    y_co_list.append(y)
    t = dt
    while y > 0:
        v_x = v_x
        x = x + v_x * dt
        x_co_list.append(x)
        v_y = v_y - A * dt
        y = y + v_y * dt
        y_co_list.append(y)
        t = t + dt
    return x_co_list, y_co_list, t


if __name__ == '__main__':
    main()