current_data = [11,22,33,44]
i = 0
j = 3
current_data = current_data[:i] + current_data[i+1:j] + current_data[j+1:]
print(current_data)