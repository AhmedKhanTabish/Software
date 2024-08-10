#include <stdio.h>
#include <string.h>

// Define constants
#define MAX_TASKS 100

// Define a structure to represent a task
struct Task {
    char description[100];
    int isCompleted;
};

// Declare global variables
struct Task tasks[MAX_TASKS];
int numTasks = 0;

// Function to add a task
void addTask(char description[]) {
    if (numTasks < MAX_TASKS) {
        strcpy(tasks[numTasks].description, description);
        tasks[numTasks].isCompleted = 0; // Initialize as not completed
        numTasks++;
        printf("Task added successfully.\n");
    } else {
        printf("To-do list is full. Cannot add more tasks.\n");
    }
}

// Function to remove a task by its index
void removeTask(int index) {
    if (index >= 0 && index < numTasks) {
        for (int i = index; i < numTasks - 1; i++) {
            tasks[i] = tasks[i + 1];
        }
        numTasks--;
        printf("Task removed successfully.\n");
    } else {
        printf("Invalid task index. Task not removed.\n");
    }
}

// Function to display all tasks
void displayTasks() {
    if (numTasks == 0) {
        printf("No tasks in the to-do list.\n");
        return;
    }

    printf("To-Do List:\n");
    for (int i = 0; i < numTasks; i++) {
        printf("%d. %s [%s]\n", i + 1, tasks[i].description,
               tasks[i].isCompleted ? "Completed" : "Not Completed");
    }
}

// Main program
int main() {
    int choice;
    char description[100];

    while (1) {
        printf("\nTo-Do List Menu:\n");
        printf("1. Add Task\n");
        printf("2. Remove Task\n");
        printf("3. View Tasks\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter task description: ");
                scanf(" %[^\n]", description); // Read string with spaces
                addTask(description);
                break;
            case 2:
                printf("Enter the task number to remove: ");
                int taskNumber;
                scanf("%d", &taskNumber);
                removeTask(taskNumber - 1); // Adjust for 0-based index
                break;
            case 3:
                displayTasks();
                break;
            case 4:
                printf("Exiting the program.\n");
                return 0;
            default:
                printf("Invalid choice. Please try again.\n");
        }
    }

    return 0;
}
