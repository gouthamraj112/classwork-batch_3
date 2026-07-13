numbers=list(map(int,input("enter numbers separated by space:").split())) 
#filter even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

#square the even numbers
squared_evens = list(map(lambda x: x ** 2, even_numbers))

print("Squared even numbers:", squared_evens)