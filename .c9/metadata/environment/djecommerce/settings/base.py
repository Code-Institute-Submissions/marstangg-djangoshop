{"filter":false,"title":"base.py","tooltip":"/djecommerce/settings/base.py","undoManager":{"mark":20,"position":20,"stack":[[{"start":{"row":9,"column":0},"end":{"row":9,"column":12},"action":"remove","lines":["DEBUG = True"],"id":40},{"start":{"row":8,"column":0},"end":{"row":9,"column":0},"action":"remove","lines":["",""]},{"start":{"row":7,"column":0},"end":{"row":8,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":34,"column":61},"end":{"row":35,"column":0},"action":"insert","lines":["",""],"id":41},{"start":{"row":35,"column":0},"end":{"row":35,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":35,"column":4},"end":{"row":36,"column":0},"action":"insert","lines":["'whitenoise.middleware.WhiteNoiseMiddleware'",""],"id":42}],[{"start":{"row":86,"column":0},"end":{"row":86,"column":74},"action":"insert","lines":["DATABASES = {'default': dj_database_url.parse(<DATABASE_URL_FROM_HEROKU>)}"],"id":43}],[{"start":{"row":86,"column":48},"end":{"row":86,"column":71},"action":"remove","lines":["ATABASE_URL_FROM_HEROKU"],"id":44},{"start":{"row":86,"column":47},"end":{"row":86,"column":48},"action":"remove","lines":["D"]}],[{"start":{"row":86,"column":47},"end":{"row":86,"column":201},"action":"insert","lines":["postgres://svfgilawsqtkgd:2ebf7427fbb222594def4303bd257ce7debf08d11503d68402fdc4be3cc96778@ec2-174-129-229-106.compute-1.amazonaws.com:5432/d7b5271hpb2prj"],"id":45}],[{"start":{"row":86,"column":46},"end":{"row":86,"column":47},"action":"remove","lines":["<"],"id":46}],[{"start":{"row":86,"column":200},"end":{"row":86,"column":201},"action":"remove","lines":[">"],"id":47}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":22},"action":"insert","lines":["import dj_database_url"],"id":50}],[{"start":{"row":2,"column":22},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":51}],[{"start":{"row":87,"column":46},"end":{"row":87,"column":202},"action":"remove","lines":["postgres://svfgilawsqtkgd:2ebf7427fbb222594def4303bd257ce7debf08d11503d68402fdc4be3cc96778@ec2-174-129-229-106.compute-1.amazonaws.com:5432/d7b5271hpb2prj)}"],"id":52}],[{"start":{"row":87,"column":0},"end":{"row":87,"column":46},"action":"remove","lines":["DATABASES = {'default': dj_database_url.parse("],"id":53},{"start":{"row":87,"column":0},"end":{"row":87,"column":81},"action":"insert","lines":["DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)"]}],[{"start":{"row":86,"column":0},"end":{"row":87,"column":81},"action":"remove","lines":["","DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)"],"id":54}],[{"start":{"row":86,"column":0},"end":{"row":87,"column":0},"action":"insert","lines":["",""],"id":55}],[{"start":{"row":87,"column":0},"end":{"row":88,"column":0},"action":"insert","lines":["DATABASES = {'default': dj_database_url.parse(<DATABASE_URL_FROM_HEROKU>)}",""],"id":56}],[{"start":{"row":87,"column":46},"end":{"row":87,"column":72},"action":"remove","lines":["<DATABASE_URL_FROM_HEROKU>"],"id":57}],[{"start":{"row":87,"column":46},"end":{"row":87,"column":198},"action":"insert","lines":["postgres://tqujzlaayqipzb:e80c9c3f244ce69442fb2857bbae039b85759488ae6d2a334eca4d2a14bce382@ec2-54-225-205-79.compute-1.amazonaws.com:5432/d1omtc0sreomca"],"id":58}],[{"start":{"row":87,"column":46},"end":{"row":87,"column":47},"action":"insert","lines":["'"],"id":59}],[{"start":{"row":87,"column":199},"end":{"row":87,"column":200},"action":"insert","lines":["'"],"id":61}],[{"start":{"row":87,"column":47},"end":{"row":87,"column":199},"action":"remove","lines":["postgres://tqujzlaayqipzb:e80c9c3f244ce69442fb2857bbae039b85759488ae6d2a334eca4d2a14bce382@ec2-54-225-205-79.compute-1.amazonaws.com:5432/d1omtc0sreomca"],"id":62}],[{"start":{"row":87,"column":47},"end":{"row":87,"column":201},"action":"insert","lines":["postgres://svfgilawsqtkgd:2ebf7427fbb222594def4303bd257ce7debf08d11503d68402fdc4be3cc96778@ec2-174-129-229-106.compute-1.amazonaws.com:5432/d7b5271hpb2prj"],"id":63}]]},"ace":{"folds":[],"scrolltop":969.5,"scrollleft":0,"selection":{"start":{"row":85,"column":35},"end":{"row":85,"column":35},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":56,"state":"start","mode":"ace/mode/python"}},"timestamp":1567720948364,"hash":"92355bb826332739c390babe7ecba2a83c8a7c51"}