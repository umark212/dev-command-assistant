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
- <img width="453" height="662" alt="image" src="https://github.com/user-attachments/assets/2cdb722a-882d-412e-9c1a-7eaf2a6fc4fb" />


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

## Requirements

- Python 3.10 or later
- Git, for automatic repository initialisation

## Running the application

- python main.py
