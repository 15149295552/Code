import csv

with open("python.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["步惊云,你真帅", 35, "绝世好剑"])


f = open("python.csv", "a")
writer = csv.writer(f)
writer.writerow(["聂风,你真酷", 35, "血饮狂刀"])
f.close()




