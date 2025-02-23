# Tower of Hanoi
# The Tower of Hanoi is a mathematical puzzle where we have three rods and n disks.
# The disks are stacked in ascending order of size on one rod, the smallest at the top.
# The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
# 1. Only one disk can be moved at a time.
# 2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack.
# 3. No disk may be placed on top of a smaller disk.

# The Tower of Hanoi solved using iteration.

NUMBER_OF_DISKS_ITERATIVE = 4
number_of_moves = 2 ** NUMBER_OF_DISKS_ITERATIVE - 1
rods = {
    'A': list(range(NUMBER_OF_DISKS_ITERATIVE, 0, -1)), # source rod
    'B': [], # auxiliary rod
    'C': [] # target rod
}

def make_allowed_move_iterative(rod1, rod2):    
    forward = False
    if not rods[rod2]:
        forward = True
    elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]:
        forward = True              
    if forward:
        print(f'Moving disk {rods[rod1][-1]} from {rod1} to {rod2}')
        rods[rod2].append(rods[rod1].pop())
    else:
        print(f'Moving disk {rods[rod2][-1]} from {rod2} to {rod1}')
        rods[rod1].append(rods[rod2].pop())
    
    # display our progress
    print(rods, '\n')

def move_iterative(n, source_rod, auxiliary_rod, target_rod):
    # display starting configuration
    print(rods, '\n')
    for i in range(number_of_moves):
        remainder = (i + 1) % 3
        if remainder == 1:
            if n % 2 != 0:
                print(f'Move Iterative {i + 1} allowed between {source_rod} and {target_rod}')
                make_allowed_move_iterative(source_rod, target_rod)
            else:
                print(f'Move Iterative {i + 1} allowed between {source_rod} and {auxiliary_rod}')
                make_allowed_move_iterative(source_rod, auxiliary_rod)
        elif remainder == 2:
            if n % 2 != 0:
                print(f'Move Iterative {i + 1} allowed between {source_rod} and {auxiliary_rod}')
                make_allowed_move_iterative(source_rod, auxiliary_rod)
            else:
                print(f'Move Iterative {i + 1} allowed between {source_rod} and {target_rod}')
                make_allowed_move_iterative(source_rod, target_rod)
        elif remainder == 0:
            print(f'Move Iterative {i + 1} allowed between {auxiliary_rod} and {target_rod}')
            make_allowed_move_iterative(auxiliary_rod, target_rod)           

# initiate call from source A to target C with auxiliary B
move_iterative(NUMBER_OF_DISKS_ITERATIVE, 'A', 'B', 'C')


# That's all for the iterative solution. From now on I'm going to build a function that makes use of a recursive approach. Recursion is when a function calls itself. In this case, I'm going to use recursion to calculate smaller versions of the same problem.
# Recursion may seem a bit tricky at first, but it's quite useful and powerful.

# The Tower of Hanoi solved using recursion.


NUMBER_OF_DISKS = 5
A = list(range(NUMBER_OF_DISKS, 0, -1)) # source rod
B = [] # auxiliary rod
C = [] # target rod

def move(n, source, auxiliary, target):
    if n <= 0:
        return
        # move n - 1 disks from source to auxiliary, so they are out of the way
    move(n - 1, source, target, auxiliary)
    
    # move the nth disk from source to target
    target.append(source.pop())
    
    # display our progress
    print(A, B, C, '\n')
    
    # move the n - 1 disks that we left on auxiliary onto target
    move(n - 1,  auxiliary, source, target)
              
# initiate call from source A to target C with auxiliary B
move(NUMBER_OF_DISKS, A, B, C)

