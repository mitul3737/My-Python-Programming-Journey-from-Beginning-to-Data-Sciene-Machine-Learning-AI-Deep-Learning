def add_numbers(numbers):
    result=0
    for n in numbers: #n=1 then n=2 then n=30..............n=9
        result += n
    return result

result=add_numbers([1,2,30,4,5,9]) #values list to add
print(result)
