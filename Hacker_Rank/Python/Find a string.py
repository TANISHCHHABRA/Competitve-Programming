def count_substring(string, sub_string):
    l = len(sub_string)
    count = 0
    for i in range(len(string)):
        if(string[i:l + i] == sub_string):
            count += 1
    return count

