from bigtree import Node, print_tree

root = Node('💻 Software')

backend = Node('⚙️ Backend', parent=root)
frontend = Node('🎨 Frontend', parent=root)

Node('🐍 Python', parent=backend)
Node('☕️ Java', parent=backend)

Node('⚛️ React', parent=frontend)
Node('🟢 Vue', parent=frontend)

print_tree(root)