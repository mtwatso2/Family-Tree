# Family-Tree

This project generates a visual representation of a family tree using data from a CSV file. The visualization is created using the `graphviz` library in Python. Individual nodes are displayed as squares and contain personal information such as birth and death details. Marriage nodes are displayed as ellipses and contain marriage information, linking the individuals in the family tree.

## Installation

### Graphviz Installation
The `graphviz` Python package depends on the Graphviz software, which includes the `dot` executable required to render graphs. Follow these steps to install Graphviz:

1. Download and Install Graphviz:
- Go to the Graphviz download page.
- Download the appropriate installer for your operating system.
- Run the installer and follow the installation instructions.
  
2. Add Graphviz to System PATH:
- During installation, ensure you select the option to add Graphviz to your system PATH.
- If you missed this step during installation, you can manually add Graphviz to your PATH.
  
#### Manual Addition on Windows:
- Find the installation directory (e.g., C:\Program Files\Graphviz\bin).
- Copy the path to the bin directory.
- Open the Start Menu and search for "Environment Variables".
- Click on "Edit the system environment variables".
- In the System Properties window, click the "Environment Variables" button.
- In the Environment Variables window, find the Path variable in the "System variables" section and select it, then click "Edit".
- Click "New" and paste the path to the Graphviz bin directory.
- Click "OK" to close all windows.
  
3. Verify the Installation:
- Open a new command prompt (this ensures the updated PATH is loaded).
- Type `dot -V` and press Enter. You should see the version information of Graphviz if it is correctly installed and added to your PATH.

### Install Required Packages
Ensure you have `pip` installed, then run:
```
pip install pandas graphviz
```

## Usage 
1. Prepare your data
Create a CSV file, in the root directory of the project, that has the same format as the `Sample_Data.csv` file. Make sure to change the name of the file in the `py` file if needed.

2. Run the script
```
python family_tree.py
```

3. View the output
The family tree will be generated and saved as `family_tree.png` in the project directory.
