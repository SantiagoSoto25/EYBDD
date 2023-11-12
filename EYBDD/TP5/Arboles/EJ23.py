class Creature:
    def __init__(self, name, defeated_by=None, description=None, captured_by=None):
        self.name = name
        self.defeated_by = defeated_by
        self.description = description
        self.captured_by = captured_by

class TreeNode:
    def __init__(self, creature):
        self.creature = creature
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, creature):
        self.root = self._insert(self.root, creature)

    def _insert(self, node, creature):
        if node is None:
            return TreeNode(creature)

        if creature.name < node.creature.name:
            node.left = self._insert(node.left, creature)
        elif creature.name > node.creature.name:
            node.right = self._insert(node.right, creature)

        return node

    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)
            print(f"Criatura: {node.creature.name}")
            if node.creature.defeated_by:
                print(f"Derrotada por: {node.creature.defeated_by}")
            if node.creature.description:
                print(f"Descripción: {node.creature.description}")
            print()
            self.in_order_traversal(node.right)

    def level_order_traversal(self):
        if not self.root:
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(f"Criatura: {node.creature.name}")
            if node.creature.defeated_by:
                print(f"Derrotada por: {node.creature.defeated_by}")
            if node.creature.description:
                print(f"Descripción: {node.creature.description}")
            if node.creature.captured_by:
                print(f"Capturada por: {node.creature.captured_by}")
            print()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def search(self, name):
        return self._search(self.root, name)

    def _search(self, node, name):
        if node is None:
            return None
        if node.creature.name == name:
            return node.creature
        if name < node.creature.name:
            return self._search(node.left, name)
        else:
            return self._search(node.right, name)

    def update_defeated_by(self, name, defeated_by):
        creature = self.search(name)
        if creature:
            creature.defeated_by = defeated_by

    def update_captured_by(self, name, captured_by):
        creature = self.search(name)
        if creature:
            creature.captured_by = captured_by

    def remove_creatures(self, node, names_to_remove):
        if node is not None:
            if node.creature.name not in names_to_remove:
                node.left = self.remove_creatures(node.left, names_to_remove)
                node.right = self.remove_creatures(node.right, names_to_remove)
                return node
            return None

    def update_creature_name(self, old_name, new_name):
        creature = self.search(old_name)
        if creature:
            creature.name = new_name


creature_tree = Tree()

creatures = [
    Creature("Ceto", defeated_by="Teseo"),
    Creature("Tifón", defeated_by="Zeus"),
    Creature("Equidna", defeated_by=["Argos Panoptes", "Teseo"]),
    Creature("Dino", defeated_by="Atalanta"),
    Creature("Pefredo"),
    Creature("Enio", defeated_by="Heracles"),
    Creature("Escila", defeated_by="Cloto"),
    Creature("Caribdis", defeated_by="Láquesis"),
    Creature("Euríale", defeated_by="Átropos"),
    Creature("Esteno", defeated_by=["Minotauro de Creta", "Teseo"]),
    Creature("Medusa", defeated_by="Perseo"),
    Creature("Ladón"),
    Creature("Águila del Cáucaso"),
    Creature("Quimera", defeated_by="Belerofonte"),
    Creature("Hidra de Lerna", defeated_by="Heracles"),
    Creature("León de Nemea", defeated_by="Heracles"),
    Creature("Esfinge", defeated_by="Edipo"),
    Creature("Dragón de la Cólquida"),
    Creature("Cerbero"),
    Creature("Talos", defeated_by="Medea"),
    Creature("Sirenas"),
    Creature("Pitón", defeated_by="Apolo"),
    Creature("Cierva de Cerinea"),
    Creature("Basilisco"),
    Creature("Toro de Creta"),
]

for creature in creatures:
    creature_tree.insert(creature)


creature_tree.update_defeated_by("Ceto", "Teseo")
creature_tree.update_defeated_by("Pefredo", "Carcinos")
creature_tree.update_defeated_by("Águila del Cáucaso", "Aves del Estínfalo")
creature_tree.update_defeated_by("Cerbero", "Heracles")
creature_tree.update_defeated_by("Toro de Creta", "Teseo")

creature_tree.update_captured_by("Cerbero", "Heracles")
creature_tree.update_captured_by("Toro de Creta", "Heracles")
creature_tree.update_captured_by("Cierva de Cerinea", "Heracles")
creature_tree.update_captured_by("Jabalí de Erimanto", "Heracles")

creature_tree.update_creature_name("Ladón", "Dragón Ladón")


creatures_to_remove = ["Basilisco", "Sirenas"]
creature_tree.root = creature_tree.remove_creatures(creature_tree.root, creatures_to_remove)

aves_del_estinfalo = creature_tree.search("Aves del Estínfalo")
if aves_del_estinfalo:
    aves_del_estinfalo.description = "Aves del Estínfalo derrotadas por Heracles."


print("Listado por nivel del árbol:")
creature_tree.level_order_traversal()


print("\nCriaturas capturadas por Heracles:")
for creature in creatures:
    if creature.captured_by == "Heracles":
        print(creature.name)