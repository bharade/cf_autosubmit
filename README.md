# Codeforces Auto-Submitter #
This is a Python script to automate code submission on Codeforces using Selenium.

## Features ##
- Automates login to Codeforces.
- Submits code for a specific contest and problem.
- Uses Selenium to interact with the Codeforces web interface.

## Requirements ##
- Python 3.x
- Selenium WebDriver (pip install selenium)
- ChromeDriver for Selenium(make sure that the version of ChromeDriver matches your installed Chrome browser version

## Usage ##
  python script.py <contest_number> <problem_id> <file_path>
- <contest_number>: The number of the contest (e.g., 1749 for https://codeforces.com/contest/1749).
- <problem_id>: The problem letter (e.g., A for problem A).
- <file_path>: The path to the file you want to submit.

### Example ###
  python script.py 1749 A solution.cpp
- This will navigate to the Codeforces contest 1749, select problem A, and submit the file solution.cpp

