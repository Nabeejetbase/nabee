import requests
import bs4

def get_website():
	url = 'https://www.pref.miyazaki.lg.jp/police/licence/update/20200417154936.html'
	file = 'license.txt'

	res = requests.get(url)
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.content,"html.parser")# Parser
	elems = soup.find("p",{"class":"data text-right"})#最新のタグの中身を取得
	str_elems = str(elems.string) # stringに変換
	#print (str_elems)
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