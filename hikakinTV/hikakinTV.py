import sys
import random

birth = 1989
youtube = 2005
hikakin_start = 2006
hikakinTV_start = 2011
gozmez = 2057

def getArgv():
    argv = ''
    
    if len(sys.argv)<2:
        while argv == '':
            argv = input()
    else:
        #argv concatenate
        for i in range(len(sys.argv)-1):
            argv += str(sys.argv[i+1])

    return argv

def valcalc(val):
    try:
        val = eval(val)
    except (NameError, SyntaxError):
        pass
    return val

hikakinTV_unNum = ["戦時中","平安","時代劇","吃音症","精神的","次期首相","リベラル","ゴリラ","拉致","死んだ"]

hikakinTV = {
    "戦時中":"【戦時中のヒカキンによるHIKAKIN TV】\n\n♪ 光 報道〜 第二水曜日〜(無線傍受の危険のため月一の第二水曜日だけになった)\n\nぶんぶん(国旗を振る) こんにちは 牛頭馬頭(YouTubeは敵性語のため牛頭馬頭に改名しました)  どうも、開發光です(本名) 今日はもう寝ます(消灯)",
    "平安":"【平安時代のヒカキンによるHIKAKIN TV】\n\n♪ひかきむ 絵巻〜  第二水曜日〜(毎日絵巻を描くのは無理なので月一の第二水曜日だけになった)\n\nポンポン(小鼓)  へろうごずめず(平安時代のYouTubeの前身牛頭馬頭)  我は光源氏なり(大嘘) けふはもう寝む(19時)",
    "時代劇":"【時代劇のヒカキンによるHIKAKIN TV】\n\n♪開発奉行〜  水曜〜(裁きは毎週水曜にて行われる)\n\nブンブン！(悪党を斬るため刀を振りかざす) 余は比嘉金なり(元服で開発光から改名)今宵より貴様らを永久に寝かせてくれよう(成敗)\n\n※今日は19時からの放送です※",
    "吃音症":"【吃音症のヒカキンによるHIKAKIN TV】\n\n♪ Hik、k、ティッ Eぶっ、ｪ〜♪(リハビリのために毎日投稿を強要されている)\n\nぶっぶっ、はおっちゅ(うまく声が出ない)きょっ、しゃぶっれしっおまっす(今日も、喋る練習をしたいと思います)\n\nセックス(うまくいえた)",
    "精神的":"【精神的に追いやられたヒカキンによるHIKAKIN TV】\n\n♪HIKAKIN TV〜 The END〜(お別れの挨拶)\n\nうっうっ(涙を流している) へろう Youtube(YouTubeは2057年にGoz-Mezに改名するお知らせがあったが、まだ名前は変わっていない)  どうも、開發光です(遺書に名前を書く) 今日はもう寝ます(永眠)",
    "次期首相":"【次期首相を狙うヒカキンによるHIKAKIN TV】\n\n♪ HikakinTV Everyday〜♪(全国放送)\n\nｳﾞｩｩｩｩｩﾝ(音割れ)ﾊﾛｰﾏｲChildren(国民を従える)どうも、開發光です(本名) 今日は直ちに99999999999999999票私に投票しなさい(視聴者の脳内に直接コンタクトを取る)もう寝ます(勝利を確信)",
    "リベラル":"【リベラルのヒカキンによるHIKAKIN TV】\n\n♪HIKAKIN TV〜 BLM 〜(人権運動の動画を1日3本投稿している) \n\nぶっぶっ(トランプ政権にブーイング) Hello Seattle(英語がうまい) どうも、開發光です(本名) 今日はもう帰ります(暴徒に殴られて帰宅)",
    "ゴリラ":"【ゴリラのヒカキンによるHIKAKIN TV】\n\n♪HIKAKIN TV〜Daily animal channel ～(人権を無くしたため国外から追放された)\n\nｳｯﾎｰ!ﾎｯﾎｳﾎｳﾎｯﾎｳ!(人ではないため鳴き声しか喋れなくなった) ｳｯﾎﾎﾎｳﾎ!(鳴き声)ｳｯﾎﾎﾎｳﾎｳｯﾎｰ!(鳴き声)",
    "拉致":"【拉致されたヒカキンによるHIKAKIN TV】\n\n♪ HikakinTV Everyday〜♪(愉快犯による犯行)\n\nぶっぶっ(口枷をつけられ、声が出ない)\nぶっぶっぶっ　ぶーぶーぶー　ぶっぶっぶっ\nぶっぶっぶっ　ぶーぶーぶー　ぶっぶっぶっ\n(モールス信号)\n\n………(ピタリと体が動かなくなる)",
    "死んだ":"【死んだヒカキンによるHIKAKIN TV】\n\n♪……………  …………(死んだので更新されない)\n\n…………………(死んだので喋れない)…………………(YouTubeはHIKAKINの生前にGoz-Mezに改名した)…………………(戒名)…………(享年97)",
    -1:"【胎児のヒカキンによるHIKAKIN TV】\n\n♪HIKAKIN TV〜  I can't make video〜(そもそも生まれてないので動画を作れない)\n\nコポコポ(羊水の中なので喋れない) コポポ コポポ コポ(羊水の中なので喋れない) コポコポコポポポ(羊水の中なので喋れない) コポポポポ コポ コポポポ(羊水の中なので喋れない)",
    0:"【{0}歳のヒカキンによるHIKAKIN TV】\n\n♪HIKAKIN TV〜  2nd Wednesday〜(親の都合で毎日は無理なので月一の第二水曜日だけ)\n\nぶっぶっ(できない) ウウウ アアア〜？　ギャアアア\n母親「光寝るわよ〜」\nダアアアッ\n今日はもう寝かせます(19時)",
    1:"【{0}歳のヒカキンによるHIKAKIN TV】\n\n♪あうあうあ〜  あう〜 あうあうあ〜(赤ん坊なので喋ることが出来ない)\n\nうあう あうあう(YouTubeは2005年からなのでこの映像はホームビデオとして残されている)  ううあ、あいうあう(意味のある言葉を話すことは出来ない) あぅ…ZZZ(19時)",
    7:"【{0}歳のヒカキンによるHIKAKIN TV】 \n\n♪HIKAKIN TV〜 every 4 hour〜(体力が有り余っているので1日6動画投稿している) \n\nぶっぶっ(まだできない) へろう おもしろフラッシュ倉庫(YouTubeは2005年にできた) どうも、開發光です(本名) 今日はもう寝ます(18時)",
    12:"【{0}歳のヒカキンによるHIKAKIN TV】 \n\n♪HIKAKIN TV〜 every 8 hour〜(体力が有り余っているので1日3動画投稿している) \n\nぶっぶっ(まだできない) へろう おもしろフラッシュ倉庫(YouTubeは2005年にできた) どうも、開發光です(本名) 今日はもう寝ます(21時)",
    27:"【{0}歳のヒカキンによるHIKAKIN TV】\n\n♪HIKAKIN TV〜  Everyday〜({1}年当時は毎日投稿を続けていた)\n\nブンブン(特技であるヒューマンビートボックスを取り入れていた) ハローユーチューブ(Goz-Mezは当時YouTubeという名前だった)  どうも、HIKAKINです(本名) 今日はもう寝ます(19時)",
    31:"【{0}歳のヒカキンによるHIKAKIN TV】\n\n♪HIKAKIN TV〜  everyday (まだまだ現役なので毎日投稿をしている)\n\nV~NV~N(衰えのないボイパ) Hello You Tubeどうもヒカキンです(現役さながらのハキハキとした挨拶) 今日はまるおを可愛がろうと思います(ヒカキンはまるおという名前の猫を飼っている)",
    75:"【{0}歳のヒカキンによるHIKAKIN TV】  \n\n♪HIKAKIN TV〜almost everyday〜(定期検診があるため毎日は不可能になった)  \n\nぶんぶん(飽きて適当) ハロー Goz-Mez(YouTubeは2057年にGoz-Mezに改名しました)  どうも、ヒカキンおじさんです(お茶目) 今日はiPhone 29を風呂に落とします(予告)",
    80:"【{0}歳のヒカキンによるHIKAKIN TV】\n\n♪HIKAKIN TV〜  Where is here?〜(認知症になってしまったので今どこにいるかわからない)\n\nぶっぶっ(できなくなった) へろう ごずめず(YouTubeは2057年にGoz-Mezに改名しました) 私は誰ですか?(わからない) ここから出してください(自分の家がわからない)",
    93:"【{0}歳のヒカキンによるHIKAKIN TV】\n\n♪HIKAKIN TV〜 Every other day(毎日は無理なので一日おきになった)\n\nﾌﾞﾝﾌﾞ(惜しい)ハローヴィメオ(YouTubeからBANされたのでvimeoに投稿するようになった。)どうもHIKAKINです(今回は言えた)今日は…何だっけ(認知症)",
    100:"【{0}歳のヒカキンによるHIKAKIN TV】\n\n♪HIKAKIN TV〜  Every week〜(毎日は無理なので週一だけになった)\n\nブウンブウン(できなくなった) ハらう 赤動画(高齢者向けの動画サイト)  どうも、開發光です 今日は人生を振り返ろうと思う。\n\n(中略)\n\nはて...「ピーチ」とは何者だったのか？思い出せないぞ",
    120:"【{0}歳のヒカキンによるHIKAKIN TV】 \n\n♪HIKAKIN TV〜 2nd Wednesday〜(毎日は無理なので月一の第二水曜日だけになった) \n\nぶっぶっ(できなくなった) へろう ごずめず(YouTubeは2057年にGoz-Mezに改名しました) どうも、開發光です(本名) 今日はもう寝ます(19時)",
    153:"【{0}歳のヒカキンによるHIKAKIN TV】\n\n♪HIKAKIN TV〜 NewYear'sDay〜(毎日は無理なので大晦日だけになった)\n\nﾌﾞｬｯﾌﾞｧ(できなくなった)ﾋｬﾛｫ ﾕﾅｲﾋｪｯﾄﾞ ｽﾃｲﾁｭｰｳﾞｩ(YouTubeは2074年に国営になりUS TUBEに改名した) どうも開發光です 今日はチビキンの息子の血を輸血して若返",
    194:"【{0}歳のヒカキンによるHIKAKIN TV】\n\n♪HIKAKIN TV〜 Once every five years(毎日は無理なので5年に1度だけになった)\n\nﾌﾞｪブ(できなくなった)ハローDailymotion(YouTubeが無くなり違法サイトであるデイリーモーションに投稿するようになった。)どうも光です(開き直って本名)今日はもう4ぬ(絶命)",
    #200:"【{0}歳のヒカキンによるHIKAKIN TV】\n\n♪HIKAKIN AV〜 Every Friday(視聴回数が伸び悩んできたので毎週金曜にAVを投稿するようになった)\n\nﾌﾞﾝﾌﾞﾝ(巨根を振り回す)ハローエフシーツー(垢BANを喰らったのでFC2に投稿するようになった。)どうもONAKINです(98241日目)今日は、開發します(意味深)",
    240:"【{0}歳のヒカキンによるHIKAKIN TV】\n\n♪HIKAKIN TV〜  sometimes〜(毎日は無理なのでバイタルが安定している日だけになった)\n\nコヒュー(できなくなった) へろう ごずめず(YouTubeは2057年にGoz-Mezに改名しました)  どうも、F782165・標本個体です(識別コード) 今日はもう溶けます(培養液と同化)",
    12000:"【{0}歳のサイボーグヒカキンによるHIKAKIN TV】 \n\n♪HIKAKIN TV〜 every ？？？〜(人類が絶滅しているためグレゴリオ暦が用いられていない) \n\nVoo Voo(機械音) Hello 虚無(YouTubeは2095年に閉鎖した) どうも、KHH-421です(識別番号) 今日も寝ません(サイボーグなので睡眠不要)",
    "1200京":"【{0}歳のヒカキンによるHIKAKIN TV】 \n\n♪HIKAKIN TV〜 every human civilization〜(文明が繰り返し繁栄と終焉を迎えるので文明崩壊時に1回動画を投稿している) \n\nぶっぶっ(人口声帯の調子が悪い) へろう YouTube(YouTubeが存在する文明は{1}回目) どうも、開發光です(本名) 今日はもう寝ます(文明崩壊)"
}

def errorkinTV():
    print('【-35歳のヒカキンによるHIKAKIN TV】\n\nOut of range exception(1行目)', file=sys.stderr)
    sys.exit(1)

def hikakin_age(val):
    if type(val) == int or type(val) == float:
        age = int(val)
        if 794-birth < age and age <1192-birth:
            return hikakinTV["平安"]
        elif 1939-birth < age and age < 1945-birth:
            return hikakinTV["戦時中"]
        elif age < 0:
            return hikakinTV[-1]
        elif age < 1:
            return hikakinTV[0].format(age)
        elif age < 5:
            return hikakinTV[1].format(age)
        elif age < 10:
            return hikakinTV[7].format(age)
        elif age < 16:
            return hikakinTV[12].format(age)
        #17歳(2006年)youtubeが始まってからyoutubeが始まるまでのコピペは存在しない
        elif age < 29:
            return hikakinTV[27].format(age,age+birth)
        elif age < 68:
            return hikakinTV[31].format(age)
        elif age < 80:
            return hikakinTV[75].format(age)
        elif age < 90:
            return hikakinTV[80].format(age)
        elif age < 100:
            return hikakinTV[93].format(age)
        elif age < 120:
            return hikakinTV[100].format(age)
        elif age < 150:
            return hikakinTV[120].format(age)
        elif age < 180:
            return hikakinTV[153].format(age)
        elif age < 200:
            return hikakinTV[194].format(age)
        elif age < 1000:
            return hikakinTV[240].format(age)
        elif age < 100000000:
            return hikakinTV[12000].format(age)
        else:
            #さすがに死んでいる可能性がある
            if random.choice(["1200京","死んだ"]) == "死んだ":
                return hikakinTV["死んだ"]
            else:
                return hikakinTV["1200京"].format(age,random.randint(3,31))
    else:
        if val in hikakinTV :
            return hikakinTV[val]
        else:
            return random_all()


def hikakin_year(val):
    if type(val) == int or type(val) == float:
        return hikakin_age(val-birth)
    else:
        return hikakin_age(val)

def random_unNum():
    return hikakinTV[random.choice(hikakinTV_unNum)]

def random_all():
    randomHikakinTV = random.choice(list(hikakinTV.items()))[0]

    if randomHikakinTV == "1200京":
        return hikakinTV["1200京"].format(random.randint(100000000,120000000000000000),random.randint(3,31))
    elif type(randomHikakinTV) == int:
        return hikakin_age(randomHikakinTV)
    else :
        return hikakinTV[randomHikakinTV]

if __name__=='__main__':
    argv = getArgv()
    #print(argv)

    if argv == "-35":
        errorkinTV()
    
    argv = valcalc(argv)
    #print("{}:{}".format(type(argv),argv))
    print(hikakin_age(argv))

