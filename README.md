# My Plugin
# Installation Guide for VS Code, Git, and Python

This guide provides step-by-step instructions to install Visual Studio Code, Git, and Python on your local machine. Follow the appropriate section for your operating system.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation on Linux/Mac (Bash)](#installation-on-linuxmac-bash)
- [Installation on Windows (PowerShell)](#installation-on-windows-powershell)

## Prerequisites
- An internet connection.
- Administrative privileges on your machine (if required).

---

## Installation on Linux/Mac (Bash)

### Step 1: Install Visual Studio Code
1. Open your terminal.
2. Run the following commands to download and install VS Code:

   ```bash
   # For Debian-based distributions (like Ubuntu)
   sudo apt update
   sudo apt install software-properties-common apt-transport-https wget
   wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -
   sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"
   sudo apt update
   sudo apt install code

   # For Red Hat-based distributions (like Fedora)
   sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
   sudo sh -c 'echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/vscode.repo'
   sudo dnf install code
   ```

### Step 2: Install Git
1. In your terminal, run:

   ```bash
   sudo apt install git  # For Debian-based systems
   sudo dnf install git  # For Red Hat-based systems
   ```

### Step 3: Install Python
1. Install Python using the following command:

   ```bash
   sudo apt install python3 python3-pip  # For Debian-based systems
   sudo dnf install python3 python3-pip  # For Red Hat-based systems
   ```

---

## Installation on Windows (PowerShell)

### Step 1: Install Visual Studio Code
1. Open PowerShell as Administrator.
2. Run the following command to download and install VS Code:

   ```powershell
   $VSCODE_URL = "https://code.visualstudio.com/sha/download?build=stable&os=win32-x64"
   Invoke-WebRequest -Uri $VSCODE_URL -OutFile "vscode.exe"
   Start-Process -FilePath "vscode.exe" -ArgumentList "/VERYSILENT", "/NORESTART" -Wait
   Remove-Item "vscode.exe"
   ```

### Step 2: Install Git
1. Still in PowerShell, run:

   ```powershell
   $GIT_URL = "https://github.com/git-for-windows/git/releases/latest/download/Git-x86_64-v2.36.1.exe"
   Invoke-WebRequest -Uri $GIT_URL -OutFile "git-installer.exe"
   Start-Process -FilePath "git-installer.exe" -ArgumentList "/VERYSILENT", "/NORESTART" -Wait
   Remove-Item "git-installer.exe"
   ```

### Step 3: Install Python
1. Still in PowerShell, run:

   ```powershell
   $PYTHON_URL = "https://www.python.org/ftp/python/3.10.1/python-3.10.1-amd64.exe"
   Invoke-WebRequest -Uri $PYTHON_URL -OutFile "python-installer.exe"
   Start-Process -FilePath "python-installer.exe" -ArgumentList "/quiet", "InstallAllUsers=1", "PrependPath=1" -Wait
   Remove-Item "python-installer.exe"
   ```

---

## Verifying Installation
To verify that the installations were successful, run the following commands in your terminal or PowerShell:

```bash
code --version   # For VS Code
git --version    # For Git
python3 --version  # For Python (use python --version on Windows)
```

---

# Cloning a GitHub Repository in Visual Studio Code

## Overview
This guide will walk you through the process of cloning a GitHub repository using the terminal within Visual Studio Code (VS Code).

## Prerequisites
- Ensure you have [Visual Studio Code](https://code.visualstudio.com/) installed on your machine.
- Ensure you have [Git](https://git-scm.com/) installed and configured on your machine.
- You need to have access to the repository you want to clone.

## Steps

### Step 1: Open Visual Studio Code
1. **Launch VS Code**:
   - Locate the Visual Studio Code icon on your desktop or in your applications folder.
   - Right-click the icon and open the application as Administrator.

### Step 2: Open a Terminal Window
1. **Open the Terminal**:
   - Click on the **Terminal** menu in the top menu bar.
   - Select **New Terminal** from the dropdown. You can also use the shortcut:
     - **Windows/Linux**: `Ctrl + Shift + ` (backtick)
     - **Mac**: `Cmd + Shift + ` (backtick)

### Step 3: Navigate to the Desired Directory
1. **Change Directory (Optional)**:
   - We are going to clone the repository to your user folder, so change directory using the `cd` command.
   - For example, on Linux:
     ```bash
     cd /home/USERNAME_HERE/
     ```
     And on Windows:
     ```powershell
     cd C:\Users\USERNAME_HERE\
     ```

### Step 4: Clone the Repository
1. **Clone the Repository**:
   - In the terminal, run the following command to clone the repository:
     ```bash
     git clone https://github.com/Joeprobruh/myplugin.git
     ```
   - This command will create a local copy of the repository in a new folder named `myplugin`.
   - In the terminal, change directory into the repository's folder:
     ```bash
     cd myplugin
     ```

### Step 5: Open the Cloned Repository
1. **Open the Cloned Folder**:
   - After cloning, you can open the folder in VS Code.
   - Click on the **File** menu in the top menu bar.
   - Select **Open Folder...** from the dropdown.
   - Navigate to the newly created `myplugin` folder and click **Select Folder**.

---

## Conclusion
You have successfully installed Visual Studio Code, Git, and Python on your local machine.
You have successfully cloned the repository from GitHub using the terminal within Visual Studio Code. You can now start working on the project! The "docs" folder has everything you need to get started.

### Notes:
- Be sure to check for the latest version URLs for VS Code, Git, and Python and update them in the script as necessary.
- You may need administrative privileges to install some of the software on Windows.

## Additional Resources
- [Git Documentation](https://git-scm.com/doc)
- [Visual Studio Code Documentation](https://code.visualstudio.com/docs)