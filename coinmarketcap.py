from bs4 import BeautifulSoup
import requests
import pandas as pd

# Empty lists to store data
crypto_name_list = []
crypto_market_cap_list = []
crypto_price_list = []
crypto_circulating_supply_list = []
crypto_symbol_list = []

# Create empty dataframe to organise data
df = pd.DataFrame()

#Create function to scrape data

def scrape(date):

    #get url of the website that we want to scrape
    URL = 'https://coinmarketcap.com/historical/'+date

    #request to the website
    webpage = requests.get(URL)

    #parse text from website
    soup = BeautifulSoup(webpage.text, 'html.parser')

    # Set the amount of currencies I am finding for,
    topN = 10
    #find table row element
    tr = soup.find_all('tr', attrs={'class': 'cmc-table-row'})

    #COUNT variable for number of crypto that we want to scrape
    count = 0

    #Loop throw rows
    for row in tr:
        #check for count, break loop
        if count == topN:
            break
        count = count +1

        #store name of crypto into a variable
        #find td element
        name_column = row.find('td', attrs={'class': 'cmc-table__cell cmc-table__cell--sticky cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__name'})
        crypto_name = name_column.find('a', attrs={'class':'cmc-table__column-name--name cmc-link'}).text.strip()
        #store the coin market cap of crypto into a variable

        crypto_market_cap = row.find('td', attrs={'class':'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__market-cap'}).text.strip()

        #find and store crypto price
        crypto_price = row.find('td', attrs={'class':'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__price'}).text.strip()

        #find and store the crypto supply and symbol
        crypto_circulating_supply_and_symbol = row.find('td', attrs={'class':'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__circulating-supply'}).text.strip()
       
        #split data
        crypto_circulating_supply = crypto_circulating_supply_and_symbol.split(' ')[0]
        crypto_symbol = crypto_circulating_supply_and_symbol.split(' ')[1]

        # append data to list. 
        crypto_name_list.append(crypto_name)
        crypto_market_cap_list.append(crypto_market_cap)
        crypto_price_list.append(crypto_price)
        crypto_circulating_supply_list.append(crypto_circulating_supply)
        crypto_symbol_list.append(crypto_symbol)

#Insert date you are looking for here
enquiry_date = '20221219'

#scrape function 
scrape(date=enquiry_date)

# Store data into dataframe
df['Name'] = crypto_name_list
df['Market Cap'] = crypto_market_cap_list
df['Price'] = crypto_price_list
df['Circulating Supply'] = crypto_circulating_supply_list
df['symbol'] = crypto_symbol_list
print(df)

# Further implementations: use flask to show on webpage
# html_table = df.to_html()


