#!/usr/bin/env python
# -*- coding: utf-8 -*-
# remove a article from the index index

import sys
import config

input_xml_file_name = config.input_xml_file_name

sys.path.append('..')
from whoosh.qparser import QueryParser
from whoosh.index import open_dir


if len(sys.argv) > 1:
    article_title = sys.argv[1]
else:
    print "Usage remove_from_index.py article"

ix = open_dir("index_dir")

query = QueryParser("title", ix.schema).parse("'%s'" % unicode(article_title))
ix.delete_by_query(query)
ix.writer().commit()
