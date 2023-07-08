import sys
# opening the input file
ınput = str(sys.argv[1])
inputFile = open(ınput, "r")
sFile = inputFile.read()
inputFile.close()
import sys
try:
    input2=str(sys.argv[2])
    File_2 = open(input2, "r")
    lines = File_2.readlines()
    splitted_line_2 = []
    for line_2 in lines:
        line_2 = line_2.replace("\n", "")
        splitted_line_2.append(line_2)

    input1 = str(sys.argv[1])
    with open(input1, "r") as File:
        lines = File.readlines()

    for line in lines:
        line = line.replace("\n", "")
        splitted_line = line.split(" ")

        try:
            numbers = ""
            for number in range(int(float(splitted_line[2]) // 1), int(float(splitted_line[3])) // 1 + 1):
                if float(splitted_line[0]) + 0.5 >= int(float(splitted_line[0]) // 1) + 1:
                    splitted_line[0] = int(float(splitted_line[0]) // 1) + 1

                else:
                    splitted_line[0] = int(float(splitted_line[0]) // 1)
                if float(splitted_line[1]) + 0.5 >= int(float(splitted_line[1]) // 1) + 1:
                    splitted_line[1] = int(float(splitted_line[1]) // 1) + 1
                else:
                    splitted_line[1] = int(float(splitted_line[1]) // 1)

                if number % int(float(splitted_line[0])) == 0 and number % int(float(splitted_line[1])) != 0:
                    numbers += str(number) + " "

            if numbers[:-1] == splitted_line_2[0]:
                print("-" * 12)
                print("My results:\t\t", numbers[:-1])
                print("Results to compare:\t", splitted_line_2[0])
                print("Goool!!!")
            else:
                print("-" * 12)
                print("My results:\t\t", numbers[:-1])
                print("Results to compare:\t", splitted_line_2[0])
                raise AssertionError

            splitted_line_2.remove(splitted_line_2[0])

        except IndexError:
            print("-" * 12)
            print("Index Error: number of operands less than expected.")
            print("Given input : ", end=" ")
            for i in splitted_line:
                print(i, end=" ")
            print()
            splitted_line_2.remove(splitted_line_2[0])
        except ValueError:
            print("-" * 12)
            print("ValueError: only numeric input is accepted.")
            print("Given input : ", end=" ")
            for i in splitted_line:
                print(i, end=" ")
            print()
            splitted_line_2.remove(splitted_line_2[0])
        except ZeroDivisionError:
            print("-" * 12)
            print("ZeroDivisionError: You can’t divide by 0.")
            print("Given input : ", end=" ")
            for i in splitted_line:
                print(i, end=" ")
            print()
            splitted_line_2.remove(splitted_line_2[0])
        except AssertionError:
            print("Assertion Error: results don’t match.")
            splitted_line_2.remove(splitted_line_2[0])
        except Exception:
            print("kaBOOM: run for your life!")
            splitted_line_2.remove(splitted_line_2[0])

except FileNotFoundError:
    print("IOError: cannot open")

except IndexError:
    print("IndexError: number of input files less than expected.")
finally:
    print(" ˜ Game Over ˜ ")
# creating list
myList = sFile.split("\n")
number_list = []
for i in myList:
    numbers = i[0:4]
    if numbers in number_list:
        pass
    else:
        number_list.append(numbers)
number_list_sorted = sorted(number_list)

# creating dictionary
myDict = {}
for a in range(len(number_list)):
    myDict.update({str(number_list_sorted[a]): []})

# appending each row in sFile to corresponding key in the myDict
for li in myList:
    for a in number_list_sorted:
        if li[0:4] == a:
            myDict[a].append(li)

# sorting list elements in all keys
for i in myDict:
    myDict[i].sort(key=lambda string: string[5])
output = str(sys.argv[2])
outputFile = open(output, "w")
count = 1
for key in myDict:
    outputFile.write("Message " + str(count) + "\n")
    for row in myDict[key]:
        outputFile.write(row+"\n")
    count += 1

outputFile.close()
