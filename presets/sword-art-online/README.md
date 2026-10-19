# Sword Art Online – Kampagnen-Preset

Ein vollständiges Rollenspiel- und Kampagnenpaket für **Sword Art Online (Aincrad)** (ソードアート・オンライン).

## ⚔️ Charaktere

| Figur | Datei | Rolle |
|---|---|---|
| **Kirito (Kazuto Kirigaya)** | `kirito_kazuto.json` / `kirito_kazuto.png` | Der „Schwarze Schwertkämpfer“, Solo-Spieler und ehemaliger Beater |
| **Asuna Yuuki** | `asuna_yuuki.json` / `asuna_yuuki.png` | Der „Blitz“, Vize-Kommandantin der Ritter des Blutschwurs |
| **Klein (Ryoutarou Tsuboi)** | `klein_ryoutarou.json` / `klein_ryoutarou.png` | Treuer Freund, Anführer der Gilde Fuurinkazan und Katanakämpfer |
| **Lisbeth (Rika Shinozaki)** | `lisbeth_rika.json` / `lisbeth_rika.png` | Meister-Schmiedin auf Ebene 48, fertigt Kiritos Schwert Dark Repulser |

- **Bilder:** Haupt-Avatare als 700×937 PNG mit integrierter Character-Card-V2-Definition (`chara`).
- **Expressions:** Je 6 Mimik-Porträts (640×800 WebP) unter `expressions/<figur>/`: `neutral`, `happy`, `relaxed`, `surprised`, `angry`, `sad`.
- **Sprachen:** Deutsch als Ausgangssprache mit vollständigen englischen und russischen Übersetzungen (`extensions.otakusoul_i18n`).

## 🗺️ Szenen und Lorebooks

Die zugehörigen Soul-Stage-Szenen und Lorebooks sind im Gateway veröffentlicht:
- **Szenen (`stages_gateway/`):** 5 Episoden von Episode 1 (*Die Verkündung des Todes*) bis Episode 5 (*Der glänzende Blick*).
- **Hintergründe (`backgrounds/`):** 5 passende 16:9-Szenenhintergründe (1376×768 PNG), darunter die Stadt des Anfangs, Ebenen-Bossräume und Lisbeths Schmiede.
- **Lorebooks (`lorebooks_gateway/`):** `sao_aincrad_rules.json`, `sao_aincrad_sword_skills.json`, `sao_aincrad_world.json`.

## 📜 Herkunft und Lizenz

Alle Charakterporträts und Hintergründe sind originäre KI-generierte Fanarts, die aus Textbeschreibungen entstanden sind. Es wurden keine Original-Screenshots oder Grafiken aus dem Anime oder der Light Novel übernommen.

- **Eigene Texte und Skripte:** Unterliegen der GNU General Public License v3.0 (`GPL-3.0-only`, siehe [LICENSE](../../LICENSE)).
- **Marken & Urheberrecht:** *Sword Art Online* ist das geistige Eigentum von Reki Kawahara / abec / ASCII Media Works / KADOKAWA / A-1 Pictures. Dies ist ein inoffizielles Fanprojekt ohne kommerzielle Absicht oder Verbindung zu den Rechteinhabern.


## Zusatzemotionen / Additional expressions / Дополнительные эмоции — 19.10.2026

**DE:** Alle Figuren dieses Pakets haben jetzt 15 Slots. Die ursprünglichen sechs Bilder bleiben erhalten; neun einzeln generierte SFW-Varianten wurden ergänzt. Prompts und Verarbeitung: `expressions/<figur>/additional_prompts.json`. Die technisch romantisch benannten Slots zeigen höfliche Zuversicht, Aufmerksamkeit, Siegesfreude und Erleichterung, ausschließlich nichtsexuell. OpenAI image_gen (eingebaut), 640×800 WebP, Qualität 92; bestehende Herkunfts- und Rechtehinweise gelten weiter.

**EN:** All characters in this package now have 15 slots. The original six images are preserved; nine individually generated SFW variants were added. Prompts and processing: `expressions/<character>/additional_prompts.json`. Romance-named technical slots show courteous confidence, alertness, triumphant joy and relief, entirely nonsexual. Built-in OpenAI image_gen, 640×800 WebP, quality 92; existing provenance and rights notices remain applicable.

**RU:** У всех персонажей пакета теперь 15 слотов. Исходные шесть изображений сохранены; добавлены девять отдельно сгенерированных неэротических вариантов. Запросы и обработка: `expressions/<персонаж>/additional_prompts.json`. Технические слоты романтики показывают учтивую уверенность, внимание, радость победы и облегчение без эротики. Встроенный OpenAI image_gen, WebP 640×800, качество 92; прежние сведения о происхождении и правах сохраняют силу.
