# Task Manager

## Introduction:

### This task manager that allows you to add tasks to a list, mark tasks as complete, and view tasks. It provides a menu-driven interface to perform these operations.

## Quick Start
### Want to play with these notebooks online without having to install anything?

<a href="https://colab.research.google.com/drive/1Hc2NdxHXSsuo8-gnD9L8JRA5duZt3OGO#scrollTo=8fKHAquSnAcq" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> (recommended)
  
⚠ _Colab provides a temporary environment: anything you do will be deleted after a while, so make sure you download any data you care about._

### Just want to quickly look at some notebooks, without executing any code?

* <a href="https://nbviewer.org/github/AhemdMahmoud/MiniNotion/blob/main/Tasks_Manager.ipynb"><img src="https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg" alt="Render nbviewer" /></a>
* [github.com's notebook viewer](https://github.com/AhemdMahmoud/MiniNotion/blob/main/Tasks_Manager.ipynb) also works but it's not ideal: it's slower, the math equations are not always displayed correctly, and large notebooks often fail to open.

## or Usage:

### Run the script using a Python interpreter. You can do this by opening your terminal or command prompt and navigating to the directory containing the script. Then, run the following command:

~~~
python task_manager.py
~~~
## You will be presented with a menu of options:
## 1- Add tasks to a list
## 2- Mark task as complete
## 3- View tasks
## 4- Quit
* Use the numeric keys (1-4) to select an option:

* # Option 1: Add tasks to the list

### Enter a task when prompted.
### The task will be added to the list.
* # Option 2: Mark a task as complete

### You will see a list of incomplete tasks.
### Enter the task number you want to mark as complete.
### The selected task will be marked as complete.
* # Option 3: View tasks

### This option displays all tasks in the list, along with their completion status.
* # Option 4: Quit

# This option exits the program.
## Function Descriptions:

### main(): The main function that displays the menu and handles user input.

### add_task(): Adds a task to the list. The user is prompted to enter the task, and it is stored in the list as a dictionary with a "completed" field set to False.

### mark_task(): Allows the user to mark a task as complete. It lists incomplete tasks and prompts the user for the task number to mark as complete. If the task number is invalid, it handles the error and provides feedback.

### view_tasks(tasks): Displays all tasks in the list along with their completion status. It checks if the task list is empty and handles that case appropriately.

# Common Issues and Solutions:

## Invalid Task Number:
#### If you encounter an "Invalid task number" error when trying to mark a task as complete, it means you entered a number that is out of range. Make sure to enter a valid task number.

## No Tasks to Mark as Complete: 
#### If you choose to mark a task as complete (Option 2) and there are no incomplete tasks in the list, you will be informed that there are no tasks to mark as complete.

## No Tasks to Show: 
#### If you choose to view tasks (Option 3) and there are no tasks in the list, you will be informed that there are no tasks to show.

# * Note: This script is a basic example of a task manager and does not provide long-term storage for tasks. When you quit the program, any tasks added will be lost.

Conclusion:

This task manager script is a simple tool for managing tasks in a list. It provides options for adding tasks, marking them as complete, and viewing the list. You can use this script to keep track of your tasks in a straightforward manner.
