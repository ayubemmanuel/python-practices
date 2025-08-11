# File Read & Write Challenge with Error Handling

def modify_content(text):
    """Example modification: convert text to uppercase."""
    return text.upper()

def main():
    # Ask the user for the input filename
    filename = input("Enter the name of the file to read: ")

    try:
        # Try to open and read the file
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return
    except PermissionError:
        print(f"Error: You don't have permission to read '{filename}'.")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

    # Modify the content
    modified_content = modify_content(content)

    # Create a new filename for the modified file
    new_filename = "modified_" + filename

    try:
        # Write the modified content to the new file
        with open(new_filename, "w", encoding="utf-8") as new_file:
            new_file.write(modified_content)

        print(f"Modified file saved as '{new_filename}'.")

    except Exception as e:
        print(f"Error writing to '{new_filename}': {e}")

if __name__ == "__main__":
    main()
