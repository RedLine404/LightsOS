def ls(file_path, loaded_data):
    current_node = loaded_data
    clean_path = file_path.strip().strip("/")

    if clean_path:
        path_parts = clean_path.split("/")
    
        for part in path_parts:
            if "children" in current_node and part in current_node["children"]:
                current_node = current_node["children"][part]
        
            else:
                yield f"Error: path '{part}' not found"
                return
        
    if "children" in current_node:
        for filename in current_node["children"]:
            yield filename
    else:
        yield f"Error: {file_path} is not a directory."
