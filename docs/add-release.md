# Добавить продукт или версию

1. Уточнить продукт, точную версию, исходный SHA и подтверждённые платформы.
2. Получить файлы из успешного CI этого SHA. Первичный перенос уже опубликованного
   выпуска допускается с сохранением исходного SHA и побайтовой проверкой всех
   digest/size из GitHub API; такой импорт явно отмечается в release notes.
3. Создать `products/<slug>/releases/v<version>/manifest.json` и `SHA256SUMS`.
   Slug — строчные латинские буквы, цифры и дефисы; тег — `<slug>-v<version>`.
   Manifest содержит product/version/release_tag/source_commit/assets с SHA-256 и size.
   Ключ `kind` описывает источник: verified-upstream-release-import или verified-ci-artifacts;
   для нового CI-выпуска обязательны `source_run_url` и `source_repository`.
4. Обновить product.json (`latest_version`, `latest_tag`, platforms) и оба README.
   Сохранить историю старых manifest; установщики не коммитить.
5. Выполнить make check и make security, провести PR с независимым одобрением.
6. Создать draft GitHub Release с product-prefixed тегом для проверенного manifest SHA,
   загрузить только сверенные файлы и SHA256SUMS. Повторно проверить digest загрузок.
   Опубликовать при действующей авторизации владельца/maintainer.
7. Обновить download_url витрины, README проекта, Hub и profile. Ссылка ведёт на тег
   этого продукта, никогда на общий releases/latest. Проверить доступ без GitHub-входа.

Не заменять существующие установщики под тем же тегом. Не добавлять командный
брендинг в независимый продукт без запроса. Межрепозиторная автоматическая
публикация не настроена: используются проверенные артефакты CI и gh maintainer.

Сценарий агента: [cs-release-publish](https://github.com/Clear-Solutions/cs-core-skills/blob/main/skills/delivery/cs-release-publish/README.md) —
проверка происхождения и SHA-256, подготовка без публикации или разрешённый выпуск.
[cs-project-audit](https://github.com/Clear-Solutions/cs-core-skills/blob/main/skills/review/cs-project-audit/README.md)
поможет отдельно оценить готовность проекта.
