from cx_Freeze import setup, Executable
import sys
import os
import shutil

# Define the path to the folder you want to include
assets = "assets/"

build_exe_options = {
    "build_exe": "build/kamasoutrax",
    "include_files": [assets],
    "optimize": 2,
    "packages": ["pynput"],  # Ensure pynput is included
    "includes": ["pynput.keyboard"],  # Explicitly include any specific modules
}

sys.path.append(os.path.realpath(sys.path[0] + "\\src"))

setup(
    name="Kamas",
    version="1.0",
    description="Collect everything",
    options={"build_exe": build_exe_options},
    executables=[Executable("src/main.py")],
)

# Define the path to the built assets directory
built_assets_dir = os.path.join("build", "kamasoutrax", "assets", "images")

# Remove any .gitkeep files in the images directory
for root, dirs, files in os.walk(built_assets_dir):
    for file in files:
        if file == ".gitkeep":
            file_path = os.path.join(root, file)
            os.remove(file_path)
            print(f"Removed {file_path}")

# Create a .zip archive of the kamsoutrax folder
output_zip = "build/kamasoutrax.zip"
print("Creating zip...")
shutil.make_archive(
    base_name="build/kamasoutrax", format="zip", root_dir="build/kamasoutrax"
)

print(f"Created {output_zip}")
