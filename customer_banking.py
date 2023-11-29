# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account
from Account import Account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = float(input("Please enter your savings balance: "))
    savings_interest = float(input("Please enter your interest rate: "))
    savings_maturity = int(input("Please enter how many months you would like the account to mature: "))

    # Call the create_savings_account function and pass the variables from the user.
    create_savings_account(savings_balance, savings_interest, savings_maturity)
    interest_earned = savings_balance * (savings_interest/100) * (savings_maturity/12)
    updated_savings_balance = savings_balance + interest_earned
    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Your account will earn ${interest_earned: ,.2f} of interest, over the next {savings_maturity} months. Your new savings account balance will be: ${updated_savings_balance: ,.2f}.")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = float(input(f"Please enter your CD balance: "))
    cd_interest = float(input(f"Please enter your interest rate: "))
    cd_maturity = int(input(f"Please enter how many months you would like the account to mature: "))

    # Call the create_cd_account function and pass the variables from the user.
    create_cd_account(cd_balance, cd_interest, cd_maturity)
    interest_earned = cd_balance * (cd_interest/100) * (cd_maturity/12)
    updated_cd_balance = cd_balance + interest_earned
    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Your account will earn ${interest_earned: ,.2f} of interest, over the next {cd_maturity} months. Your new cd balance will be: ${updated_cd_balance: ,.2f}.")
if __name__ == "__main__":
    # Call the main function.
    main()