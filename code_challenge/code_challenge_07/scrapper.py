import requests, json

def get_json(url):
    articles = []
    
    jsons = requests.get(url).json()['hits']

    for json in jsons:
        try:
            a_title = json['title']
            a_url = json['url']
            a_points = int(json['points'])
            if json['author']:
                a_author = json['author']
            else:
                a_author = 'deleted'                
            a_num_comments = int(json['num_comments'])
            a_object_id = json['objectID']
            article = {'a_title': a_title, 'a_url': a_url, 'a_points': a_points, 'a_author': a_author, 'a_num_comments': a_num_comments, 'a_object_id': a_object_id}
            articles.append(article)
        except:
            pass    
    return articles        


def get_repl(url):
    comment_head = []

    results = requests.get(url).json()
    title = results['title']
    points = results['points']
    author = results['author']
    url = results['url']
    comment = results['children']
    comment_head = {'c_title': title, 'c_points': points, 'c_author':author, 'c_url': url}
    comments = []
    for item in comment:
        if item['author']:
            author = item['author']
        else:
            author = 'deleted'
        text = item['text']
        reply = {'author': author, 'text':text}
        comments.append(reply)
    output = [comment_head, comments]
    return output