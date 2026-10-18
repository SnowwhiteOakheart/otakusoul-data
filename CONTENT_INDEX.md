# 📑 OtakuSoul Content Index & Architektur-Wegweiser

> **Zweck für AI-Agenten:** Dieses Dokument dient als tokensparende Schnellreferenz für den gesamten Inhaltsbestand (`otakusoul-data`) sowie für die Aufrufe und Validierungs-Checks in der OtakuSoul-App (`OtakuSoul`). Anstatt ~180 KB JSON-Dateien zu parsen, enthält dieser Index alle Verknüpfungen auf einen Blick.
>
> **Stand:** 60 Charaktere · 48 Soul Stages (Szenen) · 24 Lorebooks · 21 Presets.

---

## 🏛️ Inhaltskatalog nach Universen & Kampagnen

### 1. Kampagnen-Pakete mit vollständigem Cast, Stages & Lorebooks

| Paket (`presets/<id>`) | Franchise | Charaktere (`soul_registry.json`) | Soul Stages / Episoden (`stages_gateway/*.json`) | Aktive Lorebooks (`lorebooks_gateway/*.json`) |
|---|---|---|---|---|
| `sakura-succubus-3` | Sakura Succubus 3 | `Ayu Ikue`, `Marina Wakatsuki`, `Cosmos`, `Hazel Williams`, `Hifumi Yamamoto`, `Yue`<br>*(Persona: Hiroki)* | `redaktionsschluss`<br>`der_wohltaetigkeitsball`<br>`wohnungskrieg`<br>`audienz_im_thronsaal`<br>`ein_tee_zu_zweit`<br>`matchball` (6) | • *Welt* (`sakura_succubus_3_world.json`)<br>• *Figuren* (`sakura_succubus_3_characters.json`)<br>• *Orte* (`sakura_succubus_3_locations.json`) |
| `no-game-no-life` | No Game No Life | `Sora`, `Shiro`, `Stephanie Dola`, `Jibril`, `Izuna Hatsuse`, `Chlammy Zell`, `Fiel Nirvalen`<br>*(Persona: Haru)* | `episode1_anfaenger` bis `episode12_regel_nummer_zehn` (12 fortlaufende Kapitel) | • *Welt & Gebote* (`no_game_no_life_world.json`)<br>• *Rassen & Orte* (`no_game_no_life_races_locations.json`)<br>• *Figuren* (`no_game_no_life_characters.json`) |
| `dungeon-meshi` | Dungeon Meshi | `Laios Touden`, `Marcille Donato`, `Chilchuck Tims`, `Senshi` | `dungeon_meshi_ep1_skorpionsuppe`<br>`dungeon_meshi_ep2_klingenbasilisk`<br>`dungeon_meshi_ep3_alraunenernte`<br>`dungeon_meshi_ep4_wassergeister`<br>`dungeon_meshi_ep5_roter_drache` (5) | • *Ökologie & Labyrinth-Regeln* (`dungeon_meshi_ecology.json`)<br>• *Monster-Rezepte & Kochkunst* (`dungeon_meshi_recipes.json`)<br>• *Figuren & Goldene Dynastie* (`dungeon_meshi_world.json`) |
| `steins-gate` | Steins;Gate | `Okabe Rintarou`, `Mayuri Shiina`, `Itaru Hashida`, `Suzuha Amane` | `steins_gate_ep1_erste_dmail`<br>`steins_gate_ep2_ibn5100_suche`<br>`steins_gate_ep3_operation_urd`<br>`steins_gate_ep4_schmetterlingseffekt`<br>`steins_gate_ep5_tor_zu_steins_gate` (5) | • *Weltlinien & Divergenz* (`steins_gate_divergence.json`)<br>• *Labor-Gadgets & D-Mails* (`steins_gate_gadgets.json`)<br>• *Akihabara 2010 & SERN* (`steins_gate_akihabara.json`) |
| `lycoris-recoil` | Lycoris Recoil | `Chisato Nishikigi`, `Takina Inoue`, `Kurumi`, `Mizuki Nakahara` | `lycoris_recoil_ep1_willkommen_im_cafe`<br>`lycoris_recoil_ep2_geleitschutz_tokio`<br>`lycoris_recoil_ep3_jagd_nach_walnut`<br>`lycoris_recoil_ep4_duell_im_morgengrauen` (4) | • *Café LycoReco* (`lycoris_recoil_cafe.json`)<br>• *DA & Alan Institute* (`lycoris_recoil_da.json`)<br>• *Ausrüstung & Taktik* (`lycoris_recoil_tactics.json`) |
| `sword-art-online` | Sword Art Online | `Kirito (Kazuto Kirigaya)`, `Asuna Yuuki`, `Klein (Ryoutarou Tsuboi)`, `Lisbeth (Rika Shinozaki)` | `sao_ep1_die_verkuendung`<br>`sao_ep2_boss_ebene1`<br>`sao_ep3_waerme_des_herzens`<br>`sao_ep4_duell_in_den_schatten`<br>`sao_ep5_der_glaenzende_blick` (5) | • *Aincrad-Systemregeln* (`sao_system_rules.json`)<br>• *Gilden & Fraktionen* (`sao_guilds_factions.json`)<br>• *Aincrad-Geografie* (`sao_aincrad_geography.json`) |
| `quintessential-quintuplets` | The Quintessential Quintuplets (5-toubun no Hanayome) | `Ichika Nakano`, `Nino Nakano`, `Miku Nakano`, `Yotsuba Nakano`, `Itsuki Nakano`, `Futaro Uesugi` (6) | `quintuplets_ep1_penthouse_nachhilfe`<br>`quintuplets_ep2_feuerwerk_gestaendnis`<br>`quintuplets_ep3_zwischenpruefung`<br>`quintuplets_ep4_schneefahrt_huette`<br>`quintuplets_ep5_schulfest_gestaendnisse` (5) | • *Die Nakano-Schwestern* (`quintuplets_nakano_sisters.json`)<br>• *Nachhilfe & Uesugi-Haushalt* (`quintuplets_tutoring_study.json`)<br>• *Orte & Schulalltag* (`quintuplets_world_locations.json`) |

---

### 2. Generische Welten & Crossover-Stages

Diese 3 Pakete besitzen eigene Hintergründe und Lorebooks, nutzen jedoch universelle Crossover-Besetzungen aus anderen Paketen:

| Paket / Setting | Stage-ID & Titel | Besetzung (`party`) | Aktives Lorebook |
|---|---|---|---|
| `cyberpunk-night-city` | `cyberpunk_ghost_in_subgrid` *(Geist im Subnetz)* | `Kurumi` (Lycoris), `Shinku` (NTE) | `Night City 2077 – Edgerunner, Konzerne & das Netz` (`cyberpunk_night_city.json`) |
| | `cyberpunk_afterlife_deal` *(Kalter Deal im Afterlife)* | `Lacrimosa` (NTE), `Chisato Nishikigi` (Lycoris) | `Night City 2077 – Edgerunner, Konzerne & das Netz` (`cyberpunk_night_city.json`) |
| `isekai-aetheria` | `isekai_null_mana_summoning` *(Beschworen mit Stufe Null)* | `Frieren`, `Megumin` | `Aetheria Chronicles – Isekai-Abenteuer, Gilden & Systemmagie` (`isekai_fantasy_rpg_world.json`) |
| | `isekai_labyrinth_of_aetheria` *(Der verbotene Dungeon-Kern)* | `Rem` (Re:Zero), `Marcille Donato` (Dungeon Meshi) | `Aetheria Chronicles – Isekai-Abenteuer, Gilden & Systemmagie` (`isekai_fantasy_rpg_world.json`) |
| `anime-academy-romance` | `romance_rainy_clubroom_confessions` *(Ein Schirm für vier)* | `Marin Kitagawa`, `Hayase Nagatoro`, `Aoi Mizuno` (Aobane) | `Herzensklopfen & Kirschblüten – Anime-Romance & Harem-Dynamik` (`modern_anime_academy_romance.json`) |
| | `romance_rooftop_festival_fireworks` *(Wem gehört der letzte Tanz?)* | `Kaguya Shinomiya`, `Asuna Yuuki`, `Rem` (Re:Zero) | `Herzensklopfen & Kirschblüten – Anime-Romance & Harem-Dynamik` (`modern_anime_academy_romance.json`) |

---

### 3. Standalone-Charaktere & Welten ohne eigene Kampagnen-Episoden

| Preset-Ordner | Franchise / Herkunft | Registrierte Figuren (`name` in `soul_registry.json`) | Bemerkungen / Gastauftritte |
|---|---|---|---|
| `overlord` | Overlord | `Ainz Ooal Gown` (Momonga), `Albedo`, `Shalltear Bloodfallen` (3) | Je 15 eigenständige SFW-Expressions; keine eigenen Stages/Lorebooks. |
| `re-zero` | Re:Zero | `Subaru Natsuki`, `Rem`, `Ram`, `Beatrice`, `Echidna` (5) | Rem tritt in Isekai- und Romance-Stages auf. |
| `neverness-to-everness` | Neverness to Everness | `Mint`, `Iroi`, `Lacrimosa`, `Nanally Colucci`, `Linko`, `Esper Zero (Female)`, `Esper Zero (Male)`, `Shinku` (8) | Urban-Fantasy-Cast; Lacrimosa und Shinku treten in Cyberpunk-Stages auf. |
| `frieren` | Sousou no Frieren | `Frieren` | Gastauftritt in `isekai_null_mana_summoning`. |
| `nagatoro` | Don't Toy With Me, Miss Nagatoro | `Hayase Nagatoro` | Gastauftritt in `romance_rainy_clubroom_confessions`. |
| `marin-kitagawa` | My Dress-Up Darling | `Marin Kitagawa` | Gastauftritt in `romance_rainy_clubroom_confessions`. |
| `yor-forger` | Spy x Family | `Yor Forger` | Standalone-Karte mit 6 Expressions. |
| `megumin` | KonoSuba | `Megumin` | Gastauftritt in `isekai_null_mana_summoning`. |
| `kaguya-shinomiya` | Kaguya-sama: Love Is War | `Kaguya Shinomiya` | Gastauftritt in `romance_rooftop_festival_fireworks`. |
| `elfen-lied` | Elfen Lied | `Lucy` | Gespaltene Persönlichkeit (Lucy / Nyu) mit Vektoren-Mechanik. |
| `aobane-highschool` | OtakuSoul Original | `Ren Takahashi`, `Aoi Mizuno` (2) | Aoi tritt in `romance_rainy_clubroom_confessions` auf. |

---

## ⚙️ OtakuSoul-App Integration (Aufrufe & Ausführung)

Hier wird beschrieben, an welchen Stellen im OtakuSoul-Codebase (`OtakuSoul/src-tauri/src/`) die Daten geladen, interpretiert und verarbeitet werden:

### 1. Charaktere (`Character Card V2` & Avatare)
* **Aufruf & Parser:**
  * `src-tauri/src/modules/characters.rs`:
    * `parse_character_png()`: Liest den Base64-kodierten JSON-Payload aus dem PNG-Text-Chunk `tEXt` (`chara`).
    * `parse_character_json()`: Parst die Standalone-V2-JSON (`spec == "chara_card_v2"`, `spec_version == "2.0"`).
  * `src-tauri/src/commands/characters.rs`: Stellt Tauri-Befehle bereit (`load_characters`, `import_character`, `get_character`).
* **Emotionserkennung & Expressions:**
  * `src-tauri/src/modules/emotions.rs` erkennt Emotionen und zusätzliche Porträtslots; `src/utils/characterPortraits.ts` wählt die in `extensions.expressions` hinterlegten Bilder aus (`PORTRAIT_MOODS`: sechs Grundstimmungen plus neun Zusatzslots, insgesamt 15). Overlord enthält alle 15; ältere Sechser-Sätze bleiben über den Stimmungs-Fallback kompatibel.
* **Langzeitgedächtnis:**
  * `src-tauri/src/modules/memory/soul.rs`: Verwaltet Soul Memory, Fakten-Extraktion und Kontextgedächtnis der Figur.

### 2. Soul Stages (Szenen & Stories)
* **Definition & Import:**
  * `src-tauri/src/modules/stage/scenes.rs` & `models.rs`:
    * `SceneDefinition`: Parst `title`, `description`, `party`, `lorebook`, `starting_location`, `starting_bg`, `world_context`, `opening_narration`, `first_message`, `gm_tone`, `narrator_style`.
    * Hub-Import vergibt die ID `hub_<registry-id>`.
  * `src-tauri/src/modules/stage/party.rs`:
    * Gleicht `scene.party` mit installierten Charakterkarten ab (exakter Name oder Kurzname vor der Klammer wie `"Kirito"` für `"Kirito (Kazuto Kirigaya)"`).
* **Ausführung & Spielleiter (GM):**
  * `src-tauri/src/modules/stage/engine.rs` & `director.rs`: Steuert Szenenfortschritt, Actor-Reihenfolge, Würfelwürfe (`dice.rs`) und Kontextzusammenstellung für das LLM.
* **5e-Regelsystem (optional):**
  * `src-tauri/src/modules/stage/rules5e/`: Wird aktiv, wenn in der Szene `rules.ruleset == "5e"` gesetzt ist (verarbeitet `hero_classes`, `goals`, `combat`, `spells`).
* **Story-Galerie:**
  * `src-tauri/src/modules/stage/models.rs`: Wertet `extensions.otakusoul_story` aus (`genre`, `minutes`, `difficulty`, `notes`, `choices` für Einsteiger-Auswahlmöglichkeiten).

### 3. Lorebooks (Weltenwissen & Trigger)
* **Aufruf & Injektion:**
  * `src-tauri/src/modules/lorebook.rs` & `commands/lorebook.rs`:
    * `Lorebook` / `LorebookEntry`: Liest `entries` mit `uid`, `name`, `key`, `secondary_keys`, `regex_keys`, `content`, `trigger_type`, `priority`, `injection_behavior`.
* **Trigger-Logik im Chatverlauf:**
  * Durchsucht die letzten `scan_depth` Nachrichten (Standard: 5).
  * `trigger_type`:
    * `keyword`: Auslösung durch Schlüsselwörter.
    * `regex`: Regex-Muster.
    * `always_on`: Ständige Injektion (ggf. gewichtet mit `probability`).
    * `tension`: Auslösung ab Szenenspannungs-Schwellenwert (`tension_threshold`).
  * `chain_requires` / `chain_activates`: Abhängigkeitsketten zwischen Einträgen.
  * `injection_behavior`: `passive` (Weltwissen / Fakten) vs. `active` (Modellanweisung).

### 4. Hub-Registries & Versionskontrolle
* **Registry-Abruf & Download:**
  * `src-tauri/src/modules/hub.rs`: Lädt `soul_registry.json`, `stages_registry.json`, `lorebooks_registry.json` über GitHub Raw.
  * Lädt beim Szenenimport verknüpfte Hintergrundbilder aus `extensions.otakusoul_assets.backgrounds` automatisch herunter.
* **Revisionsabgleich & Updates:**
  * `src-tauri/src/modules/hub_installed.rs`: Vergleicht lokale `revision` mit der Registry-`revision`. Höhere Zahl = Update verfügbar.

---

## 🔍 Validierungs-Checks & Werkzeuge (`otakusoul-data`)

Vor jedem Commit und Push müssen die Inhalte automatisiert validiert werden:

### 1. Zentraler Validator: `tools/validate_content.py`

| Check-Funktion | Was wird geprüft? | Typische Fehler / Ursachen |
|---|---|---|
| `check_card()` | • `spec == "chara_card_v2"`, `spec_version == "2.0"`<br>• Pflichtfelder: `name`, `description`, `first_mes`<br>• Mind. 2 `alternate_greetings`<br>• 6 Emotionsbilder (`neutral`, `happy`, `relaxed`, `surprised`, `angry`, `sad`) vorhanden<br>• Dreisprachigkeit (`otakusoul_i18n` mit `de`, `en`, `ru`)<br>• PNG `chara`-Payload identisch mit Preset-JSON | Fehlt ein Bild, ist der Pfad ungültig oder weicht die PNG-Payload vom JSON ab, bricht der Test ab. |
| `check_scene()` | • Mitspieler in `party` existieren in `soul_registry.json`<br>• Lorebooks in `lorebook` existieren in `lorebooks_registry.json`<br>• Hintergründe in `otakusoul_assets.backgrounds` existieren auf der Festplatte<br>• `persona != "None"` (darf nicht der String `"None"` sein)<br>• Keine veralteten Felder (`conversation_method`)<br>• Genau 3 Startvorschläge (`choices`) je Sprache in `otakusoul_story` | Name in `party` falsch geschrieben oder Lorebook-Titel übersetzt statt Originalname angegeben. |
| `check_lorebook()` | • `uid` je Eintrag eindeutig und ganzzahlig<br>• `trigger_type` ist `keyword`, `regex`, `always_on` oder `tension`<br>• Bei `keyword` muss `key` vorhanden sein<br>• `chain_requires` verweist auf gültige UIDs<br>• Keine veralteten Felder (`n_depth`, `sticky`, `cooldown`, `delay`) | Verwaiste Chain-Verweise oder veraltete Soul-of-Waifu-Schlüssel. |
| `check_registry()` & `check_gateway_files()` | • Alle `download_url`-Ziele existieren tatsächlich im Dateisystem<br>• Pflichtfelder `revision`, `updated`, `download_url`<br>• Keine Dubletten bei IDs / Namen<br>• Keine Windows/macOS Case-Collisions in `cards_gateway/` | Tippfehler in URLs oder geänderte Dateinamen ohne Registry-Anpassung. |

### 2. Validierungs-Befehle für die Konsole

```sh
# 1. Reine Prüfung (Exit-Code 1 bei Fehlern):
python3 tools/validate_content.py

# 2. Synchronisation der Übersetzungen und Beschreibungen aus den Gateway-Dateien in die Registries:
python3 tools/validate_content.py --sync-registry

# 3. Spezifische Validierung für die 16 Hauptkampagnen-Figuren:
python3 tools/validate_aobane.py
```

---

## 📌 Wichtige Schnellregeln für AI-Agenten
1. **Party-Namen:** In `stages_gateway/*.json` unter `party` exakt den Namen aus `soul_registry.json` verwenden (z. B. `"Kirito (Kazuto Kirigaya)"` oder `"Kirito"`).
2. **Lorebook-Namen:** In `stages_gateway/*.json` unter `lorebook` **immer** den originalen Schlüsselnamen des Buchs verwenden (Feld `name` aus `lorebooks_registry.json`), niemals die Übersetzung.
3. **Revisions-Regel:** Sobald der Text oder ein Feld einer Karte, einer Szene oder eines Lorebooks geändert wird, in der zugehörigen Registry `revision` um `1` erhöhen und `updated` auf das Tagesdatum (`JJJJ-MM-TT`) setzen.
4. **Dokumentation:** Nach Abschluss neuer Charaktere oder Kampagnen ausschließlich `ROADMAP.md` und diesen `CONTENT_INDEX.md` aktualisieren.

### Zusatzemotionen: Zwischenstand 18.10.2026

**DE:** 47 bestehende Figuren wurden um je neun separat erzeugte SFW-Emotionsbilder erweitert (423 Bilder). Zusammen mit Overlord haben jetzt 50 Figuren alle 15 Slots. Lisbeth und Yor behalten vorerst ihre sechs bisherigen Emotionen; NTE bleibt unverändert. Die vier technisch romantisch benannten Slots zeigen ausschließlich nichtsexuelle Varianten. Prompts und Verarbeitung stehen je Figur in `expressions/<figur>/additional_prompts.json`.

**EN:** 47 existing characters received nine individually generated SFW expression images each (423 images). Including Overlord, 50 characters now have all 15 slots. Lisbeth and Yor retain their six previous expressions for now; NTE is unchanged. The four technically romance-named slots contain nonsexual variants only. Per-character prompts and processing are documented in `expressions/<character>/additional_prompts.json`.

**RU:** Для 47 существующих персонажей добавлено по девять отдельно сгенерированных неэротических изображений эмоций (423 изображения). Вместе с Overlord у 50 персонажей есть все 15 слотов. У Lisbeth и Yor пока остаются прежние шесть эмоций; NTE не изменён. Четыре технических слота романтики содержат только неэротические варианты. Запросы и обработка описаны в `expressions/<персонаж>/additional_prompts.json`.
