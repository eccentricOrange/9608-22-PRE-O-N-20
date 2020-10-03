## Arrays which are supposed to be pre-populated
ItemCode = ["1001", "6056", "5557", "2568", "4458"]
ItemDescription = ["Pencil", "Pen", "Notebook", "Ruler", "Compass"]
Price = [1.0, 10.0, 100.0, 20.0, 30.0]
NumberInStock = [100, 100, 50, 20, 20]

## Constant for the initial number of element (pre-defined)
n = len(ItemCode)

## Constant for the name of the file
RecordsFile = "Item Records.txt"

## Open file for "APPEND" and assign the I/O reference to a variable
FileObject = open(RecordsFile, "a")

## Subroutine to input a valid item code
def GetItemCode():
    Valid = False

    TestItemCode = int(input("\nEnter the code of the item: "))

    while not (TestItemCode > 1000 and TestItemCode < 9999):
        TestItemCode = int(input("Re-enter the codeof the item: "))
    
    return TestItemCode

## Subroutine to extract details of a given record string into an array
def ExtractDetails(RecordString, Details):
    Position = 0
    SearchString = RecordString + ':'

    if RecordString != "":
        for Counter in range(4):
            Position += 1
            CurrentCharacter = SearchString[Position : Position + 1]

            while CurrentCharacter != ':':
                Details[Counter] += CurrentCharacter
                Position += 1
                CurrentCharacter = SearchString[Position : Position + 1]


## TASK 1.4
ThresholdLevel = int(input("Enter the minumum stock level: "))

for Counter in range(n):

    if NumberInStock[Counter] < ThresholdLevel:
        print("\nItem Code:", ItemCode[Counter])
        print("Item Description:", ItemDescription[Counter])
        print("Price:", Price[Counter])
        print("Number in stock:", NumberInStock[Counter])


## TASK 2.2
WriteString = ""

NewItemCode = int(input("\nEnter item code: "))
WriteString = ':' + str(NewItemCode)

NewItemDescription = str(input("Enter item description: "))
WriteString += ':' + NewItemDescription

NewPrice = float(input("Enter new price: "))
WriteString += ':' + str(NewPrice)

NewNumberInStock = int(input("Enter the number of items in stock: "))
WriteString += ':' + str(NewNumberInStock) + '\n'

FileObject.write(WriteString)


## TAKS 2.4 (1)
WriteString = ""
WriteString = ':' + str(GetItemCode())

NewItemDescription = str(input("Enter item description: "))
WriteString += ':' + NewItemDescription

NewPrice = float(input("Enter the price of the item: "))
WriteString += ':' + str(NewPrice)

NewNumberInStock = int(input("Enter number of items in stock: "))
WriteString += ':' + str(NewNumberInStock) + '\n'

FileObject.write(WriteString)


## Close the file and save changes
FileObject.close()

## Open the file in "READ" mode
FileObject = open(RecordsFile, "r")

## Read data from the file into an array. They are also split using the newline delimiter '\n'.
FileData = (FileObject.read()).split('\n')

## Remove last empty element
FileData.pop()

## Close the file
FileObject.close()

## TASK 2.4 (2)
Found = False
CurrentRecord = ""

print("\nEnter the code of the item you want to search for")
DesiredItemCode = GetItemCode()

for record in FileData:
    CurrentRecord = record
    if CurrentRecord[1:5] == str(DesiredItemCode):
        Found = True
        break

if Found:
    DetailsOfRecord = ["" for i in range(4)]
    ExtractDetails(CurrentRecord, DetailsOfRecord)

    print("\nItem Code: " + str(DetailsOfRecord[0]))
    print("Item Description: " + DetailsOfRecord[1])
    print("Price of item: " + str(DetailsOfRecord[2]))
    print("Number of the item in stock: " + str(DetailsOfRecord[3]))

else:
    print("Item not found.")


## TASK 2.4 (3)
DesiredItemDescription = str(input("\nEnter the description of the item you want to search for: "))

for record in FileData:
    DetailsOfRecord = ["" for i in range(4)]
    ExtractDetails(record, DetailsOfRecord)

    if DetailsOfRecord[1] == DesiredItemDescription:
        print("\nItem Code: " + str(DetailsOfRecord[0]))
        print("Item Description: " + DetailsOfRecord[1])
        print("Price of item: " + str(DetailsOfRecord[2]))
        print("Number of the item in stock: " + str(DetailsOfRecord[3]))


## TASK 2.4 (4)
DesiredPrice = float(input("\nEnter the maximum threshold price: "))

for record in FileData:
    DetailsOfRecord = ["" for i in range(4)]
    ExtractDetails(record, DetailsOfRecord)

    if float(DetailsOfRecord[2]) < DesiredPrice:
        print("\nItem Code: " + str(DetailsOfRecord[0]))
        print("Item Description: " + DetailsOfRecord[1])
        print("Price of item: " + str(DetailsOfRecord[2]))
        print("Number of the item in stock: " + str(DetailsOfRecord[3]))

