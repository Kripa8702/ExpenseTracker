# add project root
import sys
import os

project_root = os.path.join(os.path.dirname(__file__))
print(f"Adding {project_root} to sys.path")
sys.path.insert(0, project_root)