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

Bildwerkzeug: **OpenAI image_gen (eingebaut)**. Drei separat generierte Masterporträts; jede Expression als eigene identitätserhaltende Bearbeitung des zugehörigen Masterporträts. Keine offiziellen Illustrationen, Screenshots oder Scans als Bildeingabe. Größenanpassung mit oben ausgerichtetem Lanczos-Ausschnitt, WebP-Qualität 92; JSON-Karten werden unverändert im PNG-`chara`-Chunk eingebettet. Preset-Karten verwenden relative Bildpfade, Gateway-Karten öffentliche Repository-URLs. Dieses Paket ergänzt ausschließlich Charaktere, keine eigenen Lorebooks oder Soulstages.

## English

Three standalone Character Card V2 profiles: **Ainz Ooal Gown (Momonga / Overlord)**, **Albedo**, and **Shalltear Bloodfallen**, with complete German, English and Russian text, two alternative greetings and three dialogue examples each. Each character has a 700×937 PNG portrait and 15 distinct 640×800 WebP expressions matching the app’s current portrait slots. User agency and the characters’ independent loyalties are preserved.

All artwork is generated fan art made with built-in OpenAI image_gen. Each expression is an individual edit referencing its character’s generated master portrait; no official artwork is used as image input. Exact prompts, reference information and processing are linked above. The four romance-named slots are strictly nonsexual: courteous confidence, heightened attention, triumphant joy and relieved repose. Shalltear remains fully clothed and nonsexual; Ainz retains skeletal anatomy without skin, blush or tears. No lorebooks or scenes are added.

## Русский

Три самостоятельные карточки Character Card V2: **Айнз Оал Гоун (Момонга / Overlord)**, **Альбедо** и **Шалтир Бладфоллен**. Полные тексты на немецком, английском и русском, по два альтернативных приветствия и три примера диалогов. У каждого персонажа портрет PNG 700×937 и 15 отдельных эмоций WebP 640×800, соответствующих текущим слотам приложения. Сохраняются свобода пользователя и самостоятельная преданность персонажей.

Неофициальный фан-арт создан встроенным OpenAI image_gen: каждая эмоция — отдельная обработка сгенерированного основного портрета. Официальные иллюстрации не используются как входные изображения. Точные запросы, сведения о референсах и обработке указаны по ссылкам выше. Четыре технических слота романтики содержат только неэротические варианты: учтивая уверенность, повышенное внимание, радость победы и облегчение. Юная на вид Шалтир полностью одета и не сексуализирована; Айнз сохраняет скелетную анатомию без кожи, румянца и слёз. Лорбуки и сцены не добавляются.

## Quellen / Sources / Источники

- [Offizielle Anime-Charakterübersicht / Official anime cast](https://overlord-anime.com/_season1/character.html)
- [Offizielle Spiel-Charakterprofile / Official game character profiles](https://overlord-game.com/character/)

Inoffizielle KI-Fanart und eigenständig formulierte Rollenspieltexte. **Overlord**, Figuren und Originalwerk: **Kugane Maruyama, so-bin, KADOKAWA und jeweilige Rechteinhaber**. Keine offizielle Veröffentlichung oder Rechteübertragung an Figuren und Originalwerk. / Unofficial AI-generated fan art and independently written roleplay text; original rights remain with their respective holders. / Неофициальный фан-арт и самостоятельно написанные ролевые тексты; права на оригинал принадлежат соответствующим правообладателям.
