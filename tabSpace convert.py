# Specify the path to your dataset file and the path for the modified file
dataset_file = "dataset.txt"
modified_dataset_file = "newdataset.txt"

try:
    # Open the original dataset file for reading
    with open(dataset_file, 'r') as original_file:
        # Read the content of the original file
        data = original_file.read()

        # Replace tab spaces with "#" in the data
        modified_data = data.replace('\t', '#')

    # Open the modified file for writing
    with open(modified_dataset_file, 'w') as modified_file:
        # Write the modified data to the new file
        modified_file.write(modified_data)

    print("Tabs have been replaced with '#' and saved to", modified_dataset_file)

except FileNotFoundError:
    print(f"Error: The file '{dataset_file}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
