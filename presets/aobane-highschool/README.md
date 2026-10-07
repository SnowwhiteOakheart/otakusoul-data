# Aobane Highschool – Klasse 2-B

Zwei originale Anime-Figuren für OtakuSoul, erstellt am 07.10.2026. Ren Takahashi (高橋 蓮) und Aoi Mizuno (水野 葵) sind 17-jährige Schüler derselben Klasse 2-B an der fiktiven Aobane-Oberschule in Yokohama, Japan.

Ren ist ein zurückhaltender Fotograf mit trockenem Humor, der eine Ausstellung für das Kulturfest plant. Aoi ist eine lebhafte Autorin im Literaturclub, die ein Lesecafé organisieren möchte. Seit dem ersten Schuljahr arbeiten sie an der Klassenzeitung zusammen. Sie sind Freunde; eine Liebesbeziehung ist nicht vorgegeben. Beide sind unabhängig voneinander spielbar, mit {{user}} als neuem Klassenmitglied.

## Enthalten

- `ren_takahashi.json` / `ren_takahashi.png`: vollständige V2-Definition und Porträt.
- `aoi_mizuno.json` / `aoi_mizuno.png`: vollständige V2-Definition und Porträt.
- `expressions/<figur>/`: je `neutral`, `happy`, `relaxed`, `surprised`, `angry`, `sad` als 640×800 WebP.
- Hauptporträts: 700×937 PNG mit eingebettetem `chara`-Payload.
- Deutsch als Basis; sämtliche Profiltexte, Persönlichkeit, Szenario, Begrüßungen, drei Dialogbeispiele, Anweisungen, Hinweise, Titel und Tags auch auf Englisch und Russisch über `extensions.otakusoul_i18n`.
- Je zwei alternative Begrüßungen zusätzlich zur ersten Nachricht.

## Repository und Hub

Die Preset-Karten verweisen relativ auf die Bilder innerhalb dieses Pakets. Die eigenständigen Karten in `cards_gateway/Ren_Takahashi.png` und `cards_gateway/Aoi_Mizuno.png` verwenden öffentliche Repository-URLs für die Expressions. Dadurch benötigen Hub-Karten kein lokal kopiertes Preset-Verzeichnis. Beide sind in `soul_registry.json` registriert.

Die Erstellung importiert nichts in eine lokale OtakuSoul-Installation. Das Paket enthält keine Szenen oder Stimmen; die Figuren sind als Charakterkarten angelegt.

## Bilder und Herkunft

Die Bilder wurden mit dem eingebauten `image_gen`-Werkzeug erzeugt. Beide Hauptporträts entstanden aus Text; jeder Gesichtsausdruck verwendet ausschließlich das zugehörige neue Porträt als Identitätsreferenz. Die vollständigen Prompts stehen in [`image_prompts.json`](image_prompts.json). Normalisierung auf die Repository-Bildgrößen erfolgte nach der Generierung; Metadaten wurden anschließend eingebettet. Angaben zur Herkunft stehen in diesem Paket; die Nutzungsbedingungen für eigene Beiträge und KI-Bilder sowie Hinweise zu fremden Rechten stehen in [LICENSE](../../LICENSE).

## Prüfung

`python3 tools/validate_aobane.py` prüft Sprachen und Pflichtfelder, Profilumfang, Gesprächseinstiege, Dialogbeispiele, sechs Bildzuordnungen pro Figur, Bildgrößen, die eingebetteten PNG-Definitionen und die Repository-Ziele der Hub-Karten. Benötigt Python 3 und Pillow. Es erfolgt kein App-Import und keine Netzwerkabfrage.
