import re, json, os
import pydicom as dicom

directory = "/mnt/gpfs2_4m/scratch/sgu260/mimic-cxr-2/physionet.org/files/mimic-cxr/2.0.0/files/p10/"

list_dir = os.listdir(directory)
list_files = []
for x in list_dir:
    path = directory + x
    if os.path.isdir(path):
        files = os.listdir(path)
        for y in files:
            path2 = path + "/" + y
            if os.path.isdir(path2):
                files2 = os.listdir(path2)
                for z in files2:
                    if z[-3:] == "dcm":
                        txt_file = y + ".txt"
                        if txt_file in files:
                            f = open(path + "/" + txt_file, "r")
                            line = f.read()
                            findings = re.search(r'FINDINGS:(.*)IMPRESSION:', line, re.DOTALL)
                            if findings:
                                caption = findings.group(1).strip()
                                caption = caption.replace("\n", "")
                            else:
                                print("Findings not found!")
                                continue
                            image_path = path2 + "/" + z
                            ds = dicom.dcmread(image_path)
                            view_pos = ds.get("ViewPosition", None)
                            if view_pos in ["AP", "PA"]:
                                image_path = image_path[:-3] + "png"
                                png_file_name = z[:-3] +"png"
                                if png_file_name in files2:
                                    temp_dic = {"image": image_path, "caption": caption}
                                    list_files.append(temp_dic)
                                else:
                                    print(image_path, " : not processed yet.")
                            else:
                                print(image_path, ": Image does not have frontal view")
                                continue

print(len(list_files))
with open('/project/rvkavu2_uksr/sgu260/CS585/final_project/train_mimic_p10.json', 'w') as f:
    json.dump(list_files, f)



