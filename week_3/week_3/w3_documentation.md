# WEEK 3  TUTORIAL 3

## Activity 1: Identify the Components

### Inputs
- Quiz 1 Mark
- Quiz 2 Mark
- Quiz 3 Mark
- Choice (Y/N)

### Process
1. Read three quiz marks.
2. Calculate average mark.
3. Display average.
4. Determine pass or fail.
5. Ask user whether to continue.

### Outputs
- Average Mark
- PASS or FAIL
- Program Ended

---

## Activity 2: Design the Algorithm

### Pseudocode

START

SET choice = "Y"

WHILE choice = "Y"

INPUT quiz_1
INPUT quiz_2
INPUT quiz_3

average = (quiz_1 + quiz_2 + quiz_3) / 3

DISPLAY average

IF average >= 50
DISPLAY "PASS"
ELSE
DISPLAY "FAIL"
ENDIF

INPUT choice

ENDWHILE

DISPLAY "Program Ended"

STOP

---

### Algorithm Structure

#### Sequence
- Input quiz marks
- Calculate average
- Display average

#### Selection
- IF average >= 50
- Display PASS
- ELSE Display FAIL

#### Iteration
- WHILE choice == "Y"
