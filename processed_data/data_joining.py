import sys
def add_row_id(filename):
    row = 0
    with open(filename) as file:
        for line in file:
            print(row, line, end = '')
            row += 1

def select_over4k(filename):
    bus_over_4k=["ujHiaprwCQ5ewziu0Vi9rw","iCQpiavjjPzJ5_3gPD5Ebg","K7lWdNUhCbcnEvI0NhGewg",
          "f4x1YBxkLrZg652xt2KR5g","rcaPajgKOJC2vo_l3xa42A","5LNZ67Yw9RD6nf4_UhXOjw",
          "DkYS3arLOhA8si5uUEmHOw","RESDUcs7fIiihp38-d6_6g","4JNXUYY8wbaaDmk3BPzlWw",
          "KskYqH1Bi7Z_61pH6Om8pg","eoHdUeQDNgQ6WYEnP2aiRw","cYwJA2A6I12KNkm2rtXd5g",
          "El4FC8jcawUVgw_0EIcbaQ","2weQS-RnoOBhb1KsHKyoSQ","AV6weBrZFFBfRGCbcRGO4g"]

    with open(filename) as file:
        for line in file:
            bus_id = eval(line)['business_id']
            if bus_id in bus_over_4k:
                print(line, end = '')

def join(filename1,filename2):
    '''@ filename1 : restaurant_reviews_withkey.txt 
    @filename2 : textblob_score_full_withkey.txt 
    '''
    with open(filename1) as file1:
        with open(filename2) as file2:
            for line1, line2 in zip(file1, file2):
                row_id, dic = line1.split(' ',1)
                row_id2, score = line2.split(' ',1)
                score = float(str(score).strip()) #delete newline sign
                dic = eval(dic)
                #bus_id = dic['business_id']
                #text = dic['text'].replace('\n', '')
                #stars = dic['stars']
                #date = dic['date']
                print(row_id, score, dic)
                

join('restaurant_reviews_withkey.txt', 'textblob_score_full_withkey.txt' )
