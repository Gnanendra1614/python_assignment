# Python Assignment

A collection of Python solutions for 20 HackerRank Python exercises covering lists, strings, sets, dictionaries, date and time handling, NumPy arrays, regular expressions, and algorithms.

## Requirements

- Python 3.10 or newer
- NumPy for questions 11-14

Install the external dependency with:

```powershell
py -m pip install -r .\src\requirements.txt
```

Run a solution from the assignment root with:

```powershell
py .\src\01_question\answer.py
```

Each program reads input from standard input. Use the input format provided with the corresponding exercise.

## HackerRank Questions

The following table includes every HackerRank question currently represented in this assignment.

| Question | HackerRank problem | Short overview | Solution |
| --- | --- | --- | --- |
| 01 | Lists | Processes commands that insert, remove, sort, append, pop, reverse, and print list values. | [answer.py](src/01_question/answer.py) |
| 02 | Finding the Percentage | Stores student marks and calculates the selected student's average to two decimal places. | [answer.py](src/02_question/answer.py) |
| 03 | Finding the Percentage | Repeats the student-mark average exercise using dictionary and list operations. | [03_question.py](src/03_question/03_question.py) |
| 04 | Find the Runner-Up Score! | Removes duplicate scores, sorts the values, and prints the second-highest score. | [answer.py](src/04_question/answer.py) |
| 05 | Mutate String | Replaces one character at a specified position using string slicing. | [answer.py](src/05_question/answer.py) |
| 06 | Merge the Tools! | Splits a string into groups and removes repeated characters from each group. | [answer.py](src/06_question/answer.py) |
| 07 | Print Formatting | Prints number representations in aligned decimal, octal, hexadecimal, and binary columns. | [answer.py](src/07_question/answer.py) |
| 08 | Calendar Module | Uses Python's calendar module to find the weekday for a given date. | [answer.py](src/08_question/answer.py) |
| 09 | Text Alignment | Builds a symmetric H-shaped pattern using string alignment and repetition. | [answer.py](src/09_question/answer.py) |
| 10 | collections.namedtuple | Reads student records with a named tuple and calculates the average marks. | [answer.py](src/10_question/answer.py) |
| 11 | Floor, Ceil and Rint | Applies NumPy floor, ceiling, and nearest-integer rounding element by element. | [answer.py](src/11_question/answer.py) |
| 12 | Min and Max | Finds each row's minimum value and then the largest value among those minimums. | [answer.py](src/12_question/answer.py) |
| 13 | Arrays | Builds a square NumPy matrix and calculates its determinant. | [answer.py](src/13_question/answer.py) |
| 14 | Mean, Var, and Std | Calculates row means, column variances, and the standard deviation of an array. | [answer.py](src/14_question/answer.py) |
| 15 | Time Delta | Parses timezone-aware timestamps and returns the absolute difference in seconds. | [answer.py](src/15_question/answer.py) |
| 16 | No Idea! | Updates a happiness score based on membership in two sets. | [No_Idea.py](src/16_question/No_Idea.py) |
| 17 | Word Order | Counts unique words while preserving their first-seen order. | [Word_order.py](src/17_question/Word_order.py) |
| 18 | Piling Up! | Takes cubes from either end and checks whether they can be stacked in decreasing order. | [piling Up.py](src/18_question/piling%20Up.py) |
| 19 | Iterables and Iterators | Generates combinations and calculates the probability that a group contains the letter `a`. | [Iterables and Iterators.py](src/19_question/Iterables%20and%20Iterators.py) |
| 20 | Validating Email Addresses With a Filter | Uses a regular expression to filter valid email addresses and sorts the results. | [Validating Email Addresses With a Filter.py](src/20_question/Validating%20Email%20Addresses%20With%20a%20Filter.py) |

## Running Files With Spaces

Quote the path when running a file whose name contains spaces:

```powershell
py ".\src\18_question\piling Up.py"
py ".\src\19_question\Iterables and Iterators.py"
py ".\src\20_question\Validating Email Addresses With a Filter.py"
```

## Project Structure

```text
python_assignment/
├── src/
│   ├── requirements.txt
│   └── 01_question/ ... 20_question/
├── README.md
└── .venv/                 # Local virtual environment, if present
```

Images included in the `src` question folders are reference material for the exercises.

## Notes

Question 15 contains the timestamp-difference implementation, but its current main block prints `delta` before assigning it. Remove that first `print(delta)` or move it after the input loop before running the file.