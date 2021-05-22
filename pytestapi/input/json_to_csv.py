import json
import csv

months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

with open('orders_data.json') as json_file:
    data = json.load(json_file)

fname=['customer.csv','customer_address.csv','customer_order_master.csv','customer_order_details.csv', 'payment_details.csv']

def json_to_csv(fname):
     for i in fname:
        with open(f'output/{i}',"w") as json_file:
            csv_file = csv.writer(json_file)

            if i == 'customer.csv':
                csv_file.writerow(["CustomerID", "First Name", "Last Name", "Customer Email"])
                for item in data["items"]:
                    csv_file.writerow([item["customer_id"], item["customer_firstname"], item["customer_lastname"],
                                       item["customer_email"]])

            elif i =='customer_address.csv':
                csv_file.writerow(
                    ["CustomerID", "AddressID", "Address Type", "Street Address", "City", "Region", "Country", "Postcode"])
                for item in data["items"]:
                    csv_file.writerow([item["customer_id"], item["entity_id"], item["billing_address"]["address_type"],
                               item["billing_address"]["street"][0], item["billing_address"]["city"],
                               item["billing_address"]["region"], item["billing_address"]["country_id"],
                               item["billing_address"]["postcode"]])

            elif i == 'customer_order_master.csv':
                csv_file.writerow(
                    ["OrderId", "CustomerId", "OrderDate", "PaymentId", "TotalQuantity", "GrandTotal", "TotalPaid",
                     "OrderStatus"])
                for item in data["items"]:
                    csv_file.writerow([item["items"][0]["order_id"], item["customer_id"], item["updated_at"],
                                       item["extension_attributes"]["payment_additional_info"][27]["value"],
                                       item["total_qty_ordered"], item["grand_total"], item["total_paid"],
                                       item["status"]])

            elif i == 'customer_order_details.csv':
                csv_file.writerow(
                    ["OrderId", "ProductId", "ProductType", "SKU", "ProductPrice", "OrderQuantity", "AnyDiscount",
                     "PriceDiscount"])
                for item in data["items"]:
                    csv_file.writerow(
                        [item["items"][0]["order_id"], item["items"][0]["product_id"], item["items"][0]["product_type"],
                         item["items"][0]["sku"], item["items"][0]["price"], item["items"][0]["qty_ordered"],
                         item["items"][0]["discount_amount"], item["items"][0]["discount_amount"]])

            elif i =='payment_details.csv':
                csv_file.writerow(
                    ["PaymentId", "CustomerId", "Method of Payment", "Amount Paid", "Card Type", "Card last 4 digits",
                     "Card Expiry Month Year"])
                for item in data["items"]:
                    csv_file.writerow(
                        [item["extension_attributes"]["payment_additional_info"][27]["value"], item["customer_id"],
                         item["payment"]["method"], item["payment"]["amount_paid"], item["payment"]["cc_type"],
                         item["payment"]["cc_last4"], str(months[int(item["payment"]["cc_exp_month"]) + 1] + '-' + str(
                            item["payment"]["cc_exp_year"]))])

json_to_csv(fname)



