import matplotlib.lines as mlines
import matplotlib.pyplot as plt

fig, ax1 = plt.subplots()
# draw fake legend
colours = ["tab:red", "tomato", "tab:blue"]
labels = ["$L_1$", "$L_\infty$", "$L_2$"]
lines = []
for i, col in enumerate(colours):
    lines.append(mlines.Line2D([], [], color=col,
                      markersize=15, label=labels[i])) # these lines don't show besides in the legend
ax1.legend(handles = lines, loc='upper left')
