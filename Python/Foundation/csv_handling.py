import csv

with open(r"C:\Users\AnudipCOA\Desktop\file_handling\data.csv","a",newline="") as file:
    # reader=csv.reader(file)
    # for row in file:
    #     print(row)
    # print(file)
    # reader=csv.DictReader(file)
    # for row in reader:
    #     print(row["Name"])

    # writer=csv.writer(file)
    # writer.writerow(["Logesh","cse"])
    #   writer = csv.writer(file)
    #   writer.writerows([["usha","bca"],["vasu","maths"]])
        header_rows=["Name","Dept"]
        writer=csv.DictWriter(file,fieldnames=header_rows)
        writer.writeheader()
        writer.writerow({"Name":"Selvam","Dept":"cse"})
