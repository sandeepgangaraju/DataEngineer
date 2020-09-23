import pandas as pd


#Reading data from website
csv_file = pd.DataFrame(pd.read_csv("http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/pp-monthly-update-new-version.csv", sep = ",", header = 0, index_col = False))

#adding header to the data
csv_file.columns = ["TUI","Price","Date_of_transfer","postcode","Property_Type","old_new","duration","PAON","SAON","street","locality","town_city","district","county","ppd_category_type","record_status"]

#converting the dataframe to multi line json file 
csv_file.to_json("C:/Users/Sandy/Desktop/sample4.json", orient = "records",lines = True)

#grouping the data by property
grouped_data = csv_file.groupby(["postcode"])


