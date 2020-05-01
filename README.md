# DiscordOSRSBankCleaner

Takes the text file from +b --text --full and converts the list into a +sell itemName --cf format.

### Prerequisites
Notepad/Notepad++ works better though.

### Setup and use
1. ) Download the python program and put it into a file of your choice. 
1. ) Go to discord, type +b --text --full, download the generated text file
from the Old school bot. 
1. ) Right click the python program and click edit.
1. ) In the notepad, change "Ulthrauns_bank.txt" to your "username_bank.txt" i.e "Trogdors_Bank.txt"
    *```
    1. def main():
    1.    s1 = "+sell "
    1.    product = {}
    1.    count = {}
    1.    with open('**Ulthrauns_Bank.txt**', 'r') as f:
    1.        test = f.readline()
    1.        result = process_line(test)
    1.        product = [line.strip('\n') for line in f]
    1.        out = list(map(process_line, product))
    1.    with open('**Ulthrauns_Bank.txt**', 'w') as f:
    1.        f.writelines(["%s\n" % i for i in out])
    1.    print('Success!')
    1. def process_line(line):
    1.    product, count = str(line).split(':')
    1.    return f'+sell {count} {product} --cf          '
    1. main()
    ```
1. ) Save the file, run the file, open up the text file in regards to your bank. 
1. ) Make sure you delete any entries that you DON'T want to sell, and untradables.
1. ) Copy and paste to your hearts content and clean that bank out!

## Built With
[IDLE 3.7](https://www.python.org/downloads/) - The program used to code this.

## Contributing
Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning
There will only be one version of this small program as I don't plan on updating or changing anything in it personally.

## Authors
Ulthraun#4139 - UlthraunTheSecond@gmail.com

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

Ulthraun - Developer
Discord OSRS
