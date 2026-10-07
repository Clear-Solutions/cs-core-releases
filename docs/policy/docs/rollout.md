# Состояние подключения на 6 октября 2026 года

Репозитории `Clear-Solutions/cs-core-standards` и `Clear-Solutions/cs-project-showcase` перенесены в организацию Clear-Solutions на Free и остаются приватными. Витрина переименована из `-Team-Showcase`. Доступ Иры (`light2217`) на запись подтверждён в обоих репозиториях. В организацию Ире отправлено приглашение; принятие ещё ожидается. Создан приватный [GitHub Project Delivery](https://github.com/orgs/Clear-Solutions/projects/1), связанный с четырьмя репозиториями. Есть таблица, доска по статусу и roadmap, поля Priority, Size и Target date.

Созданы приватные `Clear-Solutions/cs-core-service-template` (GitHub Template, Python 3.12/FastAPI, lockfile, Docker, CI, подготовка production CD) и `Clear-Solutions/cs-core-hub` (каталог, документация, CI и доставка архива). Checks/security обоих новых репозиториев и delivery hub завершились успешно. Ире отправлены приглашения write-access в оба новых репозитория; права начнут действовать после принятия. Репозиторий infra пока не создан: он добавляется при конкретной задаче управления инфраструктурой.

Владелец уточнил требование: **одно одобрение другого участника**, а не два. CODEOWNERS содержит elementary1997 и light2217. Токены Actions имеют права read, автоматические approvals отключены, разрешён только squash merge. Эти настройки поддерживаются текущим тарифом и проверены через API.

GitHub вернул 403 для rulesets и branch protection: текущий тариф не позволяет защитить private main. Владелец выбрал подготовку сейчас; для приватных репозиториев организации понадобится GitHub Team. Нельзя считать серверную защиту активной до успешного применения и read-back. Правила общения и AGENTS запрещают прямые push, но не являются технической защитой.

После подключения GitHub Team:

1. Выполнить `tools/github_admin.py apply` для всех четырёх репозиториев и `audit`.
2. Проверить доступ участников и CODEOWNERS, затем одобрить открытые PR и дождаться обязательного CI.
3. Для сервисов установить restricted deployment command, отдельный SSH credential, известный host key и environment production. Шаблон `templates/project-cd.yml` завершает job ошибкой при недостающей конфигурации.
4. После merge проверить фактический выпуск нужного SHA, health и rollback. Для репозитория правил artifact поставляется workflow delivery.yml; к production-сервису он не подключается.

Пример правил не доказывает их применение. Указанное состояние — снимок на дату; при следующей настройке проверяйте API заново.
