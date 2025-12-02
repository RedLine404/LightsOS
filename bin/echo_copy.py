def cd(target, current_path, disk_data):
    # Handling "going back"
    if target == "..":
        if current_path:
            current_path.pop()
        return

    # Handling "moving forward"
    temp_path = current_path + [target] 

    current_node = disk_data

    for folder in temp_path:
        children = current_node.get("children", {})
        
        if folder in children:
            current_node = children[folder]

            if current_node["type"] != "dir":
                yield f"Error: '{target}' is not a directory."
                return
        else:
            yield f"Error: Directory '{target}' not found."
            return

    current_path.append(target)