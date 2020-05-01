def main():
    product = {}
    count = {}
    with open('Usernames_Bank.txt', 'r') as f:
        readFile = f.readline()
        result = process_line(readFile)
        product = [line.strip('\n') for line in f]
        out = list(map(process_line, product))
    with open('Usernames_Bank.txt', 'w') as f:
        f.writelines(["%s\n" % i for i in out])
def process_line(line):
    product, count = str(line).split(':')
    return f'+sell {count} {product} --cf'
main()

