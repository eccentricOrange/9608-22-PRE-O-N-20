# TASK 1
The following four 1D arrays can store different pieces of data about stock items in a shop:
| Array Identifier | Data Type |
| -- | -- |
|`ItemCode`|`STRING`|
|`ItemDescription`|`STRING`|
|`Price`|`REAL`|
|`NumberInStock`|`INTEGER`|

## Task 1.1
Design an algorithm to search for a specific value in ItemDescription and, if found, to output the
array index where the value is found. Output a suitable message if the value is not found.
Document the algorithm using:
* structured English
* program flowchart
* pseudocode.

### Solution
We will assume that the array `ItemDescription` is already defined and populated as an `ARRAY[1:n] OF STRING` where `n : INTEGER` is the number of items. The pseudocode for this step is in the pseudocode file.

| Identifier | Data type | Purpose |
| -- | -- | --|
| n | `INTEGER` | Total number of elements |
| Index | `INTEGER` | The index number after searching |
| Counter | `INTEGER` | The running counter for the loop |
| DesiredValue | `STRING` | The value input from the user |
| ItemDescription | `ARRAY[1:n] OF STRING` | The pre-populated array of descriptions |

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