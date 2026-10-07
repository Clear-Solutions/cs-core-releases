# Подключение проекта

1. Создайте приватный репозиторий в организации `Clear-Solutions` с именем `cs-project-<назначение>` (строчные латинские буквы, цифры, дефисы), владельцем и подтверждёнными ревьюерами. Проверьте доступность rulesets и protected environments по тарифу; не меняйте приватность для обхода ограничений.
2. Подготовьте README, проектный AGENTS.md, CODEOWNERS, CONTRIBUTING, SECURITY, PR template, lockfiles, тесты и реальные команды CI/CD. Добавьте `.clear-solutions/project.json` с pin commit правил.
3. Скопируйте/адаптируйте CI: required jobs называются `checks` и `security`, actions зафиксированы полным SHA, права ограничены, PR не получают production credentials. Настройте Dependabot и secret scanning.
4. Загрузите первоначальный commit в новый пустой `main`. Сразу примените ruleset через `tools/github_admin.py apply OWNER/REPO`. Для существующего проекта bootstrap исключения нет: изменение добавляется в feature branch и PR.
5. Выдайте согласованным аккаунтам write-access, проверьте валидность CODEOWNERS и что другой участник сможет одобрить PR автора. Если участников два, один одобряет PR другого.
6. Настройте deployment environment, scoped credentials, host key, health и rollback. Выполните тестовый выпуск и подтвердите конкретный SHA и результат. Репозиторий документации вместо сервиса поставляет версионированный artifact.
7. Проверьте через API enforcement=active, пустой bypass, одно approval, required checks и запреты force push/delete. Убедитесь, что прямой push запрещён; не пытайтесь разрушительно тестировать force push на production main.
8. Каждый следующий change — PR. Периодически делайте read-only audit прав и защиты, а обновления общего policy pin проводите отдельным PR.

Новый проект из идеи: [порядок самостоятельного выбора стека и создания](project-bootstrap.md).
