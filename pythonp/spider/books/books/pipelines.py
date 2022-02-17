# -*- coding: utf-8 -*-

import json
import codecs

class BooksPipeline(object):
    def process_item(self, item, spider):
        self.file = codecs.open(item.get('title')+ '.txt', 'w', encoding='utf-8')
        self.file.write(item.get('desc') + '\n\f')
        return item

    def spider_closed(self, spider):
        self.file.close()