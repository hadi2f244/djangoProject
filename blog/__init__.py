BlOG_CORE_APPS =[
    'blog.apps.blog',
    'blog.apps.article',
    'blog.apps.category',
    'blog.apps.comment',
  #  'blog.backEnd',
   # 'blog.frontEnd',

]

import os
BlOG_MAIN_TEMPLATE_DIR = os.path.join(
os.path.dirname(os.path.abspath(__file__)), 'templates')