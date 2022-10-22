def main():
    fn = input("File Name >")
    fn2 = fn
    fn3 = fn
    fn += ".py"
    fn2 += ".bak"
    fn3 += "_filtered.py"
    f = open(fn, "r")
    data = f.read()
    # print(data)
    f.close()
    f=open(fn2,"w")
    f.write(data)
    f.close()
    data2 = []
    dataa = data.split("\n")
    for item in dataa:
        if "{" in item:
            item = item.replace('print("', 'print(f"')
        else:
            item = item
        data2.append(item)
    # print(data2)
    f = open(fn3, "w")
    for itemm in data2:
        f.write(itemm)
        f.write("\n")
    f.close()


main()
