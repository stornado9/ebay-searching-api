import sys
import argparse
import datetime
import json
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from collections import OrderedDict
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection
from ebaysdk.finding import Connection as Finding

def draw_product_table(record):
	with pd.option_context('display.max_rows', None, 'display.max_columns', None):
		column_title = ["title", "price"]
		df = pd.DataFrame(record)
		df.columns = column_title
		print(df)
		draw_price_chart(df)

def draw_price_chart(df):		
		column_price = df['price'].values
		column_price_remove_usd = [s.replace('USD ', '') for s in column_price]
		column_price_remove_usd = np.asarray(column_price_remove_usd)
		column_price_remove_usd = column_price_remove_usd.astype(np.float)
		print(column_price_remove_usd)
		
		plt.plot(column_price_remove_usd)
		plt.xlabel('price in USD')
		plt.ylabel('range of price')
		plt.title('simple drawing on the price')
		plt.savefig("price.png")
		plt.show()
		
def generate_record(itemlist):
	record = []
	for x in itemlist:
		subrecord = list()
		try:
			#print(x['title'], x['sellingStatus']['currentPrice']['_currencyId'] + ' ' + x['sellingStatus']['currentPrice']['value'],
			#x['shippingInfo'])
			subrecord.append(x['title'])
			subrecord.append(x['sellingStatus']['currentPrice']['_currencyId'] + ' ' + x['sellingStatus']['currentPrice']['value'])
			record.append(subrecord)		
			#print(subrecord)   		
		except:
			print("invalid record")
			pass
	draw_product_table(record)
	#return record		

def find_product(upc):
	try:
		api = Connection(domain='svcs.ebay.com', appid="PEGGYXUE-MySecond-PRD-551ca6568-4365441b", config_file=None)  
		response = api.execute('findItemsByProduct','<productId type="UPC">%s</productId>' % upc)
		data = response.dict()
		#print(data)
		
		if response.reply.ack == 'Failure':
			sys.exit('Error! %s' % response.reply.errorMessage.error.message)
			
		itemlist = data['searchResult']['item']
		record = generate_record(itemlist)
		#print(record)

	except ConnectionError as e:
		print(e)
		print(e.response.dict())
		
		
if __name__ == "__main__":	

		parser = argparse.ArgumentParser(description="Retrive product based on UPC")
		parser.add_argument("-upc", help="UPC for searching product")
		args = parser.parse_args()  
		find_product(args.upc)
			
	
	

	
    
