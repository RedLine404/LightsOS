def cat(target, current_path, disk_data):
    # Handling "moving forward"
    temp_path = current_path + [target] 

    current_node = disk_data

    for folder in temp_path:
        children = current_node.get("children", {})
        
        if folder in children:
            current_node = children[folder]

            if current_node["type"] == "file":
                yield current_node["content"]
                return
        else:
            yield f"Error: Directory '{target}' not found."
            return
