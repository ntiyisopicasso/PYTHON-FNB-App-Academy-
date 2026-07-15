# Profile Generator

A simple Python script that captures user information, automatically generates a username, cleans up biographical text, and displays a formatted summary.

## Features

* **Username Generation:** Creates a unique handle using the first letter of the first name combined with the last name.
* **Name Formatting:** Merges and automatically converts names into Title Case.
* **Text Normalisation:** Trims accidental spacing from the biography and standardises "i am" to "I'm".
* **Character Counter:** Calculates and displays the exact length of the final biography.

## Prerequisites

To run this script, you only need Python 3 installed on your system.

## How to Run

1. Clone or download `project.py` to your local machine.
2. Open your terminal or command prompt.
3. Navigate to the directory containing the file.
4. Execute the script using the following command:

```bash
python project.py
```

## Example Output

```text
Enter your first name: john
Enter your last name: doe
write a short bio:   i am a software developer.  

******************************

        Infomation captured     

******************************


Your username is: jdoe
FullNames: John Doe
Your bio have 25 Characters
Short bio about yourself: I'm a software developer.
```
