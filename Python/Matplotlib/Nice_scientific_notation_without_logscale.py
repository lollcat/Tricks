# Nice scientific notation without having to use log_scale
f = mpl.ticker.ScalarFormatter(useOffset=False, useMathText=True)
g = lambda x,pos : "${}$".format(f._formatSciNotation('%1.10e' % x))
plt.gca().yaxis.set_major_formatter(mpl.ticker.FuncFormatter(g))
