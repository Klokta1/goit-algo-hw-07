class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def find_max(node):
    # Перевірка, чи дерево непорожнє
    if node is None:
        return None

    # Рухаємося в праве піддерево, поки можливо
    while node.right:
        node = node.right

    # Повертаємо ключ крайнього правого вузла
    return node.key

# Приклад створення дерева
root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.right.right = Node(40)
root.right.left = Node(25)

max_value = find_max(root)
print("Найбільше значення в дереві:", max_value)
