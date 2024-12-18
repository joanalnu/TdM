from graphviz import Digraph

# Create a directed graph for X-ray pipeline (Spectral and Photometric Separation)
dot = Digraph("TdM_workflow", format="png")
dot.attr(rankdir="TB", size="12", dpi="600")

# define nodes
# Define node styles
dot.attr("node", shape="box", style="rounded, filled", fontname="Arial", fontsize="12")
dot.node("TITLE", "Text", color="color")

# define edges
dot.edge("FROM", "TO", label="TITLE", style="linstyle")

# Render the diagram
dot.render("TdM_workflow", view=True)