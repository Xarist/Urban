import re


def extract_image_links(html_text):
    img_url_pattern = re.compile(r'<img\s+[^>]*src=[\'"](https?://[^\'"]*\.(?:jpg|jpeg|png|gif))[\'"]', re.IGNORECASE)
    img_urls = img_url_pattern.findall(html_text)
    return img_urls


html_text = "<img src='https://example.com/image1.jpg'> <img src='http://example.com/image2.png'> <img src='https://example.com/image3.gif'>"
image_links = extract_image_links(html_text)
list_links = []
if image_links:
    for image_link in image_links:
        list_links.append(image_link)
else:
    print('Нет ссылок с картинками в HTML тексте')
print(*list_links, sep='\n')
