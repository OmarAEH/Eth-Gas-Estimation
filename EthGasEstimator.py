"""
This script coded by github.com/OmarAEH
Feel free to contact me at anytime.
"""

import requests

headerdic = {
    "Authorization": "YOUR-API-KEY-HERE"
}   # header for API request for blocknative.com


def gas_estimator(probability):
    """
    This function to get ethereum gas settings from blocknative.com
    :param probability: Specified probability for the transaction to get in the next block
    :return: None 
    """
    get_url = "https://api.blocknative.com/gasprices/blockprices?confidenceLevels=" + str(probability)
    # Get Gas settings from blocknative.com
    respond = requests.get(get_url, headers=headerdic)  # Get the data from blocknative.com
    respond = respond.json().get('blockPrices')[0]  # Filter the response data
    estimatedPrices = respond['estimatedPrices']  # Get the estimated prices from data
    estimatedPrices = estimatedPrices[0]  # Get the estimated prices from data
    maxGasFee = estimatedPrices['maxFeePerGas']  # Get max Gas fees
    maxPriorityFee = estimatedPrices['maxPriorityFeePerGas']  # Get max priority fees
    print("You can use " + str(maxGasFee) + " GWEI to get " +
          str(probability) + "% probability that your transaction will get in the next block.")
    print("You can use " + str(maxPriorityFee) + " priority fee to get " +
          str(probability) + "% probability that your transaction will get in the next block.")


if __name__ == "__main__":
    probability_input = input('Please specify a probability to get your transaction in the next block, '
                              'must be between 1-100 : ')
    if 1 <= int(probability_input) <= 100:  # Check if input between 1-100
        gas_estimator(probability_input)
    else:
        print("Wrong input, please enter a number between 1-100 only!")
