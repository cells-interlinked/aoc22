
input_file = open('input.txt', 'r')
lines = input_file.readlines()
  
top = 0
current = 0

for line in lines:
    if line.strip() == '':
        print(current)
        if current > top:
            top = current
        current = 0
    else:
        current += int(line.strip())

print(top)    