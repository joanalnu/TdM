from graphviz import Digraph

# Create a directed graph for X-ray pipeline (Spectral and Photometric Separation)
dot = Digraph("TdM_workflow", format="png")
dot.attr(rankdir="TB", size="12", dpi="600")

# define nodes
# Define node styles
dot.attr("node", shape="box", style="rounded, filled", fontname="Arial", fontsize="12")
dot.node("TITLE", "Text", color="color")

dot.node("main.py", "Triggers general functions", color="pink")

dot.node("general.start()", "Returns language selection", color="lightgreen")
dot.node("general.welcome()", "Displays instructions", color="lightgreen")
dot.node("general.mode_selection()", "Returns mode selection", color="lightgreen")

# split

# training
dot.node("general.type_calc_selection()", "Returns type of calculation to be practiced", color="lightgreen")
dot.node("training()", "Runs training program", color="lightgreen")

# gaming
dot.node("Instructions", "", color='blue')
dot.node("gaming()", "Runs gaming program", color="blue")

# answers
dot.node("correct_answer()", "Displays correct answer and current points", color="pink")
dot.node("incorrect_answer()", "Displays incorrect answer and current points", color="pink")
dot.node("goodbye", "Displays points and says goodbye", color="pink")


# define edges
dot.edge("main.py", "general.start()", style="dashed")
dot.edge("general.start()", "general.welcome()", style="dashed")
dot.edge("general.welcome()", "general.mode_selection()", style="dashed")

# training
dot.edge("general.mode_selection()", "general.type_calc_selection()", style="dashed", label="Select calculation type")
dot.edge("general.type_calc_selection()", "training()", style="dashed")

# gaming
dot.edge("general.mode_selection()", "Instructions", style="dashed")
dot.edge("Instructions", "gaming()", style="dashed")

# answers
dot.edge("training()", "correct_answer()", style="dashed")
dot.edge("training()", "incorrect_answer()", style="dashed")
dot.edge("training()", "goodbye", style="dashed")

dot.edge("gaming()", "correct_answer()", style="dashed")
dot.edge("gaming()", "incorrect_answer()", style="dashed")
dot.edge("gaming()", "goodbye", style="dashed")

# Render the diagram
dot.render("TdM_workflow", view=True)