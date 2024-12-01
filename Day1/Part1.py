input_data = """"""

def parse_input():
    list1 = []
    list2 = []
    sum1 = 0
    for line in input_data.splitlines():
        # Split the line by whitespace
        column1, column2 = line.split()

        # Append the values to the lists
        list1.append(int(column1))  # Convert to int if needed
        list2.append(int(column2))  # Convert to int if needed
        list.sort(list1)
        list.sort(list2)

    for i in range(len(list1)):
        sum1 += abs(list1[i]-list2[i])

    return sum1

print(parse_input())

