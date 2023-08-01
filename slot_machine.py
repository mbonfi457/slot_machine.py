import random

MAX_LINES = 3 #set global maximum no. of lines to bet on
MAX_BET = 500 #set global max bet
MIN_BET = 1 #set global min bet
# script is written so that you can easily change these

ROWS = 3 #number of rows per reel
COLS = 3 #number of columns in slot machine

symbol_count = {  #making a dictionary to hold symbol values
    "A":2,
    "B":4,
    "C":6,
    "D":8,
}

symbol_value = { #assigning multipliers to values
    "A":5,
    "B":4,
    "C":3,
    "D":2,
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def spin_slots(rows,cols,symbols):
    #must randomly select symbols for each column
    all_symbols = []
    # using key,value indexing with '.items()' function
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    #generate values inside columns, generate same number of values as we have rows
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] #slice operator ":" copies a list
        for _ in range(rows):
            value = random.choice(current_symbols)
            #must pick and remove that value so that it can't be used again
            current_symbols.remove(value)
            column.append(value) #adds removed value to column

        columns.append(column)

    return columns

def print_slots(columns):
    #prints out slot machine columns, need a transposed matrix
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1: #print the pip if not on last column
                print(column[row], end=" | ") #prints pipe to separate columns when printed
            else:
                print(column[row], end="")

        print() #prints each row on new line

def deposit():
    # while loop asks user for valid input until input is satisfied
    while True:
        amount = input("Enter deposit: $")
        # make sure user enters positive integer
        if amount.isdigit():
            amount = int(amount)
            # make sure deposit is greater than 0
            if amount > 0:
                break
            else:
                print("Deposit must be greater than 0.")
        else:
            print("Enter a valid number.")
    return amount
    # deposit() returns an integer

def get_lines():
    while True:
        lines = input("Enter desired number of lines to bet on (1-" + str(MAX_LINES) + "). ")
        # utilizing MAX_LINES global variable
        # must add MAX_LINES as string to avoid error
        # make sure user enters positive integer
        if lines.isdigit():
            lines = int(lines)
            # make sure lines is between 1 and MAX_LINES
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("No. of liness must be at least 1.")
        else:
            print("Enter a valid number.")
    return lines

def get_bet():
    while True:
        amount = input(f"Enter bet between ${MIN_BET} and ${MAX_BET} for each line.")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print(f"Bet must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Enter a valid number.")
    return amount

def spin(balance):
    lines = get_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Bet exceeds current balance of ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is {total_bet}")

    slots = spin_slots(ROWS, COLS, symbol_count)
    print_slots(slots)  # each "slot" is a column
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines: ", *winning_lines)  # splat operator passes all winning lines
                                                    # to 'winning_lines'
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")

main()