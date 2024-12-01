#1

def is_valid_brackets(string):
    stack = []  # מחסנית לשמירת סוגריים פתוחים
    brackets = {')': '(', ']': '[', '}': '{'}  # מפה להתאמה בין סוגרים

    for char in string:
        if char in brackets.values():  # סוגר פותח
            stack.append(char)
        elif char in brackets.keys():  # סוגר סוגר
            if not stack or stack.pop() != brackets[char]:
                return False

    return len(stack) == 0  # המחסנית חייבת להיות ריקה בסוף


# דוגמאות לבדיקה:
print(is_valid_brackets("({[]})"))  # True
print(is_valid_brackets("{[(])}"))  # False
print(is_valid_brackets("[()]{}{[()()]()}"))  # True




#2
def remove_duplicates_sorted(lst):
    if not lst:
        return lst  # רשימה ריקה

    write_index = 1  # אינדקס לכתיבה
    for i in range(1, len(lst)):
        if lst[i] != lst[write_index - 1]:  # איבר חדש
            lst[write_index] = lst[i]
            write_index += 1

    return lst[:write_index]  # החזרת הרשימה ללא כפילויות


# דוגמאות לבדיקה:
print(remove_duplicates_sorted([1, 1, 2, 3, 3, 4, 4, 4, 5]))  # [1, 2, 3, 4, 5]
print(remove_duplicates_sorted([1, 1, 1, 1, 1]))  # [1]
print(remove_duplicates_sorted([]))  # []



#3
def merge_sorted_lists(list1, list2):
    merged_list = []
    i, j = 0, 0  # מצביעים לשתי הרשימות

    # איחוד תוך שמירה על סדר
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # הוספת שאר הערכים מהרשימה שלא הסתיימה
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list

# דוגמאות לבדיקה:
print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # [1, 2, 3, 4, 5, 6]
print(merge_sorted_lists([1, 2, 2, 3], [2, 3, 4]))  # [1, 2, 2, 2, 3, 3, 4]
print(merge_sorted_lists([], [1, 2, 3]))  # [1, 2, 3]
print(merge_sorted_lists([1, 2, 3], []))  # [1, 2, 3]
