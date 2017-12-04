# minipx's weekend explore on ebay-finding-api

## This is a tiny project which use ebay SDK's finding API 'findItemsByProduct' to searching for an item with UPC and display the title and price.

#### _implemented in modules please see myEbayAPI.py_
		find_product(args.upc)
		generate_record(itemlist)
		draw_price_chart(df)
		draw_product_table(record)

#### _handled error for below please see commandline.png_
	    connection error
        missing commandline arg -upc error
        wrong UPC code error  [the sample working upc is "753759077600"]

* result is **_displayed in table using pandas please see commandline.png_**


* price on range is **_displayed in chart using matplotlib please see price.png_**


* **_Environment Setup_**

  - 1. download ebay-python-sdk

  - 2. virtualenv my_ebay

  - 3. source my_ebay/bin/activate

  - 4. cd /ebaysdk-python-master

  - 5. (my_ebay) $ python myEbayAPI.py 

  - 6. (my_ebay) $ pip install lxml

  - 7. (my_ebay) $ pip install pandas

  - 8. (my_ebay) $ sudo pip install matplotlib

  - 9. production URL - >svcs.ebay.com with App ID: …441b

  - 10. (my_ebay) $ python myEbayAPI.py -upc 753759077600



