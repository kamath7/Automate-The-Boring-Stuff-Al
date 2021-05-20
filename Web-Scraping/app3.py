import bs4,requests
def getPriceFromBB(prodUrl):
    res = requests.get(prodUrl)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('td.IyLvo')
    return elems[0].text.strip('')

print(getPriceFromBB('https://www.bigbasket.com/pd/100401162/coca-cola-diet-coke-soft-drink-300-ml-can/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop'))
print(getPriceFromBB('https://www.bigbasket.com/pd/100393567/red-bull-energy-drink-350-ml-can/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop'))