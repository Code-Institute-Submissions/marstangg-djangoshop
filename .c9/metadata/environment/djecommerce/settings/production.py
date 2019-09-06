{"filter":false,"title":"production.py","tooltip":"/djecommerce/settings/production.py","undoManager":{"mark":13,"position":13,"stack":[[{"start":{"row":0,"column":0},"end":{"row":24,"column":52},"action":"insert","lines":["from .base import *","","DEBUG = config('DEBUG', cast=bool)","ALLOWED_HOSTS = ['ip-address', 'www.your-website.com']","","AUTH_PASSWORD_VALIDATORS = [","    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},","    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},","    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},","    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}","]","","DATABASES = {","    'default': {","        'ENGINE': 'django.db.backends.postgresql_psycopg2',","        'NAME': config('DB_NAME'),","        'USER': config('DB_USER'),","        'PASSWORD': config('DB_PASSWORD'),","        'HOST': config('DB_HOST'),","        'PORT': ''","    }","}","","STRIPE_PUBLIC_KEY = config('STRIPE_LIVE_PUBLIC_KEY')","STRIPE_SECRET_KEY = config('STRIPE_LIVE_SECRET_KEY')"],"id":1}],[{"start":{"row":3,"column":17},"end":{"row":3,"column":29},"action":"remove","lines":["'ip-address'"],"id":2}],[{"start":{"row":3,"column":17},"end":{"row":3,"column":86},"action":"insert","lines":["'2c7e37e20b7b4c91bc8f3bcf6508b0b0.vfs.cloud9.us-east-1.amazonaws.com'"],"id":3}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":15},"action":"insert","lines":["dj_database_url"],"id":4}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"insert","lines":["i"],"id":5},{"start":{"row":1,"column":1},"end":{"row":1,"column":2},"action":"insert","lines":["m"]},{"start":{"row":1,"column":2},"end":{"row":1,"column":3},"action":"insert","lines":["p"]},{"start":{"row":1,"column":3},"end":{"row":1,"column":4},"action":"insert","lines":["o"]},{"start":{"row":1,"column":4},"end":{"row":1,"column":5},"action":"insert","lines":["r"]},{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"insert","lines":["t"]}],[{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"insert","lines":[" "],"id":6}],[{"start":{"row":1,"column":22},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":7}],[{"start":{"row":4,"column":17},"end":{"row":4,"column":110},"action":"remove","lines":["'2c7e37e20b7b4c91bc8f3bcf6508b0b0.vfs.cloud9.us-east-1.amazonaws.com', 'www.your-website.com'"],"id":9}],[{"start":{"row":4,"column":17},"end":{"row":4,"column":18},"action":"insert","lines":["*"],"id":10}],[{"start":{"row":4,"column":17},"end":{"row":4,"column":18},"action":"insert","lines":["'"],"id":11}],[{"start":{"row":4,"column":19},"end":{"row":4,"column":20},"action":"insert","lines":["'"],"id":12}],[{"start":{"row":12,"column":0},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":16}],[{"start":{"row":11,"column":1},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":17},{"start":{"row":12,"column":0},"end":{"row":13,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":65},"action":"insert","lines":["SECRET_KEY = 'kobl@t=yw9d*0y%jt2gjnq78=u!z_rrxb&w8e47l!(jz@m79zy'"],"id":18}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":13,"column":65},"end":{"row":13,"column":65},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1567753887581,"hash":"07280e20af4f1f3250b3279ced2cc76a7128e7b8"}