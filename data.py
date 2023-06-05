with open("life-expectancy.csv") as file:
    next(file) # to jump the first line of the file and start in the next line. 

    entities = []
    years = []
    life_expect = []

    index = 0
    user_entities = []
    user_years = []
    user_life_expect = []

    highest_life_country = ""
    highest_life = 0
    highest_year = 0


    lowest_life_country = ""
    lowest_life = 9999
    lowest_year = 9999

    for line in file:
        line_stripped = line.strip()
        line_splited = line_stripped.split(",")
        

        entities.append(line_splited[0])
        years.append(int(line_splited[2]))
        life_expect.append(float(line_splited[3]))


    for i in range(len(entities)):
        
        country = entities[i]
        max_life = life_expect[i]
        min_life = life_expect[i]
        year = years[i]

        if max_life > highest_life: #HIGHEST
            highest_life = max_life
            highest_life_country = country
            highest_year = year

        elif min_life < lowest_life: #LOWEST
            lowest_life = min_life
            lowest_life_country = country
            lowest_year = year
    
    print(f"The overall max life expectancy is: {highest_life:.2f} from {highest_life_country} in {highest_year}")
    print(f"The overall min life expectancy is: {lowest_life:.2f} from {lowest_life_country} in {lowest_year}")

    highest_life_country = ""
    highest_life = 0
    highest_year = 0

    lowest_life_country = ""
    lowest_life = 9999
    lowest_year = 9999

    user_input = int(input("\nEnter the year of interest: "))
    
    for i in years: 
        if i == user_input:

            user_entities.append(entities[index])
            user_years.append(int(years[index]))
            user_life_expect.append(float(life_expect[index]))
        
        index += 1


    for i in range(len(user_life_expect)):
        
        country = user_entities[i]
        max_life, min_life = user_life_expect[i], user_life_expect[i]

        if max_life > highest_life: #HIGHEST
            highest_life = max_life
            highest_life_country = country

        
        if min_life < lowest_life: #LOWEST
            lowest_life = min_life
            lowest_life_country = country
     
    average = sum(user_life_expect) / len(user_life_expect)
    print(f"The average life expectancy across all countries was {average:.2f}")
    print(f"The max life expectancy was in {highest_life_country} with {highest_life:.2f}")
    print(f"The min life expectancy was in {lowest_life_country} with {lowest_life:.2f}")

    #---RESET VARIABLES AND LISTS---
    index = 0
    user_entities = []
    user_years = []
    user_life_expect = []

    highest_life_country = ""
    highest_life = 0
    highest_year = 0

    lowest_life_country = ""
    lowest_life = 9999
    lowest_year = 9999  

    user_input = input("\nEnter the country of interest: ") # to receive extra points I am doing the same here but intead of asking for the year I am asking for the country 
    
    #Add to lists matches between user and full lists
    for i in entities: 

        if i == user_input.title():

            user_entities.append(entities[index])
            user_years.append(int(years[index]))
            user_life_expect.append(float(life_expect[index]))
        
        index += 1

    for i in range(len(user_life_expect)):
        
        country = user_entities[i]
        max_life, min_life = user_life_expect[i], user_life_expect[i]

        if max_life > highest_life: #HIGHEST
            highest_life = max_life
            highest_life_country = country

        
        if min_life < lowest_life: #LOWEST
            lowest_life = min_life
            lowest_life_country = country

    average = sum(user_life_expect) / len(user_life_expect)     
    print(f"The overall life expectancy is {average:.2f}")
    print(f"The max life expectancy was in {highest_life_country} with {highest_life:.2f}")
    print(f"The min life expectancy was in {lowest_life_country} with {lowest_life:.2f}")