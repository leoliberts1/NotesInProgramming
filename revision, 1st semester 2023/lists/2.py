sample_list = [34, 54, 67, 89, 11, 43, 94]
sample_list.append(sample_list[4])
sample_list.pop(4)
sample_list.insert(2,sample_list[-1])
print(sample_list)