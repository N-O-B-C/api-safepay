import requests, os
import xlrd  
from xlutils.copy import copy
import xlsxwriter

def get_transaction():
    headers = {'content-type': 'application/json', 'x-access-token': "5443b693E341cb0ab695Xb8"}
    url = "https://safe-payy.herokuapp.com/api/v1/safepay/querypayment/initiated"

    try:
      
        r = requests.get(url=url, headers=headers)
        print(f"Status code: {r.status_code}") 
        response = r.json()
    except Exception as e:
        return f"Encountered error: {e}"

    if not response.get("status"):
        return response.get("message")

 
    records = response.get("data")   
    print(f"first record: {records[0]}")

    workbook = xlsxwriter.Workbook("samson.xlsx")
    worksheet = workbook.add_chartsheet("firstSheet")

    worksheet.write(0,0, "#")
    worksheet.write(0, 1, "initiating_date")
    worksheet.write(0, 2, "paymentref")
    worksheet.write(0,3, "merchant_id")
    worksheet.write(0,4, "business_name")
    worksheet.write(0,5, "product_amount")

    for index, entry in enumerate(records):
        worksheet.write(index+1, 0, str(index))
        worksheet.write(index+1, 1, entry["initiating_date"])
        worksheet.write(index+1, 2, entry["paymentref"])
        worksheet.write(index+1, 3, entry["merchant_id"])
        worksheet.write(index+1, 4, entry["business_name"])
        worksheet.write(index+1, 5, entry["product_amount"])

    workbook.close()


get_transaction()
