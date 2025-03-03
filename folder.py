import os

# Define the project structure
project_structure = [
    "meetup/backend/src/controllers",
    "meetup/backend/src/models",
    "meetup/backend/src/routes",
    "meetup/backend/src/services",
    "meetup/backend/src/utils",
    "meetup/backend/src/config",
    "meetup/backend/src/middlewares",
    "meetup/backend/tests",
    
    "meetup/frontend/src/components",
    "meetup/frontend/src/pages",
    "meetup/frontend/src/hooks",
    "meetup/frontend/src/styles",
    "meetup/frontend/src/context",
    "meetup/frontend/src/utils",
    "meetup/frontend/public",
    
    "meetup/ai-engine/models",
    "meetup/ai-engine/scripts",
    "meetup/ai-engine/dataset",
    
    "meetup/graph-rag/nodes",
    "meetup/graph-rag/edges",
    "meetup/graph-rag/queries",
    "meetup/graph-rag/embeddings",
    
    "meetup/docs",
    "meetup/tests",
    "meetup/scripts"
]

# Files to create in the structure
files_to_create = {
    "meetup/backend/.env": "",
    "meetup/backend/package.json": "{}",
    "meetup/backend/server.js": "// Express server entry point",
    
    "meetup/frontend/.env.local": "",
    "meetup/frontend/package.json": "{}",
    "meetup/frontend/next.config.js": "// Next.js Config File",
    
    "meetup/ai-engine/inference.py": "# Model Inference Logic",
    "meetup/graph-rag/integration.py": "# Graph + AI Connection",
    
    "meetup/.gitignore": "node_modules/\n.env",
    "meetup/README.md": "# Meetup Project"
}

# Function to create folders
def create_folders():
    for folder in project_structure:
        os.makedirs(folder, exist_ok=True)
        # Create __init__.py for Python directories
        if "ai-engine" in folder or "graph-rag" in folder:
            init_file = os.path.join(folder, "__init__.py")
            if not os.path.exists(init_file):
                with open(init_file, "w") as f:
                    f.write("# Init file for package structure\n")

# Function to create files
def create_files():
    for file, content in files_to_create.items():
        with open(file, "w") as f:
            f.write(content)

# Run folder and file creation
if __name__ == "__main__":
    create_folders()
    create_files()
    print("Meetup project structure created successfully!")
