# Build a User Configuration Manager

A Python program that allows users to manage their personal settings such as theme, language, and notifications. Users can add, update, delete, and view their settings easily.

## Features
- Add a new setting (if it doesn't already exist)
- Update existing settings
- Delete settings
- View current user settings

## Example Usage
```python
# Initial settings
settings = {
    "theme": "light",
    "language": "english",
    "notifications": "enabled"
}

# Trying to add an existing setting
add_setting(settings, ("theme", "dark"))  
# Output: Setting 'theme' already exists! Cannot add a new setting with this name.

# Updating a setting
update_setting(settings, ("language", "spanish"))  
# Output: Setting 'language' updated to 'spanish' successfully!

# Deleting a setting
delete_setting(settings, "notifications")  
# Output: Setting 'notifications' deleted successfully!

# Viewing settings
view_settings(settings)

Theme: light
Language: spanish

Objectives
	•	Practice working with Python dictionaries
	•	Implement CRUD operations for user settings
	•	Handle duplicate entries and error messages
	•	Build a simple interactive application
