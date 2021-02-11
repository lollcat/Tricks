# read file
with open(file_path, "r") as f:
            file = f.read()
            
# write file example 
with open(os.path.join(os.getcwd(), target_file), "w") as g:
    g.write("\n".join(list_of_lines))
