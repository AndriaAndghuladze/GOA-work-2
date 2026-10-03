#1
#Your task is to split the chocolate bar of given dimension n x m into small squares. Each square is of size 1x1 and unbreakable. Implement a function that will return minimum number of breaks needed.
def break_chocolate(n, m):
    if n > 0 and m > 0:
        return n * m -1
    else:
        return 0


#2
#Make your strings more nerdy: Replace all 'a'/'A' with 4, 'e'/'E' with 3 and 'l' with 1 e.g. "Fundamentals" --> "Fund4m3nt41s"

def nerdify(txt):
    return (txt.replace('a', '4')
                .replace('A', '4')
                .replace('e', '3')
                .replace('E', '3')
                .replace('l', '1'))


#3
#Given a Divisor and a Bound , Find the largest integer N , Such That ,
def max_multiple(divisor, bound):
    return bound - (bound % divisor)


#4
#Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.
def count_positives_sum_negatives(arr):
    
    if arr == [] : 
        return []
    
    result = [0, 0]
    
    for value in arr:
        if value > 0:
            result[0] += 1
        else:
            result[1] += value
        
    return result


#5
#Complete the function which takes two arguments and returns all numbers which are divisible by the given divisor. First argument is an array of numbers and the second is the divisor.
def divisible_by(numbers, divisor):
    return [num for num in numbers if num % divisor == 0]


#6
#Write a function that takes a list of strings as an argument and returns a filtered list containing the same elements but with the 'geese' removed.
geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    return [bird for bird in birds if bird not in geese]


#7
#Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.
def fake_bin(x):
    return ''.join(['0' if int(digit) < 5 else '1' for digit in x])