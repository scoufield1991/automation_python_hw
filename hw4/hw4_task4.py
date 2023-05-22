import re

""" 4. you have html page markup, convert it to structure 
[('google', 'www.google.com', 'Google'), 
('facebook', 'http://facebook.com/dign-in', ' Facebook'), 
('amazon', 'amazon.com', 'Amazon')] using only regular expressions. 
The first element of the tuple is the id of the container the link is in, the second is the link, and the third is the text of the link
"""

html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My super star task</title>
</head>
<body>
    <div id="block-with-links">
        <div id="google">
            <a href="www.google.com">
                Google
            </a>
        <div/>
        <div id="facebook">
            <a href="http://facebook.com/dign-in">
                Facebook
            </a>
        </div>
            <div id="amazon">
                <a href="amazon.com">
                    Amazon
                </a>
            </div>
        </div>
    </div>
</body>
</html>
'''

pattern_urls = r'\b(?:https?:\/\/)?(?:www\.)?([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)\b'
list_urls = re.findall(pattern_urls, html)
pattern_id = r'\b(google|facebook|amazon)\b(?![.])'
list_id = re.findall(pattern_id, html)
pattern_names = r'\b(Google|Facebook|Amazon)\b(?![.])'
list_names = re.findall(pattern_names, html)

structure_list = []
for index in range(3):
    structure_list.append((list_id[index], list_urls[index], list_names[index]))

print(f'Structure: {structure_list}')
