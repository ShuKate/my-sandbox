#Is it a lucky ticket?
t = int(input('Enter the number: '))
if ((t % 1000) % 10) + (((t % 1000) % 100) // 10) + ((t % 1000) // 100) != ((t // 1000) % 10) + (((t // 1000) % 100) // 10) + ((t // 1000) // 100):
    print('Unlucky :(')
else:
    print('Congrats! :)')