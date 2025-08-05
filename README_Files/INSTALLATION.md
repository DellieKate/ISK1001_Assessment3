<!-- Installation Steps and Requirements -->
# Installation

Here you will find an in depth guide to installating the <u>**KLM LabTest Advisor**</u>.

To utilise this app, users will need to meet certain prerequisites.  These include:  

Operating System(s):  **Windows 10 (or higher)/macOS 13 (or higher)/Linux**

Specfic Programming Languages:  **Python version 3.13**

Software: 
- **Git 2.43.0 (or higher).**
- **VSCode or IDE of your choice.**

If aforementioned prerequisites are met, users can continue with the process.  From here, the repository can be cloned locally onto personal computers/servers, by running one of these commands within the terminal:

### Clone:

HTTPS: 
```
git clone https://github.com/username/repository-name.git
```

SSH: 
```
git clone git@github.com:DellieKate/ISK1001_Assessment3.git
```

GitHub CLI: 
```
gh repo clone DellieKate/ISK1001_Assessment3
```

Now that the app is accessible from your local repository, you will need to change directories into the newly imported repository, where you will then create a virtual environment, to hold the necessary dependencies, followed by activating said virtual environment.  To do this, run the applicable commands in the terminal:

### Create: 

Windows: 
```
python -m venv myenv
``` 

macOS or WSL/Linux: 
```
python3 -m venv myenv
```

### Activate:

Windows: 
```
myenv\Scripts\activate
```

macOS or WSL/Linux: 
```
source myenv/bin/activate
```

Now that are virtual environment is up and running, we install the dependencies required for the app to function.  Since this app utilises various necessary modules/packages, rather than downloading each one individually, we can automatically download and install all of them at once. From within the virtual environment, run the command in the terminal:

```
pip install -r ./requirements.txt
```

Once this is done, you are all set to start using the <u>**KLM LabTest Advisor**</u>.  To make changes/alterations or to have a look at the code itself, you can do so by opening the directory in your preferred IDE of choice.  To do so from the terminal, if you use VS Code, from within the local repository, you can run:

To open everything:
```
Code .
```

To open a specific file:
```
Code <file_name_here.py>
```  
  
For instructions on how to use the app, refer to the [README](../README.md) for a brief summary, or the [Instruction Guide](INSTRUCTIONS.md) for a more detailed guide.