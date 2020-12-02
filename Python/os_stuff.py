# How to make a new paths if intermediate folders are nested
if not os.path.exists(os.path.join(os.getcwd(), target_path)): # check if path exists, also shows how to use os join
    os.makedirs(os.path.join(os.getcwd(), target_path))
