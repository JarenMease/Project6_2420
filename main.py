from pathlib import Path
from string import whitespace, punctuation
from bst import BST


class Pair:
    def __init__(self, letter, count=1):
        self.letter = letter
        self.count = count

    def __eq__(self, other):
        return self.letter.lower() == other.letter.lower()

    def __hash__(self):
        return hash(self.letter.lower())

    def __ne__(self, other):
        return self.letter != other.letter

    def __lt__(self, other):
        return self.letter < other.letter

    def __le__(self, other):
        return self.letter <= other.letter

    def __gt__(self, other):
        return self.letter > other.letter

    def __ge__(self, other):
        return self.letter >= other.letter

    def __repr__(self):
        return f'({self.letter}, {self.count})'

    def __str__(self):
        return f'({self.letter}, {self.count})'


def make_tree():
    char_count_tree = BST()

    file_path = Path("around-the-world-in-80-days-3.txt")

    with open(file_path, 'r', encoding='utf-8') as file:
        for char in file.read():
            if char not in (whitespace + punctuation):
                char = char.lower()
                try:
                    char_count = char_count_tree.find(Pair(char))
                    char_count.count += 1
                except ValueError:
                    char_count_tree.add(Pair(char, 1))

    return char_count_tree


def create_bst_from_letter_occurrences():
    with open("around-the-world-in-80-days-3", 'r') as file:
        text = file.read()

    bst = BST()

    for char in text:
        if char == 'z':
            bst.add(1)

    print("Nodes added to the BST:")
    bst.print_tree_structure()

    bst_size = bst.size()

    print(f"Occurrences of 't' in the file: {bst_size}")
    print(f"Size of the BST: {bst_size}")

    bst = BST()

    with open("around-the-world-in-80-days-3", 'r') as file:
        text = file.read()

    for char in text:
        if char == 'z':
            bst.add(1)

    tree_height = bst.height()
    print(f"Height of the BST for 'z' occurrences: {tree_height}")


if __name__ == '__main__':
    create_bst_from_letter_occurrences()



