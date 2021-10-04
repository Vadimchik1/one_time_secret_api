# one_time_secret_api
Апи для приложения с одноразовыми секретами
HTTP сервис для одноразовых секретов наподобие https://onetimesecret.com/.

Позволяет создать секрет, задать кодовую фразу для его открытия и cгенерировать код, по которому можно прочитать секрет только один раз. 

Документация api:
    Метод /generate должен принимать секрет и кодовую фразу и отдавать secret_key по которому этот секрет можно получить.
    Метод /secrets/{secret_key} принимает на вход кодовую фразу и отдает секрет.

Посмотреть документацию можно по адресу:
 - 127.0.0.1:8000/swagger/

Для запуска приложения нужно ввести команду:
 - docker-compose up 

В качестве СУБД используется postgresql
