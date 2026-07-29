# Rushmore Developer Command Assistant
<img width="1280" height="640" alt="rushmore_banner" src="https://github.com/user-attachments/assets/bd7d6300-14a4-49aa-9d63-756b1942e8fc" />

A modular Python command-line application named Rushmore that automates common
developer and file-management tasks, with an ASCII art of Rushmore himself, changing each menu display for a dynamic experience.

## Features

- Create structured project directories
- Automatically initialise Git repositories
- Organise files by extension
- Search recursively for files
- Analyse text files
- Generate folder statistics
- Record activity in a log
- Configure behaviour through JSON
- ASCII art display

## Preview

<img width="453" height="662" alt="Rushmore command-line menu" src="https://github.com/user-attachments/assets/2cdb722a-882d-412e-9c1a-7eaf2a6fc4fb" />

## Project Structure

```text
dev-command-assistant/
├── managers/
│   ├── file_manager.py
│   ├── git_manager.py
│   ├── project_manager.py
│   └── text_manager.py
├── animator.py
├── ascii_art.py
├── assistant.py
├── config.json
├── config_manager.py
├── logger.py
└── main.py
```

## Architecture
The application is divided into focused components:

- DeveloperAssistant coordinates the menu and application flow.
- ProjectManager creates structured project directories.
- GitManager initialises Git repositories using Python's subprocess module.
- FileManager organises files, performs recursive searches and generates folder statistics.
- TextManager analyses text files.
- ConfigManager loads configurable behaviour from config.json.
- Logger records application activity.
- AsciiAnimator controls the rotating command-line artwork.

## Requirements

- Python 3.10 or later
- Git, for automatic repository initialisation

## Running the Application

Clone the repository:

```bash
git clone https://github.com/umark212/dev-command-assistant.git
```
Move into the project directory:
```bash
cd dev-command-assistant
```
Run the application:
```bash
python main.py
```
On some systems, use:
```bash
python3 main.py
```

## Configuration
Rushmore's behaviour can be changed through the config.json file.

Example:
```json
{
    "default_project_directory": "",
    "auto_git_init": true
}
```

Configuration Options
- default_project_directory controls where new projects are created.
- An empty value causes projects to be created in the current working directory.
- auto_git_init determines whether new projects are automatically initialised as Git repositories.

## Skills Demonstrated
- Object-oriented programming in Python
- Modular software architecture
- File-system automation
- JSON configuration
- Git integration
- Subprocess management
- Exception handling
- Activity logging
- Command-line interface development

## Future Improvements
- Add automated unit tests
- Add configurable project templates
- Support multiple .gitignore templates
- Add additional Git operations
- Improve user-input validation
- Package Rushmore as an installable command-line tool


## Author
Developed by Umar Choudhary
