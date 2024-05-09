# Question_2

# 2. Movie Ticket Pricing
# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

while True:
    
    day = input("pls Enter Day Name(enter in LowerCase): ")
    age = int(input("Enter the value of age: "))

    movie_tickets_price = None

    if day == "wednesday":
        if age < 18:
            movie_tickets_price = 6
            print(movie_tickets_price)
        if age >=  18:
            movie_tickets_price = 10
            print(movie_tickets_price)


    else:
        if age < 18:
            movie_tickets_price = 8
            print(movie_tickets_price)

        elif age >=  18:
            movie_tickets_price = 12
            print(movie_tickets_price)