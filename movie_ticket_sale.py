total_bill_amount = 0.0
total_number_of_tickets = 0

while True :
  coustmer_name = input(" Enter ticket type (adult / child / senior) or type 'done' to finish: " )
  if coustmer_name == "done" :
    break

  if coustmer_name == "adult" :
    total_bill_amount += 12.0
    total_number_of_tickets += 1

  elif coustmer_name == "child" :
    total_bill_amount += 7.50
    total_number_of_tickets += 1

  elif coustmer_name == "senior" :
    total_bill_amount += 9.0
    total_number_of_tickets += 1
    
  else :
    print("Invalid ticket type. Please enter 'adult', 'child', or 'senior'.")
    continue
     
print(f"total bill = {total_bill_amount}")
print(f"total number of tickets = {total_number_of_tickets}")
