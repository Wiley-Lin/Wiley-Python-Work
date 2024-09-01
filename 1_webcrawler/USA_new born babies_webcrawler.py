"""
File: webcrawler.py
Name: Wiley Lin
Skills used in this file: webcrawler, for loops, conditional (if) statements.
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10905209
Female Number: 7949058
---------------------------
2000s
Male Number: 12979118
Female Number: 9210073
---------------------------
1990s
Male Number: 14146775
Female Number: 10644698
"""

import requests
from bs4 import BeautifulSoup


def main():
    """
    This function inputs data from website: https://www.ssa.gov/
    It reads the data of Popular names of the period (from 1990s - 2010s)

    Returns: The sum of the name's number belonging to each gender in that year.

    """
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #

        tags = soup.find_all('tbody')

        x = []
        boy_number = []
        boy_sum = 0
        girl_number = []
        girl_sum = 0
        for tag in tags:
            x = tag.text.split()

        # boy calculation
        for i in range(2, len(x)-20, 5):
            boy_number.append(x[i])
        for j in range(len(boy_number)):
            ans = ''
            for k in range(len(boy_number[j])):
                num = boy_number[j][k]
                if num != ',':
                    ans = ans + num
            boy_sum += int(ans)

        # girl calculation
        for i in range(4, len(x)-18, 5):
            girl_number.append(x[i])
        for j in range(len(girl_number)):
            ans = ''
            for k in range(len(girl_number[j])):
                num = girl_number[j][k]
                if num != ',':
                    ans = ans + num
            girl_sum += int(ans)
        print('Male Number: ' + str(boy_sum))
        print('Female Number: ' + str(girl_sum))


if __name__ == '__main__':
    main()
