img_url = ''
def get_image(strategy,*arg, **kwargs):
    global img_url
    img_url = (kwargs['response'].get('image').get('url'))
    img_url = img_url[:-2]
    img_url += '250'
    # print(img_url)
def image():
    global img_url
    return img_url