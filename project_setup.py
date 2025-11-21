import os

# Define folder structure
folders = ["src", "src/protocols", "src/core", "src/utils", "tests"]

# Define files to create
files = {
    "src/main.py": "",
    "src/protocols/__init__.py": "",
    "src/protocols/smtp.py": "",
    "src/protocols/protocol_base.py": "",
    "src/core/__init__.py": "",
    "src/core/router.py": "",
    "src/core/packet.py": "",
    "src/core/connection.py": "",
    "src/utils/__init__.py": "",
    "src/utils/logger.py": "",
    "src/utils/config.py": "",
    "tests/test_protocols.py": "",
    "tests/test_core.py": "",
    "tests/test_utils.py": "",
    "README.md": "# Network Simulation System\n",
    ".gitignore": "__pycache__/\n*.log\n.env\n.vscode/\n.idea/\n",
    "requirements.txt": "",
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for filepath, content in files.items():
    with open(filepath, "w") as f:
        f.write(content)

print("Project structure created successfully.")
