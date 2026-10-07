# Clear Solutions · Releases

Общий публичный каталог готовых выпусков наших продуктов. Исходный код хранится
в отдельных проектных репозиториях; их приватность не меняется при публикации установщиков.

| Продукт | Платформы | Текущий выпуск |
| --- | --- | --- |
| [Агент распознавания речи и голосового ввода](products/easystt/README.md) | Windows / Linux x64 | [v0.1.3 — скачать](https://github.com/Clear-Solutions/cs-core-releases/releases/tag/easystt-v0.1.3) |

## Структура

```text
products/
  easystt/
    README.md
    product.json
    releases/
      v0.1.3/
        manifest.json
        SHA256SUMS
```

Установщики лежат в GitHub Releases, а не в Git. Теги имеют вид
`<product>-v<version>`, например `easystt-v0.1.3`. Для каждого продукта
`product.json` указывает текущую версию и тег; README содержит кликабельную ссылку.
Общий `/releases/latest` не используется для скачивания отдельных продуктов.
Новый продукт добавляется отдельной папкой с теми же метаданными; список платформ
берётся из проверенных сборок, а не из предпочтений агента.

## Проверки и поставка

`make setup`, `make check`, `make security`. Python 3.12+, Git, Linux x64
для закреплённых инструментов безопасности; локальная проверка manifest работает
на macOS/Windows/Linux. CI проверяет политики, версии, SHA-256 каталоги, ссылки и workflow.
CD сохраняет каталог проверенного main с точным SHA. Это архив метаданных, не установщики.

Ветка → PR → одно независимое одобрение → checks/security → squash merge.
[Агенты](AGENTS.md) · [Публикация и откат](docs/deployment.md) ·
[Добавление продукта и версии](docs/add-release.md) · [Безопасность](SECURITY.md).

Сценарий агента: [cs-release-publish](https://github.com/Clear-Solutions/cs-core-skills/blob/main/skills/delivery/cs-release-publish/README.md) —
проверка происхождения и SHA-256, подготовка без публикации или разрешённый выпуск.
[cs-project-audit](https://github.com/Clear-Solutions/cs-core-skills/blob/main/skills/review/cs-project-audit/README.md)
поможет отдельно оценить готовность проекта.
