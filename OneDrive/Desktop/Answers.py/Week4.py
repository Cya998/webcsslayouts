def file_manager(file_name):
    try:
        # Read the file content
        with open(file_name, 'r') as infile:
            content = infile.readlines()

        # Create a new file name (adds "_numbered" before .txt)
        file_name_numbered = file_name.replace(".txt", "_numbered.txt")

        # Write modified content
        with open(file_name_numbered, 'w') as outfile:
            for i, line in enumerate(content, start=1):
                outfile.write(f"{i}: {line}")
                
        print(f"Modified file saved as '{file_name_numbered}'")
        return content

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except IOError:
        print(f"Error: Could not read the file '{file_name}'.")

file_name = input("Enter the name of the text file (with .txt extension): ")
file_manager(file_name)


