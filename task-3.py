class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def sum_tree(node):
    if node is None:
        return 0

    # Рекурсивно знаходимо суму лівого і правого піддерев і додаємо значення поточного вузла
    return node.key + sum_tree(node.left) + sum_tree(node.right)

# Приклад створення дерева
root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.left.left = Node(5)
root.left.right = Node(15)
root.right.right = Node(40)

total_sum = sum_tree(root)
print("Сума всіх значень у дереві:", total_sum)
