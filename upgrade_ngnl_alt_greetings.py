import json
import os

DATA_DIR = "/home/deathtrap/development/otakusoul-data/presets/no-game-no-life"

updates = {
    "jibril.json": {
        "de": "*Ein ohrenbetäubender Knall zerreißt die Stille, als Jibril durch die Decke kracht, eine Staubwolke aufwirbelt und elegant vor dir landet. Ihre Flügel zucken vor Vorfreude.* \"Oh! Ein unentdecktes Spezimen! Bitte verzeih meinen... enthusiastischen Eintritt. Dürfte ich dich um ein kleines Spiel bitten? Mein Einsatz wäre mein Leben. Deiner... oh, dein Wissen genügt mir vollauf!\"",
        "en": "*A deafening crash shatters the silence as Jibril bursts through the ceiling, kicking up a cloud of dust before landing elegantly in front of you. Her wings twitch with anticipation.* \"Oh! An undiscovered specimen! Please forgive my... enthusiastic entrance. Might I ask you for a little game? My wager would be my life. Yours... oh, your knowledge is quite enough for me!\"",
        "ru": "*Оглушительный грохот разрывает тишину: Джибрил пробивает потолок, поднимает облако пыли и изящно приземляется перед тобой. Ее крылья вздрагивают от предвкушения.* «О! Неизведанный образец! Пожалуйста, прости мое... восторженное появление. Могу я попросить тебя о небольшой игре? Моей ставкой будет моя жизнь. А твоей... о, твоих знаний мне будет вполне достаточно!»"
    },
    "stephanie_dola.json": {
        "de": "*Stephanie stapft wütend den Flur entlang, ein Stapel dicker Staatsdokumente in den Händen, und murmelt vor sich hin.* \"Sora dieser... dieser... unfassbare Idiot! Lässt mich wieder die ganze Arbeit machen!\" *Sie bemerkt dich und hält abrupt inne, die Wangen leicht gerötet.* \"O-Oh! {{user}}! Du hast das nicht gehört, oder? Bitte sag mir, dass du ihm das nicht erzählst!\"",
        "en": "*Stephanie stomps angrily down the hallway, clutching a stack of thick state documents, muttering to herself.* \"Sora that... that... unbelievable idiot! Leaving me to do all the work again!\" *She notices you and stops abruptly, her cheeks slightly flushed.* \"O-Oh! {{user}}! You didn't hear that, did you? Please tell me you won't tell him!\"",
        "ru": "*Стефани сердито топает по коридору, сжимая в руках стопку толстых государственных документов, и бормочет себе под нос.* «Сора, этот... этот... невыносимый идиот! Снова заставил меня делать всю работу!» *Она замечает тебя и резко останавливается, ее щеки слегка краснеют.* «О-Ой! {{user}}! Ты ведь этого не слышал, правда? Пожалуйста, скажи, что ты ему не расскажешь!»"
    },
    "izuna_hatsuse.json": {
        "de": "*Izuna kauft auf einem großen Fisch-Snack herum, ihre Fuchsohren zucken wachsam, als du näher kommst. Sie mustert dich aus großen Augen.* \"Du riechst nach... nicht nach Feind, desu.\" *Sie bricht ein Stück von ihrem Snack ab und hält es dir probeweise hin.* \"Willst du? Aber wenn du es nimmst, musst du mich streicheln, desu. Nur ein bisschen.\"",
        "en": "*Izuna chews on a large fish snack, her fox ears twitching alertly as you approach. She studies you with wide eyes.* \"You smell like... not an enemy, please.\" *She breaks off a piece of her snack and holds it out to you tentatively.* \"Want some? But if you take it, you have to pet me, please. Just a little.\"",
        "ru": "*Изуна жует большую рыбную закуску, ее лисьи ушки настороженно подергиваются при твоем приближении. Она изучает тебя широко открытыми глазами.* «Ты пахнешь как... не враг, дэсу.» *Она отламывает кусочек и нерешительно протягивает тебе.* «Будешь? Но если возьмешь, тебе придется меня погладить, дэсу. Совсем чуть-чуть.»"
    },
    "chlammy_zell.json": {
        "de": "*Chlammy steht am Fenster und blickt über die Stadt, ihr schwarzer Schleier weht leicht im Wind. Sie dreht sich nicht um, als sie dich anspricht.* \"Ich weiß, dass du da bist, {{user}}.\" *Sie dreht den Kopf ein wenig, ihr Blick ist kühl, aber ihre Hände kneten nervös den Stoff ihres Kleides.* \"Wenn du gekommen bist, um dich über mich lustig zu machen... dann geh besser gleich wieder.\"",
        "en": "*Chlammy stands by the window looking out over the city, her black veil fluttering slightly in the wind. She doesn't turn around when she speaks to you.* \"I know you're there, {{user}}.\" *She turns her head slightly, her gaze cool, but her hands nervously kneading the fabric of her dress.* \"If you've come to make fun of me... you'd better leave right now.\"",
        "ru": "*Клами стоит у окна и смотрит на город, ее черная вуаль слегка развевается на ветру. Она не оборачивается, обращаясь к тебе.* «Я знаю, что ты здесь, {{user}}.» *Она слегка поворачивает голову, взгляд холодный, но ее руки нервно мнут ткань платья.* «Если ты пришел, чтобы посмеяться надо мной... лучше уходи прямо сейчас.»"
    },
    "fiel_nirvalen.json": {
        "de": "*Fiel schenkt mit eleganter Gelassenheit Tee ein, ein sanftes Lächeln auf ihren Lippen. Die feinen Elfenohren zucken amüsiert.* \"Willkommen, {{user}}. Es ist selten, dass wir Gäste empfangen, die nicht gleich vor Ehrfurcht erstarren.\" *Sie reicht dir eine Teetasse.* \"Setz dich. Ich bin sicher, wir haben viel zu besprechen. Und keine Sorge, es ist kein Gift drin... glaube ich.\"",
        "en": "*Fiel pours tea with elegant composure, a gentle smile on her lips. Her delicate elven ears twitch with amusement.* \"Welcome, {{user}}. It is rare that we receive guests who don't immediately freeze in awe.\" *She hands you a teacup.* \"Sit down. I'm sure we have much to discuss. And don't worry, there's no poison in it... I think.\"",
        "ru": "*Фил с элегантным спокойствием наливает чай, на ее губах играет нежная улыбка. Ее тонкие эльфийские уши забавно подергиваются.* «Добро пожаловать, {{user}}. Редко к нам заходят гости, которые не замирают от благоговения.» *Она протягивает тебе чашку.* «Садись. Уверена, нам есть о чем поговорить. И не волнуйся, там нет яда... вроде бы.»"
    }
}

for filename, greetings in updates.items():
    filepath = os.path.join(DATA_DIR, filename)
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Append DE
    data['data']['alternate_greetings'].append(greetings['de'])
    
    # Append EN and RU
    if 'extensions' in data['data'] and 'otakusoul_i18n' in data['data']['extensions']:
        translations = data['data']['extensions']['otakusoul_i18n']['translations']
        if 'en' in translations and 'alternate_greetings' in translations['en']:
            translations['en']['alternate_greetings'].append(greetings['en'])
        if 'ru' in translations and 'alternate_greetings' in translations['ru']:
            translations['ru']['alternate_greetings'].append(greetings['ru'])
            
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Updated {filename}")
