#In this script, we first set up our Stripe API key. We then calculate the date range for the past 7 days using the datetime module. We use these dates to create a filter for the Stripe API query, using the gte and lte parameters to specify a range of created dates.
#We retrieve the transactions using the stripe.Charge.list() method, passing in our date filter and a limit parameter to retrieve up to 100 transactions at a time.
#We convert the transactions to a JSON format using the json.dumps() method, and print the JSON to the console. You can adjust the indent parameter to change the formatting of the JSON output.



import stripe
import json
import datetime

# Set up Stripe API keys
stripe.api_key = 'your_api_key'

# Calculate the date range for the past 7 days
end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(days=7)

# Retrieve all transactions within the date range
transactions = stripe.Charge.list(
    created={
        'gte': int(start_date.timestamp()),
        'lte': int(end_date.timestamp())
    },
    limit=100
)

# Convert the transactions to a JSON format
json_transactions = json.dumps(transactions, indent=4)

# Print the JSON transactions to the console
print(json_transactions)
