import bs4
import requests

res = requests.get('https://www.bigbasket.com/pd/100401162/coca-cola-diet-coke-soft-drink-300-ml-can/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop')
# res.raise_for_status()
print(res.status_code)
soup = bs4.BeautifulSoup(res.text,'html.parser')
elems = soup.select('td.IyLvo')
elems = elems[0].text.strip()
print(elems)


