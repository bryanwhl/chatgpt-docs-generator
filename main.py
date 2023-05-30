import os

TEST_DIR = ''

def traverse_folder(parent_dir):
    for filename in os.listdir(parent_dir):
        f = os.path.join(parent_dir, filename)
        if os.path.isfile(f):
            # Print file name
            print(f)
        elif os.path.isdir(f):
            # Traverse through subfolder
            traverse_folder(f)

def main():
    
    # Traverse through folder of the directory
    traverse_folder(TEST_DIR)


if __name__ == '__main__':
    main()