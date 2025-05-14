print("Hello World!!!")

print("Привет после первого комита")

# Git система контроля версий

# Это простое изменение

# Изначально git не знает что эта папка должна
# иметь контроль версий

# git init - иницаилизирует git репозиторий
# git status - показывает текущий статус файлов(что изменено, добавлено и т.д.)
# git add путь_к_файлу - собирает файлы в которых произошли изменения
# git commit -m "сообщение" - подписывает изменения комментарием
# git log - позволяет просмотреть все существующие коммиты
# git diff - различия между текущими изменениями и последним коммитом
# git restore путь_к_файлу - удаляет несохраненные изменения
# git reset --soft HEAD~1 - отменяет последний коммит, но не удаляет. можно
#                           закоммитить обратно
# git reset --hard HEAD~1 - отменяет последний коммит, и изменяет файлы
# git reset --mixed HEAD~1 - отменяет последний коммит, но оставляет файлы. можно
#                           закоммитить обратно
# git revert хеш_коммита - отменяет нужный коммент указанный в хеше и заменяет его
#                          на новый

# git config --global user.name "Axelerts"
# git config --global user.email "bertus2016@mail.ru"
# git remote add название_подключения ссылка_на репозиторий
# git remote remove название_подключения

# git remote add origin https://github.com/Axelerts/Github_projects.git

# git add .
# git commit -m "делаем пуш в гит репо"
# git push origin master
# ssh-keygen -t rsa
# c:\users\user/.ssh/tst_github_rsa