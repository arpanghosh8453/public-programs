from fillpdf import fillpdfs
import pandas as pd


CSV_DATA = "C:/Users/thisi/OneDrive/Desktop/data.csv"
TEMPLATE_PDF = "C:/Users/thisi/OneDrive/Desktop/pdf_template.pdf"
OUTPUT_FOLDER = "C:/Users/thisi/OneDrive/Desktop/test"

COMPANY_DATA_1 = "Konstad Legacysale"
COMPANY_DATA_2 = "923 326 693"
COMPANY_DATA_3 = "C. J. Hambroes Veg 9, 2816 Gjøvik"

#print(fillpdfs.get_form_fields(TEMPLATE_PDF))

df = pd.read_csv(CSV_DATA, engine='python', names=["name","address_1","address_2","date", "amount", "product","id"])

for index, row in df.iterrows():
    print("processing row >>> \n\n", row, "\n\n")
    data_dict = {
    'name': row['name'],
    'address': row["address_1"]+", "+row["address_2"],
    'date1': row['date'],
    'date2': row['date'],
    'data1': COMPANY_DATA_1,
    'data2': COMPANY_DATA_2,
    'data3': COMPANY_DATA_3,
    'product': row['product'],
    'price1': row['amount'],
    'price2': row['amount'],
    'id': row['id']

    }
    outfile_path = OUTPUT_FOLDER + "/" + row['date'] + " - " + row['name'] + ".pdf"
    fillpdfs.write_fillable_pdf(TEMPLATE_PDF, outfile_path , data_dict, flatten=True)
    print("successfully saved as ",outfile_path,"\n\n")