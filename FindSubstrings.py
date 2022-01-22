#Create a program that takes a string and find substrings that begin and end with the same number, with only integers in between.
#Test input: 29535123p48723487597645723645

input = "29535123p48723487597645723645"

def find_substrings(input):
    i = 0
    temp_int = 0
    substrings = []
    int_substrings = []
    #stops the function at the end of the string
    while i < len(input):
        #ignores non-integer characters at the start/end (don't strictly need this b/c final step would eleminate any appended non-neumeric substrings)
        if input[i].isdigit():
            #sets the starting value to check for as a temporary variable
            temp_int = input[i]
            for character in range(i+1, len(input)):
                #identify when there is a match
                if temp_int == input[character]:
                    #append the string to the substrings list
                    substrings.append(input[i:character+1])
                    break
        i+=1
    #loop through substrings to remove any that are non-numeric
    for string in substrings:
        if string.isdigit() == True:
            int_substrings.append(int(string))
    return(int_substrings)

def calc_sum(lst):
    sum = 0
    for int in lst:
        sum += int
    return sum

final_answer = find_substrings(input)
sum = calc_sum(final_answer)
print("The final list of integers is: ", final_answer)
print("The total of the list is: " + str(sum))