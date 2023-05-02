import os
import json
import pip

# pip.main(["install", "--upgrade", "pandas"])
# pip.main(["install", "pandasql"])
pip.main(["install", "SQLAlchemy==1.4.46"])

import pandas as pd
from pandasql import sqldf

pysqldf = lambda q: sqldf(q, globals())

list_data = []

image_path = "/mnt/gpfs2_4m/scratch/sgu260/CS585/BLIP/iudataset/images_normalized/"
projections_path = "/mnt/gpfs2_4m/scratch/sgu260/CS585/BLIP/iudataset/indiana_projections.csv"
reports_path = "/mnt/gpfs2_4m/scratch/sgu260/CS585/BLIP/iudataset/indiana_reports.csv"

dir_list = os.listdir(image_path)

proj = pd.read_csv(projections_path)
rep = pd.read_csv(reports_path)
rep = rep.astype({'uid': 'string'})

q1 = "SELECT * from proj where projection = 'Frontal';"
frontal = pysqldf(q1)
frontal = frontal.astype({'uid': 'string'})

for index, row in frontal.iterrows():
    uid = row["uid"]
    img_name = row["filename"]

    q2 = "SELECT findings from rep where rep.uid = " + uid
    finding_tbl = pysqldf(q2)
    finding = finding_tbl["findings"][0]

    if finding is not None:
        finding = finding.lower()
        finding = finding.replace("xxxx", "")
        if img_name in dir_list:
            dictionary = {'image': image_path + img_name, 'caption': finding}
            list_data.append(dictionary)
        else:
            print(img_name, " could not be found")
    else:
        print(uid, " null finding")

json_str = json.dumps(list_data)
with open('/project/rvkavu2_uksr/sgu260/CS585/final_project/IUdata_updated.json', 'w') as f:
    json.dump(list_data, f)
