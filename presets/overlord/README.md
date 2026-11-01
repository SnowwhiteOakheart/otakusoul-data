# Overlord – Nazarick

## Deutsch

Drei eigenständig importierbare Character-Card-V2-Profile für OtakuSoul: **Ainz Ooal Gown (Momonga / Overlord)**, **Albedo** und **Shalltear Bloodfallen**. Alle Profiltexte liegen auf Deutsch, Englisch und Russisch vor, jeweils mit zwei alternativen Begrüßungen und drei Dialogbeispielen. Die Begegnungen lassen Rolle und Entscheidungen des Nutzers offen; Loyalität gegenüber Ainz wird nicht automatisch auf den Nutzer übertragen.

| Figur | Profil | Bildreferenz und tatsächliche Prompts |
|---|---|---|
| Ainz Ooal Gown | [ainz_ooal_gown.json](ainz_ooal_gown.json) | [prompts.json](expressions/ainz_ooal_gown/prompts.json) |
| Albedo | [albedo.json](albedo.json) | [prompts.json](expressions/albedo/prompts.json) |
| Shalltear Bloodfallen | [shalltear_bloodfallen.json](shalltear_bloodfallen.json) | [prompts.json](expressions/shalltear_bloodfallen/prompts.json) |

Jede Figur enthält ein **700×937-PNG-Porträt** und **15 eigenständige Expressions als 640×800-WebP**. Die Schlüssel entsprechen `PORTRAIT_MOODS` in der App (`src/utils/characterPortraits.ts`) und den sechs Grundstimmungen plus `EXTRA_PORTRAITS` (`src-tauri/src/modules/emotions.rs`), geprüft am 18.10.2026:

`neutral`, `happy`, `sad`, `angry`, `surprised`, `relaxed`, `blush`, `teasing`, `fear`, `disgust`, `crying`, `seductive`, `aroused`, `ecstasy`, `afterglow`.

Die technisch als Romance benannten vier letzten Slots sind **nichtsexuelle SFW-Varianten**: höflich-selbstsicherer Empfang, erhöhte Aufmerksamkeit vor einer Aufgabe, Siegesfreude und Erleichterung nach einer bewältigten Aufgabe. Sie bilden keine erotischen Zustände ab. Shalltears jugendlich wirkende Darstellung bleibt vollständig bekleidet und nichtsexualisiert. Ainz zeigt alle Emotionen durch Augenlichter, Schädelwinkel, Kiefer und Schulterhaltung; er erhält weder Haut, Wangenröte noch Tränen. Die sechs Basisslots bleiben mit älteren App-Versionen kompatibel.

Bildwerkzeug: **OpenAI image_gen (eingebaut)**. Drei separat generierte Masterporträts; jede Expression als eigene identitätserhaltende Bearbeitung des zugehörigen Masterporträts. Keine offiziellen Illustrationen, Screenshots oder Scans als Bildeingabe. Größenanpassung mit oben ausgerichtetem Lanczos-Ausschnitt, WebP-Qualität 92; JSON-Karten werden unverändert im PNG-`chara`-Chunk eingebettet. Preset-Karten verwenden relative Bildpfade, Gateway-Karten öffentliche Repository-URLs.

### Sammlung, Story & Lorebooks (01.11.2026)
Die Figuren sind über die Hub-Sammlung `overlord` gebündelt („Alles installieren“ lädt den vollständigen Cast). Zur Sammlung gehören:
- **Soul Stage:** `overlord_ep1_audienz_in_nazarick` (*Audienz im Thronsaal von Nazarick*, 3 Gruppenmitglieder, 3 Startvorschläge je Sprache, automatischer Hintergrunddownload).
- **Lorebooks:** `overlord_nazarick_world.json` (*Die Große Gruft von Nazarick*, 6 Einträge) und `overlord_supreme_guardians.json` (*Herrscher & Wächter*, 5 Einträge), jeweils vollständig in DE/EN/RU/JA.
- **Bilder:** Sammlungstitelbild `cover.webp` (960×540 WebP) und Szenenhintergrund `backgrounds/overlord_thronsaal.webp` (1376×768 WebP); Prompts und Nachbearbeitung dokumentiert in `cover_prompt.json`.

## English

Three standalone Character Card V2 profiles: **Ainz Ooal Gown (Momonga / Overlord)**, **Albedo**, and **Shalltear Bloodfallen**, with complete German, English and Russian text, two alternative greetings and three dialogue examples each. Each character has a 700×937 PNG portrait and 15 distinct 640×800 WebP expressions matching the app’s current portrait slots. User agency and the characters’ independent loyalties are preserved.

All artwork is generated fan art made with built-in OpenAI image_gen. Each expression is an individual edit referencing its character’s generated master portrait; no official artwork is used as image input. Exact prompts, reference information and processing are linked above. The four romance-named slots are strictly nonsexual: courteous confidence, heightened attention, triumphant joy and relieved repose. Shalltear remains fully clothed and nonsexual; Ainz retains skeletal anatomy without skin, blush or tears.

### Collection, Story & Lorebooks (01.11.2026)
Characters are bundled under the Hub collection `overlord` ("Install All" downloads the full cast). Included in the collection:
- **Soul Stage:** `overlord_ep1_audienz_in_nazarick` (*Audience in the Throne Room of Nazarick*, 3 party members, 3 choices per language, auto-downloading background).
- **Lorebooks:** `overlord_nazarick_world.json` (*The Great Tomb of Nazarick*, 6 entries) and `overlord_supreme_guardians.json` (*Supreme Being & Guardians*, 5 entries), fully localized in DE/EN/RU/JA.
- **Visuals:** Collection cover `cover.webp` (960×540 WebP) and stage background `backgrounds/overlord_thronsaal.webp` (1376×768 WebP); prompt documentation in `cover_prompt.json`.

## Русский

Три самостоятельные карточки Character Card V2: **Айнз Оал Гоун (Момонга / Overlord)**, **Альбедо** и **Шалтир Бладфоллен**. Полные тексты на немецком, английском и русском, по два альтернативных приветствия и три примера диалогов. У каждого персонажа портрет PNG 700×937 и 15 отдельных эмоций WebP 640×800, соответствующих текущим слотам приложения. Сохраняются свобода пользователя и самостоятельная преданность персонажей.

Неофициальный фан-арт создан встроенным OpenAI image_gen: каждая эмоция — отдельная обработка сгенерированного основного портрета. Официальные иллюстрации не используются как входные изображения. Точные запросы, сведения о референсах и обработке указаны по ссылкам выше. Четыре технических слота романтики содержат только неэротические варианты: учтивая уверенность, повышенное внимание, радость победы и облегчение. Юная на вид Шалтир полностью одета и не сексуализирована; Айнз сохраняет скелетную анатомию без кожи, румянца и слёз.

### Коллекция, сюжет и книги знаний (01.11.2026)
Персонажи объединены в коллекцию Hub `overlord` (кнопка «Установить всё» скачивает весь состав). В коллекцию входят:
- **Soul Stage:** `overlord_ep1_audienz_in_nazarick` (*Аудиенция в Тронном зале Назарика*, 3 персонажа группы, по 3 начальных варианта выбора на язык, фоновое изображение).
- **Lorebooks:** `overlord_nazarick_world.json` (*Великая гробница Назарик*, 6 статей) и `overlord_supreme_guardians.json` (*Владыка и Стражи*, 5 статей) на DE/EN/RU/JA.
- **Иллюстрации:** Обложка коллекции `cover.webp` (960×540 WebP) и фон сцены `backgrounds/overlord_thronsaal.webp` (1376×768 WebP); описание промпта в `cover_prompt.json`.

## Quellen / Sources / Источники

- [Offizielle Anime-Charakterübersicht / Official anime cast](https://overlord-anime.com/_season1/character.html)
- [Offizielle Spiel-Charakterprofile / Official game character profiles](https://overlord-game.com/character/)

Inoffizielle KI-Fanart und eigenständig formulierte Rollenspieltexte. **Overlord**, Figuren und Originalwerk: **Kugane Maruyama, so-bin, KADOKAWA und jeweilige Rechteinhaber**. Keine offizielle Veröffentlichung oder Rechteübertragung an Figuren und Originalwerk. / Unofficial AI-generated fan art and independently written roleplay text; original rights remain with their respective holders. / Неофициальный фан-арт и самостоятельно написанные ролевые тексты; права на оригинал принадлежат соответствующим правообладателям.
