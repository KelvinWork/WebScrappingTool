import time
import datetime







#local_time = time.ctime(seconds)
#print("Local time:", local_time)
#print(type(local_time))

run = True

while run ==True:
    seconds = time.time()
    mins2 = seconds + 10.0
    # print(type(seconds))
    # print(mins2)
    # print(seconds)


    if(seconds>= mins2 ):
        print("two mins has passed")