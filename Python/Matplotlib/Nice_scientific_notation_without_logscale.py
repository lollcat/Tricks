# Nice scientific notation without having to use log_scale
f = mpl.ticker.ScalarFormatter(useOffset=False, useMathText=True)
g = lambda x,pos : "${}$".format(f._formatSciNotation('%1.10e' % x))
plt.gca().yaxis.set_major_formatter(mpl.ticker.FuncFormatter(g)) # if there is a specific axis (e.g. when using subplots, then call on specific axis (ax[0].yaxis...etc) instead of gca
