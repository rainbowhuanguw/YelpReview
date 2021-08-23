import json
import sys
import timeit

'''filtering restaurant from business dataset
'''

def line_counts(filename):
    '''output : line counts of a file'''
    with open(filename) as file:
        counts = len(file.readlines())
    return counts


def get_restaurants(filename, field):
    '''@filename : business.json
    @field: field needed to be matched
    output: lines of restaurant info'''

    #lookup_words: list of words needed to look up in the field
    lookup_words = ['restaurant', 'restaurants']
    no_words = ['hotels', 'hotels & travel','hotels and travel', 'casino']
    

    with open(filename) as file:
        for line in file:
            line = json.loads(line)

            try:
                categ = [cat.strip().lower() for cat in line[field].split(',')]
                intersect1 = list(set(lookup_words) & set(categ)) # lookup_words in category
                intersect2 = list(set(no_words) & set(categ)) # no_words not in category
                if len(intersect1) > 0 and len(intersect2) == 0:
                    print(line)
            except:
                continue


def get_restaurant_ids(filename):
    '''@filename: only_restaurants.txt
    output: a list of restaurant ids'''
    with open(filename) as file:
        #for line in file:
        #    print(eval(line)['business_id'])
        id_lst = [eval(line)['business_id'] for line in file]
    #print(id_lst)
    return id_lst


def get_restaurants_reviews(filename):
    '''@filename: review.json
    output: reviews for only restaurants
    '''
    id_lst = get_restaurant_ids('only_restaurants.txt')

    with open(filename) as file:
        for line in file:
            line = json.loads(line)
            try:
                if line['business_id'] in id_lst:
                    print(line)
            except:
                continue

def further_filter_reviews(filename):
    '''@filename:full_join.txt
    filter out reviews not in new id list'''
    
    id_lst = set(get_restaurant_ids('only_restaurants.txt'))
    
    with open(filename) as file:
        for line in file:
            ids, score, content = line.split(' ' , 2)
            content = eval(content)
            business_id = content['business_id']
            if business_id in id_lst:
                print(line, end = '')
        

def add_number_id(filename):
    '''@filename: review.json
    output: dictionary: (number, line)
    '''
    i = 0
    data_dic={}
    with open(filename) as file:
        for line in file:
            data_dic[i] = json.loads(line)
            i += 1
            if i> 500000:
                break
    print(data_dic)



def read_txt(filename):
    with open(filename) as file:
        count = 0
        for line in file:
            count += 1
            line = eval(line)
            if line['stars'] <= 3:
                print(line)
            if count > 5000:
                break


if __name__ == '__main__':
    #cleaning business.json
    #get_restaurants('business.json', 'categories')

    #compare lengths-business
    #print(line_counts('business.json'))
    #print(line_counts('only_restaurants.txt'))
    #print(line_counts('only_restaurant_reviews.txt'))
    print(line_counts('only_count_strip.txt'))

    #cleaning review.json
    #get_restaurants_reviews('review.json')
    #get_restaurant_ids('only_restaurants.txt')

    #compare lengths-review
    #print(line_counts('review.json'))
    #print(line_counts('restaurant_reviews.txt'))
    
    #add_number_id('review.json')

    #further_filter_reviews('full_join.txt')
 
