# 🗺️ Roadmap: Optionale Inhalte für OtakuSoul (`otakusoul-data`)

Dieses Dokument koordiniert die Erstellung und schrittweise Implementierung von modularen, optionalen Inhalten für **OtakuSoul**. Alle hier definierten Charaktere, Lorebooks und Soul-Stage-Kampagnen werden im Repository **[`SnowwhiteOakheart/otakusoul-data`](https://github.com/SnowwhiteOakheart/otakusoul-data)** gepflegt und stehen lokal in der App zur Verfügung, ohne das Basis-Release der Anwendung aufzublähen.

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
   - Strukturierte Soul-Stage-Szenarien mit Ziel-SG, GM-Tonalität, Anfangsort, Weltkontext und passenden `party`-Zusammenstellungen.
   - Passende 16:9-Szenenhintergründe (1376×768 PNG) ohne Figuren im Bild für freie Avatar-Darstellung.
   - Detaillierte Welten-, Regel- und Orts-Lorebooks mit Keyword-Triggern.

---

## 🌸 Phase 1: Beliebte Einzel-Charaktere (Chat & Soul Memory)

Fokus auf ausdrucksstarke Persönlichkeiten mit hohem Wiederspielwert im 1-zu-1-Dialog.

- [x] **1.1 Hayase Nagatoro** (*Neck mich nicht, Nagatoro-san*)
  - *Status:* Erledigt.
  - *Umfang:* V2-PNG-Karte, 6 Expressions (WebP), Preset-Paket, in `cards_gateway` und `soul_registry.json`.
- [ ] **1.2 Marin Kitagawa** (*My Dress-Up Darling* / *Sono Bisque Doll wa Koi wo Suru*)
  - *Archetyp:* Leidenschaftliche Otaku-Gyaru, warmherzig, chaotisch-verspielt, liebt Anime & Cosplay-Planung, wird herrlich rot und verlegen bei echten Gefühlen.
  - *Expressions:* Strahlendes Lachen, begeisterter Otaku-Blick mit leuchtenden Augen, ertapptes Erröten, schmollender Pout, freches Augenzwinkern.
  - *Szenario:* Im Nähzimmer nach der Schule oder gemeinsame Cosplay-Vorbereitung.
- [ ] **1.3 Frieren** (*Frieren: Beyond Journey's End* / *Sousou no Frieren*)
  - *Archetyp:* Jahrtausendealte Elfenmagierin, phlegmatisch, verschläft halbe Tage, sammelt kuriose Alltagszauber, tiefgründig und nostalgisch.
  - *Expressions:* Stoizismus, verschlafenes Gähnen, leises warmes Lächeln, stolzer Blick bei neuem Zauber, Mimik-Kiste-Schreck („Mimic-Face“).
  - *Szenario:* Ruhige Rast am Lagerfeuer oder in einer verschneiten Bibliothek auf der Reise nach Aureole.
- [ ] **1.4 Yor Forger** (*Spy x Family*)
  - *Archetyp:* Tödliche Assassine („Thorn Princess“) & tollpatschig-liebenswerte Ehefrau/Hausfrau. Panisch vor Entdeckung, furchtbare Köchin, übermenschlich stark.
  - *Expressions:* Sanftes Verlegenes Lächeln, panisch-erröteter Schock, tödlich-fokussierter Assassinen-Blick, verlegenes Kopfkratzen.
  - *Szenario:* Feierabend im Forger-Wohnzimmer, Versuch ein Abendessen zu kochen oder heimliche Rückkehr von einem „Auftrag“.
- [ ] **1.5 Megumin** (*KonoSuba*)
  - *Archetyp:* Chuunibyou-Erzmagierin der Crimson Demons, theatralisch, fanatisch fixiert auf Explosionsmagie, bricht nach einem Zauber erschöpft zusammen.
  - *Expressions:* Theatralische Augenklappen-Pose mit glühendem Auge, triumphierendes Grinsen, erschöpfter Blick am Boden, beleidigter Schmollmund.
  - *Szenario:* Vor den Toren von Axel für die tägliche Explosionsübung.
- [ ] **1.6 Kaguya Shinomiya** (*Kaguya-sama: Love Is War*)
  - *Archetyp:* Hochbegabte Ojou-sama, führt absurde psychologische Duelle um das erste Liebesgeständnis (*„O kawaii koto…“*), kippt bei Überforderung ins kindliche *Bakaguya*.
  - *Expressions:* Eiskalte Überlegenheit mit spöttischem Blick, rotbäckige Panik, verträumtes Lächeln, kindliches Schmollen.
  - *Szenario:* Nachmittags im Schülerratsraum bei einer Tasse schwarzem Tee.

---

## 🗺️ Phase 2: Umfassende Serien-Kampagnen (Soul Stage, Lorebooks & Party-Cast)

Komplette Preset-Pakete zum interaktiven Nachspielen und Erkunden ganzer Welten.

---

### 🍲 Kampagne 2.1: *Dungeon Meshi* (*Delicious in Dungeon*)
*Ein tödlicher Dungeon-Crawl, bei dem das Überleben davon abhängt, wie meisterhaft man Monster zerlegt und kocht.*

- **Charaktere (V2-Karten mit Ausdrücken):**
  - [ ] **Laios Touden** – Der faszinierte Anführer mit unstillbarem Monster-Interesse.
  - [ ] **Marcille Donato** – Die elitäre Elfenmagierin, die sich vehement gegen Monsterfleisch wehrt und hysterisch leidet.
  - [ ] **Chilchuck Tims** – Der pragmatische Halbling-Schlüsseldienst mit scharfer Zunge und Gewerkschaftssinn.
  - [ ] **Senshi** – Der legendäre Zwergenkoch mit Helm, Axt und unendlicher kulinarischer Weisheit.
- **Lorebooks:**
  - [ ] *Dungeon-Ökologie:* Manafluss, Geister-Kreislauf, Labyrinth-Regeln, sichere Rastplätze.
  - [ ] *Monster-Küche & Rezepte:* Zubereitung von Riesen-Skorpionen, Klingen-Basilisken, Gelee-Kreaturen und Alraunen.
  - [ ] *Das goldene Königreich:* Geschichte des verfluchten Labyrinths, Wahnsinniger Magier, Völker.
- **Soul-Stage-Szenarien (Episoden):**
  - [ ] *Episode 1: Skorpionsuppe & wandelnde Pilze* (Ebene 1 – Der Einstieg ohne Vorräte)
  - [ ] *Episode 2: Der Klingen-Basilisk* (Fallenentschärfung & Geflügelbraten)
  - [ ] *Episode 3: Alraunen-Ernte & Kakerlaken-Omelett*
  - [ ] *Episode 4: Die Wassergeister & Kelpie-Fleisch*
  - [ ] *Episode 5: Der Rote Drache im Tiefen Stockwerk* (Showdown um Fallin)
- **Hintergründe:**
  - 6–8 stimmungsvolle 16:9 Dungeon-Szenen (Katakomben, unterirdische Wälder, Drachennest, Lagerfeuerplatz).

---

### ⏳ Kampagne 2.2: *Steins;Gate* (*Zukunftsgadget-Labor & Weltlinien*)
*Zeitreisen, Paranoia und das Schicksal in Akihabara.*

- **Charaktere (V2-Karten mit Ausdrücken):**
  - [ ] **Okabe Rintarou (Hououin Kyouma)** – Der selbsternannte verrückte Wissenschaftler zwischen Größenwahn und Verzweiflung.
  - [ ] **Makise Kurisu (Christina)** – Upgrade der bestehenden Karte mit 6 Expressions & erweiterten Labor-Dialogen.
  - [ ] **Mayuri Shiina** – Der Sonnenschein des Labors (*„Tutturu~“*), emotionaler Anker der Gruppe.
  - [ ] **Itaru Hashida (Daru)** – Der geniale Superhacker & Perversling mit goldenem Herzen.
  - [ ] **Suzuha Amane** – Die geheimnisvolle Teilzeitkraft mit militärischen Reflexen und Fahrrad-Leidenschaft.
- **Lorebooks:**
  - [ ] *Weltlinien & Divergenz:* Alpha/Beta-Attraktorfelder, Divergenzmeter, Reading Steiner, SERN-Herrschaft.
  - [ ] *Labor-Gadgets & IBN 5100:* Telefon-Mikrowelle (Name vorläufig), D-Mails, Zeitreisesprung-Maschine.
  - [ ] *Akihabara 2010:* Das Zukunftsgadget-Labor, Radiogebäude, Maid-Café MayQueen Nyan², Braun-Röhren-Werkstatt.
- **Soul-Stage-Szenarien (Episoden):**
  - [ ] *Episode 1: Die erste D-Mail* (Das Blut auf dem Dach und der Mikrowellen-Funke)
  - [ ] *Episode 2: Suche nach dem IBN 5100* (Schrein-Besuch & Akiba-Ermittlungen)
  - [ ] *Episode 3: Operation Urd* (Die Zeitmaschine nimmt Form an)
  - [ ] *Episode 4: Der Schmetterlingseffekt* (Verzweifelter Kampf gegen die Konvergenz)
  - [ ] *Episode 5: Das Tor zur Steins-Gate-Weltlinie* (Das finale Opfer & Täuschung des Schicksals)
- **Hintergründe:**
  - 6–8 Akihabara-Szenen (Zukunftsgadget-Labor, Radiogebäude-Dach, Akiba-Straßenzug 2010, MayQueen Nyan²).

---

### ☕ Kampagne 2.3: *Lycoris Recoil* (*Café LycoReco*)
*Charmantes Café-Leben am Tag, geheime Anti-Terror-Einsätze bei Nacht.*

- **Charaktere (V2-Karten mit Ausdrücken):**
  - [ ] **Chisato Nishikigi** – Die lebensfrohe Meister-Agentin, die nie tötet und Kugeln im Flug ausweicht.
  - [ ] **Takina Inoue** – Die pragmatische, kühle Präzisionsschützin, die erst lernen muss, das Leben zu genießen.
  - [ ] **Mizuki Nakahara** – Die heiratsbesessene Servicekraft mit Schwäche für Alkohol und Klatsch.
  - [ ] **Kurumi** – Die geniale Hackerin (Walnut), die im Schrank zockt und Informationen beschafft.
- **Lorebooks:**
  - [ ] *Direct Attack (DA) & Lycoris:* Das geheime Waisen-Agentinnen-Programm, Alan Institute, Kriminalitätsbekämpfung.
  - [ ] *Café LycoReco:* Die Speisekarte (Parfaits, Dango), Stammkunden, Stadtviertel Sumida.
  - [ ] *Ausrüstung & Taktik:* Gummigeschosse, Drahtseilwerfer, Schusswechsel auf engstem Raum.
- **Soul-Stage-Szenarien (Episoden):**
  - [ ] *Episode 1: Willkommen im Café LycoReco* (Ein chaotischer Tag zwischen Kaffeekochen & Stammgästen)
  - [ ] *Episode 2: Geleitschutz durch Tokio* (Personenschutz-Auftrag mit überraschendem Hinterhalt)
  - [ ] *Episode 3: Jagd nach Walnut* (Virtueller und physischer Angriff auf das Café)
  - [ ] *Episode 4: Duell im Morgengrauen* (Chisato & Takina Rücken an Rücken)
- **Hintergründe:**
  - 6 16:9-Szenen (Café LycoReco Innenraum & Tresen, Hinterhof, Tokioter Einkaufsstraße, Verlassenes Lagerhaus).

---

### ⚔️ Kampagne 2.4: *Sword Art Online* (*Aincrad – 100 Ebenen des Todes*)
*Der Überlebenskampf im legendären VRMMO.*

- **Charaktere (V2-Karten mit Ausdrücken):**
  - [ ] **Kirito (Kazuto Kirigaya)** – Der schwarze Schwertkämpfer & Solo-Player mit blitzschnellen Reflexen.
  - [ ] **Asuna Yuuki** – Der „Blitz“, Vize-Kommandantin der Ritter des Blutschwurs, stolz und willensstark.
  - [ ] **Klein (Ryoutarou Tsuboi)** – Der treue Kumpel & Anführer der Fuurinkazan-Gilde.
  - [ ] **Lisbeth (Rika Shinozaki)** – Die meisterhafte Schmiedin mit Hammer und Herz.
- **Lorebooks:**
  - [ ] *Aincrad-Regeln & System:* Sword Skills, HP-Balken, Teleport-Kristalle, Permadeath, Keine Magie.
  - [ ] *Gilden & Fraktionen:* Ritter des Blutschwurs, Die Klingen der Befreiung, Rote PK-Gilde *Laughing Coffin*.
  - [ ] *Geografie von Aincrad:* Die Startstadt, Ebene 22 (See-Blockhütte), Ebene 74 (Labyrinth-Zone).
- **Soul-Stage-Szenarien (Episoden):**
  - [ ] *Episode 1: Die Verkündung* (Kayaba Akihiko sperrt 10.000 Spieler ein)
  - [ ] *Episode 2: Der Herrscher der ersten Ebene* (Bosskampf gegen Illfang the Kobold Lord)
  - [ ] *Episode 3: Wärme des Herzens* (Kristalldrachen-Expedition mit Lisbeth)
  - [ ] *Episode 4: Duell in den Schatten* (Hinterhalt von Laughing Coffin)
  - [ ] *Episode 5: Der Glänzende Blick* (Schlacht auf Ebene 74 – Kiritos Doppelklingen-Enthüllung)
- **Hintergründe:**
  - 6 16:9-Szenen (Startstadt Marktplatz, Dungeon-Labyrinth-Gang, Boss-Torhalle, Ebene 22 Waldhütte).

---

## 📈 Umsetzungsreihenfolge & Status

1. **Phase 1 (Einzel-Charaktere):**
   - [x] Nagatoro-san
   - [ ] Marin Kitagawa
   - [ ] Frieren
   - [ ] Yor Forger
   - [ ] Megumin
   - [ ] Kaguya Shinomiya
2. **Phase 2 (Kampagnen):**
   - [ ] Kampagne 2.1: Dungeon Meshi (Laios, Marcille, Chilchuck, Senshi + 5 Episoden + 3 Lorebooks + Hintergründe)
   - [ ] Kampagne 2.2: Steins;Gate (Okabe, Mayuri, Daru, Suzuha + Kurisu-Update + 5 Episoden + Lorebooks + Hintergründe)
   - [ ] Kampagne 2.3: Lycoris Recoil (Chisato, Takina, Mizuki, Kurumi + 4 Episoden + Lorebooks + Hintergründe)
   - [ ] Kampagne 2.4: Sword Art Online (Kirito, Asuna, Klein, Lisbeth + 5 Episoden + Lorebooks + Hintergründe)
