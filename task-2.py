class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def find_min(node):
    # Перевірка, чи дерево непорожнє
    if node is None:
        return None

    # Рухаємося в ліве піддерево, поки можливо
    while node.left:
        node = node.left

    # Повертаємо ключ крайнього лівого вузла
    return node.key

# Приклад створення дерева
root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.left.left = Node(5)
root.left.right = Node(15)

min_value = find_min(root)
print("Найменше значення в дереві:", min_value)
