# test_telegram_admin
template admin panel for telegram


create ".env" file with:  
+ BOT_TOKEN = bot_tocken  
+ DB_NAME = "sqllite.db"  
+ SUPER_ADMIN = id_telegram_user @userinfobot  
+ LOG_LEVEL = [CRITICAL=50,ERROR=40,WARNING=30,INFO=20,DEBUG=10,NOTSET=0]
+ + exemple: LOG_LEVEL = 40

DOCKER run
+ install docker
+ cd to this directory
+ build image: sudo docker build -t telega .
+ run docker conteiner
+ + with rm stoped conteiner:  sudo docker run -v $(pwd):/opt/test_telegram_admin --rm -d telega
+ + always run: sudo docker run -v $(pwd):/opt/test_telegram_admin -d --restart unless-stopped --name telega_con telega