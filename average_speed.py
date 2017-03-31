import time

speed_limit = 100
car = str(input("what is your number plate boy"))

input("Press enter to start")
start_time = time.time()
input("Press enter to stop")
stop_time = time.time()
distance = (1000)
time_taken = stop_time - start_time

print('Time taken: {:.2f} seconds'.format(time_taken))
print('Distance: {:.2f}'.format(distance))
Average_Speed = distance / time_taken
print('Average_Speed: {:.2f}'.format(Average_Speed))

if Average_Speed > speed_limit:
    print("the car is over the speed limit which is 100")
    text_file = open("Output.txt", "a")
    text_file.write(car)
    text_file.close()
