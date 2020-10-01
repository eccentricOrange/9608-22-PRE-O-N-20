# TASK 1 – Algorithms, arrays and pseudocode
The following four 1D arrays can store different pieces of data about stock items in a shop:
| Array Identifier | Data Type |
| -- | -- |
| ItemCode | `STRING` |
| ItemDescription | `STRING` |
| Price | `REAL` |
| NumberInStock | `INTEGER` |
 
## Task 1.1
Design an algorithm to search for a specific value in ItemDescription and, if found, to output the
array index where the value is found. Output a suitable message if the value is not found. <br> Document the algorithm using:
* structured English
* program flowchart
* pseudocode.

### Solution
We will assume that the array `ItemDescription` is already defined and populated as an `ARRAY[1:n] OF STRING` where `n : INTEGER` is the number of items. The program in structured English and the identifier table are given below, and the pseudocode for this step is in the pseudocode file.

| Identifier | Data type | Purpose |
| -- | -- | --|
| n | `INTEGER` | Total number of elements |
| Index | `INTEGER` | The index number after searching |
| Counter | `INTEGER` | The running counter for the loop |
| DesiredValue | `STRING` | The value input from the user |
| ItemDescription | `ARRAY[1:n] OF STRING` | The pre-populated array of descriptions |
<br>

**Program in Structured English**
1. Set `Index` equal to `-1`.
2. Prompt the user for the value they would like to search, and input `DesiredValue`.
3. Traverse `ItemDescription` and check whether any element is equal to `DesiredValue`.
4. If any element is equal, record the its index value in `Index` and break out of the loop. The loop may end before the element was found.
5. If `Index` is equal to `-1`, the element was not found. Output an error message to the user.
6. Otherwise (if `Index` was not equal to `-1`), the element was found. Output the value `Index` in this case.

## TASK 1.2
Consider the difference between algorithms that search for a single or multiple instance of the value.

### Solution
To search for multiple values, we can consider an array `Indices : ARRAY[1:n] OF INTEGER`, initialized to contain `-1`s, instead of the `Index` value. The program can then record the indices of matches in the array instead of a single value. We can then use a `REPEAT UNTIL` loop to traverse `Indices` and output the indices of matches until it reaches a value if `-1`.

## TASK 1.3
Extend the algorithm from Task 1.1 to output the corresponding values from the other arrays.

## Solution
Extension is recorded in the pseuducode file. We will assume that the following arrays pre-populated.

| Identifier | Data type | Purpose |
| -- | -- | --|
| ItemCode | `ARRAY[1:n] OF STRING` | The pre-populated array of codes for items |
| Price | `ARRAY[1:n] OF REAL` | The pre-populated array of prices of items |
| NumberInStock | `ARRAY[1:n] OF INTEGER` | The pre-populated array of the number of items in stock |

## TASK 1.4
Write program code to produce a report displaying all the information stored about each item for
which the number in stock is below a given level.

### Solution
This segment will be planned using pseudocode in the pseudocode file. The identifier table is given below.

| Identifier | Data type | Purpose |
| -- | -- | --|
| n | `INTEGER` | Total number of elements |
| ThresholdLevel | `INTEGER` | The minumum stock threshold input to check against |
| Counter | `INTEGER` | The running counter for the loop |

<br><br>

# TASK 2 – Programs containing several components
The stock data described in Task 1 are now to be stored in a text file. Each line of the file will correspond to one stock item.

## TASK 2.1
Define a format in which each line of the text file can store the different pieces of data about one stock
item. <br> Consider whether there is a requirement for data type conversion.

### Solution
The values for any given reocrd will be separated by colons. Records themselves will be separated by newline characters.

```text
:ItemCode_0:ItemDescription_0:Price_0:NumberInStock_0\n
:ItemCode_1:ItemDescription_1:Price_1:NumberInStock_1\n
:ItemCode_2:ItemDescription_2:Price_2:NumberInStock_2\n
```
Values for `Price` and `NumberInStock` would have to be convetred to `STRING` using `NUM_TO_STRING()` in pseudocode or `str()` in Python because the functions to write only take a `STRING` as an input.

## TASK 2.2
Design an algorithm to input the four pieces of data about a stock item, form a string according to your format design, and write the string to the text file. <br> First draw a program flowchart, then write the equivalent pseudocode.

# Solution
The pseudocode and flowcharts for this section are stored in their repective files. The identifier table is given below here.
| Identifier | Data type | Purpose |
| -- | -- | -- |
| RecordsFile | `STRING` | Constant to store the name of the file containing the records
| NewItemCode | `STRING` | The code of the new item |
| NewItemDescription | `STRING` | The description of the new item |
| NewPrice | `REAL` | The price of the new item |
| NewNumberInStock | `INTEGER` | The number of the new item in stock |
| WriteString | `STRING` | The string that will be written to the file after concatenation
