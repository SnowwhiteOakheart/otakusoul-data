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
recommended_models.json         Empfehlungen, keine Modellgewichte
locales/de.json / ru.json        externe App-Sprachdateien
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

Vorhandene zusätzliche Felder erhalten. Jeder Download-Link muss auf eine vorhandene, eingecheckte Datei zeigen. Keine doppelten Einträge oder IDs. Keine lokalen Dateisystempfade in Registries.

Neue Szenen/Lorebooks nach einem bestehenden vollständigen Beispiel desselben Pakets erstellen. Szenen verwenden unter anderem `title`, `description`, `world_context`, `starting_location`, `opening_narration`, `first_message`, `party` und optionale Hintergrund-/Erzählparameter. Figurenbezüge und Bildpfade tatsächlich prüfen. Lorebooks müssen vollständige Einträge enthalten; `entry_count` muss zur veröffentlichten Datei passen.

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
