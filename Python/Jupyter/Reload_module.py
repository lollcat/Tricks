import importlib
import LDA_class # from python file that get's updated (in which case we need to import the updated version)
importlib.reload(LDA_class)
LDA = LDA_class.LDA   # equivalent to reloading from LDA_class import LDA
