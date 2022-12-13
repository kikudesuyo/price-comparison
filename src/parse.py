from html.parser import HTMLParser
class Parser(HTMLParser):
  def reset(self):
    super().reset()
    self.flag = False
    self.list = [
      {'attr': 'class', 'value': 'a-price-whole'},
      {'attr': 'id', 'value': 'productTitle'},
    ]

  def feed(self, data):
    super().feed(data)

  def handle_starttag(self, tag, attrs):
    if tag == 'span':
      for attr in attrs:
        for elm in self.list:
          if attr[0] == elm['attr'] and attr[1] == elm['value']:
            self.flag = True
    elif tag == 'img':
      if ('id', 'landingImage') in attrs:
        for attr in attrs:
          if attr[0] == 'src':
            print(attr[1])

  def handle_data(self, data):
    if self.flag:
      print(data)
      self.flag = False

with open('../data/apple-pencil.html', 'r') as f:
    parse = Parser()
    parse.feed(f.read())

# parse = Parser()
# parse.feed('<img id="landingImage" class="bar" src="https://example.png">')
