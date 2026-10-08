# Write a Python program to display action based on traffic light color:
# - Red: Stop
# - Yellow: Wait
# - Green: Go

traffic_light = input("Enter the traffic light color (Red/Yellow/Green): ").lower()

if traffic_light == "red":
    print("Stop")
elif traffic_light == "yellow":
    print("Wait")
elif traffic_light == "green":
    print("Go")