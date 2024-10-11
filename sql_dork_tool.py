# EDİT BY S4NR1

import requests
from bs4 import BeautifulSoup
import time
import random
import argparse

# Proxy desteği için gerekli modül
from itertools import cycle

# Arama motoru URL'leri
SEARCH_ENGINES = {
    "google": "https://www.google.com/search?q=",
    "bing": "https://www.bing.com/search?q=",
    "yahoo": "https://search.yahoo.com/search?p="
}

# Proxy desteği (isteğe bağlı, kullanıcı proksi ekleyebilir)
PROXIES = ["http://proxy1.com", "http://proxy2.com"] # Bu listeyi güncelleyebilirsiniz.

# Proxy döngüsü için
proxy_pool = cycle(PROXIES)

# Kullanıcı aracısı (User-Agent) sahteciliği
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'
]

# Google'dan arama sonuçlarını çeker
def search_query(query, engine="google", use_proxy=False):
    headers = {
        'User-Agent': random.choice(USER_AGENTS)
    }

    if engine not in SEARCH_ENGINES:
        print(f"Arama motoru {engine} desteklenmiyor. Google varsayılan olarak kullanılacak.")
        engine = "google"

    url = SEARCH_ENGINES[engine] + query

    # Proxy kullanma seçeneği
    if use_proxy:
        proxy = next(proxy_pool)
        proxies = {
            "http": proxy,
            "https": proxy
        }
        response = requests.get(url, headers=headers, proxies=proxies)
    else:
        response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        return soup
    else:
        return None

# Bağlantıları ayıklar
def extract_links(soup):
    links = []
    for item in soup.find_all('a'):
        href = item.get('href')
        if href and "url?q=" in href:
            links.append(href.split("url?q=")[1].split("&")[0])
    return links

# Sonuçları dosyaya kaydet
def save_results(filename, dork, links):
    with open(filename, "a") as file:
        file.write(f"\nDork: {dork}\n")
        for link in links:
            file.write(link + "\n")

# Komut satırı argümanlarını ayarla
def parse_args():
    parser = argparse.ArgumentParser(description="SQL Dork Arama Tarayıcısı")
    parser.add_argument("-d", "--dork", help="SQL dorkunu girin veya dork listesini dosyadan yükleyin.", required=True)
    parser.add_argument("-e", "--engine", help="Kullanılacak arama motorunu seçin (google, bing, yahoo).", default="google")
    parser.add_argument("-o", "--output", help="Sonuçları kaydetmek için dosya adı.", default="results.txt")
    parser.add_argument("-p", "--proxy", help="Proxy kullanarak arama yapın.", action="store_true")
    parser.add_argument("-r", "--rate", help="Her istek arasında bekleme süresi (saniye).", type=int, default=5)
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    # Dorkları ya dosyadan oku ya da komut satırından al
    if args.dork.endswith(".txt"):
        with open(args.dork, "r") as file:
            dorks = [line.strip() for line in file.readlines()]
    else:
        dorks = [args.dork]

    # Her dork için arama yap
    for dork in dorks:
        print(f"Aranıyor: {dork}")
        soup = search_query(dork, engine=args.engine, use_proxy=args.proxy)
        
        if soup:
            links = extract_links(soup)
            print(f"Bulunan Linkler ({dork}):")
            for link in links:
                print(link)
            
            # Sonuçları kaydet
            save_results(args.output, dork, links)
        else:
            print(f"{dork} için arama yapılamadı.")
        
        # Rate limiting (istek hızını kontrol etme)
        time.sleep(args.rate)
