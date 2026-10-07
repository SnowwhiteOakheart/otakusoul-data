# 🌸 OtakuSoul Data – Optionale Inhalte & Community-Hub

Offizielles Daten- und Community-Repository für optionale Inhalte von **[OtakuSoul](https://github.com/SnowwhiteOakheart/OtakuSoul)**.

Dieses Repository enthält modulare Inhalte, die **nicht** fest im Basis-Release von OtakuSoul ausgeliefert werden, sondern optional über den In-App **Soul Hub** geladen oder manuell importiert werden können:
- Zusätzliche **Charakterkarten** (V2 PNG mit eingebetteten Metadaten & Lorebooks)
- Vollständige **Kampagnen & Presets** (mit Szenen, Hintergründen, Lorebooks und Expressions)
- **Soul-Stage-Szenarien** für das interaktive Rollenspiel
- **Welt-Lorebooks** für Lore- und Wissensintegration
- Optionale **3D-VRM-Avatarmodelle**

---

## 📂 Verzeichnisstruktur

```
otakusoul-data/
├── cards_gateway/         # Standalone V2 PNG-Charakterkarten für das Soul Gateway
├── lorebooks_gateway/     # Welt-Lorebooks im JSON-Format für das Lorebook Gateway
├── stages_gateway/        # Szenarien im JSON-Format für das Soul-Stage Gateway
├── presets/               # Vollständige Kampagnenpakete
│   ├── cards/             # Standalone-Charakterkarten (PNG)
│   ├── no-game-no-life/   # NGNL-Kampagne (Charaktere, 12 Episoden, Lorebooks, Hintergründe, Expressions)
│   └── sakura-succubus-3/ # Sakura-Succubus-3-Paket (Charaktere, 6 Szenen, Lorebooks, Hintergründe)
├── avatars/
│   └── vrm/               # Optionale 3D-VRM-Avatare inkl. lizenzen.txt
├── soul_registry.json     # Online-Katalog für Charakterkarten im Soul Hub
├── lorebooks_registry.json# Online-Katalog für Welt-Lorebooks im Soul Hub
├── stages_registry.json   # Online-Katalog für Szenarien im Soul Hub
└── recommended_models.json# Empfohlene GGUF-Modelle für den Model-Hub
```

---

## 🛠️ Neue Inhalte hinzufügen

### 1. Neuen Charakter für das Soul Gateway bereitstellen
1. Speichere die V2-Charakterkarte als PNG in `cards_gateway/<Name>.png`.
2. Trage den Charakter in `soul_registry.json` ein:
   ```json
   {
     "name": "Charakter Name",
     "author": "Dein Name",
     "download_url": "https://raw.githubusercontent.com/SnowwhiteOakheart/otakusoul-data/main/cards_gateway/Charakter_Name.png"
   }
   ```

### 2. Neues Welt-Lorebook bereitstellen
1. Lege die JSON-Datei in `lorebooks_gateway/<name>.json` ab.
2. Trage das Lorebook in `lorebooks_registry.json` ein.

### 3. Neues Soul-Stage-Szenario bereitstellen
1. Lege die Szenen-JSON in `stages_gateway/<name>.json` ab.
2. Trage das Szenario in `stages_registry.json` ein.

### 4. Ein ganzes Kampagnen-Preset bereitstellen
1. Erstelle einen Ordner unter `presets/<kampagnen-name>/`.
2. Strukturiere das Preset mit Charakteren, `scenes/`, `lorebooks/`, `backgrounds/` und optional `expressions/`.
3. Siehe `presets/no-game-no-life/` oder `presets/sakura-succubus-3/` als Referenz.

---

## 🎭 3D-VRM-Avatare
Unter `avatars/vrm/` liegen zusätzliche VRM-Modelle für OtakuSoul.
- Die Lizenz- und Quellangaben für alle Modelle sind in `avatars/vrm/lizenzen.txt` hinterlegt.
- Nur Modelle mit freier Weiterverbreitungserlaubnis (z. B. CC-BY oder Erlaubnis auf VRoid Hub) dürfen hier aufgenommen werden.

---

## 📜 Lizenz
- Der Repository-Rahmen und eigene Daten stehen unter der **MIT-Lizenz** (siehe [LICENSE](LICENSE)).
- Einzelne Charakterkarten, Texte und 3D-Modelle unterliegen ihren jeweiligen Urheberrechten bzw. Fan-Content-Lizenzen (siehe Dokumentation im jeweiligen Ordner).

## Schulalltag in Aobane

Das Originalpaket [`presets/aobane-highschool/`](presets/aobane-highschool/README.md) enthält Ren Takahashi und Aoi Mizuno, zwei 17-jährige Mitschüler der Klasse 2-B einer fiktiven Highschool in Yokohama. Beide Karten sind in Deutsch, Englisch und Russisch vollständig ausgearbeitet und verfügen über sechs Expressions. Die beiden Figuren sind im Soul Hub einzeln verfügbar.

Auch die vorhandenen Roadmap-Figuren Yor Forger, Megumin, Kaguya Shinomiya sowie die jeweils vier Figuren der Pakete Dungeon Meshi, Steins;Gate, Lycoris Recoil und Sword Art Online sind nun im Charakter-Hub registriert. Die Kampagnenfiguren verwenden ihre bestehenden Hauptporträts; die sechs Expressions je Figur werden einzeln ergänzt. Der genaue Fortschritt steht in der Roadmap.

Der aktuelle Arbeitsstand steht in [`ROADMAP.md`](ROADMAP.md); `roadmap_optional_content.md` enthält denselben Stand.

## Kampagnen-Expressions prüfen

Jede fertiggestellte Kampagnenfigur erhält sechs WebP-Bilder (640×800) unter `presets/<paket>/expressions/<figur>/` und die zugehörigen Bildprompts in `prompts.json`. Die Preset-Karte referenziert Paketdateien, die Hub-Karte öffentliche Repository-URLs. Beide PNG-Karten enthalten die aktualisierte V2-Definition.

`python3 tools/package_campaign_expressions.py <paket> <figur>` prüft ein fertiges Paket auf sechs unterschiedliche Bilder, korrekte Größen und identische PNG/JSON-Metadaten. Benötigt Python 3 und Pillow. Bildgenerierung erfolgt mit dem eingebauten `image_gen`-Werkzeug anhand des vorhandenen Avatars; die Texte und ihre Übersetzungen bleiben erhalten.
