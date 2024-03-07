''' **********************************************************
Importing Libraries
***********************************************************'''
import os

''' **********************************************************
Defining Functions
***********************************************************'''

# Function to find files within a defined path location

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       files_system[0] found results as a text
       files_system[1] found results as a list
    """

    # Initializing the list to store the found paths
    if 'files_system' not in locals():
        files_system = ' '

    # Exploring the selected path locations
    if type(path) is list:
        if (len(path) > 1):
            path[-1] = os.path.join('\\'.join(path[0].split('\\')[:-1]), path[-1])

        # Adding files to the found results
        if os.path.isfile(path[-1]):
            if (suffix is None) or (suffix == path[-1][-len(suffix):]):
                files_system += ' '+path[-1]
                
            if len(path) == 1:
                return files_system, files_system.split()
            else:
                path = path[:-1]
                tmp = find_files(suffix, path[0])[0]
                if (suffix is None) or (suffix == tmp[-len(suffix):]):
                    files_system += ' '+tmp

        # Adding folders to the found results
        if os.path.isdir(path[0]):
            if len(path) == 1:
                tmp = find_files(suffix, path[0])[0]
                if (suffix is None) or (suffix == tmp[-len(suffix):]):
                    files_system += ' '+tmp
                    return files_system, files_system.split()
            elif (len(path) > 1):
                path[1] = os.path.join('\\'.join(path[0].split('\\')[:-1]), path[1])
                path = path[1:]
                tmp = find_files(suffix, path)[0]
                if (suffix is None) or (suffix == tmp[-len(suffix):]):
                    files_system += ' '+tmp

    # Starting recursion
    elif type(path) is str:
        path = [path]
        if (suffix is None) or (suffix == path[0][-len(suffix):]):
            files_system += ' '+path[0]
    
    # Starting exploring levels found within the selected location
    if len(path) > 0:
        if os.path.isdir(path[0]):
            if (suffix is None) or (suffix == path[0][-1]):
                files_system += ' '+path[0]
            new_content = os.listdir(path[0])
            new_content[0] = os.path.join(path[0], new_content[0])
            tmp = find_files(suffix, new_content)[0]
            if (suffix is None) or (suffix == tmp[-len(suffix):]):
                files_system += ' '+tmp
            # Removing duplicates and formmating the found results
            files_system = list(set(files_system.split()))
            files_system.sort()
            files_system = ' '.join(files_system)
            
        return files_system, files_system.split()

# Main function to test this code

def main():

    print('''\n ---------------- UDACITY TEST ---------------- \n''')

    path = os.path.join(os.getcwd(),'DirExample_Problem2', 'testdir')
    print('''Search of paths within folder:\n{}'''.format(path))

    print('''\n ---------------- TEST CASE 1 ---------------- \n''')

    suffix = None
    print('Displaying all paths within the selected folder: \n')

    Results = find_files(suffix, path)
    [print(res) for res in Results[1]]


    print('''\n ---------------- TEST CASE 2 ---------------- \n''')

    suffix = '.c'
    print('''Displaying {} files paths within the selected folder: \n'''.format(suffix))

    path = os.path.join(os.getcwd())

    Results = find_files(suffix, path)
    [print(res) for res in Results[1]]


    print('''\n ---------------- TEST CASE 3 ---------------- \n''')

    suffix = '.gitkeep'
    print('''Displaying {} files paths within the selected folder: \n'''.format(suffix))

    Results = find_files(suffix, path)
    [print(res) for res in Results[1]]


''' **********************************************************
Running Code - Main
***********************************************************'''

if __name__ == "__main__":
    main()

''' **********************************************************
END
***********************************************************'''
