
class Node:
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent
        self.children = []
    running_total = 0
    
    def get_child(self, name):
        for i in range(len(self.children)):
            if self.children[i].name == name:
                return self.children[i]

        return None

    def print(self, depth):
        print((depth * '    - ') + self.name + ' (' + str(self.size) + ')')

        for child in self.children:
            child.print(depth+1)

    def get_total_size_below(self, nodes_to_delete):
        total_size = 0
        for child in self.children:
            if child.size > 0:
                total_size += child.size
            else:
                total_size += child.get_total_size_below(nodes_to_delete)
        
        if (total_size <= 100000): nodes_to_delete.append(total_size)
        return total_size

    def get_total_size_above(self, nodes_to_delete, amount_above):
        total_size = 0
        for child in self.children:
            if child.size > 0:
                total_size += child.size
            else:
                total_size += child.get_total_size_above(nodes_to_delete, amount_above)
        
        if (total_size >= amount_above): nodes_to_delete.append(total_size)
        return total_size

def part_one():
    input_file = open('input.txt', 'r')
    lines = input_file.readlines()

    root_node = Node('/', 0, None)
    current_node = root_node

    for line in lines:
        if line.strip() == '$ cd /':
            current_node = root_node
        elif line.strip() == '$ cd ..':
            if current_node.parent != None:
                current_node = current_node.parent
        elif line.strip().startswith('$ cd'):
            directory_name = line.strip().split(' ')[2]
            target_child = current_node.get_child(directory_name)
            if target_child != None:
                current_node = target_child
            else:
                new_node = Node(directory_name, 0, current_node)
                current_node.children.append(new_node)
                current_node = new_node
        elif line.strip() == '$ ls':
            continue
        elif line.startswith('dir'):
            directory_name = line.strip().split(' ')[1]
            target_child = current_node.get_child(directory_name)

            if target_child == None:
                new_node = Node(directory_name, 0, current_node)
                current_node.children.append(new_node)
        else:
            file_size = line.strip().split(' ')[0]
            file_name = line.strip().split(' ')[1]
            target_child = current_node.get_child(file_name)
            if target_child == None:
                new_node = Node(file_name, int(file_size), current_node)
                current_node.children.append(new_node)

    nodes_to_delete = []
    root_node.print(0)
    root_node.get_total_size_below(nodes_to_delete)

    print('part one: ' + str(sum(nodes_to_delete)))

def part_two():
    input_file = open('input.txt', 'r')
    lines = input_file.readlines()

    root_node = Node('/', 0, None)
    current_node = root_node

    for line in lines:
        if line.strip() == '$ cd /':
            current_node = root_node
        elif line.strip() == '$ cd ..':
            if current_node.parent != None:
                current_node = current_node.parent
        elif line.strip().startswith('$ cd'):
            directory_name = line.strip().split(' ')[2]
            target_child = current_node.get_child(directory_name)
            if target_child != None:
                current_node = target_child
            else:
                new_node = Node(directory_name, 0, current_node)
                current_node.children.append(new_node)
                current_node = new_node
        elif line.strip() == '$ ls':
            continue
        elif line.startswith('dir'):
            directory_name = line.strip().split(' ')[1]
            target_child = current_node.get_child(directory_name)

            if target_child == None:
                new_node = Node(directory_name, 0, current_node)
                current_node.children.append(new_node)
        else:
            file_size = line.strip().split(' ')[0]
            file_name = line.strip().split(' ')[1]
            target_child = current_node.get_child(file_name)
            if target_child == None:
                new_node = Node(file_name, int(file_size), current_node)
                current_node.children.append(new_node)

    root_node.print(0)
    currently_used = root_node.get_total_size_below([])

    file_system_size = 70000000
    needed_space = 30000000
    left = file_system_size - currently_used
    actual_needed = needed_space - left
    print(actual_needed)

    nodes_to_delete = []
    root_node.print(0)
    currently_used = root_node.get_total_size_above(nodes_to_delete, actual_needed)
    nodes_to_delete.sort()

    print('part two: ' + str(nodes_to_delete[0]))

#part_one()
part_two()