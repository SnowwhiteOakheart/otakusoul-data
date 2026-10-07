# otakusoul-data

[Deutsch](#deutsch) · [English](#english) · [Русский](#русский)

## Deutsch

Separates Inhaltsrepository für [OtakuSoul](https://github.com/SnowwhiteOakheart/OtakuSoul): Charakterkarten, Emotionsbilder, Soul-Stage-Szenen, Lorebooks, Hintergründe, VRM-Avatare, Sprachdateien und Modellempfehlungen. Änderungen hier importieren nichts in eine lokale App-Installation.

### Struktur

| Pfad | Inhalt |
|---|---|
| `soul_registry.json` / `cards_gateway/` | Charakterkatalog und eigenständig importierbare PNG-Karten |
| `lorebooks_registry.json` / `lorebooks_gateway/` | Lorebook-Katalog und JSON-Dateien |
| `stages_registry.json` / `stages_gateway/` | Szenenkatalog und JSON-Dateien |
| `presets/` | Themenpakete mit JSON-/PNG-Karten, Expressions, Hintergründen und Dokumentation; teilweise eigenen Szenen und Lorebooks |
| `presets/cards/` | Einzelkarten als JSON und PNG |
| `avatars/` | Zusätzliche Avatare; VRM-Modelle und Herkunftshinweise unter `avatars/vrm/` |
| `locales/` | Deutsche und russische App-Sprachdateien; Englisch wird in der App gepflegt |
| `recommended_models.json` | Modellempfehlungen und Metadaten, keine Modelldateien |
| `tools/` | Wiederverwendbare Wartungs- und Prüfwerkzeuge |

### Inhalte und Verwendung

Die Pakete umfassen **No Game No Life**, **Sakura Succubus 3**, **Dungeon Meshi**, **Steins;Gate**, **Lycoris Recoil**, **Sword Art Online**, weitere Anime-Einzelkarten und die Originalfiguren **Ren Takahashi / Aoi Mizuno** aus der Aobane Highschool. Der Arbeitsstand einschließlich der Emotionsbilder steht in [ROADMAP.md](ROADMAP.md).

Die App lädt die drei Registries über ihre Hub-/Gateway-Ansichten. PNG-Charakterkarten lassen sich auch manuell importieren: Sie enthalten die Character-Card-V2-Definition als `chara`-Metadaten. Preset-Karten verwenden relative Bildpfade; Gateway-Karten öffentliche Repository-URLs. Für den manuellen Paketimport die Verzeichnisstruktur beibehalten. Hintergründe und VRM-Modelle bei Bedarf separat importieren; es gibt keinen eigenen Hintergrundkatalog.

Charakterübersetzungen für **DE, EN und RU** liegen in `data.extensions.otakusoul_i18n`. Die Ausgangssprache steht in `source_language`; die anderen Sprachen in `translations`. Paketbeschreibungen erläutern Besonderheiten der jeweiligen Inhalte.

### Pflege und Herkunft

[AI.md](AI.md) beschreibt Dateiformate, Übersetzungen, Bildvorgaben, Registries und den Veröffentlichungsablauf. [AGENTS.md](AGENTS.md) und [CLAUDE.md](CLAUDE.md) verweisen darauf. Nur [ROADMAP.md](ROADMAP.md) wird als Roadmap gepflegt.

Die Python-Werkzeuge sind optionale Repository-Wartung, keine App-Abhängigkeit. Installation: `python3 -m pip install -r tools/requirements.txt` in einer eigenen virtuellen Umgebung. Prüfungen ohne Schreibzugriff:

```sh
python3 tools/validate_aobane.py
python3 tools/package_campaign_expressions.py dungeon-meshi laios_touden
```

Der zweite Befehl prüft einen vorhandenen Kampagnencharakter. Mit `--manifest` paketiert das Werkzeug neue Expressions und aktualisiert die Roadmap; Details stehen in [AI.md](AI.md).

[LICENSE](LICENSE) enthält die Nutzungsbedingungen und Hinweise zu KI-generierter Fanart, eigenen Beiträgen und fremden Rechten. Herkunft, Bildprompts und vorhandene Lizenzhinweise bleiben bei den Paketen erhalten, insbesondere [VRM-Hinweise](avatars/vrm/lizenzen.txt). Die Veröffentlichung stellt keine pauschale Lizenz für zugrunde liegende Anime-/Spielwerke oder fremde Modelle dar.

## English

Separate content repository for [OtakuSoul](https://github.com/SnowwhiteOakheart/OtakuSoul): character cards, expression images, Soul Stage scenes, lorebooks, backgrounds, VRM avatars, language files and model recommendations. Repository changes do not import content into a local app installation.

### Structure

| Path | Contents |
|---|---|
| `soul_registry.json` / `cards_gateway/` | Character catalog and independently importable PNG cards |
| `lorebooks_registry.json` / `lorebooks_gateway/` | Lorebook catalog and JSON files |
| `stages_registry.json` / `stages_gateway/` | Scene catalog and JSON files |
| `presets/` | Themed packages with JSON/PNG cards, expressions, backgrounds and documentation; some include their own scenes and lorebooks |
| `presets/cards/` | Individual JSON and PNG cards |
| `avatars/` | Additional avatars; VRM models and attribution in `avatars/vrm/` |
| `locales/` | German and Russian app language files; English is maintained in the app |
| `recommended_models.json` | Model recommendations and metadata, without model binaries |
| `tools/` | Reusable maintenance and validation tools |

### Content and usage

Packages include **No Game No Life**, **Sakura Succubus 3**, **Dungeon Meshi**, **Steins;Gate**, **Lycoris Recoil**, **Sword Art Online**, additional anime cards and original **Ren Takahashi / Aoi Mizuno** characters from Aobane Highschool. [ROADMAP.md](ROADMAP.md) tracks progress, including expression images.

The app reads the three registries through its Hub/Gateway views. PNG character cards also support manual import: they embed the Character Card V2 definition in `chara` metadata. Preset cards use relative image paths; Gateway cards use public repository URLs. Preserve the folder structure when importing a package manually. Import backgrounds and VRM models separately as needed; there is no dedicated background catalog.

Character translations for **DE, EN and RU** are stored in `data.extensions.otakusoul_i18n`. `source_language` identifies the base language; `translations` contains the other languages. Package documentation explains content-specific details.

### Maintenance and attribution

[AI.md](AI.md) documents file formats, translations, image requirements, registries and publication. [AGENTS.md](AGENTS.md) and [CLAUDE.md](CLAUDE.md) point to it. [ROADMAP.md](ROADMAP.md) is the only maintained roadmap.

Python tools are optional repository maintenance utilities, not app dependencies. Install with `python3 -m pip install -r tools/requirements.txt` in a dedicated virtual environment. Read-only checks:

```sh
python3 tools/validate_aobane.py
python3 tools/package_campaign_expressions.py dungeon-meshi laios_touden
```

The second command validates an existing campaign character. With `--manifest`, the tool packages new expressions and updates the roadmap; see [AI.md](AI.md).

[LICENSE](LICENSE) contains usage terms and notices about AI-generated fan art, original contributions and third-party rights. Attribution, image prompts and existing license notices remain with the packages, especially [VRM notices](avatars/vrm/lizenzen.txt). Publication does not grant a blanket license to underlying anime/game works or third-party models.

## Русский

Отдельный репозиторий контента для [OtakuSoul](https://github.com/SnowwhiteOakheart/OtakuSoul): карточки персонажей, изображения эмоций, сцены Soul Stage, лорбуки, фоны, VRM-аватары, языковые файлы и рекомендации моделей. Изменения в репозитории не импортируют контент в локальную установку приложения.

### Структура

| Путь | Содержимое |
|---|---|
| `soul_registry.json` / `cards_gateway/` | Каталог персонажей и PNG-карточки для отдельного импорта |
| `lorebooks_registry.json` / `lorebooks_gateway/` | Каталог лорбуков и JSON-файлы |
| `stages_registry.json` / `stages_gateway/` | Каталог сцен и JSON-файлы |
| `presets/` | Тематические наборы: JSON-/PNG-карточки, эмоции, фоны и документация; некоторые содержат собственные сцены и лорбуки |
| `presets/cards/` | Отдельные карточки в JSON и PNG |
| `avatars/` | Дополнительные аватары; VRM-модели и сведения об источниках в `avatars/vrm/` |
| `locales/` | Немецкие и русские языковые файлы приложения; английский поддерживается в приложении |
| `recommended_models.json` | Рекомендации и метаданные моделей без файлов самих моделей |
| `tools/` | Повторно используемые инструменты обслуживания и проверки |

### Контент и использование

Доступны наборы **No Game No Life**, **Sakura Succubus 3**, **Dungeon Meshi**, **Steins;Gate**, **Lycoris Recoil**, **Sword Art Online**, дополнительные аниме-карточки и оригинальные персонажи **Ren Takahashi / Aoi Mizuno** из старшей школы Aobane. Ход работы, включая изображения эмоций, отражён в [ROADMAP.md](ROADMAP.md).

Приложение читает три реестра в разделах Hub/Gateway. PNG-карточки также можно импортировать вручную: определение Character Card V2 встроено в метаданные `chara`. Карточки наборов используют относительные пути к изображениям, а карточки Gateway — публичные URL репозитория. При ручном импорте набора сохраняйте структуру каталогов. Фоны и VRM-модели при необходимости импортируются отдельно; отдельного каталога фонов нет.

Переводы персонажей на **DE, EN и RU** хранятся в `data.extensions.otakusoul_i18n`. `source_language` задаёт исходный язык, а `translations` содержит остальные языки. Особенности наборов описаны в их документации.

### Обслуживание и источники

[AI.md](AI.md) описывает форматы файлов, переводы, требования к изображениям, реестры и публикацию. [AGENTS.md](AGENTS.md) и [CLAUDE.md](CLAUDE.md) ссылаются на него. Единственная поддерживаемая дорожная карта — [ROADMAP.md](ROADMAP.md).

Python-инструменты предназначены для необязательного обслуживания репозитория и не являются зависимостью приложения. Установка: `python3 -m pip install -r tools/requirements.txt` в отдельном виртуальном окружении. Проверки без изменения файлов:

```sh
python3 tools/validate_aobane.py
python3 tools/package_campaign_expressions.py dungeon-meshi laios_touden
```

Вторая команда проверяет существующего персонажа кампании. С параметром `--manifest` инструмент упаковывает новые изображения эмоций и обновляет дорожную карту; подробности — в [AI.md](AI.md).

[LICENSE](LICENSE) содержит условия использования и сведения о фан-арте ИИ, собственных материалах и правах третьих лиц. Источники, промпты изображений и имеющиеся лицензионные сведения сохраняются в наборах, особенно [сведения о VRM](avatars/vrm/lizenzen.txt). Публикация не предоставляет общую лицензию на исходные аниме, игры или сторонние модели.
