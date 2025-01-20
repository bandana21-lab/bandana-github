# numbers=[1,2,3,4,5,6]
# odd_numbers=[i for i in numbers if i%2!=0]
# print(odd_numbers)

# numbers=[1,2,3,4,5,6,7]
# result=[i if i%2!=0 else i**2 for i in numbers]
# print(result)

# numbers=[1,2,3,4,5,6,7]
# result={x: "Odd" if x%2!=0 else "Even" for x in numbers}
# print(result)

# result=(i for i in numbers if i%2==0 )
# print(tuple(result))


# numbers=[-2,-3,-1,0,1,2,3]
# result=["positive" if i>0 else "negative" if i<0 else "zero" for i in numbers]
# print(result)

# s="the quick fox jump over the lazy dog"
# splitted_text=s.split()
# filtered_splitted_text=list(filter(lambda x:x!="the",splitted_text))
# result=[len(word) for word in filtered_splitted_text]
# print(result)

# Find the total sum of unique positive even numbers from the given numbers from the given set 
# numbers=[
#     [-1,-2,3,9,1,2],
#     [2,3,0,-1,-2,-4],
#     [10,9,8,-8,-10,-4],
#     [2,3,4,0,-1,-2,-3]
# ]
# unique_number_sum=sum({y for x in numbers for y in x if y>0 and y%2==0})
# print(unique_number_sum)