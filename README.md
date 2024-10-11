# SQLi-DS

# Programın Açıklaması:

# 1. Arama Motorları: Google, Bing, Yahoo gibi farklı arama motorlarını kullanabilirsiniz. args.engine ile seçilebilir.


# 2. Proxy Desteği: Proxilerle arama motorlarına bağlanabilir, böylece IP adresinizi gizleyebilirsiniz. args.proxy parametresi ile aktif hale getirilebilir.


# 3. Sonuçları Dosyaya Kaydetme: Dork başına bulunan bağlantıları bir dosyaya (results.txt) kaydeder.


# 4. Rate Limiting: Google’ın sizi engellemesini önlemek için args.rate ile her isteğin arasında belirli bir süre (varsayılan: 5 saniye) bekleyebilirsiniz.


# 5. Komut Satırı Kullanımı: Aracı komut satırı üzerinden esnek bir şekilde kullanabilirsiniz.



# Örnek Komut Satırı Kullanımı:

# Tek bir dork ile arama yapmak:

python sql_dork_tool.py -d "inurl:index.php?id=" -e google -r 10

# Bir dork listesini bir dosyadan yüklemek ve proxy ile kullanmak:

python sql_dork_tool.py -d dork_list.txt -e bing -p -r 15


# Gelişmiş Özellikler:

# 1. Proxy Kullanımı: Proxy desteği ile IP adresinizi gizleyerek aramalar yapabilirsiniz. Proxileri kendiniz PROXIES listesine ekleyebilirsiniz.


# 2. Çoklu Arama Motoru: Google, Bing, Yahoo gibi arama motorlarını seçerek arama yapabilirsiniz.


# 3. Sonuçları Kaydetme: Her dorkun arama sonuçları belirttiğiniz bir dosyaya kaydedilir.


# 4. Kapsamlı Rate Limiting: İstek hızını kontrol ederek Google’ın sizi engellemesini engelleyebilirsiniz.


# KESİNLİKLE OKU (MUST READ!!!)

# Bu araç kullanıcıya profesyonel bir yapı sunmakta ve güvenlik testi veya eğitim amacıyla kullanılabilir. İzinsiz tarama ve SQL saldırıları yasadışıdır, bu yüzden etik hacking kurallarına dikkat edin. Herhangi bir izinsiz tarama ve SQL saldırısından Şahsım sorumlu değildir ve yükümlülük kabul etmeyeceğim !!!
