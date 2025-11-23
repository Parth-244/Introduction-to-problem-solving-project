# Simple Command-Line Personal Diary

This project is a small, functional Python script (`Project.py`) that implements a basic, session-based diary in the command line. It includes a password protection feature for added privacy during the session.

## ✨ Features

* **Session-Based Password Protection:** Requires the user to set and correctly enter a password to access the diary for the current run.
* **Simple Command-Line Interface:** Allows users to easily type and save entries line by line.
* **Temporary Storage:** Diary entries are held in memory and displayed upon exiting.
* **Ease of Use:** Simply type "EXIT" to conclude the entry session.

## 🚀 Getting Started

### Prerequisites

* Python 3.x installed on your system.

### Running the Script

1.  **Save the code:** Ensure the provided Python code is saved into a file named `Project.py`.
2.  **Open your terminal or command prompt.**
3.  **Navigate** to the directory where you saved `Project.py`.
4.  **Execute the script** using the Python interpreter:

    ```bash
    python Project.py
    ```

## 📝 How to Use

The application follows a simple three-step process:

1.  **Set and Confirm Password:**
    * The script first asks you to `Set a password for this session:`.
    * It then immediately asks you to `Enter password to unlock diary:`.
    * Access is granted only if the passwords match.

2.  **Write Entries:**
    * Once unlocked, the script prints the header: `____PERSONAL DIARY____`.
    * Type your entries freely, pressing Enter after each line.

3.  **Save and Close:**
    * When you are finished, type the command `EXIT` (case-insensitive) on a new line and press Enter.
    * The script will print all your saved entries under the header `____YOUR SAVED DIARY____` and then close.

## ⚠️ Important Note

This script uses **temporary storage**. Entries are kept only in the computer's memory while the script is running. Once the script finishes, the diary content is **lost** and is **not** saved to a file. The password protection is also only valid for the current session.