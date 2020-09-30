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
We will assume that the array `ItemDescription` is already defined and populated as an `ARRAY[1:n] OF STRING` where `n : INTEGER` is the number of items.

| Identifier | Data type | Purpose |
| -- | -- | --|
| n | `INTEGER` | Total number of elements |
| Index | `INTEGER` | The index number after searching |
| Counter | `INTEGER` | The running counter for the loop |
| DesiredValue | `STRING` | The value input from the user |
| ItemDescription | `ARRAY[1:n] OF STRING` | The pre-populated arrays of descriptions |

1. Set `Index` equal to `-1`.
2. Prompt the user for the value they would like to search, and input `DesiredValue`.
3. Traverse `ItemDescription` and check whether any element is equal to `DesiredValue`.
4. If any element is equal, record the its index value in `Index` and break out of the loop. The loop may end before the element was found.
5. If `Index` is equal to `-1`, the element was not found. Output an error message to the user.
6. Otherwise (if `Index` was not equal to `-1`), the element was found. Output the value `Index` in this case.

