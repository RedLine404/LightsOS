def cd(target, current_path, disk_data):
    # Handling "going back"
    if target == "..":
        if current_path:
            current_path.pop()
        return

    # Handling "moving forward"
    target_parts = target.strip("/").split("/")
    full_test_path = current_path + target_parts
    current_node = disk_data        # Traverse (Verify the path exists)

    for folder in full_test_path:
        children = current_node.get("children", {})
        
        if folder in children:
            current_node = children[folder]
            
            # Check if it is a directory or not
            if current_node["type"] != "dir":
                yield f"Error: '{folder}' is not a directory."
                return
        else:
            yield f"Error: Directory '{folder}' not found."
            return

    for part in target_parts:
        current_path.append(part)
