# 🗺️ Roadmap: Optionale Inhalte für OtakuSoul (`otakusoul-data`)

Dieses Dokument koordiniert die Erstellung und schrittweise Implementierung von modularen, optionalen Inhalten für **OtakuSoul**. Alle hier definierten Charaktere, Lorebooks und Stage-Geschichten werden im Repository **[`SnowwhiteOakheart/otakusoul-data`](https://github.com/SnowwhiteOakheart/otakusoul-data)** gepflegt und stehen lokal in der App zur Verfügung, ohne das Basis-Release der Anwendung aufzublähen.


## Inochi2D: Nagatoro v12 · 31.10.2026

- **DE:** [v12 veröffentlicht](https://github.com/SnowwhiteOakheart/otakusoul-data/releases/tag/nagatoro-inochi2d-v12): zwei eigenständige vollständige Dreiviertelzeichnungen links/rechts, fünf Ansichten, 85 Clips. Drehclips nutzen die Zwischenzeichnungen; Blinzeln, Sprechen, leichte Kopfbewegung, Atmung und Haarreaktion eingebaut. Neutrale Front weiterhin pixelgleich. 144 neue Winkelkombinationen und 1.187.328 sichtbare Dreiecke ohne Umklappen sowie bisherige Prüfungen bestanden. Katalog v4 bietet v12; alte Releases bleiben verfügbar. Grenzen: diskrete Ansichten; Arme/Beine und eigene Geh-/Handposen in den Dreiviertelwinkeln noch nicht artikuliert. Vollständiger App-UI-Import weiterhin nicht manuell geprüft.
- **EN:** v12 adds independently drawn complete left/right three-quarter views: five views and 85 clips. Turns use the intermediate drawings, with blinking, speech, slight head movement, breathing and hair response. Neutral front stays pixel-identical. Passed 144 new view combinations, 1,187,328 visible triangles without folding and existing checks. Registry v4 offers v12; earlier releases remain. Views remain discrete; arms/legs and dedicated gait/hand poses are not articulated in the new intermediate angles yet. Full app UI import has not been manually tested.
- **RU:** v12 добавляет два отдельно нарисованных полнофигурных ракурса в три четверти слева/справа: пять ракурсов и 85 клипов. Повороты используют промежуточные рисунки; добавлены моргание, речь, лёгкие движения головы, дыхание и реакция волос. Нейтральный анфас не изменён. Проверены 144 сочетания, 1.187.328 видимых треугольников без инверсии и прежние тесты. Реестр v4 предлагает v12; старые релизы сохранены. Ракурсы дискретные; руки/ноги и походка/позы кистей в новых ракурсах пока не артикулированы. Полный импорт через интерфейс вручную не проверен.


## Inochi2D: Nagatoro v11 · 31.10.2026

- **DE:** [v11 veröffentlicht](https://github.com/SnowwhiteOakheart/otakusoul-data/releases/tag/nagatoro-inochi2d-v11): Profilmimik mit Blinzeln, Sprechformen, Lachen und Brauen; vier Drehclips mit Blinzeln beim diskreten Ansichtswechsel. 67 Clips, 57 Parameter. Katalog v3 ersetzt den v10-Eintrag durch v11; das frühere Release bleibt abrufbar und vorhandene Installationen bleiben unberührt. Frontansicht pixelgleich zu v10. 252 Profilkombinationen und 580 Dreh-Samples sowie Arm-/Fuß-/Haartests und WebGL bestanden. Offene Punkte: Dreiviertelansichten, automatische Clipübergänge in der App, Kollisionsbehandlung und vollständiger UI-Importtest.
- **EN:** v11 adds profile blinking, speech, laughter and brows plus four blink-assisted clips for discrete view changes. 67 clips, 57 parameters. Registry v3 replaces the v10 entry with v11; the earlier release and existing installations remain available. Neutral front is pixel-identical to v10. Passed 252 profile combinations, 580 turn samples, arm/contact/hair tests and WebGL. Remaining: three-quarter views, automatic app clip transitions, collision handling and full UI import testing.
- **RU:** v11 добавляет моргание, речь, смех и брови в профиль, а также четыре клипа дискретной смены ракурса с морганием. 67 клипов, 57 параметров. Реестр v3 заменяет запись v10 на v11; прежний релиз и установленные модели сохраняются. Нейтральный анфас попиксельно совпадает с v10. Проверены 252 сочетания мимики, 580 отсчётов поворота, тесты рук, контакта стоп, волос и WebGL. Далее: ракурсы в три четверти, автоматические переходы клипов в приложении, столкновения и полный тест импорта через интерфейс.


## Inochi2D: Nagatoro v10 · 31.10.2026

- **DE:** Vollständiges Fanmodell mit 45 Clips und getrennter Haarphysik veröffentlicht: [Release mit INP, Vorschau, Prüfsumme und Nutzungsbedingungen](https://github.com/SnowwhiteOakheart/otakusoul-data/releases/tag/nagatoro-inochi2d-v10). Katalogversion 2 führt es neben Aka/Midori; verfügbar über Hub → Avatare → Inochi2D nach Katalogaktualisierung/Neustart. Keine Puppen-Binärdatei im Git-Baum. OtakuSoul-Parser, Physik und WebGL geprüft; vollständiger UI-Import noch nicht manuell geprüft. Nächste Modellarbeiten: Profilmimik, weichere Ansichts-/Clipübergänge und Überschneidungen in Extremposen.
- **EN:** Full-body fan model with 45 clips and layered hair physics released: INP, preview, checksum and terms are attached to the release above. Registry version 2 adds it alongside Aka/Midori; available under Hub → Avatars → Inochi2D after a catalog refresh/restart. No puppet binary in the Git tree. Tested with the OtakuSoul parser, physics and WebGL; full UI import has not been manually tested. Remaining: profile expressions, smoother view/clip transitions and overlap cleanup in extreme poses.
- **RU:** Опубликована полнофигурная фан-модель с 45 клипами и раздельной физикой волос. INP, превью, контрольная сумма и условия — в релизе выше. Реестр версии 2 добавляет модель к Aka/Midori: Hub → Аватары → Inochi2D после обновления каталога/перезапуска. Бинарный файл модели не добавлен в Git. Проверены парсер, физика и WebGL OtakuSoul; импорт через полный интерфейс вручную не проверен. Далее: мимика в профиль, плавные переходы и устранение пересечений в крайних позах.


---

## 💎 Qualitätsstandards je Inhalt

Jeder Charakter und jedes Kampagnenpaket folgt den etablierten Standards:
1. **Charakterkarten:**
   - Format: **Tavern / OtakuSoul Character Card V2** (PNG mit integrierter JSON-Metadaten-Payload & Standalone-JSON).
   - Ausführliche Persönlichkeits-, Welt- und Sprachmuster-Definitionen (inkl. typischer Ticks, Eigenheiten und Beziehungsdynamiken).
   - Mindestens eine stimmungsvolle Einstiegsnachricht (`first_mes`) + 2 alternative Begrüßungen (`alternate_greetings`).
   - Mehrteilige Dialogbeispiele (`mes_example`), die die Reaktionsbreite der Figur verankern.
   - Mehrsprachigkeit über `extensions.otakusoul_i18n` (Deutsch als Basis, Englisch und Russisch integriert).
2. **Bildgenerierung & Expressions:**
   - Hochauflösender Haupt-Avatar (700×937 PNG, passend zum Anime-Stil der Vorlage).
   - Mindestens 5–6 abgestimmte Mimik-Porträts (640×800 WebP) für die automatische Emotionserkennung im Chat:
     - `neutral` (Standard / Ruhe-Ausdruck)
     - `happy` (Lachen / Frech / Begeistert)
     - `relaxed` / `smug` (Gelassen / Schelmisch / Selbstsicher)
     - `surprised` (Errötet / Verblüfft / Ertappt)
     - `angry` (Schmollend / Wütend / Fokussiert)
     - `sad` (Betrübt / Nachdenklich / Pout)
3. **Kampagnen & Lorebooks:**
   - Strukturierte Stage-Szenarien mit Ziel-SG, GM-Tonalität, Anfangsort, Weltkontext und passenden `party`-Zusammenstellungen.
   - Passende 16:9-Szenenhintergründe (1376×768 PNG) ohne Figuren im Bild für freie Avatar-Darstellung.
   - Detaillierte Welten-, Regel- und Orts-Lorebooks mit Keyword-Triggern.

---

## 🌸 Phase 1: Beliebte Einzel-Charaktere (Chat & Soul Memory)

- [x] **1.1 Hayase Nagatoro** (*Neck mich nicht, Nagatoro-san*)
  - *Status:* **Vollständig abgeschlossen.**
  - *Bilder:* Avatar + 6 Expressions (neutral, happy, relaxed, surprised, angry, sad) vollständig neu generiert.
  - *Dateien:* V2-PNG in `cards_gateway`, Preset in `presets/nagatoro/`, in `soul_registry.json` und lokal in `~/.local/share/otakusoul/characters`.
- [x] **1.2 Marin Kitagawa** (*My Dress-Up Darling*)
  - *Status:* **Vollständig abgeschlossen.**
  - *Bilder:* Avatar + 6 Expressions (neutral, happy, relaxed, surprised, angry, sad) vollständig neu generiert.
  - *Dateien:* V2-PNG in `cards_gateway`, Preset in `presets/marin-kitagawa/`, in `soul_registry.json` und lokal in `~/.local/share/otakusoul/characters`.
- [x] **1.3 Frieren** (*Sousou no Frieren*)
  - *Status:* **Implementiert & spielbar.**
  - *Bilder:* Haupt-Avatar (Bibliothek), Grimoire-Pose und 6 Expressions vollständig neu generiert, einschließlich Mimic-Face, Pout und Sleepy.
  - *Dateien:* V2-PNG in `cards_gateway`, Preset in `presets/frieren/`, in `soul_registry.json` und lokal in `~/.local/share/otakusoul/characters`.
- [x] **1.4 Yor Forger** (*Spy x Family*)
  - *Status:* **Text, Avatar und 6 Expressions fertig.**
  - *Dateien:* V2-Definition in `presets/yor-forger/yor_forger.json` mit voller deutscher Persönlichkeit, First Message & Szenario.
  - *Bilder:* Avatar und 6 Expressions neu generiert; V2-PNG mit eingebetteter Definition vorhanden.
- [x] **1.5 Megumin** (*KonoSuba*)
  - *Status:* **Text, Avatar und 6 Expressions fertig.**
  - *Dateien:* V2-Definition in `presets/megumin/megumin.json` mit Chuunibyou-Beschwörungen, First Message & Szenario.
  - *Bilder:* Avatar und 6 Expressions neu generiert; V2-PNG mit eingebetteter Definition vorhanden.
- [x] **1.6 Kaguya Shinomiya** (*Kaguya-sama: Love Is War*)
  - *Status:* **Text, Avatar und 6 Expressions fertig.**
  - *Dateien:* V2-Definition in `presets/kaguya-shinomiya/kaguya_shinomiya.json` mit psychologischem Liebeskrieg & Szenario.
  - *Bilder:* Avatar und 6 Expressions neu generiert; V2-PNG mit eingebetteter Definition vorhanden.
- [x] **1.7 Lucy (Kaede / Nyu)** (*Elfen Lied*)
  - *Status:* **Vollständig abgeschlossen.**
  - *Bilder:* Avatar (700×937 PNG) + 6 Expressions (neutral, happy, relaxed, surprised, angry, sad; 640×800 WebP) neu generiert.
  - *Dateien:* V2-PNG in `cards_gateway`, Preset in `presets/elfen-lied/`, in `soul_registry.json`. Dreisprachig (DE/EN/RU), Vektor-Mechanik & gespaltene Persönlichkeit.

---

## 🗺️ Phase 2: Umfassende Serien-Kampagnen (Stage, Lorebooks & Party-Cast)

---

### 🍲 Kampagne 2.1: *Dungeon Meshi* (*Delicious in Dungeon*)
*Ein tödlicher Dungeon-Crawl, bei dem das Überleben davon abhängt, wie meisterhaft man Monster zerlegt und kocht.*

- **Lorebooks:** *(Alle 3 in `lorebooks_gateway` & `lorebooks_registry.json` registriert)*
  - [x] *Dungeon-Ökologie:* Manafluss, Geister-Kreislauf, Labyrinth-Regeln (`dungeon_meshi_ecology.json`).
  - [x] *Monster-Küche & Rezepte:* Zubereitung von Riesen-Skorpionen, Basilisken (`dungeon_meshi_recipes.json`).
  - [x] *Figuren & Goldene Dynastie:* Labyrinth-Geschichte, Fallin-Rettung (`dungeon_meshi_world.json`).
- **Stage-Szenarien (Episoden):** *(Alle 5 in `stages_gateway` & `stages_registry.json` registriert)*
  - [x] *Episode 1: Skorpionsuppe & Pilze* (`dungeon_meshi_ep1_skorpionsuppe.json`)
  - [x] *Episode 2: Der Klingen-Basilisk* (`dungeon_meshi_ep2_klingenbasilisk.json`)
  - [x] *Episode 3: Alraunen-Ernte* (`dungeon_meshi_ep3_alraunenernte.json`)
  - [x] *Episode 4: Die Wassergeister* (`dungeon_meshi_ep4_wassergeister.json`)
  - [x] *Episode 5: Der Rote Drache* (`dungeon_meshi_ep5_roter_drache.json`)
- **Charaktere (V2-Karten in `presets/dungeon-meshi/`):**
  - [x] Laios Touden, Marcille Donato, Chilchuck Tims, Senshi (JSONs angelegt).
- **Bilder:**
  - [x] Neu generiert: 4 Charakter-Avatare & 5 Dungeon-Hintergründe.

---

### ⏳ Kampagne 2.2: *Steins;Gate* (*Zukunftsgadget-Labor & Weltlinien*)
*Zeitreisen, Paranoia und das Schicksal in Akihabara.*

- **Lorebooks:** *(Alle 3 in `lorebooks_gateway` & `lorebooks_registry.json` registriert)*
  - [x] *Weltlinien & Divergenz:* Alpha/Beta-Attraktorfelder, Reading Steiner (`steins_gate_divergence.json`).
  - [x] *Labor-Gadgets & D-Mails:* Telefon-Mikrowelle, IBN 5100 (`steins_gate_gadgets.json`).
  - [x] *Akihabara 2010 & SERN:* Zukunftsgadget-Labor, Radiogebäude (`steins_gate_akihabara.json`).
- **Stage-Szenarien (Episoden):** *(Alle 5 in `stages_gateway` & `stages_registry.json` registriert)*
  - [x] *Episode 1: Die erste D-Mail* (`steins_gate_ep1_erste_dmail.json`)
  - [x] *Episode 2: Suche nach dem IBN 5100* (`steins_gate_ep2_ibn5100_suche.json`)
  - [x] *Episode 3: Operation Urd* (`steins_gate_ep3_operation_urd.json`)
  - [x] *Episode 4: Der Schmetterlingseffekt* (`steins_gate_ep4_schmetterlingseffekt.json`)
  - [x] *Episode 5: Das Tor zu Steins Gate* (`steins_gate_ep5_tor_zu_steins_gate.json`)
- **Charaktere (V2-Karten in `presets/steins-gate/`):**
  - [x] Okabe Rintarou (Hououin Kyouma), Mayuri Shiina, Itaru Hashida (Daru), Suzuha Amane.
- **Bilder:**
  - [x] Neu generiert: 4 Charakter-Avatare & 5 Akiba-Hintergründe.

---

### ☕ Kampagne 2.3: *Lycoris Recoil* (*Café LycoReco*)
*Charmantes Café-Leben am Tag, geheime Anti-Terror-Einsätze bei Nacht.*

- **Lorebooks:** *(Alle 3 in `lorebooks_gateway` & `lorebooks_registry.json` registriert)*
  - [x] *DA & Alan Institute:* Organisation, Lycoris-Agentinnen (`lycoris_recoil_da.json`).
  - [x] *Café LycoReco:* Café in Sumida, Menü, Stammkunden (`lycoris_recoil_cafe.json`).
  - [x] *Ausrüstung & Taktik:* Nicht-tödliche Munition, Chisatos Ausweichen (`lycoris_recoil_tactics.json`).
- **Stage-Szenarien (Episoden):** *(Alle 4 in `stages_gateway` & `stages_registry.json` registriert)*
  - [x] *Episode 1: Willkommen im Café LycoReco* (`lycoris_recoil_ep1_willkommen_im_cafe.json`)
  - [x] *Episode 2: Geleitschutz durch Tokio* (`lycoris_recoil_ep2_geleitschutz_tokio.json`)
  - [x] *Episode 3: Jagd nach Walnut* (`lycoris_recoil_ep3_jagd_nach_walnut.json`)
  - [x] *Episode 4: Duell im Morgengrauen* (`lycoris_recoil_ep4_duell_im_morgengrauen.json`)
- **Charaktere (V2-Karten in `presets/lycoris-recoil/`):**
  - [x] Chisato Nishikigi, Takina Inoue, Mizuki Nakahara, Kurumi (JSONs angelegt).
- **Bilder:**
  - [x] Neu generiert: 4 Charakter-Avatare & 4 Café-/Tokio-Hintergründe.

---

### ⚔️ Kampagne 2.4: *Sword Art Online* (*Aincrad – 100 Ebenen des Todes*)
*Der Überlebenskampf im legendären VRMMO.*

- **Lorebooks:** *(Alle 3 in `lorebooks_gateway` & `lorebooks_registry.json` registriert)*
  - [x] *Aincrad-Systemregeln:* Sword Skills, HP-Regeln, Permadeath (`sao_system_rules.json`).
  - [x] *Gilden & Fraktionen:* KoB, Fuurinkazan, Laughing Coffin (`sao_guilds_factions.json`).
  - [x] *Aincrad-Geografie:* Die 100 Ebenen, Startstadt, Labyrinthzonen (`sao_aincrad_geography.json`).
- **Stage-Szenarien (Episoden):** *(Alle 5 in `stages_gateway` & `stages_registry.json` registriert)*
  - [x] *Episode 1: Die Verkündung* (`sao_ep1_die_verkuendung.json`)
  - [x] *Episode 2: Der Herrscher der ersten Ebene* (`sao_ep2_boss_ebene1.json`)
  - [x] *Episode 3: Wärme des Herzens* (`sao_ep3_waerme_des_herzens.json`)
  - [x] *Episode 4: Duell in den Schatten* (`sao_ep4_duell_in_den_schatten.json`)
  - [x] *Episode 5: Der Glänzende Blick* (`sao_ep5_der_glaenzende_blick.json`)
- **Charaktere (V2-Karten in `presets/sword-art-online/`):**
  - [x] Kirito, Asuna, Klein, Lisbeth (JSONs angelegt).
- **Bilder:**
---

### 🌸 Kampagne 2.5: *The Quintessential Quintuplets* (*5-toubun no Hanayome*)
*Fünf hoffnungslose Schwestern, ein genialer Nachhilfelehrer und der gemeinsame Kampf um den Schulabschluss.*

- **Lorebooks:** *(Alle 3 in `lorebooks_gateway` & `lorebooks_registry.json` registriert)*
  - [x] *Die Nakano-Schwestern:* Eigenschaften, Familiendynamik, Mutter Rena (`quintuplets_nakano_sisters.json`).
  - [x] *Nachhilfe & Uesugi-Haushalt:* Futaros Methoden, Maruos Klausel, Raiha (`quintuplets_tutoring_study.json`).
  - [x] *Orte & Schulalltag:* Penthouse, Asahiyama-Oberschule, Bäckerei Revontulet (`quintuplets_world_locations.json`).
- **Stage-Szenarien (Episoden):** *(Alle 5 in `stages_gateway` & `stages_registry.json` registriert)*
  - [x] *Episode 1: Nachhilfe im Penthouse* (`quintuplets_ep1_penthouse_nachhilfe.json`)
  - [x] *Episode 2: Das Sommer-Feuerwerk* (`quintuplets_ep2_feuerwerk_gestaendnis.json`)
  - [x] *Episode 3: Die Bewährungsprobe* (`quintuplets_ep3_zwischenpruefung.json`)
  - [x] *Episode 4: Eingeschneit im Skigebiet* (`quintuplets_ep4_schneefahrt_huette.json`)
  - [x] *Episode 5: Das Schulfest der Erinnerungen* (`quintuplets_ep5_schulfest_gestaendnisse.json`)
- **Charaktere (V2-Karten in `presets/quintessential-quintuplets/`):**
  - [x] Ichika Nakano, Nino Nakano, Miku Nakano, Yotsuba Nakano, Itsuki Nakano, Futaro Uesugi (vollständige Profile, 2+ Begrüßungen, 3 Dialogbeispiele, DE/EN/RU).
- **Bilder:**
  - [x] Finale KI-Fanart: 6 Charakter-Avatare & 36 eigenständige, identitätserhaltende Expressions (Formate, PNG-Metadaten und Hub-Pfade geprüft).
  - [x] Quintuplets: Futaro Uesugi – finales Porträt und sechs eigenständige Emotionen, Preset- und Hub-Karte synchronisiert.
  - [x] Quintuplets: Ichika Nakano – finales Porträt und sechs eigenständige Emotionen, Preset- und Hub-Karte synchronisiert.
  - [x] Quintuplets: Itsuki Nakano – finales Porträt und sechs eigenständige Emotionen, Preset- und Hub-Karte synchronisiert.
  - [x] Quintuplets: Miku Nakano – finales Porträt und sechs eigenständige Emotionen, Preset- und Hub-Karte synchronisiert.
  - [x] Quintuplets: Nino Nakano – finales Porträt und sechs eigenständige Emotionen, Preset- und Hub-Karte synchronisiert.
  - [x] Quintuplets: Yotsuba Nakano – finales Porträt und sechs eigenständige Emotionen, Preset- und Hub-Karte synchronisiert.
  - [x] 5 finale KI-Szenenhintergründe (1376×768 PNG); eindeutige lokale Importnamen verhindern, dass vorhandene Platzhalter den Download blockieren.

---

## 📈 Aktueller Status

1. **Phase 1 (Einzel-Charaktere):**
   - [x] **Hayase Nagatoro** *(fertig inkl. 6 neuen Expressions, 2 Alternate Greetings & vollständiger i18n DE/EN/RU)*
   - [x] **Marin Kitagawa** *(fertig inkl. 6 neuen Expressions, 2 Alternate Greetings & vollständiger i18n DE/EN/RU)*
   - [x] **Frieren** *(tiefgründige Lore ~2400 Zeichen, 2 Alternate Greetings, i18n DE/EN/RU; neuer Avatar, neue Grimoire-Pose und 6 Expressions vorhanden)*
   - [x] **Yor Forger** *(tiefgründige Lore ~2800 Zeichen, 2 Alternate Greetings, Dialogbeispiele & vollständige i18n DE/EN/RU; Bilder vollständig neu generiert)*
   - [x] **Megumin** *(tiefgründige Lore ~2500 Zeichen, 2 Alternate Greetings, Dialogbeispiele & vollständige i18n DE/EN/RU; Bilder vollständig neu generiert)*
   - [x] **Kaguya Shinomiya** *(tiefgründige Lore ~2300 Zeichen, 2 Alternate Greetings, Dialogbeispiele & vollständige i18n DE/EN/RU; Bilder vollständig neu generiert)*
2. **Phase 2 (Kampagnen – 15 Lorebooks, 24 Episoden & 22 Cast-Karten fertig implementiert):**
   - [x] **Kampagne 2.1: Dungeon Meshi** *(Lorebooks, Szenarien & 4 Cast-Karten komplett mit voller Lore, 2 Alt-Greetings, Beispielen & i18n DE/EN/RU; Bilder vollständig neu generiert)*
   - [x] **Kampagne 2.2: Steins;Gate** *(Lorebooks, Szenarien & 4 Cast-Karten komplett mit voller Lore, 2 Alt-Greetings, Beispielen & i18n DE/EN/RU; Bilder vollständig neu generiert)*
   - [x] **Kampagne 2.3: Lycoris Recoil** *(Lorebooks, Szenarien & 4 Cast-Karten komplett mit voller Lore, 2 Alt-Greetings, Beispielen & i18n DE/EN/RU; Bilder vollständig neu generiert)*
   - [x] **Kampagne 2.4: Sword Art Online** *(Lorebooks, Szenarien & 4 Cast-Karten komplett mit voller Lore, 2 Alt-Greetings, Beispielen & i18n DE/EN/RU; Bilder vollständig neu generiert)*
   - [x] **Kampagne 2.5: The Quintessential Quintuplets** *(3 Lorebooks, 5 Episoden & 6 Cast-Karten komplett mit voller Lore, 2 Alt-Greetings, Beispielen & i18n DE/EN/RU; 6 finale KI-Porträts, 36 eigenständige Expressions und 5 finale Hintergründe; Prompts dokumentiert)*

## Bildbestand vom 04.10.2026

22 neue Avatare (700×937 PNG mit V2-Payload), 36 Expressions (640×800 WebP), eine zusätzliche Grimoire-Pose und 19 leere Szenenhintergründe (1376×768 PNG). Alle Avatare wurden ausschließlich aus Text generiert. Die Expressions und Grimoire-Pose verwenden nur die jeweils neu generierten Avatare als Referenz. Vorhandene Roadmap-Bilder wurden ersetzt.

Die Hintergründe liegen im jeweiligen Preset unter `backgrounds/`; Szenen referenzieren ihren Dateinamen über `starting_bg`. Beim Hub-Import einer Szene lädt die App die in `extensions.otakusoul_assets` gelisteten Hintergründe automatisch mit. Expressions liegen unter `presets/<paket>/expressions/`; die Karten-Zuordnung verwendet `expressions/<paket>/<emotion>.webp` für das lokale Expressions-Verzeichnis. Bereits importierte lokale Karten bei Bedarf erneut importieren.

## Originalfiguren vom 07.10.2026

- [x] Ren Takahashi und Aoi Mizuno, zwei 17-jährige Mitschüler der Klasse 2-B an der fiktiven Aobane-Oberschule in Yokohama. Vollständige V2-Profile auf DE/EN/RU, je ein Avatar, sechs Expressions, zwei alternative Begrüßungen und Hub-Karten. Paket: `presets/aobane-highschool/`. Ausschließlich im Repository bereitgestellt.


## Repository-Hub vom 07.10.2026

- [x] Ren Takahashi und Aoi Mizuno: zwei originale Mitschüler aus Klasse 2-B, vollständige Profile auf Deutsch, Englisch und Russisch, je ein V2-Porträt und sechs Expressions. Paket: `presets/aobane-highschool/`.
- [x] Yor Forger, Megumin und Kaguya Shinomiya als eigenständige Gateway-Karten in `cards_gateway/` und `soul_registry.json` aufgenommen. Expressions der Gateway-Karten verwenden Repository-URLs, damit sie ohne lokale Preset-Verzeichnisse funktionieren.
- [x] Alle 16 vorhandenen Kampagnenfiguren aus Dungeon Meshi, Steins;Gate, Lycoris Recoil und Sword Art Online mit ihren bestehenden Profilen und Avataren als Gateway-Karten registriert.
- [x] Den veralteten Bildstatus in `ROADMAP.md` anhand der tatsächlich vorhandenen Dateien abgeglichen; beide Roadmap-Dateien sind synchron.

Diese Arbeiten betreffen ausschließlich das Daten-Repository. Es wurden keine Charaktere, Bilder oder Szenen in eine lokale App-Installation importiert.

### Abgeschlossene Erweiterungen

- [x] Kampagnen-Expressions: 16/16 Figuren und 96/96 Bilder fertig (Einzelstand unten).


## Gesicherte Inhaltsarbeiten vom 07.10.2026

- [x] Vorhandene offene Profiländerungen von `sow_*` auf `custom_*` übernommen; neun Standalone-JSON-Karten und neue Expressions für die Standalone- und Sakura-Figuren ergänzt.
- [x] Vorhandene englische und russische Sakura-Szenenübersetzungen erhalten, PNG-Karten mit ihren JSON-Definitionen abgeglichen und relative Expressions-Pfade auf vorhandene Paketdateien korrigiert.
- [x] Bildinhalte der offenen Dateien unverändert erhalten; keine lokale App-Installation verändert.


<!-- campaign-expressions:start -->
### Kampagnen-Expressions – Fortschritt

16/16 Figuren vollständig; 96/96 Emotionsbilder fertig, 0 noch offen.

- [x] **Laios Touden** (dungeon-meshi): sechs Expressions geprüft und in Preset- und Hub-Karte eingebunden.
- [x] **Marcille Donato** (dungeon-meshi): sechs Expressions geprüft und in Preset- und Hub-Karte eingebunden.
- [x] **Chilchuck Tims** (dungeon-meshi): sechs Expressions geprüft und in Preset- und Hub-Karte eingebunden.
- [x] **Senshi** (dungeon-meshi): sechs Expressions geprüft und in Preset- und Hub-Karte eingebunden.
- [x] **Okabe Rintarou** (steins-gate): sechs Expressions geprüft und in Preset- und Hub-Karte eingebunden.
- [x] **Mayuri Shiina** (steins-gate): sechs Expressions geprüft und in Preset- und Hub-Karte eingebunden.
- [x] **Itaru Hashida** (steins-gate): sechs Expressions geprüft und in Preset- und Hub-Karte eingebunden.
- [x] **Suzuha Amane** (steins-gate): sechs Expressions geprüft und in Preset- und Hub-Karte eingebunden.
- [x] **Chisato Nishikigi** (lycoris-recoil): sechs Expressions geprüft und in Preset- und Hub-Karte eingebunden.
- [x] **Takina Inoue** (lycoris-recoil): sechs Expressions geprüft und in Preset- und Hub-Karte eingebunden.
- [x] **Mizuki Nakahara** (lycoris-recoil): sechs Expressions geprüft und in Preset- und Hub-Karte eingebunden.
- [x] **Kurumi** (lycoris-recoil): sechs Expressions geprüft und in Preset- und Hub-Karte eingebunden.
- [x] **Kirito (Kazuto Kirigaya)** (sword-art-online): sechs Expressions geprüft und in Preset- und Hub-Karte eingebunden.
- [x] **Asuna Yuuki** (sword-art-online): sechs Expressions geprüft und in Preset- und Hub-Karte eingebunden.
- [x] **Klein (Ryoutarou Tsuboi)** (sword-art-online): sechs Expressions geprüft und in Preset- und Hub-Karte eingebunden.
- [x] **Lisbeth (Rika Shinozaki)** (sword-art-online): sechs Expressions geprüft und in Preset- und Hub-Karte eingebunden.
<!-- campaign-expressions:end -->

## Kampagnen-Bildbestand vom 07.10.2026

Alle 16 Kampagnenfiguren verfügen jetzt zusätzlich zum bestehenden Hauptporträt über sechs neue Emotionsbilder (`neutral`, `happy`, `relaxed`, `surprised`, `angry`, `sad`): insgesamt 96 WebP-Dateien in 640×800. Die Bilder wurden mit dem eingebauten `image_gen`-Werkzeug anhand des jeweiligen vorhandenen Avatars erstellt und visuell geprüft. Preset-JSON, Preset-PNG und Hub-PNG sind abgeglichen; die bisherigen Profiltexte und Übersetzungen sowie die Hauptporträts bleiben erhalten. Vollständige Prompts liegen unter `presets/<paket>/expressions/<figur>/prompts.json`. Jede Figur wurde einzeln committed und gepusht. Keine lokale App-Installation wurde verändert.

## Repository-Pflege (2026-10-07)

- [x] Sieben veraltete Einmalskripte und drei überholte Root-Kartenkopien entfernt; wiederverwendbare Werkzeuge unter `tools/` erhalten.
- [x] Doppelte Roadmap entfernt; Paketierungswerkzeug pflegt ausschließlich `ROADMAP.md`, reine Prüfung schreibt keine Dateien.
- [x] README in DE, EN und RU aktualisiert; `AI.md` mit Struktur-/Formatregeln und Verweisen aus `AGENTS.md` / `CLAUDE.md` ergänzt.
- [x] `LICENSE` mit DE-/EN-/RU-Hinweisen zu KI-generierter Fanart, eigenen Beiträgen und fremden Rechten ergänzt; VRM-Lizenzhinweise erhalten.
- [x] Falschen Download-Link der Szene „Sky-Pirate Boarding Action“ auf die vorhandene eigene Szenendatei korrigiert.
- [x] 18 Gateway-Szenen und 6 Gateway-Lorebooks mit den vollständigen englischen und russischen Übersetzungen aus den Presets von No Game No Life und Sakura Succubus 3 synchronisiert.
- [x] Englische und russische Übersetzungen für alle 4 Dungeon-Meshi-Charaktere (Laios, Marcille, Chilchuck, Senshi) vollständig an das deutsche Original angeglichen, Dialogbeispiele übersetzt und PNG-Payloads synchronisiert.
- [x] Englische und russische Übersetzungen für alle 4 Steins;Gate-Charaktere (Okabe, Mayuri, Daru, Suzuha) vollständig an das deutsche Original angeglichen, Dialogbeispiele übersetzt und PNG-Payloads synchronisiert.
- [x] Englische und russische Übersetzungen für alle 4 Lycoris-Recoil-Charaktere (Chisato, Takina, Mizuki, Kurumi) vollständig an das deutsche Original angeglichen, Dialogbeispiele übersetzt und PNG-Payloads synchronisiert.
- [x] Englische und russische Übersetzungen für alle 4 Sword-Art-Online-Charaktere (Kirito, Asuna, Klein, Lisbeth) vollständig an das deutsche Original angeglichen, Dialogbeispiele übersetzt und PNG-Payloads synchronisiert.
- [x] Englische und russische Übersetzungen für alle 6 Phase-1-Charaktere (Nagatoro, Marin, Frieren, Yor, Megumin, Kaguya) vollständig an das deutsche Original angeglichen, Dialogbeispiele übersetzt, Gateway-Expressions verlinkt und PNG-Payloads synchronisiert.
- [x] Englische und russische Übersetzungen für alle 5 Szenen und 3 Lorebooks der Kampagne Dungeon Meshi sinngemäß implementiert.
- [x] Englische und russische Übersetzungen für alle 5 Szenen und 3 Lorebooks der Kampagne Steins;Gate sinngemäß implementiert.
- [x] Englische und russische Übersetzungen für alle 4 Szenen und 3 Lorebooks der Kampagne Lycoris Recoil sinngemäß implementiert.
- [x] Englische und russische Übersetzungen für alle 5 Szenen und 3 Lorebooks der Kampagne Sword Art Online sinngemäß implementiert.
- [x] Deutsche und russische Übersetzungen für alle 8 eigenständigen Szenen (The Vault of Eternal Winds, The Abyssal Trench, Reincarnated as the Unwanted Sage, Sky-Pirate Boarding, Infiltration of the Neon Hive, Rainy Day Library Sanctuary, The Last Supermarket, The Whispering Manor) sinngemäß implementiert.
- [x] Deutsche und russische Übersetzungen für 4 eigenständige Lorebooks (Cyberpunk 2077: Night City, Elden Ring: Lands Between, Modern Anime Academy & Romance, Isekai: Fantasy RPG World) sinngemäß implementiert.
- [x] Deutsche und russische Übersetzungen für 4 weitere eigenständige Lorebooks (Rust & Steel: Ruined Earth, Dimensional Rift: Anime Crossover, Outbreak: Realistic Zombie Survival, Voidfarer: Hard Sci-Fi Space Survival) sinngemäß implementiert.
- [x] Deutsche und russische Übersetzungen für das Spice and Wolf Lorebook sinngemäß implementiert.
- [x] Neuer Einzel-Charakter Lucy (Kaede / Nyu) aus Elfen Lied mit 700×937 Avatar, 6 abgestimmten 640×800 Expressions, V2-Definition, DE/EN/RU-Übersetzungen und Hub-Registrierung implementiert.
- [x] Story-Daten (`extensions.otakusoul_story`: Genre, Dauer, Schwierigkeit, Inhaltshinweise, Einsteiger-Markierung, je drei Startvorschläge in DE/EN/RU) sowie übersetzte Startorte und Tageszeiten für alle 45 Gateway-Szenen und die 18 Paket-Szenen von No Game No Life und Sakura Succubus 3 ergänzt.
- [x] Alle Registry-Einträge (47 Karten, 27 Lorebooks, 45 Szenen) mit `revision: 1` und `updated` versehen; Regel zum Erhöhen der Revision in `AI.md`; Spieltext „{name} (own version)“ in DE/RU ergänzt.
- [x] Alle 27 Gateway-Lorebooks und die 6 Paket-Lorebooks (No Game No Life, Sakura Succubus 3) ins App-Format umgestellt: `scan_depth` statt `n_depth`, `depends_on` → `chain_requires`, Trigger `semantic`/`range` → `keyword`, `random` → `always_on`, `chain` → `always_on` mit Voraussetzung, fehlende UIDs im Cyberpunk-Lorebook ergänzt, wirkungslose Soul-of-Waifu-Felder entfernt; Revisionen erhöht.
- [x] Alle 45 Gateway-Szenen: `extensions.otakusoul_assets` mit den Hintergründen ihres Pakets (die App lädt sie beim Hub-Import mit), veraltetes `conversation_method` entfernt (auch in den 18 Paket-Szenen), Platzhalter-Persona `"None"` der 8 eigenständigen Szenen geleert; Revisionen erhöht.
- [x] Acht NTE-Charakterkarten (Mint, Iroi, Lacrimosa, Nanally, Linko, Shinku sowie Esper Zero weiblich/männlich) mit je einem 700×937-Hauptporträt, vollständigen V2-Profilen auf DE/EN/RU, zwei Alternativbegrüßungen und drei Dialogbeispielen veröffentlicht. Damals auf Wunsch ohne Expressions; auf neuen Auftrag vom 19.10.2026 um vollständige Serien ergänzt (siehe NTE-Abschnitt unten). Paket: `presets/neverness-to-everness/`.
- [x] `recommended_models.json` als Spiegel des Starter-Katalogs der App neu aufgebaut (5 Apache-2.0-Modelle mit SHA-256, Grafikspeicher und DE/EN/RU-Beschreibung); ungeprüfte 70B-Liste vom Juni entfernt.
- [x] `AI.md` um Szenen- und Lorebook-Format der App, Hintergrund-Assets, 5e-Regeln, Spieltexte und Modellkatalog ergänzt; README DE/EN/RU („Stage“, automatische Hintergründe, Modellübersicht); Spieltext „None.“ in DE/RU.
- [x] `recommended_models.json` wird von der App beim Start geladen und ersetzt deren mitgelieferten Katalog, wenn die `version` höher ist; Format und Prüfregeln in `AI.md`.
- [x] `LICENSE`, `README.md` (DE/EN/RU) und die Lizenzhinweise der Paket-READMEs analog zu OtakuSoul auf die GNU General Public License v3.0 (`GPL-3.0-only`, Copyright (C) 2026 SnowwhiteOakheart) mit dreisprachigen Hinweisen zu Fanart, KI, Marken, VRM und Credits für Soul of Waifu (`jofizcd`) aktualisiert.


- [x] Fremde Inhalte entfernt: 8 Lorebooks und 8 Szenen von Jofi (Soul of Waifu / `sow-data`) sowie das Lorebook „Spice and Wolf“ (Don Chacha Muchacho); Registries, LICENSE-Credits und README angepasst. Das Repository enthält nur noch eigene Inhalte.

- [x] 20 verwaiste Altkarten in `cards_gateway/` entfernt (17 davon unterschieden sich nur in der Groß-/Kleinschreibung von den aktuellen und brachen das Klonen unter Windows/macOS) sowie die drei überholten Karten in `presets/cards/`.

- [x] `post_history_instructions` (die Anweisung, die jede Runde an das Modell geht) für 20 Figuren aus Dungeon Meshi, Steins;Gate, Lycoris Recoil, Sword Art Online, Frieren, Megumin, Kaguya und Yor in EN/RU ergänzt (Preset-JSON, Preset-PNG und Gateway-PNG); Registry-Revisionen erhöht.

- [x] Je eine weitere alternative Begrüßung (DE/EN/RU) für Chlammy, Fiel, Izuna, Jibril und Stephanie, damit alle Karten mindestens zwei haben.

- [x] `tools/validate_content.py`: allgemeiner Validator für Karten, Szenen, Lorebooks und Registries; `--sync-registry` übernimmt Listentexte samt Übersetzungen in die Registries (die App zeigt die Hub-Liste damit in der Oberflächensprache).
- [x] Drei neue, eigens für OtakuSoul entwickelte Feature-Lorebooks (je 12 Einträge, DE/EN/RU, mit `always_on`, `keyword`, `regex`, `tension`, `secondary_keys`, `exclude_key`, `chain_requires`, `chain_activates`, `injection_behavior` `active`/`passive`), sechs darauf abgestimmte Stage-Szenen (DE/EN/RU, mit `otakusoul_story`, `otakusoul_assets`, 5e-SG und Party-Integration) sowie 9 maßgeschneiderte 16:9-Szenenhintergründe (1376×768 PNG ohne Figuren im Bild, je 3 pro Themenwelt inklusive Wechsel-Kulissen für den Spielleiter):
  - **Night City 2077 – Edgerunner, Konzerne & das Netz** (`cyberpunk_night_city.json`) + Szenen *Night City 2077: Geist im Subnetz* (`cyberpunk_ghost_in_subgrid.json`) & *Night City 2077: Kalter Deal im Afterlife* (`cyberpunk_afterlife_deal.json`) + 3 Hintergründe in `presets/cyberpunk-night-city/backgrounds/`
  - **Aetheria Chronicles – Isekai-Abenteuer, Gilden & Systemmagie** (`isekai_fantasy_rpg_world.json`) + Szenen *Isekai-Chroniken: Beschworen mit Stufe Null* (`isekai_null_mana_summoning.json`) & *Isekai-Chroniken: Der verbotene Dungeon-Kern* (`isekai_labyrinth_of_aetheria.json`) + 3 Hintergründe in `presets/isekai-aetheria/backgrounds/`
  - **Herzensklopfen & Kirschblüten – Anime-Romance & Harem-Dynamik** (`modern_anime_academy_romance.json`) + Szenen *Herzklopfen nach Schulschluss: Ein Schirm für vier* (`romance_rainy_clubroom_confessions.json`) & *Kulturfest-Legende: Wem gehört der letzte Tanz?* (`romance_rooftop_festival_fireworks.json`) + 3 Hintergründe in `presets/anime-academy-romance/backgrounds/`

- [x] `recommended_models.json` 3.1.0: mit der SoW-Liste abgeglichen, 9 Kandidaten in der App gemessen (RTX 4070 Ti SUPER); Gemma 4 E4B/12B/26B-A4B/31B, Qwen3.5 9B, Qwen3.6 35B-A3B, Hearthfire 24B sowie Rocinante-X 12B und Cydonia 24B (ohne Lizenzangabe, mit Hinweis).

<!-- re-zero:start -->
### Re:Zero-Charaktere mit Expressions

6/6 Figuren mit DE/EN/RU-Profilen, je einem Hauptporträt und sechs Emotionsbildern veröffentlicht.

- [x] Rem: Hauptporträt, sechs Expressions, V2-Preset und Gateway.
- [x] Ram: Hauptporträt, sechs Expressions, V2-Preset und Gateway.
- [x] Echidna: Hauptporträt, sechs Expressions, V2-Preset und Gateway.
- [x] Beatrice: Hauptporträt, sechs Expressions, V2-Preset und Gateway.
- [x] Subaru Natsuki: Hauptporträt, sechs Expressions, V2-Preset und Gateway.
- [x] Emilia: aus der OtakuSoul-App übernommen (19.10.2026), Hauptporträt im Altformat 640×800, sechs Expressions, V2-Preset und Gateway.
- [ ] Emilia: neun Zusatzslots (`blush` … `afterglow`) wie bei den übrigen Re:Zero-Figuren ergänzen.
- [x] Frühere App-Starter-Geschichten unverändert übernommen (19.10.2026): `frozen_bells_emilia` (Emilia) sowie `hanami_live_ayu_cosmos`, `missing_mic_ayu_cosmos`, `ryokan_night_ayu_cosmos` (Ayu und Cosmos); die App bringt Neufassungen mit eigenen Figuren mit.
<!-- re-zero:end -->


### Overlord – Charaktere und erweiterte Expressions

- [x] **Ainz Ooal Gown**: V2-Profil DE/EN/RU, zwei alternative Begrüßungen, drei Dialogbeispiele, finales Profilbild und alle 15 Bildslots; PNG-Karten, Hub-URLs und Bildformate geprüft.
- [x] **Albedo**: V2-Profil DE/EN/RU, zwei alternative Begrüßungen, drei Dialogbeispiele, finales Profilbild und alle 15 Bildslots; PNG-Karten, Hub-URLs und Bildformate geprüft.
- [x] **Shalltear Bloodfallen**: V2-Profil DE/EN/RU, zwei alternative Begrüßungen, drei Dialogbeispiele, finales Profilbild und alle 15 Bildslots; PNG-Karten, Hub-URLs und Bildformate geprüft.


### Zusatzemotionen – bestehende Figuren (ohne NTE)

49 Figuren erhalten je neun Zusatzbilder (441 insgesamt). Nur bestehende Emotionssätze; NTE bleibt ausgeschlossen.

- [x] **Ichika Nakano** (quintessential-quintuplets): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Futaro Uesugi** (quintessential-quintuplets): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Itsuki Nakano** (quintessential-quintuplets): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Miku Nakano** (quintessential-quintuplets): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Nino Nakano** (quintessential-quintuplets): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Yotsuba Nakano** (quintessential-quintuplets): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Aoi Mizuno** (aobane-highschool): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Ren Takahashi** (aobane-highschool): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Chilchuck Tims** (dungeon-meshi): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Laios Touden** (dungeon-meshi): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Marcille Donato** (dungeon-meshi): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Senshi** (dungeon-meshi): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Lucy** (elfen-lied): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Frieren** (frieren): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Kaguya Shinomiya** (kaguya-shinomiya): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Chisato Nishikigi** (lycoris-recoil): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Kurumi** (lycoris-recoil): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Mizuki Nakahara** (lycoris-recoil): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Takina Inoue** (lycoris-recoil): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Marin Kitagawa** (marin-kitagawa): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Megumin** (megumin): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Chlammy Zell** (no-game-no-life): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Fiel Nirvalen** (no-game-no-life): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Izuna Hatsuse** (no-game-no-life): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Jibril** (no-game-no-life): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Shiro** (no-game-no-life): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Sora** (no-game-no-life): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Stephanie Dola** (no-game-no-life): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Beatrice** (re-zero): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Echidna** (re-zero): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Ram** (re-zero): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Rem** (re-zero): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Subaru Natsuki** (re-zero): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Ayu Ikue** (sakura-succubus-3): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Cosmos** (sakura-succubus-3): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Hayase Nagatoro** (nagatoro): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Hazel Williams** (sakura-succubus-3): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Hifumi Yamamoto** (sakura-succubus-3): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Marina Wakatsuki** (sakura-succubus-3): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Yue** (sakura-succubus-3): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Itaru Hashida** (steins-gate): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Mayuri Shiina** (steins-gate): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Okabe Rintarou** (steins-gate): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Suzuha Amane** (steins-gate): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Asuna Yuuki** (sword-art-online): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Kirito (Kazuto Kirigaya)** (sword-art-online): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Klein (Ryoutarou Tsuboi)** (sword-art-online): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.

**Abgeschlossen am 19.10.2026:** 49/49 Figuren, 441 Zusatzbilder. Lisbeth und Yor sind vollständig ergänzt. Alle 52 Figuren mit bestehendem Emotionssatz einschließlich Overlord haben 15 Slots; NTE bleibt unverändert.

- [x] **Lisbeth (Rika Shinozaki)** (sword-art-online): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Yor Forger** (yor-forger): alle 15 Slots, neun neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.


### NTE – vollständige Emotionsserien

Acht NTE-Figuren erhalten auf Auftrag vom 19.10.2026 je 15 Bilder (120 insgesamt).

- [x] **Lacrimosa** (neverness-to-everness): alle 15 Slots, 15 neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Linko** (neverness-to-everness): alle 15 Slots, 15 neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Shinku** (neverness-to-everness): alle 15 Slots, 15 neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Iroi** (neverness-to-everness): alle 15 Slots, 15 neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Esper Zero (Female)** (neverness-to-everness): alle 15 Slots, 15 neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Mint** (neverness-to-everness): alle 15 Slots, 15 neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Nanally Colucci** (neverness-to-everness): alle 15 Slots, 15 neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.
- [x] **Esper Zero (Male)** (neverness-to-everness): alle 15 Slots, 15 neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.

**NTE abgeschlossen:** 8/8 Figuren, 120/120 einzeln generierte Emotionsbilder. Alle 60 Charaktere des Repositorys haben damit vollständige 15er-Serien. Profile und bestehende Porträtpixel erhalten.
- [x] Stimmbeschreibungen (`data.extensions.otakusoul_voice.description`, Englisch) für alle 61 Hub-Charaktere in JSON-, Preset-PNG- und Gateway-PNG-Karten ergänzt (23.10.2026); Registry-Revisionen erhöht.


## 🚀 Sternenbruch – Die letzte Verbindung (23.10.2026)

Eigenständige Science-Fiction-Kampagne für den Hub; keine lokale App-Installation. Alle Hauptfiguren erwachsen, SFW, Texte in DE/EN/RU/JA.

- [x] Sechs individuelle V2-Profile: Mara Venn, Juno Serrat, Saeli, Dr. Idris Vale, Kian Rook und IVO; jeweils zwei alternative Einstiege und drei eigene Dialogbeispiele.
- [x] Drei Lorebooks mit 16 gezielt ausgelösten Einträgen: Welt & Technik, Kulturen & Fraktionen, Crew & Orte.
- [x] Sechs Soulstages mit eigenständigem Einstieg, überprüfbaren Hinweisen, je drei Startvorschlägen pro Sprache und mehreren Lösungswegen.
- [x] Sechs PNG-Porträts und 90 einzeln generierte, referenzgestützte Emotionsbilder; zehn Hintergründe.
- [x] PNG-Payloads, Gateway-Karten, drei Registries und Bildverweise geprüft; vollständige Inhaltsvalidierung: 0 Fehler.
- [x] Japanisch nachgetragen (27.10.2026): sechs Profile (JSON, Preset- und Gateway-PNG über `tools/set_card_translations.py`, Bildpixel unverändert) und sechs Soulstages samt je drei Startvorschlägen; Registries synchronisiert, Revisionen erhöht. Validierung: 0 Fehler, 0 Warnungen.

Prompts, Herkunft und nichtsexuelle Interpretation der technischen Romance-Slots: `presets/sternenbruch/image_prompts.json`; Paketbeschreibung in DE/EN/RU: `presets/sternenbruch/README.md`.

### Geprüfte Sternenbruch-Figuren

- [x] Mara Venn: V2-JSON/PNG, Gateway-Karte und 15 unterschiedliche Emotionsbilder geprüft.
- [x] Juno Serrat: V2-JSON/PNG, Gateway-Karte und 15 unterschiedliche Emotionsbilder geprüft.
- [x] Saeli: V2-JSON/PNG, Gateway-Karte und 15 unterschiedliche Emotionsbilder geprüft.
- [x] Dr. Idris Vale: V2-JSON/PNG, Gateway-Karte und 15 unterschiedliche Emotionsbilder geprüft.
- [x] Kian Rook: V2-JSON/PNG, Gateway-Karte und 15 unterschiedliche Emotionsbilder geprüft.
- [x] IVO: V2-JSON/PNG, Gateway-Karte und 15 unterschiedliche Emotionsbilder geprüft.

## Sammlungs-Titelbilder (25.10.2026)

- [x] Alle 11 Sammlungen mit individuellen, KI-generierten Figuren-/Schauplatz-Keyvisuals als `presets/<paket>/cover.webp` (960×540) ausgestattet; Referenzen, Prompts und Nachbearbeitung je Paket in `cover_prompt.json` dokumentiert.

- [x] Quintuplets-Titelbild wegen fehlerhafter Arm-Anatomie neu generiert, Figurenposen vereinfacht und Arme/Hände visuell geprüft.
