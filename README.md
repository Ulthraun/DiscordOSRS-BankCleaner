# Discord OSRS Bank Cleaner

Takes the text file from +b --text --full and converts the list into a +sell itemName --cf format.

### Prerequisites
Notepad/Notepad++ works better though.

### Setup and use
1. ) Download the python program and put it into a file of your choice. 
1. ) Go to discord, type +b --text --full, download the generated text file
from the Old school bot. 
1. ) Right click the python program and click edit.
1. ) In the notepad, change "Usernames_bank.txt" to your "username_bank.txt" i.e "Trogdors_Bank.txt"
```python
     #Line number                  #Line Description
          5         with open('**Usernames_Bank.txt**', 'r') as f:
         10         with open('**Usernames_Bank.txt**', 'w') as f:
 ```
 to
 ```python
     #Line number                  #Line Description
          5         with open('**Trogdors_Bank.txt**', 'r') as f:
         10         with open('**Trogdors_Bank.txt**', 'w') as f:
 ```
1. ) Save the file, run the file, open up the text file in regards to your bank. 
1. ) Make sure you delete any entries that you DON'T want to sell, and untradables.
1. ) Copy and paste to your hearts content and clean that bank out!

## Built With
[IDLE 3.7](https://www.python.org/downloads/) - The program used to code this.

## Contributing
Please read [CONTRIBUTING](https://github.com/Ulthraun/DiscordOSRS-BankCleaner/blob/master/CONTRIBUTING) for details on the code of conduct, and the process for submitting pull requests to me.

## Versioning
There will only be one version of this small program as I don't plan on updating or changing anything in it personally.

## Authors
Ulthraun#4139 - UlthraunTheSecond@gmail.com

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Ulthraun/DiscordOSRSBankCleaner/blob/master/LICENSE) file for details

## Acknowledgments

* Ulthraun - Developer
* Discord OSRS
