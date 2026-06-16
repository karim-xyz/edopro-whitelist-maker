import requests, sys
from yaspin import yaspin

start_date = input("banlist date [yyyy-mm]: ")
date = start_date[:4]+"."+start_date[6:]

filename = f"{date}.lflist.conf"

ban_url = f"https://yugioh-banlists-api.onrender.com/api/v1/{start_date}"

all_url = "https://db.ygoprodeck.com/api/v7/cardinfo.php"

spinner = yaspin(text="generating file")

def getBanlist(url, date, filename):
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        spinner.stop()
        print("no internet connection")
        sys.exit()
    if response.status_code == 200:
        banlist_data = response.json()
        if banlist_data is None:
            spinner.stop()
            print("no such banlist")
            sys.exit()
        else:
            format_ = " "+banlist_data['format']
            if format_ != " ":
                filename = format_
            with open(filename, 'w') as f:
                f.write(f"#[{date}{format_}]\n")
                f.write(f"!{date}{format_}\n")
                f.write("$whitelist\n")
            global end_date
            end_date = banlist_data['endDate']
            global list_
            list_ = []

            with open(filename, 'a') as f:
                f.write(f"#forbidden\n")
                for card in banlist_data['forbidden']:
                    f.write(str(card['id'])+" 0 --"+card['name']+"\n")
                    list_.append(card['id'])
                f.write(f"#limited\n")
                for card in banlist_data['limited']:
                    f.write(str(card['id'])+" 1 --"+card['name']+"\n")
                    list_.append(card['id'])
                f.write(f"#semi limited\n")
                for card in banlist_data['semiLimited']:
                    f.write(str(card['id'])+" 2 --"+card['name']+"\n")
                    list_.append(card['id'])


def getCards(url, end_date, filename):
    url = f"{url}?enddate={end_date}&dateregion=tcg"
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        spinner.stop()
        print("no internet connection")
        sys.exit()
    if response.status_code == 200:
        cards = response.json()
        with open(filename, 'a') as f:
            f.write("#unlimited\n"  )
            for card in cards['data']:
                if card['id'] not in list_:
                    f.write(str(card['id'])+ " 3 --"+ card['name']+"\n")        
    else:
        spinner.stop()
        print("error ", str(response.status_code))
        sys.exit()

spinner.start()
getBanlist(ban_url, date, filename)
getCards(all_url, end_date, filename)
spinner.stop()
print("Done")

