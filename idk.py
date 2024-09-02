meme_dict = {
            "CRINGE": "Garip veya utandırıcı şeye söylenir -çoğunlukla eskiden yaşanan utanç verici olaylara söylenir-",
            "LOL": "Laughing Out Loud -Sesli bir şekilde gülmek- -Birisi komik bir şey söylediğinde/gönderdiğinde bununla cevap verilebilir",
            "TTYL": "Talk To You Later -sonra konuşuruz-"
            }

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harferle yazın!)")

if word in meme_dict.keys():
    print (meme_dict[word])                                                                        
else:
    "Bu kelimeyi bilmiyorum ¯\_(ツ)_/¯"
