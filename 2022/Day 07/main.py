from dataclasses import dataclass


# Yeah, I know. They didn't start out the same.
@dataclass
class Directory:
    name: str
    parent: None
    children: list
    size: int = 0
    delete: bool = False


@dataclass
class File:
    name: str
    parent: None
    children: list
    size: int = 0
    delete: bool = False


def build_directories(l):
    root = Directory('/', None, [], 0)
    current_directory = root
    listing = False
    for line in l:
        if line[:4] == '$ cd':
            listing = False
            if '/' in line:
                current_directory = root
            elif '..' in line:
                current_directory = current_directory.parent
            else:
                new_directory = Directory(line[5:], current_directory, [], 0)
                current_directory.children.append(new_directory)
                current_directory = new_directory
        elif line[:4] == '$ ls':
            listing = True
        elif listing:
            if line[:3] == 'dir':
                pass
            else:
                file_size, file_name = line.split(' ')
                current_directory.children.append(File(file_name, current_directory, [], int(file_size)))

    return root


def calculate_directory_size(filesystem):
    if isinstance(filesystem, Directory):
        for child in filesystem.children:
            filesystem.size += calculate_directory_size(child)

    return filesystem.size


def mark_for_deletion(filesystem, threshold):
    if isinstance(filesystem, Directory):
        filesystem.delete = filesystem.size <= threshold
        for child in filesystem.children:
            mark_for_deletion(child, threshold)


def find_delete_options(filesystem, threshold):
    if isinstance(filesystem, Directory):
        if filesystem.size >= threshold:
            delete_options.append(filesystem.size)
        for child in filesystem.children:
            find_delete_options(child, threshold)


def calculate_space_saved(filesystem):
    global space_saved
    for child in filesystem.children:
        if isinstance(child, Directory):
            space_saved += child.size if child.delete else 0
        calculate_space_saved(child)


def print_filesystem(filesystem, level=0):
    if isinstance(filesystem, Directory):
        print(f'{" " * level}- {filesystem.name} (dir, size={filesystem.size}) {"DELETE" if filesystem.delete else ""}')
        for child in filesystem.children:
            print_filesystem(child, level+1)
    elif isinstance(filesystem, File):
        print(f'{" " * level}- {filesystem.name} (file, size={filesystem.size})')


def parse_command_line(l):
    directory_tree = build_directories(l)
    return directory_tree


def open_commands(c):
    with open(c, 'r') as f:
        return [line for line in f.read().split('\n')]


if __name__ == '__main__':
    example_input = './input/example.txt'
    puzzle_input = './input/puzzle_input.txt'

    command_line = open_commands(puzzle_input)

    filesystem = parse_command_line(command_line)
    # print_filesystem(filesystem)

    calculate_directory_size(filesystem)
    mark_for_deletion(filesystem, 100000)
    space_saved = 0
    calculate_space_saved(filesystem)
    print(f'Part 1: {space_saved}')

    free_space = 70000000 - filesystem.size
    space_needed = 30000000 - free_space
    delete_options = []
    find_delete_options(filesystem, space_needed)
    print(f'Part 2: {sorted(delete_options)[0]}')



