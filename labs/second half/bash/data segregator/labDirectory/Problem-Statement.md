# Data Segregator and Grader

The task:

- You have been given a csv file called "grades.csv" which consists of "," separated columns "rollno,quiz1,quiz2,midsem,endsem,total-marks". The column names should be self-explanatory for this csv file.
- The first line of the csv file contains header in the sequence described above, and from line 2 onwards the csv file contains actual data within their respective column.
- The csv file contains all the students from btech batch 2023 (roll no starting from 23B001 to 23B999) and 2024 (roll no starting from 24B001 to 24B999) in an unordered manner.
- Your task is to create a bash script in "submission.sh" file where below conditions are fulfilled:

  1. Segregate the data based on if a row contains student of batch 2023 or 2024. All the data of batch 2023 should be written in a separate file called "ug23.csv", and the same way all the data of batch 2024 should be written in a separate file called "ug24.csv"
  2. You also have to add a new "grades" column in these data with following matrix:

     | marks         | grades |
     | ------------- | ------ |
     | >85           | AA     |
     | >65 and <=85  | AB     |
     | >45 and <= 65 | BB     |
     | >35 and <= 45 | CC     |
     | <=35          | F      |

  3. The final csv file must be sorted by grades column(from AA to F) and if 2 students have same grades than then are sorted in non-descending order of the roll no.

- The filename must be taken via command-line argument. Ideally the execution of bash script must be done via:
  - "bash submission.sh grades.csv"
- **NOTE**: You can assume that the total-marks add up using quiz1,quiz2,midsem,and endsem marks. You can also assume that total-marks in range [0,100].
- **EXTRA**: You are also given you some extra testcases in /home/labDirectory/testcases folder for you to refer.

## An example:

**`grades.csv`**

```
rollno,quiz1,quiz2,midsem,endsem,total-marks
23B001,10,8,25,45,88
23B010,9,8,25,40,82
23B009,5,0,25,45,75
23B002,10,5,25,5,45
24B001,10,8,25,45,88
24B010,3,2,10,5,20
24B009,5,10,25,45,85
24B002,10,5,25,25,65
```

---

**`ug23.csv`**

```
rollno,name,quiz1,quiz2,midsem,endsem,total-marks,grades
23B001,10,8,25,45,88,AA
23B009,5,0,25,45,75,AB
23B010,9,8,25,40,82,AB
23B002,10,5,25,5,45,CC
```

**`ug24.csv`**

```
rollno,quiz1,quiz2,midsem,endsem,total-marks,grades
24B001,10,8,25,45,88,AA
24B009,5,10,25,45,85,AB
24B002,10,5,25,25,65,BB
24B010,3,2,10,5,20,F
```
