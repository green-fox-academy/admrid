accounts = [
	{ 'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2 },
	{ 'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204100071.23 },
	{ 'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1353600.0 }
]

# Create function that returns the name and balance of cash on an account

# Create function that transfers an amount of cash from one account to another
# it should have three parameters:
#  - from account_number
#  - to account_number
#  - amount to transfer
#
# Print "404 - account not found" if any of the account numbers don't exist

def acc():
    accnum = int(input('Your account number: '))
    for i in accounts:
        if i['account_number'] == accnum:
            print(i['client_name'], i['balance'])
        else:
            print('No such account')

# acc()

def trans(from_account_number, to_account_number, amount_to_transfer):
    # acc1 = from_account_number
    # acc2 = to_account_number
    for i in accounts:
        print(i)
        if from_account_number == i['account_number']:
            i['balance'] -= amount_to_transfer
            print("")
            for t in accounts:
                if to_account_number == t['account_number']:
                    t['balance'] += amount_to_transfer
                    print('sucess')

                else:
                    print('404 - account not found')
        else:
            print('404 - account not found')
            return('no')


trans(11234543, 23456311, 100)