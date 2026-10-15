# Sakura Succubus 3 - characters, scenes and lorebooks (German, English, Russian)

A ready-made set for the visual novel *Sakura Succubus 3*: seven character cards (six characters and
one user persona), six Soul Stage scenes and three lorebooks. The texts were written in **German**;
cards, scenes and lorebooks also come in English and Russian (see below).

| File | Who |
|---|---|
| `ayu_ikue.json` | Ayu - the tsundere pop idol |
| `marina_wakatsuki.json` | Marina - the corporate CEO |
| `cosmos.json` | Cosmos - the playful cat girl |
| `hazel_williams.json` | Hazel - the tomboy tennis pro |
| `hifumi_yamamoto.json` | Hifumi - the actress, a Yamato Nadeshiko |
| `yue.json` | Yue - the dethroned succubus queen |
| `persona_hiroki.json` | Hiroki as a **user persona** - who *you* are in the chat |

Each card carries description, personality, scenario, one greeting plus two alternate greetings
(the app offers them as variants of the first message) and three example dialogues. `{{user}}` and
`{{char}}` are filled in by the app, so the cards are not hard-wired to the name "Hiroki".

Names and occupations follow the game's own script (Ayu **Ikue**, Marina **Wakatsuki**, Hifumi
**Yamamoto**, an actress; Hiroki is a photographer at the tabloid *Sakura Daily*).

The files are plain **chara_card_v2** JSON and work in SillyTavern, Chub and anything else that
reads that format. Every card points at its `<name>.png` next to it through
`extensions.custom_avatar` (relative to the card), at its emotion pictures through `extensions.expressions`
and at its matching Live2D model through `extensions.custom_live2d`.

**Translations.** The character cards also carry English and Russian versions in
`extensions.otakusoul_i18n` (`{"source_language": "de", "translations": {"en": {...}, "ru": {...}}}`).
OtakuSoul shows a card in the interface language and uses the reply language for the prompt and the
greeting; missing fields fall back to the German base text. Other apps ignore the extension and see the
German card.

## Scenes and lorebooks

`scenes/` holds six **Soul Stage** scenes, `lorebooks/` three lorebooks for the same universe - German
with English and Russian translations, and written from the game's own story rather than from a summary of it.

| Scene | Tone | Party |
|---|---|---|
| Redaktionsschluss | Slice of Life | Cosmos, Ayu |
| Der Wohltätigkeitsball | Mystery & Noir | Marina, Ayu |
| Wohnungskrieg | Comedy | all six |
| Audienz im Thronsaal | Epic Fantasy | Yue, Marina, Hazel |
| Ein Tee zu zweit | Romance | Hifumi |
| Matchball | Slice of Life | Hazel, Cosmos |

Every scene brings its own world context, starting location, opening narration and narrator style, uses
Hiroki as the persona and pulls in all three lorebooks:

| Lorebook | Entries | Contents |
|---|---|---|
| Sakura Succubus 3 – Welt | 10 | succubi, the realm and the portal, Hiroki's scent, the shared flat, the newspaper, secrecy, the rules of the harem |
| Sakura Succubus 3 – Figuren | 10 | all six women, Hiroki, and the side characters around them |
| Sakura Succubus 3 – Orte | 9 | flat, newsroom, cosplay cafe, board floor, stage, tennis court, tea room, throne hall, receptions |

The world entry is `always_on`, everything else is triggered by keywords, so the lorebooks cost almost
nothing until they are needed.

## Importing

**In the Hub (easiest).** Open **Hub** in OtakuSoul: the characters, lorebooks and scenes of this pack are
listed there and are imported with one click each. Characters from the Hub load their emotion pictures from
this repository.

**By hand.** Download this folder and import in the app:

- character cards (`*.png` or `*.json`) in the character library via **Import**,
- the user persona: create it under **Personas** with name and description from `persona_hiroki.json`,
- the lorebooks from `lorebooks/` under **Lorebooks → Import**,
- the scenes from `scenes/` in the Stage lobby via **Import JSON**,
- the backgrounds from `backgrounds/` in the scene editor (start picture) or the chat style panel.

Import the characters before the scenes: a scene names its party by character name.

## Backgrounds

`backgrounds/` holds nine 16:9 widescreen anime visual novel background scenes (empty scenery without characters,
so Live2D models and dialogue boxes render unobstructed):

- **6 Story Backgrounds:**
  - `Horizontal Tokyo Living Room.png` (Scene: *Wohnungskrieg*)
  - `Horizontal Newsroom Office.png` (Scene: *Redaktionsschluss*)
  - `Horizontal Gala Ballroom.png` (Scene: *Der Wohltätigkeitsball*)
  - `Horizontal Succubus Throne Room.png` (Scene: *Audienz im Thronsaal*)
  - `Horizontal Japanese Tea Room.png` (Scene: *Ein Tee zu zweit*)
  - `Horizontal Tennis Court.png` (Scene: *Matchball*)
- **3 Character Lore Backgrounds:**
  - `Horizontal Idol Stage.png` (Ayu Ikue - Concert Idol Stage)
  - `Horizontal Corporate Office.png` (Marina Wakatsuki - Penthouse Executive Office)
  - `Horizontal Cosplay Cafe.png` (Cosmos - Cosplay Maid Cat Café)

## About the pictures

The avatars are **AI generated** from the prompts in [AVATAR-PROMPTS.md](AVATAR-PROMPTS.md). They
show original characters described by archetype - a blonde idol with twintails, a CEO in a suit, a
cat girl in a maid uniform and so on - and use no artwork, sprite or reference image from the game.
The game's own art stays where it is, inside its archives.

License of the cards and pictures: same as the rest of this repository (GPL-3.0). *Sakura Succubus*
is a trademark of its publisher; this is unofficial fan content and not affiliated with them.
