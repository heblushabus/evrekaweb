import json

def html_to_txt(json_file, txt_file):
    """
    JSON dosyasındaki isim, soyisim ve açıklama bilgilerini okur ve
    HTML benzeri bir yapıda TXT dosyasına kaydeder.

    Args:
        json_file (str): Okunacak JSON dosyasının adı.
        txt_file (str): Yazılacak TXT dosyasının adı.
    """

    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Hata: {json_file} dosyası bulunamadı.")
        return
    except json.JSONDecodeError:
        print(f"Hata: {json_file} dosyası geçerli bir JSON dosyası değil.")
        return

    try:
        with open(txt_file, 'w', encoding='utf-8') as f:
            for item in data:
                isim = kerem(item.get('isim', ''))  # Eğer 'isim' yoksa boş string
                aciklama = item.get('aciklama', '')  # Eğer 'aciklama' yoksa boş string
                

                # HTML benzeri yapıyı oluştur
                f.write(f' <div id="w-node-cc1d5f45-7cd3-ef8d-f564-be9772f86680-18054bdb" class="team-card"><img src="img/{isim['id']}.webp" loading="lazy" sizes="100vw" alt="" class="team-member-image" />\n')
                f.write(f'    <div class="team-member-name-2">{isim['isim'].upper()} {isim['soyisim'].upper()}</div>\n')
                f.write(f'    <p>"{aciklama}" Yazarı </p>\n')
                f.write('</div>\n')
                f.write('\n')  # Her bir kart arasına boşluk bırak

        print(f"Veriler {txt_file} dosyasına başarıyla kaydedildi.")

    except Exception as e:
        print(f"Dosyaya yazma hatası: {e}")
def kerem(ad_soyad):
  """
  Verilen ad soyad bilgisinden isim, soyisim ve ID oluşturur.

  Args:
    ad_soyad: Ad soyad bilgisini içeren string.

  Returns:
    Bir sözlük (dictionary) döner. Sözlük, 'isim', 'soyisim' ve 'id' anahtarlarını içerir.
    Hata durumunda None döner.
  """
  try:
    ad_soyad_listesi = ad_soyad.split()
    if len(ad_soyad_listesi) < 2:
      print("Hata: Ad soyad bilgisi en az bir ad ve bir soyad içermelidir.")
      return None

    isim = " ".join(ad_soyad_listesi[:-1])  # Son kelime hariç tüm kelimeler isim
    soyisim = ad_soyad_listesi[-1]  # Son kelime soyisim
    id = isim.replace(" ", "").lower() + "-" + soyisim.lower() # Boşlukları silip küçük harfe çevirerek ID oluştur

    return {
        "isim": isim,
        "soyisim": soyisim,
        "id": id
    }
  except Exception as e:
    print(f"Hata: Bir hata oluştu: {e}")
    return None
# Örnek kullanım:
json_dosyasi = 'data.json'  # JSON dosyanızın adı
txt_dosyasi = 'cikti.txt'  # Oluşturulacak TXT dosyasının adı
html_to_txt(json_dosyasi, txt_dosyasi)