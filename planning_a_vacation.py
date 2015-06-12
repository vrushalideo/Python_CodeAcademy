def hotel_cost(nights):
    return(140 * nights)
def plane_ride_cost(city):
    if city == "Charlotte":
        cost = 183
        return (cost)
    if city == "Tampa":
        cost = 220
        return (cost)
    if city == "Pittsburgh":
        cost = 222
        return (cost)
    if city == "Los Angeles":
        cost = 475
        return (cost)
    else:
        return (0)
    
def rental_car_cost(days):
    if days >= 7:
        rent = (days*40) - 50
        return (rent)
    elif days >=3:
        rent = (days*40) - 20
        return (rent)
    else:
        rent = days * 40
        return (rent)
        
def trip_cost(city, days, spending_money):
        return plane_ride_cost(city) + rental_car_cost(days) + hotel_cost(days) + spending_money

print trip_cost("Los Angeles", 5, 600)
