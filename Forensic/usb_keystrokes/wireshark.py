# Open the flag.txt file and process its content
with open("flag.txt", "r") as file:
    lines = file.readlines()

# Iterate through the lines and extract HID Data values
hid_data_values = []
for line in lines:
    if "HID Data:" in line:
        # Extract the value after "HID Data:"
        value = line.split("HID Data:")[1].strip()
        # Add a colon after every 2 characters
        formatted_value = ":".join(value[i:i+2] for i in range(0, len(value), 2))
        hid_data_values.append(formatted_value)

# Save the formatted values to keyboard.txt
with open("keyboard.txt", "w") as output_file:
    for value in hid_data_values:
        output_file.write(value + "\n")