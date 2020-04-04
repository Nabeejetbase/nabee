import requests
import bs4

def get_website():
	url = 'https://www.soumu.go.jp/main_sosiki/jichi_gyousei/koumuin_seido/shushoku_hyogaki_shien.html'
	file = 'notifdata.txt'

	res = requests.get(url)
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.content,"html.parser")# Parser
	elems = soup.find("span",{"class":"aly_tx_f_red"})#最新のタグの中身を取得
	str_elems = str(elems.string) # stringに変換
	try:
		f = open(file)
		old_elems  = f.read()
	except:
		old_elems = ' '
	if(str_elems == old_elems):
		return False
	else:
		f = open(file, 'w') # 上書きする
		f.writelines(str_elems)
		f.close()
		return True

if __name__ == "__main__":
    	if(get_website()):
		        print("False") #通知処理