#scenario 1
#Thomas Young
def dist(distance,rear):
    add = (distance + rear)
    divide = (add/2)
    return(divide)

##def adding():
##    return(distance,rear)
##add = (distance + rear)
##divide = (add/2)
##print(divide)
def weather(weath,no_boogers):
    
    if weath == ("dry"):
        return(no_boogers)
    else:
        return(no_boogers*2)

  

def main():
    distance = int(input("what is the difference in the distance between you and the car in front"))
    rear = int(input("what is the difference between cars to your side in meters"))
    no_boogers = dist(distance,rear)
    print(no_boogers)
   
    weath = str(input("is the weather dry"))
    doodo = weather(weath,no_boogers)
    print(doodo)
    


if __name__ == "__main__":
    main()

    

    

                   
                   
                   
    
            
                   
