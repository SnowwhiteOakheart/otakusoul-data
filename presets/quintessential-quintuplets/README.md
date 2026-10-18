# The Quintessential Quintuplets (5-toubun no Hanayome)

Paket für **OtakuSoul**: Die fünf Nakano-Schwestern (*Ichika*, *Nino*, *Miku*, *Yotsuba*, *Itsuki*) und ihr engagierter Nachhilfelehrer *Futaro Uesugi* an der Asahiyama-Oberschule.

## Inhalt

- **Charaktere (6):**
  - `Ichika Nakano`: Älteste Schwester, modisch, verspielt, heimliche Schauspielerin (`ichika_nakano.json`).
  - `Nino Nakano`: Zweitälteste, stolze Tsundere, beschützende Köchin mit Schmetterlingsschleifen (`nino_nakano.json`).
  - `Miku Nakano`: Drittälteste, schüchterne Sengoku-Historikerin, lernt backen, trägt Kopfhörer (`miku_nakano.json`).
  - `Yotsuba Nakano`: Viertälteste, sonniges Sport-Ass mit grünem Schleifenband, selbstlose Helferin (`yotsuba_nakano.json`).
  - `Itsuki Nakano`: Jüngste, ernste Schülerin mit Sternchen-Spangen, will Lehrerin werden, heimliche Feinschmeckerin (`itsuki_nakano.json`).
  - `Futaro Uesugi`: Akademischer Überflieger, pragmatischer Musterschüler und hingebungsvoller Nachhilfelehrer (`futaro_uesugi.json`).
- **Soul Stages (5):**
  - *Episode 1: Nachhilfe im Penthouse* (`quintuplets_ep1_penthouse_nachhilfe.json`)
  - *Episode 2: Das Sommer-Feuerwerk* (`quintuplets_ep2_feuerwerk_gestaendnis.json`)
  - *Episode 3: Die Bewährungsprobe* (`quintuplets_ep3_zwischenpruefung.json`)
  - *Episode 4: Eingeschneit im Skigebiet* (`quintuplets_ep4_schneefahrt_huette.json`)
  - *Episode 5: Das Schulfest der Erinnerungen* (`quintuplets_ep5_schulfest_gestaendnisse.json`)
- **Lorebooks (3):**
  - *Die Nakano-Schwestern* (`quintuplets_nakano_sisters.json`)
  - *Nachhilfe & Uesugi-Haushalt* (`quintuplets_tutoring_study.json`)
  - *Orte & Schulalltag* (`quintuplets_world_locations.json`)
- **Hintergründe (5):**
  - Penthouse-Wohnzimmer, Sommerfest-Schreintreppe, Klassenzimmer, Skihütte, Schuldach bei Abenddämmerung.

## Bildherkunft und Formate

Die Platzhalter wurden durch KI-generierte Fanart mit dem eingebauten OpenAI-Bildgenerator (`image_gen`) ersetzt: sechs Porträts (700×937 PNG), je sechs eigenständige Emotionen (640×800 WebP: neutral, happy, relaxed, surprised, angry, sad) und fünf Hintergründe (1376×768 PNG). Alle Emotionsbilder wurden mit dem jeweiligen Masterporträt als Identitätsreferenz erstellt; Yotsubas Profil zeigt die fröhliche und Itsukis Profil die neutrale Variante mit erweitertem Bildausschnitt. Frisur, Kleidung und Zeichenstil bleiben je Figur konsistent. Preset- und Gateway-PNGs enthalten weiterhin die vollständigen bisherigen V2-Kartendaten.

Die tatsächlich verwendeten Prompts, Referenzen und Nachbearbeitung stehen in [`image_prompts.json`](image_prompts.json) sowie `expressions/<figur>/prompts.json`. Die ursprünglichen Promptentwürfe bleiben zur Nachvollziehbarkeit erhalten. Es handelt sich um inoffizielle Fanart; Rechte an Figuren und Originalwerk verbleiben bei den jeweiligen Rechteinhabern.

Die fünf Soulstages laden die Bilder unter eindeutigen lokalen Namen (`quintuplets_*_artwork.png`), damit bereits importierte Platzhalter den Download beim Szenenupdate nicht verhindern. Die öffentlichen Bildpfade im Repository bleiben erhalten. Die Schauplätze entsprechen zugleich den Orten der drei Lorebooks; Lorebooks selbst unterstützen derzeit keine Hintergrundbild-Zuordnung.

EN: AI-generated fan art created with OpenAI image_gen: six portraits, 36 individual expressions and five scene backgrounds. Exact prompts and processing are documented in image_prompts.json and expressions/<character>/prompts.json. Character and original-work rights remain with their respective owners. Updated scenes use new local background filenames so installed placeholders do not prevent downloading the final artwork.

RU: Неофициальный фан-арт, созданный с помощью OpenAI image_gen: шесть портретов, 36 отдельных эмоций и пять фонов. Точные запросы и обработка описаны в image_prompts.json и expressions/<персонаж>/prompts.json. Права на персонажей и оригинальное произведение принадлежат соответствующим правообладателям. Обновлённые сцены используют новые локальные имена фонов, чтобы установленные заглушки не мешали загрузке готовых изображений.
