# NTE: Neverness to Everness – Charakter-Preset

Acht eigenständige Character-Card-V2-Karten für **NTE: Neverness to Everness**:

| Figur | Datei | Schwerpunkt |
|---|---|---|
| **Mint** | `mint.json` / `mint.png` | Kontaktfreudige CSU-2-Spürnase mit Hethereau-Ortskenntnis |
| **Iroi** | `iroi.json` / `iroi.png` | Höfliche Traum-Esperin mit drei Traumschafen |
| **Lacrimosa** | `lacrimosa.json` / `lacrimosa.png` | Schläfriges ETD-4-Kraftpaket und Tomatenfan |
| **Nanally Colucci** | `nanally.json` / `nanally.png` | Großspurige, warmherzige Ichi-daime von Eibon |
| **Linko** | `linko.json` / `linko.png` | Sprunghafte ETD-6-Telepathin mit Xiaozhen |
| **Esper Zero (Female)** | `zero_female.json` / `zero_female.png` | Weibliche Variante des Nexus-spürenden Eibon-Appraisers |
| **Esper Zero (Male)** | `zero_male.json` / `zero_male.png` | Männliche Variante des Nexus-spürenden Eibon-Appraisers |
| **Shinku** | `shinku.json` / `shinku.png` | Reservierte CSU-2-Drachin mit kompromisslosem Schutzinstinkt |

- **Bilder:** Pro Charakter genau ein neu generiertes Hauptporträt als 700×937 PNG mit eingebetteter Character-Card-V2-Definition (`chara`). Die ursprünglich auf Wunsch ausgelassenen Emotionsbilder wurden auf neuen Auftrag vom 19.10.2026 ergänzt: 15 je Figur, 120 insgesamt.
- **Profile:** Deutsch als Ausgangssprache mit vollständigen englischen und russischen Übersetzungen, zwei alternativen Begrüßungen und drei Dialogbeispielen je Sprache.
- **Hub:** Eigenständige Gateway-PNGs unter `cards_gateway/`; keine Inhalte wurden in eine lokale App-Installation importiert.

### Sammlung, Story & Lorebooks (01.11.2026)
Die Figuren sind über die Hub-Sammlung `neverness_to_everness` gebündelt („Alles installieren“ lädt den vollständigen Cast). Zur Sammlung gehören:
- **Soul Stage:** `nte_ep1_die_anomalie_im_spiegelbezirk` (*Die Anomalie im Spiegelbezirk*, 6 Gruppenmitglieder: Nanally, Mint, Iroi, Linko, Esper Zero weiblich & männlich; 3 Startvorschläge je Sprache, automatischer Hintergrunddownload).
- **Lorebooks:** `nte_hethereau_world.json` (*Die Metropole Hethereau*, 6 Einträge) und `nte_eibon_crew.json` (*Eibon-Crew & Agenten*, 6 Einträge), jeweils vollständig in DE/EN/RU/JA.
- **Bilder:** Sammlungstitelbild `cover.webp` (960×540 WebP) und Szenenhintergrund `backgrounds/nte_hethereau_city.webp` (1376×768 WebP); Prompts und Nachbearbeitung dokumentiert in `cover_prompt.json`.

## Bildherkunft

Die Porträts sind neu erzeugte KI-Fanarts. Das integrierte OpenAI-ImageGen-Werkzeug erhielt ausschließlich Textbeschreibungen; es wurden keine Originalbilder, Screenshots oder fremden Fanarts als Bildeingabe verwendet. Die visuellen Merkmale und Profile wurden anhand öffentlich zugänglicher NTE-Charaktervorstellungen und des offiziellen Charakterbereichs geprüft. Der vollständige Generierungs- und Nachbearbeitungsnachweis steht in [`image_prompts.json`](image_prompts.json).

## Marken und Urheberrecht

*NTE: Neverness to Everness*, seine Figuren und die zugehörigen Marken sind Eigentum von Hotta Studio / Perfect World. Dieses Paket ist ein inoffizielles Fanprojekt und steht in keiner Verbindung zu den Rechteinhabern. Die neu verfassten Profildaten und Hilfsstrukturen unterliegen der Repository-Lizenz; diese Lizenz beansprucht keine Rechte an den zugrunde liegenden Figuren oder Marken.

## Emotionen / Expressions / Эмоции — 19.10.2026

**DE:** Jede der acht Figuren hat alle 15 aktuellen Slots: `neutral`, `happy`, `sad`, `angry`, `surprised`, `relaxed`, `blush`, `teasing`, `fear`, `disgust`, `crying`, `seductive`, `aroused`, `ecstasy`, `afterglow`. Alle 120 Bilder wurden einzeln mit dem eingebauten OpenAI image_gen aus dem jeweiligen Hauptporträt erzeugt, visuell geprüft und als 640×800 WebP (Qualität 92, Lanczos-Ausschnitt) gespeichert. Die vier technisch romantisch benannten Slots zeigen ausschließlich höfliche Zuversicht, Aufmerksamkeit, Siegesfreude und Erleichterung; alle Darstellungen sind nichtsexuell und altersgerecht. Hauptporträtpixel und Profiltexte bleiben erhalten. Prompts und Referenzen: `expressions/<figur>/additional_prompts.json`. Gateway-Karten und Registry-Revisionen sind aktualisiert. Die obigen Angaben zur reinen Textgenerierung betreffen die ursprünglichen Hauptporträts.

**EN:** Each of the eight characters has all 15 current slots, totalling 120 individually generated expression images. Built-in OpenAI image_gen used each original AI portrait as its reference. The images were visually checked and saved as 640×800 WebP (quality 92, Lanczos crop). Romance-named technical slots contain only courteous confidence, alertness, triumphant joy and relief; all images are nonsexual and age-appropriate. Main portrait pixels and profile text are preserved. Exact prompts and references: `expressions/<character>/additional_prompts.json`. Gateway cards and registry revisions are updated. The text-only generation description above applies to the original main portraits. Characters are bundled under the `neverness_to_everness` Hub collection including story `nte_ep1_die_anomalie_im_spiegelbezirk` (Nanally, Mint, Iroi, Linko, Esper Zero female & male), lorebooks `nte_hethereau_world.json` and `nte_eibon_crew.json`, cover `cover.webp` (960×540) and background `backgrounds/nte_hethereau_city.webp`.

**RU:** У каждого из восьми персонажей есть все 15 слотов, всего 120 отдельно сгенерированных изображений эмоций. Встроенный OpenAI image_gen использовал исходный ИИ-портрет соответствующего персонажа как референс. Изображения визуально проверены и сохранены в WebP 640×800 (качество 92, обрезка Lanczos). Технические слоты романтики содержат только учтивую уверенность, внимание, радость победы и облегчение; все изображения неэротические и соответствуют возрасту. Пиксели основных портретов и тексты профилей сохранены. Точные запросы и референсы: `expressions/<персонаж>/additional_prompts.json`. Карточки Gateway и ревизии реестра обновлены. Описание генерации только по тексту выше относится к исходным основным портретам. Персонажи объединены в коллекцию Hub `neverness_to_everness`, включающую сюжет `nte_ep1_die_anomalie_im_spiegelbezirk` (Наналли, Минт, Ирои, Линко, Эспер Зеро ж/м), книги знаний `nte_hethereau_world.json` и `nte_eibon_crew.json`, обложку `cover.webp` (960×540) и фон `backgrounds/nte_hethereau_city.webp`.
