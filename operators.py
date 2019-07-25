taskList = [23, "Jane",["Lesson 23",560,{"currency": "KES"}],987,(76,"John")]
# print(type(taskList))
# print(taskList[2][2]["currency"])
# print(taskList[2][1])
taskList[3] = "".join(reversed(str(taskList[3])))
taskList[2][1] = "".join(reversed(str(taskList[2][1])))
print(taskList[2][1])
print(taskList[3])
# print(taskList)
# another_list =(taskList[2])
# dict = another_list[2]
# print(dict["currency"])
# print(another_list[1])
# print(len(taskList))
