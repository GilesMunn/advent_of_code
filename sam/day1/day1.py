count=0
total=0
calories_list=[]
calories_file = open('calories.txt')
for line in calories_file:
    if line in ['\n', '\r\n']:
        total=0
    else:
        total=total+int(line)
        calories_list.append(total)
print("Most Calories is ", max(calories_list))
calories_file.close()