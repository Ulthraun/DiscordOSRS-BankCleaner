def main():
    s1 = "+sell "
    product = {}
    count = {}
    with open('Usernames_Bank.txt', 'r') as f:
        test = f.readline()
        result = process_line(test)
        product = [line.strip('\n') for line in f]
        out = list(map(process_line, product))
    with open('Usernames_Bank.txt', 'w') as f:
        f.writelines(["%s\n" % i for i in out])
    print('Success!')
def process_line(line):
    product, count = str(line).split(':')
    return f'+sell {count} {product} --cf          '
main()

