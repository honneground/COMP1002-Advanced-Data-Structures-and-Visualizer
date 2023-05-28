import os


def teardown():

    # Get the current working directory
    folder_path = os.getcwd()

    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Iterate over each file
    for file in files:
        if file.endswith('.png'):
            file_path = os.path.join(folder_path, file)
            os.remove(file_path)
            print(f"Deleted: {file}")

    print("PNG files in the current folder deleted successfully.")
    os.remove("outfile.csv")
    print("CSV files in the current folder deleted successfully.")

if __name__ == "__main__":
    teardown()