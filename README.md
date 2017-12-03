# ebay-searching-api

##This is a tiny project which use ebay SDK's finding API 'findItemsByProduct' to searching
##for an item with UPC and display the title and price.

###implemented in modulars please see myEbayAPI.py
		find_product(args.upc)
		generate_record(itemlist)
		draw_price_chart(df)
		draw_product_table(record)

###handled error for below please see commandline.png
		  connection error
          missing commandline argument error
          missing UPC argument error

###result is displayed in table using pandas please see table.png


###price on range is displayed in chart using matplotlib please see price.png


###Environment Setup

1)download ebay-python-sdk

2)virtualenv my_ebay

3)source my_ebay/bin/activate

4)cd /ebaysdk-python-master

5)(my_ebay) $ python myEbayAPI.py 

6)(my_ebay) $ pip install lxml

7)(my_ebay) $ pip install pandas

8)(my_ebay) $ sudo pip install matplotlib

9) production URL - >svcs.ebay.com with App ID: …441b

10)(my_ebay) $ python myEbayAPI.py



