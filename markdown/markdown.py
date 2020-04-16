import re

def parse(markdown):
    return Markdown(markdown).parse()

class Markdown:
    def __init__(self, markdown):
        self.markdown = markdown

    def parse(self):
        self.__strong_tag()
        self.__em_tag()
        self.__header_tag()
        self.__li_tag()
        self.__ul_tag()
        self.__p_tag()

        self.markdown = re.sub(r'\n', '', self.markdown)
        
        return self.markdown
    
    def __strong_tag(self):
        self.markdown = re.sub(r'__([^\n]+?)__', r'<strong>\1</strong>', self.markdown)

    def __em_tag(self):
        self.markdown = re.sub(r'_([^\n]+?)_', r'<em>\1</em>', self.markdown)

    def __header_tag(self):
        for i in range(6, 0, -1):
            self.markdown = re.sub(r'^{} (.*?$)'.format('#' * i), r'<h{0}>\1</h{0}>'.format(i), self.markdown, flags=re.M)
            
    def __li_tag(self):
        self.markdown = re.sub(r'^\* (.*?$)', r'<li>\1</li>', self.markdown, flags=re.M)

    def __ul_tag(self):
        self.markdown = re.sub(r'(<li>.*</li>)', r'<ul>\1</ul>', self.markdown, flags=re.S)

    def __p_tag(self):
        self.markdown = re.sub(r'^(?!<[hlu])(.*?$)', r'<p>\1</p>', self.markdown, flags=re.M)


