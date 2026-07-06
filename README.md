# STUDENT-MANAGEMENT-SYSTEM-
A CLI Student Management System in Python to add, view, search, delete, and persist student records using JSON file storage!

**Features**
- **Add Student** – Store a student's name along with their marks,
- **View All Students** – Display every student currently in the system,
- **Search Student** – Look up an individual student's marks by name,
- **Delete Student** – Remove a student's record from the system,
- **Save Data** – Save all student records to a `students.json` file,
- **Load Data** – Load previously saved records from `students.json,
- **Exit** – Safely exit the program,

**How It Works**
**1.The program runs in an infinite loop, presenting a menu of options. 
Based on user input,
**2.it performs the corresponding action using a Python 
dictionary (`student`) as an in-memory database, where each key is a 
student's name and the value is their marks.
**3.Data can be saved to and 
loaded from a JSON file for persistence.

## Tech Stack
- Python 3
- Built-in `json` and `os` modules (no external dependencies)
- 
## Future Improvements
- Add marks-checking / grading feature (currently commented out)
- Fix numbering inconsistency (currently missing "4")
- Add update/edit student functionality
- Add input validation for non-numeric marks
- Support multiple subjects per student
