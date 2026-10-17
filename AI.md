# AI.md – Wegweiser für dieses Inhaltsrepository

Vor jeder Änderung vollständig lesen. Dieses Repository ist `SnowwhiteOakheart/otakusoul-data`, das separate Inhaltsrepository von OtakuSoul. Es enthält Daten und Bilder, keinen App-Code. Keine Inhalte in eine lokale App-Installation importieren, sofern nicht ausdrücklich beauftragt.

## Zusammenarbeit und Veröffentlichung

- Mit dem Nutzer auf Deutsch kommunizieren; thematische Commit-Beschreibungen auf Deutsch.
- Bestehende Nutzeränderungen vorab mit `git status` prüfen. Nur beauftragte Änderungen committen; parallel entstandene Änderungen nicht beiläufig aufnehmen.
- Beauftragte Arbeit darf auf `main` committed und gepusht werden. Nach jedem fertiggestellten Charakter: prüfen, `ROADMAP.md` aktualisieren, committen und sofort pushen.
- Nur `ROADMAP.md` pflegen; keine zweite Roadmap erzeugen. README bei strukturellen Änderungen in DE, EN und RU synchron aktualisieren.
- Keine Maschinenpfade, Geheimnisse, virtuellen Umgebungen, Caches, temporären Kontaktbögen oder einmaligen Migrationsskripte einchecken.
- Bestehende öffentliche Pfade nicht ohne Prüfung aller Registry- und Kartenverweise umbenennen. Groß-/Kleinschreibung beachten.

## Verzeichnisstruktur

```text
README.md                       Einstieg in DE / EN / RU
AI.md                           dieser verbindliche Wegweiser
AGENTS.md / CLAUDE.md            kurze Verweise auf AI.md
LICENSE                         Rechte- und Nutzungshinweise
ROADMAP.md                      Arbeitsstand, einzige Roadmap
soul_registry.json              Charakterindex
cards_gateway/*.png             eigenständige Hub-Karten
lorebooks_registry.json          Lorebook-Index
lorebooks_gateway/*.json         veröffentlichte Lorebooks
stages_registry.json             Szenenindex
stages_gateway/*.json            veröffentlichte Szenen
recommended_models.json         Spiegel des Starter-Katalogs der App, keine Modellgewichte
locales/de.json / ru.json        Spieltexte der App (Schlüssel = englischer Text)
avatars/                        zusätzliche Avatar-Dateien
avatars/vrm/lizenzen.txt         Herkunft und Bedingungen der VRM-Modelle
presets/cards/                  bestehende Einzelkarten
presets/<paket>/                 zusammengehörige Inhalte
  <figur>.json / <figur>.png     Profil und eingebettete PNG-Karte
  expressions/<figur>/          sechs Emotionsbilder und Promptnachweise
  backgrounds/                  optionale Szenenhintergründe
  scenes/ / lorebooks/          optional, entsprechend vorhandenem Paket
  README.md                     Paketbeschreibung
  image_prompts.json            oder bestehende Promptdokumentation
tools/                          wiederverwendbare lokale Wartungswerkzeuge
```

Neue Paketnamen in `kebab-case`, neue Figuren-IDs in `snake_case`, ASCII ohne Leerzeichen. Vorhandene Dateinamen und Formate bleiben kompatibel. Gateway-Dateien sind bewusst eigene Varianten: relative Preset-Pfade werden dort durch öffentliche URLs ersetzt. Nicht als vermeintliche Duplikate entfernen. Auch Bildprompts, Herkunftshinweise und vorhandene Lizenztexte behalten.

Die vier neueren Kampagnenpakete haben Hintergründe und Charakterkarten im Paket, ihre Szenen und Lorebooks liegen in den Gateway-Verzeichnissen. Keine leeren Unterverzeichnisse zur optischen Vereinheitlichung anlegen.

## Charakterkarten und Übersetzungen

- Character Card V2: JSON mit `spec: "chara_card_v2"`, `spec_version: "2.0"` und `data`.
- Profiltexte: `name`, `description`, `personality`, `scenario`, `first_mes`, `mes_example`, `system_prompt`, `post_history_instructions`, `creator_notes`.
- Zusätzlich `alternate_greetings`, `tags` und bestehende Metadaten erhalten. Bei neuen vollständigen Profilen mindestens zwei alternative Begrüßungen und drei aussagekräftige Dialogbeispiele liefern; Rollen, Beziehungen und Gesprächsstil konsistent halten.
- Alle nutzerseitigen Profiltexte, Begrüßungen, Beispiele, Titel und Tags in DE, EN und RU pflegen. Ausgangstexte stehen direkt in `data`; `data.extensions.otakusoul_i18n.source_language` benennt ihre Sprache, `translations` enthält die anderen beiden Sprachobjekte. Bestehende Karten können eine englische Ausgangssprache haben; nicht pauschal Deutsch erzwingen.
- Platzhalter wie `{{char}}`, `{{user}}` und `{{original}}` unverändert erhalten. IDs, URLs, Dateipfade und technische Emotionsschlüssel nicht übersetzen.
- Erweiterungen über vorhandene `custom_*`-Schlüssel pflegen; keine neuen `sow_*`-Schlüssel erzeugen.
- PNG-Karten tragen dasselbe vollständige JSON als Base64-kodiertes UTF-8-JSON im PNG-`tEXt`-Eintrag `chara`. Nach Textänderungen immer JSON und eingebettete PNG-Definition synchronisieren.
- Preset-PNG muss mit der zugehörigen JSON-Karte übereinstimmen. Gateway-PNG muss alle Profiltexte und Übersetzungen erhalten; nur benötigte Bildpfade auf öffentliche Repository-URLs umstellen.

## Bilder und Herkunft

Neue Standardporträts: PNG, 700×937 Pixel. Expressions: WebP, 640×800 Pixel, genau `neutral`, `happy`, `relaxed`, `surprised`, `angry`, `sad`. Bestehende abweichende Altformate nicht ungefragt neu skalieren.

Expressions unter `presets/<paket>/expressions/<figur>/<emotion>.webp` ablegen. `data.extensions.expressions` ordnet die sechs Schlüssel den Bildern zu. Preset-Pfade sind relativ zum Paket; Gateway-Pfade verwenden `https://raw.githubusercontent.com/SnowwhiteOakheart/otakusoul-data/main/…`.

Bilder mit dem verfügbaren Bildgenerierungswerkzeug erstellen. Für Emotionsvarianten das zugehörige Porträt als Referenz verwenden: gleiche Identität, Frisur, Kleidung und Stil; erkennbare unterschiedliche Gesichtsausdrücke. Keine Kopien eines Bildes als sechs Emotionen ausgeben. Minderjährige Figuren altersgerecht darstellen.

Generierungswerkzeug, Prompts, Referenzpfade und Nachbearbeitung dokumentieren; keine absoluten Entwicklerpfade speichern. Metadatenänderungen sollen vorhandene Porträtpixel erhalten. Fanart und KI-Herkunft transparent benennen. Fremde Werke, Modelle und deren Lizenz-/Quellenhinweise nicht durch eine allgemeine Eigenlizenz ersetzen; `LICENSE` beachten.

## Registries, Szenen und Lorebooks

Registries sind JSON-Objekte mit `version` und der entsprechenden Liste:

- `soul_registry.json`: `characters`; Einträge mit `name`, `author`, `download_url`.
- `lorebooks_registry.json`: `lorebooks`; Einträge mit `name`, `author`, `description`, `entry_count`, `download_url`.
- `stages_registry.json`: `scenes`; Einträge mit `id`, `title`, `author`, `description`, `starting_location`, `download_url`.
- Jeder Registry-Eintrag trägt `revision` (Ganzzahl ab 1) und `updated` (Datum `JJJJ-MM-TT`). Die App vergleicht die Revision
  mit der installierten Kopie und bietet „Aktualisieren“ an. **Bei jeder inhaltlichen Änderung einer Karte, eines Lorebooks
  oder einer Szene die `revision` des Eintrags um 1 erhöhen und `updated` setzen** (reine Formatierung zählt nicht).
  Szenen behalten beim Update ihren Spielstand, Karten werden ersetzt (alte Fassung in den Papierkorb), lokal veränderte
  Lorebooks bleiben als Kopie erhalten. Die Registry-`id` einer Szene bzw. der Name einer Karte/eines Lorebooks ist der
  Schlüssel für Updates und darf nicht geändert werden.

Vorhandene zusätzliche Felder erhalten (Ausnahme: die unten genannten veralteten Felder). Jeder Download-Link muss auf eine vorhandene, eingecheckte Datei zeigen. Keine doppelten Einträge oder IDs. Keine lokalen Dateisystempfade in Registries.

Neue Szenen/Lorebooks nach einem bestehenden vollständigen Beispiel desselben Pakets erstellen. Figurenbezüge und Bildpfade tatsächlich prüfen.

### Szenen (`stages_gateway/*.json`)

- Felder: `title`, `description`, `world_context`, `starting_location`, `time_of_day`, `opening_narration`, `first_message`,
  `party` (Figurennamen wie in `soul_registry.json`), `gm_tone`, `narrator_style`, `persona`, `lorebook`, optional
  `solo_mode`, `max_actor_depth`, `dice_rolls_enabled`, `starting_bg`, `starting_ambient` (`"None"` = Stille), `lock_bg`,
  `disable_ambient`. Die `id` vergibt die App beim Import (`hub_<registry-id>`).
- `persona`: Name, mit dem die Figuren den Spieler ansprechen (z. B. eine feste Hauptfigur der Geschichte). Leer = die
  aktive Persona des Nutzers. Nie einen Platzhalter wie `"None"` eintragen – die App würde ihn als Namen verwenden.
- `lorebook`: Liste von Lorebook-Namen in der Ausgangssprache des Lorebooks (Feld `name`, nicht die Übersetzung).
- Übersetzt werden in `extensions.otakusoul_i18n.translations.<sprache>` genau diese Felder: `title`, `description`,
  `world_context`, `starting_location`, `time_of_day`, `opening_narration`, `first_message`, `gm_tone`, `narrator_style`.
- Hintergründe: `starting_bg` ist der Dateiname. Damit die App die Bilder beim Hub-Import mitlädt, listet
  `extensions.otakusoul_assets.backgrounds` sie als `[{ "file": "<datei>", "path": "presets/<paket>/backgrounds/<datei>" }]`
  (Startbild zuerst, dann die übrigen Bilder des Pakets, zwischen denen der Spielleiter wechseln kann). Nur PNG/JPG/WebP,
  `path` relativ zum Repository unter `presets/`, ohne `..`; vorhandene Dateien überschreibt die App nicht.
- 5e-Regeln (optional): `rules` mit `ruleset: "5e"`, `hero_classes` (Figur → Klasse), `control_companions`,
  `heroic_death`, `map_id`, `goals`, `next_scene`. Monster, Zauber, Karten und Klassen müssen in der jeweiligen App-Version
  existieren (SRD-Daten im App-Repository unter `presets/srd5/`); ohne Prüfung keine 5e-Szenen veröffentlichen.
- Story-Daten für die Story-Galerie (ab OtakuSoul 0.5): `extensions.otakusoul_story` mit `genre` (`fantasy`, `adventure`,
  `slice_of_life`, `comedy`, `romance`, `mystery`, `scifi`, `horror`), `minutes` (typische Spieldauer), `difficulty`
  (`easy`/`medium`/`hard`), `notes` (Inhaltshinweise: `mild_danger`, `mild_violence`, `action`, `spooky`, `suspense`,
  `flirting`, `romance`, `dark_themes`, `death`), `beginner` (für Einsteiger empfohlen, z. B. erste Episode) und `choices` =
  je Sprache (`de`, `en`, `ru`) drei Startvorschläge `{text, badge, action_type}` (`action_type` `say`/`do`, `badge`
  optional eine Fertigkeit wie „Wahrnehmung“).
- Veraltet und zu entfernen: `conversation_method` (die App wählt das Modell selbst).

### Lorebooks (`lorebooks_gateway/*.json`)

Format der App (`LorebookEntry` in `src-tauri/src/modules/lorebook.rs`):

- Buch: `name`, `description`, `scan_depth` (wie viele letzte Nachrichten durchsucht werden, Standard 5), optional
  `is_global`, `entries`, `extensions.otakusoul_i18n` (übersetzt `name`, `description`). Keine `id` – die vergibt der Import.
- Eintrag: `uid` (eindeutige Ganzzahl im Buch), `name`, `key` (Schlüsselwörter), optional `secondary_keys`, `exclude_key`
  (verhindert das Auslösen), `regex_keys`, `content`, `trigger_type`, `probability` (0–100), optional `priority` (höher =
  früher, Standard 10), `enabled`, `injection_behavior` (`passive` = Weltwissen, `active` = Anweisung an das Modell),
  optional `case_sensitive`, `match_whole_words`, `chain_requires` / `chain_activates` (UIDs als Text, z. B. `["4"]`),
  `tension_threshold`, `extensions.otakusoul_i18n` (übersetzt `name`, `content`, `key`).
- `trigger_type`: `keyword` (Schlüsselwort im Verlauf), `regex`, `always_on` (immer, mit `probability` als Zufall),
  `tension` (ab `tension_threshold` Szenenspannung). Ein Folge-Eintrag, der nur zusammen mit einem anderen erscheinen soll,
  ist `always_on` mit `chain_requires`.
- Alte Soul-of-Waifu-Felder wertet die App nicht aus; nicht mehr verwenden: `n_depth` (→ `scan_depth`), `depends_on`
  (→ `chain_requires`), `sticky`, `cooldown`, `delay`, `chain_delay`, `min_msg`/`max_msg`, `semantic_trigger`, Trigger
  `semantic`/`range` (→ `keyword`), `random` (→ `always_on`), `chain` (→ `always_on` + `chain_requires`), `sow_*`-Erweiterungen.
  Die App wandelt solche Dateien beim Import zwar um, im Repository steht nur das App-Format.
- Lorebooks müssen vollständige Einträge enthalten; `entry_count` muss zur veröffentlichten Datei passen.

### Spieltexte (`locales/`)

`locales/de.json` und `ru.json` übersetzen Texte, die die App selbst in Geschichten schreibt (`ContentLang::t`). Schlüssel ist
der englische Text aus dem App-Code, Platzhalter wie `{name}` bleiben erhalten. Die App lädt die Dateien beim Start nach;
neue Texte zuerst im App-Code anlegen und hier in beiden Sprachen ergänzen.

### Modelle (`recommended_models.json`)

Spiegel des eingebauten Starter-Katalogs der App (`models_hub::STARTERS`). Maßgeblich ist der Katalog in der App; Änderungen
dort hier nachziehen (`version` erhöhen, `last_updated` setzen). Nur frei lizenzierte, ohne Anmeldung ladbare Modelle mit
SHA-256 aus der Quelle; keine Modellgewichte im Repository, keine nicht-kommerziellen Sprachmodelle.

Übersetzungen in bestehenden Erweiterungsstrukturen vollständig erhalten. Die Repo-Datei allein garantiert nicht, dass jede App-Version jede Erweiterung beim Import übernimmt; keine App-Kompatibilität behaupten, die nicht geprüft wurde. App-Code nur nach gesondertem Auftrag ändern. Englisch benötigt hier keine künstliche `locales/en.json`: die englische App-Basis liegt im App-Repository.

## Werkzeuge und Prüfungen

Python und Pillow werden nur für optionale Wartung benötigt. Abhängigkeit: `tools/requirements.txt`; virtuelle Umgebung außerhalb versionierter Inhalte bzw. unter ignoriertem `.venv/`.

```sh
python3 tools/validate_aobane.py
python3 tools/package_campaign_expressions.py dungeon-meshi laios_touden
```

Beide Befehle prüfen ausschließlich. Das zweite Werkzeug unterstützt die 16 Figuren der Pakete `dungeon-meshi`, `steins-gate`, `lycoris-recoil`, `sword-art-online` gemäß seiner `CAST`-Liste. Es ist kein allgemeiner Validator aller Karten.

Mit `--manifest <datei.json>` schreibt es neue Expressions, Kartenmetadaten und die Roadmap. Manifest: Liste mit je einem Eintrag pro Emotion; Feldschema vor Verwendung in `package()` prüfen. Vorhandene Bilder werden nicht überschrieben. Die Generierung erfolgt separat; das Werkzeug erzeugt selbst keine KI-Bilder.

Vor Veröffentlichung passend zum Umfang prüfen:

1. Alle geänderten JSON-Dateien lassen sich laden; Übersetzungen und Pflichtfelder sind vollständig.
2. PNG-Payloads entsprechen den JSON-Profilen; Gateway-Karten erhalten deren Inhalte.
3. Bildformat, Maße, sechs tatsächlich unterschiedliche Emotionsbilder und alle Pfade/URLs stimmen.
4. Registry-Verweise führen zu vorhandenen Dateien; entfernte Dateien werden nirgends mehr benötigt.
5. Dokumentationslinks funktionieren; README-Sprachen, Herkunftshinweise und Roadmap sind aktuell.
6. `git diff --check` besteht; Diff enthält ausschließlich beauftragte Änderungen. Anschließend thematisch committen und pushen.

Keine großen App-Testläufe für reine Inhalts-/Dokumentationsbereinigung. Keine Einmalskripte im Root sammeln: wiederverwendbare, dokumentierte Helfer gehören nach `tools/`, temporäre Migrationen außerhalb des Repositorys.
