#Initialize balance
balance = 0.0
 
# Load balance and transaction log from files
try:
    with open("Bank Data.txt", "r") as file:
        balance = float(file.read())
except FileNotFoundError:
    #If the file doesn't exist, balance remains 0.0
    pass
except ValueError:
    print("Invalid data in the file. Starting with a balance of 0.0.")
 
#Main loop
while True:
    print(f'Current balance:{balance}')
    response = input("Would you like to make a transaction? (Yes/No):")
 
    if response.lower() == 'yes':
        transaction_type = input("Would you like to make a deposit or withdrawal? (Deposit/Withdraw):")
 
        if transaction_type.lower() == 'deposit':
            the_amount = input("How much would you like to deposit? ")
            amount = the_amount.replace(" ", "").strip()
            if amount.replace('.', '',1).isdigit():
                amount = float(amount)
                balance += amount
                print(f'Deposit of {amount} successful.')
 
            #Log the deposit in the transaction log file
            with open("Transaction Log.txt", "a") as log_file:
                log_file.write(f"Deposit: +{amount}\n")
 
        elif transaction_type.lower() == 'withdraw':
            the_amount = input("How much would you like to withdraw? ")
            amount = the_amount.replace(" ", "").strip()
            if amount.replace('.', '',1).isdigit():  # Check if input is a valid number
                amount = float(amount)
           
                if amount <= balance:
                    balance -= amount
                    print(f'Withdrawal of {amount} successful.')
 
                #Log the withdrawal in the transaction log file
                with open("Transaction Log.txt", "a") as log_file:
                    log_file.write(f"Withdrawal: -{amount}\n")
            else:
                print("Insufficient funds.")
   
        else:
            print("you provided an invalid input.")
 
    elif response.lower() == 'no':
        #Saving the updated balance to the file
        with open("Bank Data.txt", "w") as file:
            file.write(str(balance))
        print("Thank you for using the banking applciation.")
        break
   
    else:
        print("You provided an invalid input.")