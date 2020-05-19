import graphviz
from sklearn.tree import export_graphviz


def graph_generator(decision_tree, feature_names, target_names, graph_name, filled=True, rounded=True):
    dot_data = export_graphviz(decision_tree  # ,out_file = None
                               , feature_names=feature_names
                               , class_names=target_names
                               , filled=filled  # 让树的每一块有颜色，颜色越浅，表示不纯度越高
                               , rounded=rounded  # 树的块的形状
                               )
    graph = graphviz.Source(dot_data)
    graph.render(graph_name)
    graph.view()
