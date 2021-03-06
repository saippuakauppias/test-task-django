# test-task-django
Решение тестового задания о сервисе напоминаний на Django Framework

## Задание

Реализовать сервис напоминаний. В данном сервисе должна быть возможность регистрации пользователя. После регистрации пользователь должен иметь возможность авторизоваться. После авторизации пользователь может создать напоминалку которая в указанное время пришлет напоминание на почту как автору напоминания так и пользователям которых можно прикрепить к напоминанию. Пользователей прикреплять можно из тех которые уже есть в системе. Реализовать возможность смотреть конкретное напоминание как своих напоминаний так и тех в которые тебя пригласили. Реализовать возможность посмотреть список напоминаний как тех в которых ты являешься автором так и те в которые тебя пригласили. Реализовать механизм редактирования и удаления своих напоминаний. В теле напоминания должны быть следующие поля: заголовок, описание, место, участники, дата создания, дата наступления.

Требования к функционалу:
- Регистрация пользователя + профиль
- Создание, изменение и удаление напоминалок
- Привязка участников (из этой же системы)
- Оповещение на почту участников и создателя
- Иметь возможность отмечать таск завершенным

Требования к программной части:
- Код на python/Django
- БД MySQL или PostgreSQL
- Docker
- Api на django rest framework
- git
- celery
- минимальный набор тестов

фронтовая часть не особо важна

## Запуск

Skeleton проекта основан на Cookiecutter Django, поэтому запуск аналогичен тому, как советуют [в документации](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally-docker.html):

```shell
docker-compose -f local.yml up --build
```

## Линтеры и тесты

В GitHub Actions на каждый коммит в мастер и PR запускается [workflow](.github/workflows/ci.yml) с линтерами (с помощью `git pre commit`) и прогоном тестов.

Используемые линтеры: `flake8`, `isort` и `black`.

Тесты запускаются с помощью `pytest`.
