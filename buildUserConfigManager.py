# user_config_manager.py

# Test settings dictionary
test_settings = {
    "theme": "light",
    "language": "english",
    "notifications": "enabled"
}

def add_setting(settings, key_value):
    key, value = key_value
    key = key.lower()
    value = value.lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    
    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings, key_value):
    key, value = key_value
    key = key.lower()
    value = value.lower()

    if key not in settings:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
    
    settings[key] = value
    return f"Setting '{key}' updated to '{value}' successfully!"

def delete_setting(settings, key):
    key = key.lower()

    if key not in settings:
        return "Setting not found!"
    
    del settings[key]
    return f"Setting '{key}' deleted successfully!"

def view_settings(settings):
    if not settings:
        return "No settings available."

    result = "Current User Settings:\n"
    for key, value in settings.items():
        result += f"{key.capitalize()}: {value}\n"
    return result


# Example usage
if __name__ == "__main__":
    print("Initial settings:")
    print(view_settings(test_settings))
    
    print(add_setting(test_settings, ("Theme", "Dark")))
    print(update_setting(test_settings, ("language", "Spanish")))
    print(delete_setting(test_settings, "notifications"))
    
    print("\nUpdated settings:")
    print(view_settings(test_settings))