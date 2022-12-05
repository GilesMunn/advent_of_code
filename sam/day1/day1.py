total=0
calories_list=[]
calories_file = open('calories.txt')
for line in calories_file:
    if line in ['\n', '\r\n']:
        calories_list.append(total)
        total=0
    else:
        total=total+int(line)
print("Most Calories is ", max(calories_list))
calories_file.close()