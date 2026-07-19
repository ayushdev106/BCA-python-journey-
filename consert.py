#conert tikets and budget
band_name = "imagine dragons"
tickets_bought = 10
ticket_price = 6000
total_budge = 300000
auto_fare_per_person = 300
#calculaion
total_ticket_cost = tickets_bought * ticket_price
total_travel_cost = auto_fare_per_person * tickets_bought
grand_total = total_ticket_cost + total_travel_cost
money_left = total_budge - grand_total
snacks_per_person = money_left // tickets_bought
party_fund_savings =money_left % tickets_bought
#summry
print(f"""{total_ticket_cost} 
{total_travel_cost} 
{grand_total} 
{money_left}
{snacks_per_person} 
{party_fund_savings}""" )
