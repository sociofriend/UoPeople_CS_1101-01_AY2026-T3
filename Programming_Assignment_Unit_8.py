# Programming Assignment Unit 8
# This program reads a dictionary from a text file, inverts the dictionary,
# and writes the inverted dictionary to another text file. Simple plain-text format is used.
# Includes error handling for missing files and malformed lines.
from logging import exception


# -----------------------------
# Function to read a dictionary from a file
# -----------------------------
def read_dict_from_file(file_name):
    dictionary = {}
    try:
        with open(file_name, 'r') as fin:
            for line in fin:
                line = line.strip()
                if not line:
                    continue  # skip empty lines
                # Ensure the line contains a colon
                if ':' not in line:
                    print(f"Skipping malformed line (no colon found): {line}")
                    continue
                try:
                    # Split only on the first colon
                    key, values_str = line.split(":", 1)
                    key = key.strip()
                    values = [v.strip() for v in values_str.split(",") if v.strip()]
                    if not values:
                        print(f"Skipping line with no values: {line}")
                        continue
                    dictionary[key] = values
                except ValueError:
                    # Catch other split/unpack errors
                    print(f"Skipping malformed line (cannot unpack key and values): {line}")
                    continue
                except Exception as e:
                    print(f"Error: {e}')")
                    continue
        return dictionary
    except FileNotFoundError:
        print(f"Error: File {file_name} not found.")
        return {}
    except Exception as e:
        print(f"Error reading file {file_name}: {e}")
        return {}

# -----------------------------
# Function to invert a dictionary
# -----------------------------
def invert_dict(original_dict):
    inverted_dict = {}
    for key, values in original_dict.items():
        for value in values:
            if value not in inverted_dict:
                inverted_dict[value] = [key]
            else:
                inverted_dict[value].append(key)
    return inverted_dict

# -----------------------------
# Function to write a dictionary to a file
# -----------------------------
def write_dict_to_file(dictionary, file_name):
    try:
        with open(file_name, 'w') as fout:
            fout.write("{\n")
            for key, values in dictionary.items():
                line = f"{key}: {', '.join(values)}\n"
                fout.write(f"    {line}")
            fout.write("}")
        print(f"Inverted dictionary successfully written to {file_name}")
    except Exception as e:
        print(f"Error writing to file {file_name}: {e}")

# -----------------------------
# Main execution
# -----------------------------
def execute():
    file_to_read_from = "Programming_Assignment_Unit_8_read_file.txt"   # Input file with original dictionary
    file_to_write_to = "Programming_Assignment_Unit_8_write_file.txt"   # Output file for inverted dictionary

    # Step 1: Read the original dictionary
    original_dict = read_dict_from_file(file_to_read_from)
    print("Original Dictionary:")
    print(original_dict)

    # Step 2: Invert the dictionary
    inverted_dict = invert_dict(original_dict)
    print("\nInverted Dictionary:")
    print(inverted_dict)

    # Step 3: Write the inverted dictionary to file
    write_dict_to_file(inverted_dict, file_to_write_to)

# Execute the program
if __name__ == "__main__":
    execute()