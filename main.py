import os

VERSION = 0.1
# Made for the final project of Code in Place 2024
# By Yoko Ivan - Connect with me on LinkedIn: linkedin.com/in/yokoivan2707

# Function for selection number 1 - to add prefix
def operation_prefix(file_path):
    prefix_to_add = input('Step 3) Type in the prefix you want to add to the beginning to all the files in the selected folder: ')
    keep_existing = input("Step 4) Type 'Y' if you want to add prefix only to files that currently do not have the it, otherwise press any other keys: ")
    all_files = os.listdir(file_path)

    if keep_existing == "Y":
        for file in all_files:
            if file.startswith(prefix_to_add):
                continue
            else:
                old_filepath = os.path.join(file_path, file)
                new_filepath = os.path.join(file_path, prefix_to_add + file)

                os.rename(old_filepath, new_filepath)
                print(f'A file has been renamed and saved: {new_filepath}')
    else:
        for file in all_files:
            old_filepath = os.path.join(file_path, file)
            new_filepath = os.path.join(file_path, prefix_to_add + file)

            os.rename(old_filepath, new_filepath)
            print(f'A file has been renamed and saved: {new_filepath}')

# Function for selection number 2 - to add suffix
def operation_suffix(file_path):
    suffix_to_add = input('Step 3) Type in the suffix you want to add to the end to all the files in the selected folder: ')
    keep_existing = input("Step 4) Type 'Y' if you want to add suffix only to files that currently do not have it, otherwise press any other keys: ")
    all_files = os.listdir(file_path)

    if keep_existing == "Y":
        for file in all_files:
            file_and_extension_list = file.split(".")
            file_name = file_and_extension_list[0]
            extension = file_and_extension_list[1]

            if file_name.endswith(suffix_to_add):
                continue
            else:
                old_filepath = os.path.join(file_path, file)
                new_filepath = os.path.join(file_path, file_name + suffix_to_add + "." + extension)

                os.rename(old_filepath, new_filepath)
                print(f'A file has been renamed and saved: {new_filepath}')
    else:
        for file in all_files:
            file_and_extension_list = file.split(".")
            file_name = file_and_extension_list[0]
            extension = file_and_extension_list[1]
            old_filepath = os.path.join(file_path, file)
            new_filepath = os.path.join(file_path, file_name + suffix_to_add + "." + extension)

            os.rename(old_filepath, new_filepath)
            print(f'A file has been renamed and saved: {new_filepath}')

# Function for selection number 3 - replacement
def operation_replace(file_path):
    to_be_replaced = input('Step 3) Type the exact word / string to be replaced: ')
    replacement = input('Step 4) Type the replacement word / string: ')
    all_files = os.listdir(file_path)

    for file in all_files:
        file_and_extension_list = file.split(".")
        file_name = file_and_extension_list[0]
        extension = file_and_extension_list[1]

        if to_be_replaced in file_name:
            old_filepath = os.path.join(file_path, file)
            
            new_file_name = file_name.replace(to_be_replaced, replacement)
            new_filepath = os.path.join(file_path, new_file_name + "." + extension)

            os.rename(old_filepath, new_filepath)
            print(f'A file has been renamed and saved: {new_filepath}')

        else:
            continue

def main():
    print(f'----------------- Batch File Renaming for Windows ver.{VERSION} -----------------')
    print('>> Use this program to modify file and folder names in batch by inserting prefix, suffix, or replacing a certain word.')
    print('(In just 4 simple steps!!)')
    print('')

    while True: 
        file_path = input('Step 1) Please copy and paste the full folder path where the files are located: ')
        if file_path is None:
            print('Path not entered, please try again.')
            continue

        elif not os.path.exists(file_path):
            print('Invalid path, please provide the full folder path.')
            continue

        else:
            break

    print('Please select your batch operation:')
    print('Enter number 1 to add prefix BEFORE all file names in the folder')
    print('Enter number 2 to add suffix AFTER all file names in the folder')
    print('Enter number 3 to REPLACE certain word from all file names in the folder')
            
    while True:
        file_operation = int(input('Step 2) Please enter 1, 2, or 3: '))
        if file_operation not in [1, 2, 3]:
            print('Invalid operation selected, please try again.')
            continue

        elif file_operation == 1:
            operation_prefix(file_path=file_path)
            print('The prefix addition batch job is complete')
            break

        elif file_operation == 2:
            operation_suffix(file_path=file_path)
            print('The suffix addition batch job is complete')
            break

        elif file_operation == 3:
            operation_replace(file_path=file_path)
            print('The replace batch job is complete')
            break

if __name__ == '__main__':
    main()
