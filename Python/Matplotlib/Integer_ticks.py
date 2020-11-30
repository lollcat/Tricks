fig, axs = plt.subplots(1,2, figsize=(6,3))
axs[0].plot(np.arange(0, len(f0_history), dtype="int"), f0_history)  # plot some stuff
axs[0].xaxis.set_major_locator(mpl.ticker.MaxNLocator(integer=True))  # set tick labels to integer
...etc
