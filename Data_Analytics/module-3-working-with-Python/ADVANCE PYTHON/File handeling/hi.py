import subprocess

# Get all saved WiFi profile names
profiles = subprocess.check_output(
    "netsh wlan show profiles",
    shell=True
).decode()

# Extract profile names
names = [
    line.split(":")[1].strip()
    for line in profiles.split("\n")
    if "All User Profile" in line
]

# Display available WiFi profiles
for i, n in enumerate(names, 1):
    print(f"[{i}] {n}")

# Ask the user to choose a profile
ch = int(input("\nChoose WiFi number: "))
wifi = names[ch - 1]

# Show the selected WiFi profile including the password
result = subprocess.check_output(
    f'netsh wlan show profile "{wifi}" key=clear',
    shell=True
).decode()

print("\n" + result)