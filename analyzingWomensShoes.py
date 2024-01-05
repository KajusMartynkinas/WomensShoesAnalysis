import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv

ebay_df = pd.read_csv('ebay.csv')
ali_df = pd.read_csv('aliExpress.csv')


while True:
    def show_1():
        average_price_ebay = ebay_df['price'].mean()
        average_price_ali = ali_df['price'].mean()
        plt.style.use('dark_background')
        plt.bar('eBay', average_price_ebay, color='lime')
        plt.bar('AliExpress', average_price_ali, color='magenta')
        plt.xlabel('Platform')
        plt.ylabel('Average Price')
        plt.title('Average Price Comparison Between eBay and AliExpress')
        plt.show()


    def show_2():
        plt.style.use('dark_background')
        sold_ebay = ebay_df['sold'].sum()
        sold_ali =ali_df['sold'].sum()
        plt.bar('eBay', sold_ebay, color='lime')
        plt.bar('AliExpress', sold_ali, color='magenta')
        plt.xlabel('Platform')
        plt.ylabel('Amount Sold')
        plt.title('Amount of Sales from Each Platform')
        plt.show()


    def show_3():
        top15_ebay = ebay_df.nlargest(15, 'price')
        top15_ali = ali_df.nlargest(15, 'price')
        ebay_x = np.arange(len(top15_ebay))
        aliexpress_x = np.arange(len(top15_ali)) + len(top15_ebay)
        plt.style.use('dark_background')
        plt.figure(figsize=(10, 6))
        plt.scatter(ebay_x, top15_ebay['price'], color='lime', label='eBay')
        plt.scatter(aliexpress_x, top15_ali['price'], color='magenta', label='AliExpress')
        plt.plot(ebay_x, top15_ebay['price'], color='green', alpha=0.5)
        plt.plot(aliexpress_x, top15_ali['price'], color='purple', alpha=0.5)
        plt.ylabel('Price')
        plt.title('Top 15 Most Expensive Products on eBay and AliExpress')
        plt.xticks([])
        plt.legend()
        plt.show()


    def show_4():
        top15_ebay = ebay_df.nsmallest(15, 'price')
        top15_ali = ali_df.nsmallest(15, 'price')
        ebay_x = np.arange(len(top15_ebay))
        aliexpress_x = np.arange(len(top15_ali)) + len(top15_ebay)
        plt.style.use('dark_background')
        plt.figure(figsize=(10, 6))
        plt.scatter(ebay_x, top15_ebay['price'], color='lime', label='eBay')
        plt.scatter(aliexpress_x, top15_ali['price'], color='magenta', label='AliExpress')
        plt.plot(ebay_x, top15_ebay['price'], color='green', alpha=0.5)
        plt.plot(aliexpress_x, top15_ali['price'], color='purple', alpha=0.5)
        plt.ylabel('Price')
        plt.title('Top 15 Cheapest Products on eBay and AliExpress')
        plt.xticks([])
        plt.legend()
        plt.show()


    def show_5():
        ebay_df['platform'] = 'eBay'
        ali_df['platform'] = 'AliExpress'
        combined_df = pd.concat([ebay_df, ali_df])
        bins = [0, 20, 50, 100, 150, 200, 300, float('inf')]
        labels = ['0-20', '21-50', '51-100', '101-150', '151-200', '201-300', '300+']
        combined_df['price_range'] = pd.cut(combined_df['price'], bins=bins, labels=labels)
        price_range_counts = combined_df.groupby(['platform', 'price_range']).size().unstack(fill_value=0)
        plt.style.use('dark_background')
        price_range_counts.T.plot(kind='bar', figsize=(12, 10), color=['magenta', 'lime'])
        plt.xlabel('Price Range')
        plt.ylabel('Number of Products')
        plt.title('Product Counts in Price Ranges for eBay and AliExpress')
        plt.xticks(rotation=45)
        plt.show()


    print("Select the graph that you want to be displayed:")
    print("1: Average Price Comparison Between eBay and AliExpress")
    print("2: The Sum of Sales for Each Platform")
    print("3: Top 15 Most Expensive Products on eBay and AliExpress")
    print("4: Top 15 Cheapest Products on eBay and AliExpress")
    print("5: Product Counts in Price Ranges for eBay and AliExpress")
    print("0: Exit program")
    print("Enter the number of your choice: \n")
    choice = input()

    if choice == '1':
        show_1()
    elif choice == '2':
        show_2()
    elif choice == '3':
        show_3()
    elif choice == '4':
        show_4()
    elif choice == '5':
        show_5()
    elif choice == '0':
        print('The program is closing. Goodbye')
        break
    else:
        print('Incorrect choice. Try again: \n')
