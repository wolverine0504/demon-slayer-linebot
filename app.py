#import tensorflow.keras
#import time
#import numpy as np
#from PIL import Image, ImageOps

from flask import Flask, request, abort
from random import randint, random, choice
# from flask_ngrok import run_with_ngrok

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
#import requests
import os
app = Flask(__name__)
# run_with_ngrok(app)
# Channel Access Token 填上你的 channel access token
line_bot_api = LineBotApi(
    'URtK3q5o/BTNQJGAeLTA1jrs7Y2aUKxboGpzpe72LFHUPfUq/KhxjsBD6uBLEEpjHLscnXkj4CugsKFKPB+vITKDRnfCnUVNIO6Ki2yJdzANRWgo8dyPN+FJ+21GxPz2+cpXGkUr7AH1q1TOWW1wngdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('1f9c051bccbcaff271acf1633aaba6c4')

# 監聽所有來自 /callback 的 Post Request
# 連上我的heroku
# 1.line webhook URL 改成 https://demon-slayer.herokuapp.com/callback

# 本地端用ngrok測試
# 1.另開終端執行ngrok在有ngrok執行檔的地方 ./ngrok http 5000
# 2.line webhook URL 改成 https://ngrok的網址/callback
# 3.執行app.py python3 app.py


Mitsuri = {
    "type": "template",
    "alt_text": "this is a buttons template",
    "template": {
        "type": "buttons",
        "thumbnail_image_url": "https://cdn.hk01.com/di/media/images/cis/5e635bb1a5af56141f1d887a.jpg/PNRlRBm9RLRkqi4g7rwBlW0GH5DqZvpp0kmp1NJJqdQ?v=w1920",
        "image_aspect_ratio": "square",
        "image_background_color": "#EC6BC4",
        "title": "戀柱 甘露寺蜜璃",
        "text": "擁有一個鮮艷粉紅色長髮的甘露寺蜜璃，戀柱可以說是鬼殺隊中最少女、最性感並總是在害羞妄想的柱。",
        "actions": [
            {
                "type": "message",
                "label": "基本資料",
                "text": "年齡：19歲\n性別:女\n身高：167cm\n體重：56kg\n出生：東京府麻布區飯倉\n生日：6月1日\n星座：雙子座\n興趣：料理、尪仔標\n喜歡的食物：櫻餅\n鬼殺隊階級：柱\n使用呼吸法：戀之呼吸"
            },
            {
                "type": "uri",
                "label": "開箱全裸爆乳戀柱GK",
                "uri": "https://youtu.be/joVjfxQ9ZT8?t=123"
            },
            {
                "type": "message",
                "label": "今天好無聊怎麼辦",
                "text": "o(*////▽////*)q 跟男女朋友出去玩啊"
            },
            {
                "type": "postback",
                "label": "抽桌布",
                "text": "抽！！！",
                "data": "Wallpaper&Mitsuri"
            }
        ]
    }
}

Shinobu = {
    "type": "template",
    "alt_text": "this is a buttons template",
    "template": {
        "type": "buttons",
        "thumbnail_image_url": "https://cdn-origin.cool-style.com.tw/cool/2020/03/vU2X0BX-1024x879.jpg",
        "image_aspect_ratio": "square",
        "image_background_color": "#B129EE",
        "title": "蟲柱 蝴蝶忍",
        "text": "唯一不會斬斷鬼頭的柱，身高僅151公分的蝴蝶忍是擅長調製毒藥來殺鬼的劍士，給人第一印象是腹黑冷笑小姐姐。",
        "actions": [
            {
                "type": "message",
                "label": "基本資料",
                "text": "年齡：18歲\n性別：女\n身高：151cm\n體重：37kg\n出生：東京府北豐島郡瀧野川村\n生日：2月24日\n星座：雙魚座\n興趣：怪談\n喜歡的食物：生薑製作的鹹菜\n鬼殺隊階級：柱\n使用呼吸法：蟲之呼吸"
            },
            {
                "type": "uri",
                "label": "蝴蝶忍x炭治郎",
                "uri": "https://www.youtube.com/watch?v=EWu4Hh42NOM"
            },
            {
                "type": "message",
                "label": "好想交女朋友喔",
                "text": "你快死吧下三濫。 (•‿•)"
            },
            {
                "type": "postback",
                "label": "抽桌布",
                "text": "抽！！！",
                "data": "Wallpaper&Shinobu"
            }
        ]
    }
}

Giyu = {
    "type": "template",
    "alt_text": "this is a buttons template",
    "template": {
        "type": "buttons",
        "thumbnail_image_url": "https://truth.bahamut.com.tw/s01/201909/2cbb85de4cf4bebafcacc503966f78f9.JPG",
        "image_aspect_ratio": "square",
        "title": "水柱 富岡義勇",
        "text": "第一印象是給人冷漠木訥的印象，但事實上個性真的很少根筋，內心其實是個重情重義的人。",
        "actions": [
            {
                "type": "message",
                "label": "基本資料",
                "text": "年齡：19歲\n性別：男\n身高：176cm\n體重：69kg\n出生：東京府豐多摩郡野方町\n生日：2月8日\n星座：水瓶座\n興趣：研究將棋\n喜歡的食物：鮭魚蘿蔔\n鬼殺隊階級：柱\n使用呼吸法：水之呼吸"
            },
            {
                "type": "uri",
                "label": "水之呼吸 拾壹之型 凪",
                "uri": "https://www.youtube.com/watch?v=GaCyjgCo2nw"
            },
            {
                "type": "message",
                "label": "你為什麼被其他柱討厭",
                "text": "我才沒有被討厭"
            },
            {
                "type": "postback",
                "label": "抽桌布",
                "text": "抽！！！",
                "data": "Wallpaper&Giyu"
            }

        ]
    }
}

Kyoguro = {
    "type": "template",
    "alt_text": "this is a buttons template",
    "template": {
        "type": "buttons",
        "thumbnail_image_url": "https://i.pinimg.com/564x/00/b2/ee/00b2eeb8386e662dd7059481bd9c5bee.jpg",
        "image_aspect_ratio": "square",
        "title": "炎柱 煉獄杏壽郎",
        "text": "給人第一印象是有著紅黃相間長發的爽朗少年，事實上本人就是勇往直前、充滿正義感的大哥。剛生來便擁有超過於常人的大力量。",
        "actions": [
            {
                "type": "message",
                "label": "基本資料",
                "text": "年齡：20歲\n性別：男\n身高：177cm\n體重：72kg\n出生：東京府荏原郡駒澤\n生日：5月10日\n星座：金牛座\n興趣：能樂、歌舞伎、看相撲比賽\n喜歡的食物：地瓜味噌湯\n鬼殺隊階級：柱\n使用呼吸法：炎之呼吸"
            },
            {
                "type": "uri",
                "label": "大哥沒有輸！！！",
                "uri": "https://www.youtube.com/watch?v=IAwSLbStI1o"
            },
            {
                "type": "message",
                "label": "你怎麼打輸了",
                "text": "大哥沒有輸！！！"
            },
            {
                "type": "postback",
                "label": "抽桌布",
                "text": "抽！！！",
                "data": "Wallpaper&Kyoguro"
            }
        ]
    }
}

Nezuko = {
    "type": "template",
    "alt_text": "this is a buttons template",
    "template": {
        "type": "buttons",
        "thumbnail_image_url": "https://i.pinimg.com/564x/cb/93/95/cb9395babc67393eb790bab27db0eb3d.jpg",
        "image_aspect_ratio": "square",
        "title": "竈門禰豆子",
        "text": "竈門家長女，炭治郎的大妹，竈門家被屠殺後的唯一生還者，被鬼的始祖—鬼舞辻無慘攻擊時沾染到其血液而變成「鬼」",
        "actions": [
            {
                "type": "message",
                "label": "基本資料",
                "text": "年齡：12歲\n性別：女\n身高：153cm\n體重：45kg\n出生日期：12月28日\n興趣：縫紉\n喜歡的食物：金平糖\n能力：血鬼術「爆血」"
            },
            {
                "type": "message",
                "label": "禰豆子highlights",
                "text": "https://www.youtube.com/watch?v=C7-9Z_dk_Wc"
            },
            {
                "type": "message",
                "label": "……！",
                "text": "……？"
            },
            {
                "type": "postback",
                "label": "抽桌布",
                "text": "抽！！！",
                "data": "Wallpaper&Nezuko"
            }
        ]
    }
}

Tanjiro = {
    "type": "template",
    "alt_text": "this is a buttons template",
    "template": {
        "type": "buttons",
        "thumbnail_image_url": "https://i.pinimg.com/564x/5b/fe/53/5bfe53ed22a14b51d75e96b5c0463765.jpg",
        "image_aspect_ratio": "square",
        "title": "竈門炭治郎",
        "text": "竈門家長子，有敏銳的嗅覺，能在與鬼的戰鬥中聞出破綻的「氣味」為了將妹妹變回人類，並為死去的家人報仇，加入了鬼殺隊",
        "actions": [
            {
                "type": "message",
                "label": "基本資料",
                "text": "年齡：15歲\n性別：男\n身高：165cm\n體重：61kg\n出生日期：7月14日\n興趣：頭槌、掃除\n喜歡的食物：楤木的芽\n能力：水之呼吸、火之神神樂"
            },
            {
                "type": "uri",
                "label": "火之神神樂 vs 下弦之五",
                "uri": "https://www.youtube.com/watch?v=XxQOjb1GZjk"
            },
            {
                "type": "message",
                "label": "你怎麼可以把鬼帶在身上",
                "text": "她是我妹妹，他不會傷害人"
            },
            {
                "type": "postback",
                "label": "抽桌布",
                "text": "抽！！！",
                "data": "Wallpaper&Tanjiro"
            }
        ]
    }
}

Zen = {
    "type": "template",
    "alt_text": "this is a buttons template",
    "template": {
        "type": "buttons",
        "thumbnail_image_url": "https://i.pinimg.com/564x/8a/c3/5e/8ac35e26c1c1a862ea5620d8ba9869cb.jpg",
        "image_aspect_ratio": "square",
        "title": "我妻善逸",
        "text": "對自己極度沒有自信，常常說出自嘲的發言。擁有極佳聽覺，能分別出鬼和人類的聲音。極度恐懼時會陷入沉睡，並激發出強勁的實力。",
        "actions": [
            {
                "type": "message",
                "label": "基本資料",
                "text": "年齡：15歲\n性別：男\n身高：164.5cm\n體重：58kg\n出生日期：9月3日\n興趣：花札、雙六\n喜歡的食物：甜食、高級料理（例如鰻魚\n能力：雷之呼吸"
            },
            {
                "type": "uri",
                "label": "雷之呼吸 壹之型 霹靂一閃",
                "uri": "https://www.youtube.com/watch?v=iYyNgeccixE"
            },
            {
                "type": "message",
                "label": "我跟禰豆子誰比較可愛",
                "text": "禰豆子 (*´∀`)~♥"
            },
            {
                "type": "postback",
                "label": "抽桌布",
                "text": "抽！！！",
                "data": "Wallpaper&Zen"
            }
        ]
    }
}

Muichirou = {
    "type": "template",
    "alt_text": "this is a buttons template",
    "template": {
        "type": "buttons",
        "thumbnail_image_url": "https://i.pinimg.com/564x/76/c7/e9/76c7e97f701247a338adf523a1b1cd8e.jpg",
        "image_aspect_ratio": "square",
        "title": "霞柱 時透無一郎",
        "text": "無一郎是握刀僅2個月就當上柱的天才少年，給人的第一印象是什麼事都不關心的詭異14歲少年，年紀比男主角炭治郎還要小。",
        "actions": [
            {
                "type": "message",
                "label": "基本資料",
                "text": "年齡：14歲\n性別：男\n身高：160cm\n體重：56kg\n出生：東京府八王子市景信山\n生日：8月8日\n星座：獅子座\n興趣：剪紙、摺紙\n喜歡的食物：醬佃煮蘿蔔\n鬼殺隊階級：柱\n使用呼吸法：霞之呼吸"
            },
            {
                "type": "uri",
                "label": "霞柱悲慘人生（有劇透）",
                "uri": "https://www.youtube.com/watch?v=GSmtA6fxUbM"
            },
            {
                "type": "message",
                "label": "為什麼要一直發呆",
                "text": "我......也不知道"
            },
            {
                "type": "postback",
                "label": "抽桌布",
                "text": "抽...",
                "data": "Wallpaper&Muichirou"
            }
        ]
    }
}
Inosuke = {
    "type": "template",
    "alt_text": "this is a buttons template",
    "template": {
        "type": "buttons",
        "thumbnail_image_url": "https://i.pinimg.com/564x/14/3b/bb/143bbb5422d642b5d8b0c15b27afe85e.jpg",
        "image_aspect_ratio": "square",
        "title": "嘴平伊之助",
        "text": "文字經常戴著野豬頭套，性格極為好戰。因為在山林中成長而有著銳利的觸覺，能精確捕捉到尚未進入視野的對象之所在位置。",
        "actions": [
            {
                "type": "message",
                "label": "基本資料",
                "text": "年齡：15歲\n性別：男\n身高：164cm\n體重：63kg\n出生日期：4月22日\n興趣：老鷹捉小雞遊戲、羽子板\n喜歡的食物：天婦羅\n能力：我流 獸之呼吸"
            },
            {
                "type": "uri",
                "label": "那些伊之助的有趣時刻",
                "uri": "https://www.youtube.com/watch?v=KzGs9d_mSPI"
            },
            {
                "type": "message",
                "label": "炭治郎跟善逸誰比較厲害",
                "text": "本大爺最厲害"
            },
            {
                "type": "postback",
                "label": "抽桌布",
                "text": "給我抽！！！！",
                "data": "Wallpaper&Inosuke"
            }
        ]
    }
}

Kanao = {
    "type": "template",
    "alt_text": "this is a buttons template",
    "template": {
        "type": "buttons",
        "thumbnail_image_url": "https://i.pinimg.com/564x/9b/a2/d5/9ba2d5c0ed9f44e5adf6ee53322acbf7.jpg",
        "image_aspect_ratio": "square",
        "title": "栗花落香奈乎",
        "text": "總是笑臉迎人，但其實有溝通障礙，被香奈會教導以擲銅板做決定，後期因炭治郎而開始有自己的想法。",
        "actions": [
            {
                "type": "message",
                "label": "基本資料",
                "text": "性別:女\n年齡:16歲\n身高:156cm\n體重:46kg\n出生日期:1月7日\n出生地:東京府本所區\n興趣:吹泡泡"
            },
            {
                "type": "uri",
                "label": "超越柱最強繼子",
                "uri": "https://www.youtube.com/watch?v=h91WLCzu79g&feature=youtu.be"
            },
            {
                "type": "message",
                "label": "中午吃什麼好呢?",
                "text": "(擲硬幣)"
            },
            {
                "type": "postback",
                "label": "抽桌布",
                "text": "！！！",
                "data": "Wallpaper&Kanao"
            }
        ]
    }
}

Genya = {
    "type": "template",
    "alt_text": "this is a buttons template",
    "template": {
        "type": "buttons",
        "thumbnail_image_url": "https://i.pinimg.com/564x/a9/4b/2e/a94b2e6eeee5a1592bcd1ea9245e1d4b.jpg",
        "image_aspect_ratio": "square",
        "title": "不死川玄彌",
        "text": "風柱的親弟弟，和炭治郎為同梯的鬼殺隊員。故事前期個性粗暴，後期因長時間和竈門兄妹相處，有慢慢改善。",
        "actions": [
            {
                "type": "message",
                "label": "基本資料",
                "text": "物種:人類 (仿鬼) \n性別:男\n年齡:16歲\n身高:180cm\n體重:76kg\n出生日期:1月7日\n出生地:東京府京橋區\n興趣:盆栽"
            },
            {
                "type": "uri",
                "label": "風柱弟弟!! | 特異食鬼體質!!",
                "uri": "https://youtu.be/nvydXeRraKM"
            },
            {
                "type": "message",
                "label": "你臉上為什麼有疤痕?",
                "text": "乾你屁事？"
            },
            {
                "type": "postback",
                "label": "抽桌布",
                "text": "抽就抽閉嘴",
                "data": "Wallpaper&Genya"
            }
        ]
    }
}

Muzan = {
    "type": "template",
    "alt_text": "this is a buttons template",
    "template": {
        "type": "buttons",
        "thumbnail_image_url": "https://n.sinaimg.cn/sinacn10111/170/w600h370/20191008/08ab-ifrwayw6115535.jpg",
        "title": "鬼舞辻無慘",
        "text": "自私自利、膽小怕死、不懂感激、殘忍無情。",
        "actions": [
            {
                "type": "message",
                "label": "背景故事",
                "text": "未變成鬼前，無慘自小就體弱多病，在未20歲時便罹患了絕症，一位善良的醫生為了幫他延續壽命而研製了一種藥，無慘卻誤會藥的作用讓他的病症加劇而把醫生給殺了。在之後他才發現他恢復健康並獲得了不老不死之軀，並開始以人的血肉為食，然而他卻無法曝曬在陽光下。為了找到青色彼岸花來克服這個弱點，他用他的血製造了大量的鬼。在與緣壹大戰，被緣壹使用的日之呼吸所傷，之後便建立了十二鬼月來保護他自己。在珠世的藥效發作時，即將被鬼殺隊殲滅生命的最後一刻，他吞噬了炭治郎，封住炭治郎的意識並將意識灌輸進炭治郎體內，要他「成為最強大的鬼王」，但在眾人的呼喊炭治郎的情況下，他最終沒有得逞。"
            },
            {
                "type": "uri",
                "label": "無慘全面分析！！",
                "uri": "https://youtu.be/-P37JfFFF9o"
            },
            {
                "type": "message",
                "label": "拜託不要殺我",
                "text": "去死吧"
            },
            {
                "type": "postback",
                "label": "抽桌布",
                "text": "我先抽死你",
                "data": "Wallpaper&Muzan"
            }
        ]
    }
}

Tengen = {
    "type": "template",
    "alt_text": "this is a buttons template",
    "template": {
        "type": "buttons",
        "thumbnail_image_url": "https://i.pinimg.com/564x/6f/c7/b5/6fc7b513621db8ec74c24b169debb3d1.jpg",
        "image_aspect_ratio": "rectangle",
        "title": "音柱 宇髄天元",
        "text": "給人的第一印象是個高傲的夯哥，實際上也真的很夯，有三個老婆。口頭禪是「華麗」。",
        "actions": [
            {
                "type": "message",
                "label": "基本資料",
                "text": "年齡：23歲\n性別：男\n身高：198cm\n體重：95kg\n出生：不明\n生日：10月31日\n星座：天蠍座\n興趣：和老婆們泡溫泉、尋找祕密溫泉\n喜歡的食物：河豚刺身\n鬼殺隊階級：柱\n使用呼吸法：音之呼吸"
            },
            {
                "type": "uri",
                "label": "鬼殺隊音柱 | 華麗之神!!",
                "uri": "https://www.youtube.com/watch?v=FLPthR5y0BE"
            },
            {
                "type": "message",
                "label": "三個老婆==，怎麼做到的?",
                "text": "因為我華麗又瀟灑啊！"
            },
            {
                "type": "postback",
                "label": "抽桌布",
                "text": "來個華麗的抽吧！！",
                "data": "Wallpaper&Tengen"
            }
        ]
    }
}

Sanemi = {
    "type": "template",
    "alt_text": "this is a buttons template",
    "template": {
        "type": "buttons",
        "thumbnail_image_url": "https://i.pinimg.com/564x/e2/ec/6e/e2ec6ef67b2cec259c6d2225660cf40d.jpg",
        "image_aspect_ratio": "square",
        "title": "風柱 不死川實彌",
        "text": "給人第一印象是十分殘暴的暴力狂。但實則不然，只是因為悲慘的童年際遇，比別人更痛恨鬼。",
        "actions": [
            {
                "type": "message",
                "label": "基本資料",
                "text": "年齡：21歲\n性別：男\n身高：179cm\n體重：75kg\n出生：東京府京橋區\n生日：11月29日\n星座：射手座\n興趣：養獨角仙\n喜歡的食物：萩餅\n鬼殺隊階級：柱\n使用呼吸法：風之呼吸"
            },
            {
                "type": "uri",
                "label": "弟控背後的溫柔？？？",
                "uri": "https://www.youtube.com/watch?v=bsngmi9fuLU"
            },
            {
                "type": "message",
                "label": "AAAA開墮！我跟鬼一樣",
                "text": "鬼?我要殺了你！"
            },
            {
                "type": "postback",
                "label": "抽桌布",
                "text": "我看你是欠抽吧？",
                "data": "Wallpaper&Sanemi"
            }
        ]
    }
}

Gyomei = {
    "type": "template",
    "alt_text": "this is a buttons template",
    "template": {
        "type": "buttons",
        "thumbnail_image_url": "https://i.pinimg.com/564x/20/59/e1/2059e1ac91b59c74ee2c3cce1838bc2f.jpg",
        "image_aspect_ratio": "square",
        "title": "岩柱 悲鳴嶼行冥",
        "text": "給人的第一印象是個溫和成穩的大哥。實力是鬼殺隊中最強的，僅僅是甩動手上的佛珠就能夠震撼周圍的人。",
        "actions": [
            {
                "type": "message",
                "label": "基本資料",
                "text": "年齡：27歲\n性別：男\n身高：220cm\n體重：130kg\n出生：東京府靑梅日之出山\n生日：8月23日\n星座：處女座\n興趣：吹奏尺八\n喜歡的食物：米飯\n鬼殺隊階級：柱\n使用呼吸法：岩之呼吸"
            },
            {
                "type": "uri",
                "label": "讓柱敬而遠之最強的男人",
                "uri": "https://www.youtube.com/watch?v=WyLuj-ppgVc"
            },
            {
                "type": "message",
                "label": "感恩師傅，讚嘆師傅！",
                "text": "阿彌陀佛"
            },
            {
                "type": "postback",
                "label": "抽桌布",
                "text": "阿彌陀佛",
                "data": "Wallpaper&Gyomei"
            }
        ]
    }
}

Obanai = {
    "type": "template",
    "alt_text": "this is a buttons template",
    "template": {
        "type": "buttons",
        "thumbnail_image_url": "https://i.pinimg.com/564x/4e/41/7a/4e417af7a436820bbaaf0b6562992b6a.jpg",
        "image_aspect_ratio": "square",
        "title": "蛇柱 伊黑小芭內",
        "text": "給人的第一印象是個十分毒舌的擊敗人。雖然說話時習慣對人冷嘲熱諷，但實際上很重視夥伴。",
        "actions": [
            {
                "type": "message",
                "label": "基本資料",
                "text": "年齡：21歲\n性別：男\n身高：162cm\n體重：53kg\n出生：東京府八丈島八丈富士\n生日：9月15日\n星座：處女座\n興趣：川柳、俳句、看他人捏糖人\n喜歡的食物：海帶絲\n鬼殺隊階級：柱\n使用呼吸法：蛇之呼吸"
            },
            {
                "type": "uri",
                "label": "毒舌背后的温柔",
                "uri": "https://www.youtube.com/watch?v=y7NToFAkWc0"
            },
            {
                "type": "message",
                "label": "期末O趴囉!",
                "text": "喔是喔，可以稱讚你一下"
            },
            {
                "type": "postback",
                "label": "抽桌布",
                "text": "還敢抽啊",
                "data": "Wallpaper&Obanai"
            }
        ]
    }
}

richMenuJson = {
    "size": {
        "width": 2500,
        "height": 1686
    },
    "selected": True,
    "name": "鬼滅之刃選單",
    "chat_bar_text": "查看更多功能",
    "areas": [
        {
            "bounds": {
                "x": 11,
                "y": 11,
                "width": 1243,
                "height": 830
            },
            "action": {
                "type": "message",
                "text": "抽角色"
            }
        },
        {
            "bounds": {
                "x": 1268,
                "y": 4,
                "width": 1228,
                "height": 829
            },
            "action": {
                "type": "message",
                "text": "抽桌布"
            }
        },
        {
            "bounds": {
                "x": 7,
                "y": 848,
                "width": 1236,
                "height": 826
            },
            "action": {
                "type": "uri",
                "uri": "https://www.netflix.com/title/81091393"
            }
        }
    ]
}

GeneralWallpapers = [
    "https://i.pinimg.com/564x/b9/24/81/b92481c36b5376c7bbbbf7c62c35b60b.jpg",
    "https://i.pinimg.com/564x/ee/27/00/ee2700db840920c38aa11f9356e27781.jpg",
    "https://i.pinimg.com/564x/0d/4d/dd/0d4ddde32eda3cce318e816eab1a8d2d.jpg",
    "https://i.pinimg.com/564x/1b/ea/62/1bea625583fa827d3c781802ae57a44a.jpg",
    "https://i.pinimg.com/564x/9f/53/f7/9f53f7fad7d10747c2ab0d3d8eb4f705.jpg",
    "https://i.pinimg.com/564x/72/e9/55/72e95564f34af97fca7c98d2a7b2596b.jpg",
    "https://i.pinimg.com/564x/56/12/1e/56121e24041e1f5c68082725802a4e70.jpg",
    "https://i.pinimg.com/564x/f9/d4/fc/f9d4fce7a1a361dadef67fbcb60c165d.jpg",
    "https://i.pinimg.com/564x/7f/f6/5c/7ff65c84a1b2c729b2d97d468d65847f.jpg",
    "https://i.pinimg.com/564x/4f/08/d2/4f08d25b985ad5a782296defaec0e3de.jpg",
    "https://pbs.twimg.com/media/EfcsVgdVAAAmAZr?format=jpg&name=4096x4096",
    "https://i.pinimg.com/564x/de/c9/93/dec993ebd3e730f8a41e374e51592936.jpg",
    "https://pbs.twimg.com/media/EkXfTKjU8AE52K7?format=jpg&name=4096x4096",
    "https://i.pinimg.com/564x/97/6d/c9/976dc94104d7f4fff96e4a9a73f7d8ef.jpg",
    "https://i.pinimg.com/564x/5e/d5/e8/5ed5e8bae6b7bf7cf8b803812ada255a.jpg",
    "https://i.pinimg.com/564x/1f/71/e5/1f71e53f76ace0d57cf4c897ec8a4c23.jpg",
    "https://i.pinimg.com/564x/66/c6/26/66c6268be5fa5ec225a6bb12a6072a4c.jpg",
    "https://pbs.twimg.com/media/EbgcxPRVcAAAyNU?format=jpg&name=4096x4096",
    "https://pbs.twimg.com/media/EZQj4ZCU0AES1lT?format=jpg&name=4096x4096",
    "https://pbs.twimg.com/media/EWhb6dVUEAAWEel?format=jpg&name=4096x4096",
    "https://pbs.twimg.com/media/EQLnX_8UEAA1yp8?format=jpg&name=4096x4096",
]

TanjiroWallpapers = [
    "https://i.pinimg.com/564x/30/22/33/3022338c22e85f3b3f6fd233c4c14a20.jpg",
    "https://i.pinimg.com/564x/d1/ec/94/d1ec9427188a1314b1d970b962f093cf.jpg",
    "https://www.pinterest.com/pin/602919468854571330/",
    "https://scontent.frmq3-2.fna.fbcdn.net/v/t1.0-9/91407178_201299831316240_3775186028806012928_n.jpg?_nc_cat=102&ccb=2&_nc_sid=8bfeb9&_nc_ohc=9xIbxrb0zF8AX-LCCuZ&_nc_ht=scontent.frmq3-2.fna&oh=53cbb25c1fa0dcb89563a083daaed5cd&oe=6016DF4A",
    "https://scontent.frmq3-2.fna.fbcdn.net/v/t1.0-9/91843346_201300074649549_6458810985531572224_n.jpg?_nc_cat=111&ccb=2&_nc_sid=8bfeb9&_nc_ohc=nf2JebaZtm4AX_VH3U5&_nc_ht=scontent.frmq3-2.fna&oh=b35e45c87ceaed50dbd846d393efbf97&oe=6016CA9D",
    "https://i.pinimg.com/564x/05/bd/b4/05bdb470222457b1d0ed81e665b1a5ce.jpg",
    "https://i.pinimg.com/564x/67/b9/de/67b9de8a3bbfa0288a43a750ef3e6490.jpg",


]

NezukoWallpapers = [
    "https://i.pinimg.com/564x/42/5e/b1/425eb13519263dc72874c2d4b9a5590c.jpg",
    "https://i.pinimg.com/564x/d3/8c/56/d38c56404d1b4b99d1beb322af739a51.jpg",
    "https://i.pinimg.com/564x/f8/67/45/f867455f4b8abe120ed99d74e2db39ff.jpg",
    "https://www.pinterest.com/pin/14988611247648613/",
    "https://scontent.frmq3-1.fna.fbcdn.net/v/t1.0-9/92052378_201299861316237_2001900341318123520_n.jpg?_nc_cat=104&ccb=2&_nc_sid=8bfeb9&_nc_ohc=4jIoyllmXaMAX-Y3Nnp&_nc_ht=scontent.frmq3-1.fna&oh=fca95f4dd655330da4dadda585218b3d&oe=60167EAF",
    "https://scontent.frmq3-1.fna.fbcdn.net/v/t1.0-9/91610479_201300097982880_6920213828877680640_n.jpg?_nc_cat=110&ccb=2&_nc_sid=8bfeb9&_nc_ohc=VUeySM2NyGsAX-ETZwW&_nc_ht=scontent.frmq3-1.fna&oh=a4e6c1c5d6507df4e822c4643aac2f7b&oe=60181A3E",
    "https://i.pinimg.com/564x/91/25/d2/9125d2683cc4b3802e172b6da984e1b9.jpg",
]

GiyuWallPapers = [
    "https://img.qhmanhua.com/uploadImages/wzImages/20200408/1586337344959068132.jpg",
    "https://truth.bahamut.com.tw/s01/201909/2cbb85de4cf4bebafcacc503966f78f9.JPG",
    "https://i.pinimg.com/564x/77/10/70/7710701d73aeacc519c5345836396a32.jpg",
    "https://i.pinimg.com/564x/01/a0/64/01a064866c62da820a8dd591c21b5c7c.jpg",
    "https://i.pinimg.com/564x/d4/36/bd/d436bdcf38cfd8d36cbb1aaaf037ceb2.jpg",
    "https://i.pinimg.com/564x/42/5e/b1/425eb13519263dc72874c2d4b9a5590c.jpg",
    "https://i.pinimg.com/564x/fc/fc/ae/fcfcae45fd7fa4b85ca4da452d3831a3.jpg",
    "https://i.pinimg.com/564x/28/60/eb/2860eb552f30b473fa5cc66ef872cb9c.jpg",
]

ShinobuWallpapers = [
    "https://cdn-origin.cool-style.com.tw/cool/2020/03/vU2X0BX-1024x879.jpg",
    "https://i.pinimg.com/564x/69/36/74/69367412a7dc5cff9ece72f81df1c711.jpg",
    "https://truth.bahamut.com.tw/s01/201908/da430686469fb836b0933a75874928fa.JPG",
    "https://i.pinimg.com/564x/b1/df/6e/b1df6ec5398f136c0160533287dcff06.jpg",
    "https://i.pinimg.com/564x/d4/eb/68/d4eb68d1c6cf2a4290ce2ac5ddf1f497.jpg",
]

MitsuriWallpapers = [
    "https://truth.bahamut.com.tw/s01/201907/9e7380dcd5acd250a96b1eddad228c05.JPG",
    "https://i.pinimg.com/564x/35/4c/76/354c7673d8d2fbac6232c8ad7eae081c.jpg",
    "https://steamuserimages-a.akamaihd.net/ugc/776231853774778261/C5140CE68746C389B618327438B0BA2E678395DA/?imw=450&impolicy=Letterbox",
    "https://i.pinimg.com/564x/ab/d1/dd/abd1dde54d98b5d0f9bd39f30a5e773b.jpg",
    "https://pbs.twimg.com/media/EZWq3MsUYAAXhw0?format=jpg&name=4096x4096",
]

KyoguroWallpapers = [
    "https://twgreatdaily.com/images/elastic/xdH/xdHiPXABgx9BqZZIfPPS.jpg",
    "https://i0.hdslb.com/bfs/archive/6a25cda76c1ae36e05e873fd32ab0076a0934916.jpg",
    "https://i.pinimg.com/564x/f6/00/0b/f6000b23a78e6f017d3e476ce052e1b5.jpg",
    "https://i.pinimg.com/564x/41/da/fd/41dafd8216dcdcdbc5d8e48a6e3e7225.jpg",
    "https://i.pinimg.com/564x/f9/1a/90/f91a90599bb7c19e08d13aeab2ecbafd.jpg",
    "https://i.pinimg.com/564x/66/c6/26/66c6268be5fa5ec225a6bb12a6072a4c.jpg",
]

ZenWallpapers = [
    "https://i.pinimg.com/564x/81/cc/97/81cc9735f792979189c00422382b9435.jpg",
    "https://scontent.frmq3-1.fna.fbcdn.net/v/t1.0-9/92105059_201299891316234_3794291220159660032_n.jpg?_nc_cat=105&ccb=2&_nc_sid=8bfeb9&_nc_ohc=QkCKjmggw1YAX9Fpixq&_nc_ht=scontent.frmq3-1.fna&oh=a9d2943be8195967f39365cd791e7cc4&oe=6015E294",
    "https://scontent.frmq3-2.fna.fbcdn.net/v/t1.0-9/91686244_201300154649541_1659952512842596352_n.jpg?_nc_cat=111&ccb=2&_nc_sid=8bfeb9&_nc_ohc=zHMUbpr5L1UAX-ZKtWZ&_nc_ht=scontent.frmq3-2.fna&oh=6c11630b3f2d186f6642260d4c026d87&oe=6015296E",
    "https://i.pinimg.com/564x/3e/07/d5/3e07d52eee314fa3995a1f2b06309bf5.jpg",
    "https://i.pinimg.com/564x/6a/0e/c0/6a0ec07c38d33f18da53ca4304400474.jpg",
]

InosukeWallpapers = [
    "https://scontent.frmq3-2.fna.fbcdn.net/v/t1.0-9/91812864_201299927982897_2508228533990457344_n.jpg?_nc_cat=101&ccb=2&_nc_sid=8bfeb9&_nc_ohc=aQErXu7_GIcAX96Tt4P&_nc_ht=scontent.frmq3-2.fna&oh=a34650c101bb34b8565d8fbaf03c1b18&oe=6015C242",
    "https://i.pinimg.com/564x/8a/df/a3/8adfa35c2315de9f2270740f2807d217.jpg",
    "https://www.pinterest.com/pin/770748923714899259/",
    "https://i.pinimg.com/564x/c9/05/df/c905df7bdfc175fa2f2a967068350c88.jpg",
]

MuichirouWallpapers = [
    "https://pbs.twimg.com/media/D_vtCETUEAE8b1r.jpg",
    "https://i.pinimg.com/564x/f8/b2/d1/f8b2d13a30213b79e5990def5ae9a1b6.jpg",
    "https://i.pinimg.com/564x/a9/ab/7f/a9ab7fec3b03e5c1e08a7c3d262a22e8.jpg",
    "https://i.pinimg.com/564x/f0/ee/c6/f0eec6fff131977c57caf31951490e8a.jpg",
]
KanaoWallpapers = [
    "https://i.pinimg.com/564x/34/66/8d/34668d3ffd53204920e66697c355f63d.jpg",
    "https://i.pinimg.com/564x/c4/90/03/c49003012a3a78c0a176456997e6dade.jpg",
    "https://i.pinimg.com/564x/92/6c/d7/926cd7cdb699f7f6e04894d919d81936.jpg",
    "https://i.pinimg.com/564x/3e/6f/c0/3e6fc0d94272339abc0931ed40a30dd1.jpg",
    "https://i.pinimg.com/564x/20/c5/6b/20c56bcffddf87de1ff3ba9f8488e760.jpg",
]

GenyaWallpapers = [
    "https://i.pinimg.com/564x/55/74/30/5574305f349b20fc09e00e3184d543ba.jpg",
    "https://i.pinimg.com/564x/76/1e/34/761e34b5b88ab7b0f3aa7382cc0ad21e.jpg",
    "https://i.pinimg.com/564x/38/6c/c8/386cc87f8fa6cac0160fa08fd830a37c.jpg",
    "https://64.media.tumblr.com/edfe297204648944dce43e3cf2ea70cd/tumblr_pxmgr5uaNU1usr2uyo1_r4_500.png",
]

MuzanWallpapers = [
    "https://i.pinimg.com/564x/ed/5e/bf/ed5ebfede0a4226e00ad4d72759c03eb.jpg",
    "https://i.pinimg.com/564x/f3/85/a2/f385a2d510fd9e9ea9e695d2ef437bad.jpg",
    "https://i.pinimg.com/564x/df/31/bd/df31bd0730462e895a64bb9514d9a065.jpg",
    "https://i.pinimg.com/564x/df/ad/b6/dfadb6d3704e19754de03c80e6e7a0c2.jpg",
    "https://i.pinimg.com/564x/ea/ed/59/eaed59a89ee00877054f3c3efe054813.jpg",
]
ObanaiWallpapers = [
    "https://i.pinimg.com/originals/a7/bb/39/a7bb395babf4c74793eb362549aebf38.png",
    "https://i.imgur.com/8J6PevM.jpg",
    "https://i.pinimg.com/564x/d1/26/5e/d1265ef456078641457b2613e132029c.jpg",
    "https://i.pinimg.com/564x/4b/a6/4c/4ba64c5fc7597cf82e4850c3605e51da.jpg",
    "https://i.pinimg.com/564x/66/1c/19/661c19af15e1f3120145f2aaf0795989.jpg",
]
SanemiWallpapers = [
    "https://i.pinimg.com/564x/d6/b6/72/d6b672e9919f5d304c565ac23c2b80a2.jpg",
    "https://i.pinimg.com/originals/32/23/f2/3223f278c924cf583e84ed5c56d6ff0c.jpg",
    "https://i.pinimg.com/564x/4f/fc/fa/4ffcfa5dd183773afa924935c0f87c88.jpg",
]

TengenWallpapers = [
    "https://i.pinimg.com/564x/d7/f5/93/d7f593052ec74eefc7367cd1aaf43797.jpg",
    "https://i.pinimg.com/564x/32/79/f8/3279f870fd5b828e395748bfbfb51851.jpg",
    "https://i.imgur.com/gI0LTbg.jpg",
    "https://cdn-ak.f.st-hatena.com/images/fotolife/t/toshinohaya/20191126/20191126220203.jpg",
    "https://i.pinimg.com/564x/ce/de/2b/cede2b103de032b870a6a7ec6a5e853e.jpg",

]

GyomeiWallpapers = [
    "https://i.pinimg.com/564x/0f/87/04/0f87044cb537696f9d9d203af4787b41.jpg",
    "https://cdn-ak.f.st-hatena.com/images/fotolife/t/toshinohaya/20191219/20191219225049.jpg",
    "https://i.pinimg.com/474x/39/14/1f/39141f4c3ee31a30c2d4b89bb69f0a92.jpg",
    "https://i.pinimg.com/564x/be/67/85/be678533c6f88f09e187609d1a682714.jpg",
]


WallpapersDict = {
    "Giyu": GiyuWallPapers,
    "Shinobu": ShinobuWallpapers,
    "Mitsuri": MitsuriWallpapers,
    "Zen": ZenWallpapers,
    "Tanjiro": TanjiroWallpapers,
    "Nezuko": NezukoWallpapers,
    "Kyoguro": KyoguroWallpapers,
    "Inosuke": InosukeWallpapers,
    "Kanao": KanaoWallpapers,
    "Muichirou": MuichirouWallpapers,
    "Muzan": MuzanWallpapers,
    "Genya": GenyaWallpapers,
    "Tengen": TengenWallpapers,
    "Gyomei": GyomeiWallpapers,
    "Sanemi": SanemiWallpapers,
    "Obanai": ObanaiWallpapers,
}


getCharDict = {
    "Giyu": Giyu,
    "Shinobu": Shinobu,
    "Mitsuri": Mitsuri,
    "Zen": Zen,
    "Tanjiro": Tanjiro,
    "Nezuko": Nezuko,
    "Kyoguro": Kyoguro,
    "Inosuke": Inosuke,
    "Kanao": Kanao,
    "Muichirou": Muichirou,
    "Muzan": Muzan,
    "Genya": Genya,
    "Tengen": Tengen,
    "Gyomei": Gyomei,
    "Sanemi": Sanemi,
    "Obanai": Obanai,
}

class_dict = {}
with open('converted_savedmodel/labels.txt') as f:
    for line in f:
        (key, val) = line.split()
        class_dict[int(key)] = val


CharMsgDict = {
    0: Nezuko,
    1: Tanjiro,
    2: Giyu,
    3: Shinobu,
    4: Kyoguro,
    5: Zen,
    6: Mitsuri,
    7: Obanai,
    8: Sanemi,
    9: Muzan,
    10: Kanao,
    11: Genya,
    12: Tengen,
    13: Inosuke,
    14: Gyomei,
    15: Muichirou,
}


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header values
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    rich_menu_to_create = RichMenu(**richMenuJson)
    rich_menu_id = line_bot_api.create_rich_menu(rich_menu=rich_menu_to_create)
    print(rich_menu_id)
    with open('demon_slayer.png', 'rb') as f:
        line_bot_api.set_rich_menu_image(rich_menu_id, "image/png", f)
    line_bot_api.set_default_rich_menu(rich_menu_id)

   # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msgtext = event.message.text
    if msgtext == "文字":
        print("要文字")
        message = TextSendMessage(text=event.message.text)
        line_bot_api.reply_message(event.reply_token, message)
    elif msgtext == "貼圖":
        print("要貼圖")
        message = StickerSendMessage(package_id=1, sticker_id=2)
        line_bot_api.reply_message(event.reply_token, message)
    elif event.message.text == "大哥沒有輸":
        print("大哥真的沒有輸")
        message = ImageSendMessage(original_content_url='https://i.pinimg.com/564x/8b/a1/9d/8ba19d2c866c852d73a3d7c28581de68.jpg',
                                   preview_image_url='https://i.pinimg.com/564x/8b/a1/9d/8ba19d2c866c852d73a3d7c28581de68.jpg')
        line_bot_api.reply_message(event.reply_token, message)
    elif event.message.text == "抽角色":
        print("抽角色")
        line_bot_api.reply_message(event.reply_token, TemplateSendMessage(
            **CharMsgDict.get(randint(0, 15))))
    elif event.message.text == "抽桌布":
        print("抽桌布")
        paperurl = choice(GeneralWallpapers)
        sendWallpaper = ImageSendMessage(original_content_url=paperurl,
                                         preview_image_url=paperurl)
        line_bot_api.reply_message(event.reply_token, sendWallpaper)
    else:
        result = event.message.text.split('&')
        action = result[0]
        if action == "get":
            print(result[1])
            line_bot_api.reply_message(event.reply_token, TemplateSendMessage(
                **getCharDict.get(result[1])))


# # Disable scientific notation for clarity
# np.set_printoptions(suppress=True)

# # Load the model
# model = tensorflow.keras.models.load_model(
#     'converted_savedmodel/model.savedmodel')


@handler.add(MessageEvent, message=ImageMessage)
def handle_message(event):

    # # print(time.asctime(time.localtime(time.time())))

    # message_content = line_bot_api.get_message_content(event.message.id)
    # file_name = event.message.id+'.jpg'
    # with open(file_name, 'wb') as fd:
    #     for chunk in message_content.iter_content():
    #         fd.write(chunk)

    # # print(time.asctime(time.localtime(time.time())))

    # data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # # Replace this with the path to your image
    # image = Image.open(file_name)

    # # resize the image to a 224x224 with the same strategy as in TM2:
    # # resizing the image to be at least 224x224 and then cropping from the center
    # size = (224, 224)
    # # image = ImageOps.fit(image, size, Image.ANTIALIAS)

    # # print(time.asctime(time.localtime(time.time())))

    # # turn the image into a numpy array
    # image_array = np.asarray(image)

    # # display the resized image
    # # image.show()

    # # Normalize the image
    # normalized_image_array = (image_array.astype(np.float32) / 127.0 - 1)

    # # Load the image into the array
    # data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # data[0] = normalized_image_array[0:224, 0:224, 0:3]

    # # run the inference
    # prediction = model.predict(data)

    # # print(time.asctime(time.localtime(time.time())))

    # max_probability_item_index = np.argmax(prediction[0])

    # result_text_message = TextSendMessage("最像你的鬼滅角色是%s!!!" % (
    #     class_dict.get(max_probability_item_index)))
    # print(result_text_message)

    # 改掉抓model 直接用隨機
    result_temp_message = CharMsgDict.get(randint(0, 15))
    print(result_temp_message)
    line_bot_api.reply_message(
        event.reply_token, TemplateSendMessage(**result_temp_message))

    # 老師的code
    # line_bot_api.reply_message(event.reply_token, result_image_message)
    # if prediction.max() > 0.6:
    #     line_bot_api.reply_message(
    #         event.reply_token,
    #         TextSendMessage(
    #             """這個物件極有可能是 %s ，其相似機率為 %s 。""" % (class_dict.get(
    #                 max_probability_item_index), prediction[0][max_probability_item_index])
    #         )
    #     )
    # else:
    #     line_bot_api.reply_message(
    #         event.reply_token,
    #         TextSendMessage(
    #             """再給我清楚一點的圖！！"""
    #         )
    #     )


@handler.add(PostbackEvent)
def handle_postback(event):
    print(event.postback.data)
    result = event.postback.data.split('&')
    action = result[0]
    if action == "Wallpaper":
        Wallpapers = WallpapersDict.get(result[1])
        WallpaperUrl = choice(Wallpapers)
        WallpaperSend = ImageSendMessage(original_content_url=WallpaperUrl,
                                         preview_image_url=WallpaperUrl)
        line_bot_api.reply_message(event.reply_token, WallpaperSend)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    # app.run()

# heroku爆掉
# 如何開啟對話接收特定訊息
# heroku logs --tail

# 文字換行
# 如何鎖定單一事件
# message json 轉 api
# 設計圖文選單 抽角色 或直接關鍵字搜尋 看動畫 抽桌布 提醒上傳圖片
# 蒐集圖片
# 找精華片段
# rich_menu 運作原理 每次重設一次？
# postback action??
