# We'll check a series of temperatures and print a message accordingly
temperatures = [18, 22, 30, 35]

for temp in temperatures:
    if temp < 20:
        print('It is very hot.')
        break
    elif temp > 25:
        print('It is warm outside.')
        continue
    print('Might be chilly, dress appropriately.')