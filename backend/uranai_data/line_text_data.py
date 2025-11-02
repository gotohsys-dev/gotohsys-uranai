# -*- coding: utf-8 -*-

LINE_TEXTS_DATA = [
    # 1. 乾為天 (けんいてん)
    { "hexagram_id": 1, "line_position": 1, "yao_ci_text": "初九、潜龍。勿用。", "yao_ci_meaning": "まだ潜んでいる龍。力を発揮する時ではない。軽率に行動せず、力を蓄えるべき。", "changing_line_special_meaning": "今は動くべき時ではありません。将来のために準備を整え、好機を待ちましょう。" },
    { "hexagram_id": 1, "line_position": 2, "yao_ci_text": "九二、見龍在田。利見大人。", "yao_ci_meaning": "龍が田に現れた。世に出て力を発揮する時。徳の高い指導者に会うと良い。", "changing_line_special_meaning": "才能が認められ始めます。信頼できる上司や先輩の助言を求めると、さらに道が開けるでしょう。" },
    { "hexagram_id": 1, "line_position": 3, "yao_ci_text": "九三、君子終日乾乾、夕惕若。厲无咎。", "yao_ci_meaning": "君子は一日中努力し、夜も慎重である。そうすれば危うい立場でも問題ない。", "changing_line_special_meaning": "油断大敵の時。気を引き締め、慎重に行動すれば、困難を乗り越えられます。" },
    { "hexagram_id": 1, "line_position": 4, "yao_ci_text": "九四、或躍在淵。无咎。", "yao_ci_meaning": "淵から飛び立とうか迷っている龍。進むか退くか、状況を慎重に見極めれば問題ない。", "changing_line_special_meaning": "決断の時が迫っています。状況をよく見て、進むべきか待つべきか判断してください。軽率な行動は禁物です。" },
    { "hexagram_id": 1, "line_position": 5, "yao_ci_text": "九五、飛龍在天。利見大人。", "yao_ci_meaning": "龍が天を飛ぶ。最も運気が盛んな時。徳の高い指導者の助けも得られる。", "changing_line_special_meaning": "絶好調の時です。積極的に行動し、大きな目標を達成するチャンスです。" },
    { "hexagram_id": 1, "line_position": 6, "yao_ci_text": "上九、亢龍有悔。", "yao_ci_meaning": "天の頂点まで昇りつめた龍。これ以上進むと後悔する。行き過ぎを慎むべき。", "changing_line_special_meaning": "運気の頂点を過ぎました。引き際が肝心です。やり過ぎると失敗を招きます。" },

    # 2. 坤為地 (こんいち)
    { "hexagram_id": 2, "line_position": 1, "yao_ci_text": "初六、履霜、堅冰至。", "yao_ci_meaning": "霜を踏むと、やがて固い氷の季節が来る。小さな兆候を見逃さず、将来に備えるべき。", "changing_line_special_meaning": "問題の兆候が見え隠れしています。今のうちに対処しておかないと、後で大事になります。" },
    { "hexagram_id": 2, "line_position": 2, "yao_ci_text": "六二、直方大。不習无不利。", "yao_ci_meaning": "真っ直ぐで、正しく、大きい。自然体でいれば、何事もうまくいく。", "changing_line_special_meaning": "あなたの誠実さや実直さが評価されます。小細工せず、ありのままでいるのが一番です。" },
    { "hexagram_id": 2, "line_position": 3, "yao_ci_text": "六三、含章可貞。或從王事、无成有終。", "yao_ci_meaning": "内に秘めた才能を発揮せず、上司に従うべき。自分の功績を誇らず、最後までやり遂げることが大切。", "changing_line_special_meaning": "今は自己主張を控え、サポート役に徹する時です。縁の下の力持ちとして行動すれば、最終的に評価されます。" },
    { "hexagram_id": 2, "line_position": 4, "yao_ci_text": "六四、括囊。无咎无譽。", "yao_ci_meaning": "袋の口を閉じるように、言動を慎むべき。そうすれば災いもないが、名誉もない。", "changing_line_special_meaning": "余計なことは言わず、静かにしているのが賢明です。目立たないように行動しましょう。" },
    { "hexagram_id": 2, "line_position": 5, "yao_ci_text": "六五、黄裳元吉。", "yao_ci_meaning": "黄色い裳（もすそ）は中庸の徳を示す。謙虚な姿勢でいれば、最高に良い結果となる。", "changing_line_special_meaning": "あなたの謙虚で誠実な人柄が、大きな幸運を引き寄せます。控えめな態度を貫いてください。" },
    { "hexagram_id": 2, "line_position": 6, "yao_ci_text": "上六、龍戰于野。其血玄黄。", "yao_ci_meaning": "龍が野で戦い、天地の血が流れる。陰が陽と争う時。両者ともに傷つく。", "changing_line_special_meaning": "争いごとは泥沼化し、誰も得をしません。意地を張らず、和解の道を探るべきです。" },

    # 3. 水雷屯 (すいらいちゅん)
    { "hexagram_id": 3, "line_position": 1, "yao_ci_text": "初九、磐桓。利居貞。利建侯。", "yao_ci_meaning": "大きな岩が塞がり進めない。留まって正道を守り、協力者を得て基盤を固めるべき。", "changing_line_special_meaning": "障害が多く、前に進めません。焦らず、まずは足元を固め、協力者を探すことに専念しましょう。" },
    { "hexagram_id": 3, "line_position": 2, "yao_ci_text": "六二、屯如邅如。乘馬班如。匪寇婚媾。", "yao_ci_meaning": "悩みためらって進めない。助けが来るが、それは敵ではなく、助け手である。", "changing_line_special_meaning": "困難な状況ですが、助けが現れます。最初は警戒するかもしれませんが、その助けを受け入れるべきです。" },
    { "hexagram_id": 3, "line_position": 3, "yao_ci_text": "六三、即鹿无虞。惟入于林中。君子幾不如舍。往吝。", "yao_ci_meaning": "案内人なしで鹿を追って森に入る。君子は見切りをつけて諦めるべき。深入りすると後悔する。", "changing_line_special_meaning": "見通しが甘いまま進むのは危険です。専門家の助けなしでは成功しません。一度立ち止まって計画を見直しましょう。" },
    { "hexagram_id": 3, "line_position": 4, "yao_ci_text": "六四、乘馬班如。求婚媾。往吉。无不利。", "yao_ci_meaning": "ためらっているが、助けを求めればうまくいく。積極的に協力者を求めれば吉。", "changing_line_special_meaning": "一人で悩んでいないで、積極的に助けを求めましょう。協力者を得ることで、道が開けます。" },
    { "hexagram_id": 3, "line_position": 5, "yao_ci_text": "九五、屯其膏。小貞吉。大貞凶。", "yao_ci_meaning": "恵みを与えようとしても、まだ受け入れられない。小さな事なら良いが、大きな事はまだ早い。", "changing_line_special_meaning": "あなたの善意が、すぐには相手に伝わらないかもしれません。今は小さな親切を積み重ねる時です。" },
    { "hexagram_id": 3, "line_position": 6, "yao_ci_text": "上六、乘馬班如。泣血漣如。", "yao_ci_meaning": "進退窮まり、どうしようもなく血の涙を流す。最悪の事態。", "changing_line_special_meaning": "八方塞がりで、非常に苦しい状況です。今は耐え忍ぶしかありません。いずれ状況は変わります。" },

    # 4. 山水蒙 (さんすいもう)
    { "hexagram_id": 4, "line_position": 1, "yao_ci_text": "初六、發蒙。利用刑人。用説桎梏。以往吝。", "yao_ci_meaning": "蒙昧を開くには、規律が重要。甘やかすのではなく、厳しさをもって教えるべき。", "changing_line_special_meaning": "最初のルール作りが肝心です。なあなあにせず、厳しくても規律を教えることが、長い目で見れば本人のためになります。" },
    { "hexagram_id": 4, "line_position": 2, "yao_ci_text": "九二、包蒙吉。納婦吉。子克家。", "yao_ci_meaning": "蒙昧な者を包み込むように教え導けば吉。未熟な者を受け入れ、育てれば家庭はうまくいく。", "changing_line_special_meaning": "未熟な相手を、寛大な心で受け入れ、育ててあげましょう。あなたの包容力が試される時です。" },
    { "hexagram_id": 4, "line_position": 3, "yao_ci_text": "六三、勿用取女。見金夫、不有躬。无攸利。", "yao_ci_meaning": "金持ちの男を見て、自分を見失うような女性を妻にしてはならない。何の利益もない。", "changing_line_special_meaning": "目先の利益や誘惑に目がくらむと、自分を見失います。誠実さのない相手とは関わるべきではありません。" },
    { "hexagram_id": 4, "line_position": 4, "yao_ci_text": "六四、困蒙。吝。", "yao_ci_meaning": "蒙昧な状態で困窮する。正しい師から遠ざかっているため、後悔する。", "changing_line_special_meaning": "正しい教えから遠ざかり、孤立しています。このままでは状況は悪化するばかりです。素直に教えを請いましょう。" },
    { "hexagram_id": 4, "line_position": 5, "yao_ci_text": "六五、童蒙。吉。", "yao_ci_meaning": "子供のように素直に教えを請う。謙虚な姿勢が良い結果を招く。", "changing_line_special_meaning": "先入観を捨て、子供のように素直な心で学びましょう。謙虚な姿勢が幸運を呼びます。" },
    { "hexagram_id": 4, "line_position": 6, "yao_ci_text": "上九、擊蒙。不利爲寇。利禦寇。", "yao_ci_meaning": "蒙昧を打ち破るには、厳しい態度も必要。ただし、攻撃的になるのではなく、相手を守るために行うべき。", "changing_line_special_meaning": "時には厳しい態度で、相手の間違いを正す必要があります。それは相手のためを思っての行動でなければなりません。" },

    # 5. 水天需 (すいてんじゅ)
    { "hexagram_id": 5, "line_position": 1, "yao_ci_text": "初九、需于郊。利用恒。无咎。", "yao_ci_meaning": "郊外でのんびりと待つ。変わらず待ち続ければ、問題は起こらない。", "changing_line_special_meaning": "まだ時期が早いようです。焦らず、普段通りに過ごしながら、気長に待ちましょう。" },
    { "hexagram_id": 5, "line_position": 2, "yao_ci_text": "九二、需于沙。小有言。終吉。", "yao_ci_meaning": "砂地で待つ。多少のトラブルはあるが、最終的には良い結果になる。", "changing_line_special_meaning": "少し不安な状況ですが、心配いりません。多少の批判や困難はありますが、最終的にはうまくいきます。" },
    { "hexagram_id": 5, "line_position": 3, "yao_ci_text": "九三、需于泥。致寇至。", "yao_ci_meaning": "泥の中で待つ。危険が迫っている。軽率な行動が敵を招く。", "changing_line_special_meaning": "危険が近づいています。軽率な行動は慎んでください。一歩間違えると、トラブルに巻き込まれます。" },
    { "hexagram_id": 5, "line_position": 4, "yao_ci_text": "六四、需于血。出自穴。", "yao_ci_meaning": "血の海で待つような危険な状況。しかし、そこから脱出できる。", "changing_line_special_meaning": "非常に危険で困難な状況ですが、必ず抜け出す道はあります。冷静に状況を判断し、活路を見出してください。" },
    { "hexagram_id": 5, "line_position": 5, "yao_ci_text": "九五、需于酒食。貞吉。", "yao_ci_meaning": "酒食を楽しみながら待つ。ゆったりと構えていれば、良い結果になる。", "changing_line_special_meaning": "リラックスして待つのが一番です。焦らず、楽しみながら時が来るのを待ちましょう。必ず良い結果になります。" },
    { "hexagram_id": 5, "line_position": 6, "yao_ci_text": "上六、入于穴。有不速之客三人來。敬之終吉。", "yao_ci_meaning": "穴に入り込んでしまう。予期せぬ客が三人来るが、敬意を払って迎えれば、最終的には吉となる。", "changing_line_special_meaning": "困難な状況に陥りますが、予期せぬ助けが現れます。その助けを丁重に受け入れれば、事態は好転します。" },

    # 6. 天水訟 (てんすいしょう)
    { "hexagram_id": 6, "line_position": 1, "yao_ci_text": "初六、不永所事。小有言。終吉。", "yao_ci_meaning": "争い事を長引かせない。多少の非難はあっても、早く和解すれば、最終的には良い結果になる。", "changing_line_special_meaning": "争いは長引かせず、早めに切り上げるのが賢明です。多少の不満は残っても、和解を優先しましょう。" },
    { "hexagram_id": 6, "line_position": 2, "yao_ci_text": "九二、不克訟。歸而逋。其邑人三百戸。无眚。", "yao_ci_meaning": "争いには勝てない。逃げて隠れるのが良い。そうすれば災いを免れる。", "changing_line_special_meaning": "この争いには勝ち目がありません。戦うのではなく、身を引くのが最善の策です。逃げるが勝ちです。" },
    { "hexagram_id": 6, "line_position": 3, "yao_ci_text": "六三、食舊德。貞厲。終吉。或從王事、无成。", "yao_ci_meaning": "古い徳を守って暮らす。危うい立場だが、正道を守れば最終的には吉。公の仕事に関わっても成功しない。", "changing_line_special_meaning": "新しいことを始めるより、今あるものを大切に守るべき時です。目立たず、誠実に過ごせば安泰です。" },
    { "hexagram_id": 6, "line_position": 4, "yao_ci_text": "九四、不克訟。復即命。渝安貞。吉。", "yao_ci_meaning": "争いには勝てない。天命に立ち返り、心を変えて安らかにいれば吉。", "changing_line_special_meaning": "争うことをやめ、運命を受け入れましょう。心穏やかに過ごすことで、かえって道が開けます。" },
    { "hexagram_id": 6, "line_position": 5, "yao_ci_text": "九五、訟元吉。", "yao_ci_meaning": "訴訟して、最高に良い結果を得る。公平な第三者の裁きを受ければ、正義は通る。", "changing_line_special_meaning": "あなたの主張は正当です。公平な場で判断を仰げば、必ず認められます。自信を持って訴えましょう。" },
    { "hexagram_id": 6, "line_position": 6, "yao_ci_text": "上九、或錫之鞶帶。終朝三褫之。", "yao_ci_meaning": "争いに勝って褒美をもらっても、一日のうちに三度も剥ぎ取られる。一時的な勝利に過ぎない。", "changing_line_special_meaning": "たとえ争いに勝ったとしても、その栄光は長続きしません。虚しい勝利に終わるでしょう。" },

    # 7. 地水師 (ちすいし)
    { "hexagram_id": 7, "line_position": 1, "yao_ci_text": "初六、師出以律。否臧凶。", "yao_ci_meaning": "軍隊は規律をもって出動すべき。規律が乱れると凶。", "changing_line_special_meaning": "計画を始めるにあたり、まずはルールを明確にすることが重要です。規律がなければ、うまくいくものもいきません。" },
    { "hexagram_id": 7, "line_position": 2, "yao_ci_text": "九二、在師中。吉无咎。王三錫命。", "yao_ci_meaning": "軍の中心にいて、吉。王から三度も褒美を賜る。リーダーとしての信頼が厚い。", "changing_line_special_meaning": "集団の中心人物として、あなたのリーダーシップが高く評価されます。自信を持って皆を引っ張っていきましょう。" },
    { "hexagram_id": 7, "line_position": 3, "yao_ci_text": "六三、師或輿尸。凶。", "yao_ci_meaning": "軍隊が多くの屍を車で運ぶ。無能な者が指揮を執ると、大敗する。", "changing_line_special_meaning": "リーダーの資質がない人が指揮を執ると、事態は悪化します。人選を誤らないように注意してください。" },
    { "hexagram_id": 7, "line_position": 4, "yao_ci_text": "六四、師左次。无咎。", "yao_ci_meaning": "軍隊が退却して陣を敷く。無理に進まず、一旦退くのが賢明。", "changing_line_special_meaning": "今は無理に進むべき時ではありません。一旦退却し、体勢を立て直すのが得策です。" },
    { "hexagram_id": 7, "line_position": 5, "yao_ci_text": "六五、田有禽。利執言。无咎。長子帥師。弟子輿尸。貞凶。", "yao_ci_meaning": "田に獲物がいる。捕らえて良い。ただし、経験豊かな長男が率いるべきで、未熟な者が指揮すると失敗する。", "changing_line_special_meaning": "チャンス到来ですが、誰が主導権を握るかが重要です。経験豊富な人に任せるべきで、未熟な人が出しゃばると失敗します。" },
    { "hexagram_id": 7, "line_position": 6, "yao_ci_text": "上六、大君有命。開國承家。小人勿用。", "yao_ci_meaning": "大君が恩賞を与える。功績のあった者を諸侯に取り立てる。つまらない人物を重用してはならない。", "changing_line_special_meaning": "プロジェクトが成功した後は、論功行賞を正しく行うことが重要です。実力のない人物を贔屓すると、組織は衰退します。" },

    # 8. 水地比 (すいちひ)
    { "hexagram_id": 8, "line_position": 1, "yao_ci_text": "初六、有孚比之。无咎。有孚盈缶。終來有他吉。", "yao_ci_meaning": "誠意をもって親しめば、問題ない。誠意が満ち溢れれば、思わぬ幸運が舞い込む。", "changing_line_special_meaning": "真心からの付き合いを心がけましょう。誠実な態度は、必ず相手に伝わり、良い結果をもたらします。" },
    { "hexagram_id": 8, "line_position": 2, "yao_ci_text": "六二、比之自内。貞吉。", "yao_ci_meaning": "内面から親しむ。正しい道を守れば吉。心からの付き合いが大切。", "changing_line_special_meaning": "うわべだけの付き合いではなく、心から相手と親しむことが大切です。誠実な関係を築きましょう。" },
    { "hexagram_id": 8, "line_position": 3, "yao_ci_text": "六三、比之匪人。", "yao_ci_meaning": "親しむべきでない人と親しんでいる。付き合う相手を間違えている。", "changing_line_special_meaning": "付き合う相手は慎重に選ぶべきです。悪影響を及ぼす人とは、距離を置くのが賢明です。" },
    { "hexagram_id": 8, "line_position": 4, "yao_ci_text": "六四、外比之。貞吉。", "yao_ci_meaning": "外部の賢者と親しむ。正しい道を守れば吉。自分より優れた人と付き合うべき。", "changing_line_special_meaning": "尊敬できる人や、自分を成長させてくれる人との関係を大切にしましょう。良い影響を受けられます。" },
    { "hexagram_id": 8, "line_position": 5, "yao_ci_text": "九五、顯比。王用三驅。失前禽。邑人不誡。吉。", "yao_ci_meaning": "王が狩りをするように、来る者は拒まず、去る者は追わず、という姿勢で人々と付き合えば吉。", "changing_line_special_meaning": "オープンな人間関係が幸運を呼びます。誰でも受け入れる寛大な心を持ちましょう。" },
    { "hexagram_id": 8, "line_position": 6, "yao_ci_text": "上六、比之无首。凶。", "yao_ci_meaning": "親しむべき中心を見失っている。最後まで目的が定まらず、凶。", "changing_line_special_meaning": "誰にでも良い顔をして、八方美人になっていませんか。中心となるべき関係を見失うと、全てがうまくいかなくなります。" },

    # 9. 風天小畜 (ふうてんしょうちく)
    { "hexagram_id": 9, "line_position": 1, "yao_ci_text": "初九、復自道。何其咎。吉。", "yao_ci_meaning": "自分の道に立ち返る。何の問題があろうか。吉である。", "changing_line_special_meaning": "無理に進むのをやめ、基本に立ち返ることで、かえって道が開けます。初心を忘れないでください。" },
    { "hexagram_id": 9, "line_position": 2, "yao_ci_text": "九二、牽復。吉。", "yao_ci_meaning": "人に引かれて道に立ち返る。吉である。", "changing_line_special_meaning": "周りの人の助言や誘いに乗ることで、良い方向へ進めます。人の意見を素直に聞きましょう。" },
    { "hexagram_id": 9, "line_position": 3, "yao_ci_text": "九三、輿説輻。夫妻反目。", "yao_ci_meaning": "車の部品が外れるように、夫婦が反目しあう。内部で対立が起こる。", "changing_line_special_meaning": "些細なことから、内部で対立や不和が生じやすい時です。強引に進めようとすると、関係が悪化します。" },
    { "hexagram_id": 9, "line_position": 4, "yao_ci_text": "六四、有孚。血去惕出。无咎。", "yao_ci_meaning": "誠意があれば、憂いは去り、危機を脱することができる。問題ない。", "changing_line_special_meaning": "誠実な対応を心がけることで、困難な状況を乗り越えられます。不安や恐れは消えていくでしょう。" },
    { "hexagram_id": 9, "line_position": 5, "yao_ci_text": "九五、有孚攣如。富以其鄰。", "yao_ci_meaning": "誠意をもって手を取り合えば、隣人と共に豊かになれる。", "changing_line_special_meaning": "周りの人と協力し、信頼関係を築くことで、お互いに利益を得られます。助け合いの精神が大切です。" },
    { "hexagram_id": 9, "line_position": 6, "yao_ci_text": "上九、既雨既處。尚徳載。婦貞厲。月幾望。君子征凶。", "yao_ci_meaning": "雨が降り、落ち着いた。徳が満ちた状態だが、女性がでしゃばると危うい。月は満月間近。これ以上進むのは凶。", "changing_line_special_meaning": "目標はほぼ達成されました。これ以上の深追いは禁物です。満足することを知り、現状を維持しましょう。" },

    # 10. 天沢履 (てんたくり)
    { "hexagram_id": 10, "line_position": 1, "yao_ci_text": "初九、素履。往无咎。", "yao_ci_meaning": "素朴なままで進む。そうすれば問題ない。", "changing_line_special_meaning": "余計な飾り気は不要です。ありのままの自分で、誠実に行動すれば、うまくいきます。" },
    { "hexagram_id": 10, "line_position": 2, "yao_ci_text": "九二、履道坦坦。幽人貞吉。", "yao_ci_meaning": "平坦な道を行くように、穏やかである。隠者のように静かにしていれば吉。", "changing_line_special_meaning": "穏やかで平穏な時です。目立たず、静かに自分の道を進むのが良いでしょう。" },
    { "hexagram_id": 10, "line_position": 3, "yao_ci_text": "六三、眇能視、跛能履。履虎尾、咥人。凶。武人爲于大君。", "yao_ci_meaning": "片目で見、片足で歩くような危うさ。虎の尾を踏んで食いつかれる。凶。武人が大君のために働くようなもの。", "changing_line_special_meaning": "自分の実力以上のことをしようとして、危険な状況に陥ります。分不相応な望みは捨てるべきです。" },
    { "hexagram_id": 10, "line_position": 4, "yao_ci_text": "九四、履虎尾。愬愬。終吉。", "yao_ci_meaning": "虎の尾を踏むような危険な状況。恐る恐る進めば、最終的には吉となる。", "changing_line_special_meaning": "危険な状況ですが、慎重に、細心の注意を払って行動すれば、無事に乗り越えられます。" },
    { "hexagram_id": 10, "line_position": 5, "yao_ci_text": "九五、夬履。貞厲。", "yao_ci_meaning": "思い切って進む。正道を守っていても危うい。", "changing_line_special_meaning": "強引に進めば、たとえ正しくても危険が伴います。決断は慎重に行うべきです。" },
    { "hexagram_id": 10, "line_position": 6, "yao_ci_text": "上九、視履考祥。其旋元吉。", "yao_ci_meaning": "これまでの行いを振り返り、吉凶をよく考える。そうすれば、最高の吉となる。", "changing_line_special_meaning": "これまでの経験をよく振り返り、反省すべき点は反省しましょう。それが将来の大きな成功に繋がります。" },

    # 11. 地天泰 (ちてんたい)
    { "hexagram_id": 11, "line_position": 1, "yao_ci_text": "初九、拔茅茹。以其彙。征吉。", "yao_ci_meaning": "茅の根を引き抜くと、仲間がついてくる。仲間と共に進めば吉。", "changing_line_special_meaning": "志を同じくする仲間と共に、新しいことを始めるのに良い時です。協力すれば成功します。" },
    { "hexagram_id": 11, "line_position": 2, "yao_ci_text": "九二、包荒。用馮河。不遐遺。朋亡。得尚于中行。", "yao_ci_meaning": "荒れたものを包容し、無謀な者も用い、遠い者も見捨てず、朋党を組まない。中庸の道を行けば良い。", "changing_line_special_meaning": "寛大な心で、あらゆる人や物事を受け入れましょう。公平な態度が、あなたの評価を高めます。" },
    { "hexagram_id": 11, "line_position": 3, "yao_ci_text": "九三、无平不陂。无往不復。艱貞无咎。勿恤其孚。于食有福。", "yao_ci_meaning": "平坦な道もいつかは傾き、行けば必ず帰ってくる。困難でも正道を守れば問題ない。誠意を信じ、食に福がある。", "changing_line_special_meaning": "良い時もあれば、悪い時もあります。困難な状況でも、誠実に努力を続ければ、必ず報われます。" },
    { "hexagram_id": 11, "line_position": 4, "yao_ci_text": "六四、翩翩不富。以其鄰。不戒以孚。", "yao_ci_meaning": "軽やかに舞い降りる鳥のように、富を誇示せず、隣人と共に、無警戒に誠意をもって交わる。", "changing_line_special_meaning": "謙虚な姿勢で、周りの人と誠実に付き合いましょう。見栄を張らず、心を開くことが大切です。" },
    { "hexagram_id": 11, "line_position": 5, "yao_ci_text": "六五、帝乙歸妹。以祉元吉。", "yao_ci_meaning": "帝乙が妹を嫁がせたように、身分の高い者がへりくだる。それによって幸福を得て、大いに吉。", "changing_line_special_meaning": "上の立場の人間が、謙虚な姿勢を示すことで、物事が円満に進みます。相手の立場を尊重しましょう。" },
    { "hexagram_id": 11, "line_position": 6, "yao_ci_text": "上六、城復于隍。勿用師。自邑告命。貞吝。", "yao_ci_meaning": "城壁が崩れて堀に戻る。安泰の時が終わり、乱世が始まる。軍隊は用いるべきでない。内輪揉めは後悔する。", "changing_line_special_meaning": "平和な時期は終わりを告げ、状況は悪化します。内部での争いは避け、静かに耐え忍ぶべきです。" },

    # 12. 天地否 (てんちひ)
    { "hexagram_id": 12, "line_position": 1, "yao_ci_text": "初六、拔茅茹。以其彙。貞吉亨。", "yao_ci_meaning": "茅の根を引き抜くと、仲間がついてくる。正道を守れば吉で、願いは通る。", "changing_line_special_meaning": "悪い状況ですが、同じ志を持つ仲間と結束すれば、困難を乗り越えられます。" },
    { "hexagram_id": 12, "line_position": 2, "yao_ci_text": "六二、包承。小人吉。大人否亨。", "yao_ci_meaning": "目上の者にへつらい、包み込まれる。小人は吉だが、大人は閉塞するが、やがて通る。", "changing_line_special_meaning": "目先の利益のために、信念を曲げるべきではありません。今は苦しくても、正しい道を守り抜きましょう。" },
    { "hexagram_id": 12, "line_position": 3, "yao_ci_text": "六三、包羞。", "yao_ci_meaning": "恥を包み隠している。不正な行いをしている。", "changing_line_special_meaning": "不正やごまかしは、いずれ必ず露見します。良心に恥じるような行動は、今すぐやめるべきです。" },
    { "hexagram_id": 12, "line_position": 4, "yao_ci_text": "九四、有命无咎。疇離祉。", "yao_ci_meaning": "天命があれば問題ない。仲間は幸福を得るだろう。", "changing_line_special_meaning": "正しい目的のために行動するならば、天の助けが得られます。仲間と協力して、困難に立ち向かいましょう。" },
    { "hexagram_id": 12, "line_position": 5, "yao_ci_text": "九五、休否。大人吉。其亡其亡、繋于苞桑。", "yao_ci_meaning": "閉塞が終わる。大人にとっては吉。「亡びる、亡びる」と常に危機感を持てば、桑の根のように安泰である。", "changing_line_special_meaning": "ようやく悪い状況が終わり、好転し始めます。しかし、油断せず、常に危機意識を持つことが大切です。" },
    { "hexagram_id": 12, "line_position": 6, "yao_ci_text": "上九、傾否。先否後喜。", "yao_ci_meaning": "閉塞が覆る。最初は閉塞しているが、後には喜びがある。", "changing_line_special_meaning": "長いトンネルの出口はもうすぐです。苦しい状況はまもなく終わり、喜びが訪れるでしょう。" },

    # 13. 天火同人 (てんかどうじん)
    { "hexagram_id": 13, "line_position": 1, "yao_ci_text": "初九、同人于門。无咎。", "yao_ci_meaning": "門を出たところで人と協力する。問題ない。", "changing_line_special_meaning": "まずは身近な人々と協力関係を築きましょう。オープンな姿勢が大切です。" },
    { "hexagram_id": 13, "line_position": 2, "yao_ci_text": "六二、同人于宗。吝。", "yao_ci_meaning": "仲間内だけで協力する。これでは後悔する。", "changing_line_special_meaning": "内輪だけで固まるのは良くありません。排他的な態度は、あなたの可能性を狭めてしまいます。" },
    { "hexagram_id": 13, "line_position": 3, "yao_ci_text": "九三、伏戎于莽。升其高陵。三歳不興。", "yao_ci_meaning": "草むらに兵を伏せ、高い丘に登る。疑心暗鬼になり、三年間も事を起こせない。", "changing_line_special_meaning": "相手を信用できず、疑心暗鬼になっています。これでは、物事は一向に進みません。" },
    { "hexagram_id": 13, "line_position": 4, "yao_ci_text": "九四、乘其墉。弗克攻。吉。", "yao_ci_meaning": "城壁に登るが、攻めない。そうすれば吉。", "changing_line_special_meaning": "争うべきではありません。一歩引いて、和解の道を探るのが賢明です。" },
    { "hexagram_id": 13, "line_position": 5, "yao_ci_text": "九五、同人先號咷而後笑。大師克相遇。", "yao_ci_meaning": "最初は泣き叫ぶほどの困難があるが、後には笑う。大軍を率いて、ついに会うことができる。", "changing_line_special_meaning": "多くの困難を乗り越えた末に、大きな成功と喜びが待っています。諦めないでください。" },
    { "hexagram_id": 13, "line_position": 6, "yao_ci_text": "上九、同人于郊。无悔。", "yao_ci_meaning": "郊外で人と協力する。志はまだ達成できていないが、後悔はない。", "changing_line_special_meaning": "目標達成には至りませんが、人里離れた場所で、静かに仲間と過ごすことに満足できるでしょう。" },

    # 14. 火天大有 (かてんたいゆう)
    { "hexagram_id": 14, "line_position": 1, "yao_ci_text": "初九、无交害。匪咎。艱則无咎。", "yao_ci_meaning": "害意をもって交わらなければ、問題ない。驕らず、謙虚でいれば問題ない。", "changing_line_special_meaning": "恵まれた状況ですが、驕りの気持ちが芽生えやすい時です。謙虚さを忘れなければ、安泰です。" },
    { "hexagram_id": 14, "line_position": 2, "yao_ci_text": "九二、大車以載。有攸往。无咎。", "yao_ci_meaning": "大きな車で荷物を運ぶように、多くの人材を任される。どこへ行っても問題ない。", "changing_line_special_meaning": "大きな責任を任されますが、あなたなら大丈夫です。自信を持って、その役目を果たしてください。" },
    { "hexagram_id": 14, "line_position": 3, "yao_ci_text": "九三、公用亨于天子。小人弗克。", "yao_ci_meaning": "諸侯が天子に貢物を献上する。小人にはできないことだ。", "changing_line_special_meaning": "自分の利益のためだけでなく、社会や公のために、自分の富や才能を役立てるべき時です。" },
    { "hexagram_id": 14, "line_position": 4, "yao_ci_text": "九四、匪其彭。无咎。", "yao_ci_meaning": "富を独り占めにしない。そうすれば問題ない。", "changing_line_special_meaning": "恵まれた状況に驕らず、周りの人と分かち合う気持ちが大切です。嫉妬を招かないようにしましょう。" },
    { "hexagram_id": 14, "line_position": 5, "yao_ci_text": "六五、厥孚交如。威如。吉。", "yao_ci_meaning": "誠実で、威厳がある。吉である。", "changing_line_special_meaning": "誠実さと威厳を兼ね備えた、あなたのリーダーシップが高く評価されます。自信を持って行動してください。" },
    { "hexagram_id": 14, "line_position": 6, "yao_ci_text": "上九、自天祐之。吉无不利。", "yao_ci_meaning": "天が自ら助けてくれる。吉であり、何事もうまくいく。", "changing_line_special_meaning": "これまでの善い行いによって、天の助けが得られます。万事順調に進む、最高の幸運期です。" },

    # 15. 地山謙 (ちざんけん)
    { "hexagram_id": 15, "line_position": 1, "yao_ci_text": "初六、謙謙君子。用渉大川。吉。", "yao_ci_meaning": "謙虚で謙虚な君子。大きな川を渡るような困難なことも、成し遂げられる。吉。", "changing_line_special_meaning": "どこまでも謙虚な姿勢が、困難な状況を乗り越える力となります。自信がなくても、謙虚に進めば大丈夫です。" },
    { "hexagram_id": 15, "line_position": 2, "yao_ci_text": "六二、鳴謙。貞吉。", "yao_ci_meaning": "謙虚さが自然と評判になる。正道を守れば吉。", "changing_line_special_meaning": "あなたの謙虚な人柄は、自然と周りの人に伝わります。その誠実さを持ち続けてください。" },
    { "hexagram_id": 15, "line_position": 3, "yao_ci_text": "九三、勞謙君子。有終。吉。", "yao_ci_meaning": "功績があっても謙虚な君子。最後までやり遂げ、吉となる。", "changing_line_special_meaning": "努力が実っても、決して驕らないでください。その謙虚な姿勢が、さらなる成功へと繋がります。" },
    { "hexagram_id": 15, "line_position": 4, "yao_ci_text": "六四、无不利。撝謙。", "yao_ci_meaning": "何事もうまくいく。謙虚さを発揮すべき時。", "changing_line_special_meaning": "何事もスムーズに進む時です。ますます謙虚な気持ちで、物事に取り組みましょう。" },
    { "hexagram_id": 15, "line_position": 5, "yao_ci_text": "六五、不富以其鄰。利用侵伐。无不利。", "yao_ci_meaning": "富を誇示せず、隣人と協力する。従わない者を討伐しても、何事もうまくいく。", "changing_line_special_meaning": "謙虚なリーダーシップを発揮する時です。時には厳しい決断も必要ですが、私利私欲からでなければ問題ありません。" },
    { "hexagram_id": 15, "line_position": 6, "yao_ci_text": "上六、鳴謙。利用行師。征邑國。", "yao_ci_meaning": "謙虚さが知れ渡る。軍隊を動かし、自分の国を治めるのに良い。", "changing_line_special_meaning": "あなたの謙虚な徳が、広く認められます。自信を持って、自分のコミュニティをまとめていきましょう。" },

    # 16. 雷地豫 (らいちよ)
    { "hexagram_id": 16, "line_position": 1, "yao_ci_text": "初六、鳴豫。凶。", "yao_ci_meaning": "楽しみにふけって、それを自慢する。凶。", "changing_line_special_meaning": "調子に乗って、楽しみや喜びをひけらかしてはいけません。謙虚さを失うと、足元をすくわれます。" },
    { "hexagram_id": 16, "line_position": 2, "yao_ci_text": "六二、介于石。不終日。貞吉。", "yao_ci_meaning": "石のように固い意志を持つ。一日も待たずに、正しい判断を下す。正道を守れば吉。", "changing_line_special_meaning": "周りの雰囲気に流されず、自分の意志をしっかりと持ちましょう。素早い決断が良い結果を招きます。" },
    { "hexagram_id": 16, "line_position": 3, "yao_ci_text": "六三、盱豫。悔。遲有悔。", "yao_ci_meaning": "目上の者に媚びへつらって楽しむ。後悔する。決断が遅れても後悔する。", "changing_line_special_meaning": "お世辞を言ったり、人の顔色をうかがったりして、その場を取り繕うのはやめましょう。後で必ず後悔します。" },
    { "hexagram_id": 16, "line_position": 4, "yao_ci_text": "九四、由豫。大有得。勿疑。朋盍簪。", "yao_ci_meaning": "楽しみの中心となる。大いに得るものがある。疑ってはならない。仲間が集まってくる。", "changing_line_special_meaning": "あなたが中心となって、周りの人々を楽しませる時です。自信を持って行動すれば、多くの支持者が集まります。" },
    { "hexagram_id": 16, "line_position": 5, "yao_ci_text": "六五、貞疾。恒不死。", "yao_ci_meaning": "楽しみに溺れて、病気にかかっている。しかし、すぐには死なない。", "changing_line_special_meaning": "怠惰な生活や、不摂生が続いていませんか。このままでは、心身ともに蝕まれてしまいます。生活習慣を見直しましょう。" },
    { "hexagram_id": 16, "line_position": 6, "yao_ci_text": "上六、冥豫。成有渝。无咎。", "yao_ci_meaning": "暗い楽しみ。心が変わり、改心すれば問題ない。", "changing_line_special_meaning": "間違った楽しみに 빠っていますが、今ならまだ間に合います。心を入れ替え、正しい道に戻りましょう。" },

    # 17. 沢雷随 (たくらいずい)
    { "hexagram_id": 17, "line_position": 1, "yao_ci_text": "初九、官有渝。貞吉。出門交有功。", "yao_ci_meaning": "考え方が変わる。正道を守れば吉。外に出て人と交われば、功績がある。", "changing_line_special_meaning": "固定観念を捨て、新しい考え方を取り入れるべき時です。積極的に人と交流することで、道が開けます。" },
    { "hexagram_id": 17, "line_position": 2, "yao_ci_text": "六二、係小子。失丈夫。", "yao_ci_meaning": "つまらない者と関わると、立派な人物を失う。", "changing_line_special_meaning": "付き合う相手は慎重に選びましょう。目先の利益や楽しさで、質の低い人と関わると、大切なものを失います。" },
    { "hexagram_id": 17, "line_position": 3, "yao_ci_text": "六三、係丈夫。失小子。随有求得。利居貞。", "yao_ci_meaning": "立派な人物に従えば、つまらない者は去っていく。求めれば得られる。正しくいることが大切。", "changing_line_special_meaning": "尊敬できる人や、志の高い人に従うべきです。そうすれば、自然と道は開け、願いも叶うでしょう。" },
    { "hexagram_id": 17, "line_position": 4, "yao_ci_text": "九四、随有獲。貞凶。有孚在道。以明何咎。", "yao_ci_meaning": "人に従うことで、多くのものを得る。しかし、下心があると凶。誠意をもって道に従えば、問題ない。", "changing_line_special_meaning": "人気運があり、多くの支持を得られます。しかし、それを私利私欲に使うと、全てを失います。誠実さを忘れずに。" },
    { "hexagram_id": 17, "line_position": 5, "yao_ci_text": "九五、孚于嘉。吉。", "yao_ci_meaning": "善いものに誠意を尽くす。吉である。", "changing_line_special_meaning": "自分が本当に良いと信じるものに、誠心誠意従いましょう。その純粋な気持ちが、幸運を呼び込みます。" },
    { "hexagram_id": 17, "line_position": 6, "yao_ci_text": "上六、拘係之。乃從維之。王用亨于西山。", "yao_ci_meaning": "固く結びついている。王が西山で祭祀を行うように、誠意を尽くせば、堅い絆で結ばれる。", "changing_line_special_meaning": "誠意を尽くすことで、深く、永続的な信頼関係を築くことができます。上辺だけでなく、心からの繋がりを大切に。" },

    # 18. 山風蠱 (さんぷうこ)
    { "hexagram_id": 18, "line_position": 1, "yao_ci_text": "初六、幹父之蠱。有子。考无咎。厲終吉。", "yao_ci_meaning": "父の代からの問題を解決する。有能な子がいれば、父に問題はない。危ういが、最終的には吉。", "changing_line_special_meaning": "過去からの問題や、親の代からの課題に取り組むべき時です。困難ですが、やり遂げれば良い結果になります。" },
    { "hexagram_id": 18, "line_position": 2, "yao_ci_text": "九二、幹母之蠱。不可貞。", "yao_ci_meaning": "母の代からの問題を解決する。優しさだけでは解決できない。", "changing_line_special_meaning": "馴れ合いや、なあなあな関係が問題の原因です。情に流されず、時には厳しく対処する必要があります。" },
    { "hexagram_id": 18, "line_position": 3, "yao_ci_text": "九三、幹父之蠱。小有悔。无大咎。", "yao_ci_meaning": "父の代からの問題を解決する。少しやり過ぎて後悔するが、大きな問題はない。", "changing_line_special_meaning": "改革への意欲が強すぎて、少しやり過ぎてしまうかもしれません。多少の反省はあっても、結果的には良い方向へ向かいます。" },
    { "hexagram_id": 18, "line_position": 4, "yao_ci_text": "六四、裕父之蠱。往見吝。", "yao_ci_meaning": "父の代からの問題を放置する。このままでは後悔することになる。", "changing_line_special_meaning": "問題を見て見ぬふりをしてはいけません。先延ばしにすると、事態はさらに悪化します。今すぐ取り組むべきです。" },
    { "hexagram_id": 18, "line_position": 5, "yao_ci_text": "六五、幹父之蠱。用譽。", "yao_ci_meaning": "父の代からの問題を解決する。名誉を得るだろう。", "changing_line_special_meaning": "長年の懸案事項を、見事に解決することができます。その功績は、高く評価されるでしょう。" },
    { "hexagram_id": 18, "line_position": 6, "yao_ci_text": "上九、不事王侯。高尚其事。", "yao_ci_meaning": "王侯に仕えず、自分の事を高尚にする。俗世間から離れて、自分の道を追求する。", "changing_line_special_meaning": "組織や社会の問題から距離を置き、自分の内面的な成長や、個人的な目標の追求に専念すべき時です。" },

    # 19. 地沢臨 (ちたくりん)
    { "hexagram_id": 19, "line_position": 1, "yao_ci_text": "初九、咸臨。貞吉。", "yao_ci_meaning": "感応しあって物事に臨む。正道を守れば吉。", "changing_line_special_meaning": "相手の気持ちを汲み取り、誠実に対応することで、物事は順調に進みます。思いやりの心が大切です。" },
    { "hexagram_id": 19, "line_position": 2, "yao_ci_text": "九二、咸臨。吉无不利。", "yao_ci_meaning": "感応しあって物事に臨む。吉であり、何事もうまくいく。", "changing_line_special_meaning": "あなたの誠意が相手に通じ、万事順調に進む幸運期です。積極的に行動しましょう。" },
    { "hexagram_id": 19, "line_position": 3, "yao_ci_text": "六三、甘臨。无攸利。既憂之。无咎。", "yao_ci_meaning": "甘い言葉で人に臨む。何の利益もない。しかし、その非に気づいて改めれば、問題ない。", "changing_line_special_meaning": "口先だけの甘い言葉や、安易な態度は、信用を失います。過ちに気づいたら、すぐに改めることが大切です。" },
    { "hexagram_id": 19, "line_position": 4, "yao_ci_text": "六四、至臨。无咎。", "yao_ci_meaning": "誠意をもって物事に臨む。問題ない。", "changing_line_special_meaning": "真心をもって、物事や人に接しましょう。その誠実な態度は、必ず良い結果に繋がります。" },
    { "hexagram_id": 19, "line_position": 5, "yao_ci_text": "六五、知臨。大君之宜。吉。", "yao_ci_meaning": "知恵をもって物事に臨む。大いなる君主の徳である。吉。", "changing_line_special_meaning": "感情的にならず、知恵と理性をもって物事を判断すべき時です。その賢明な判断が、成功へと導きます。" },
    { "hexagram_id": 19, "line_position": 6, "yao_ci_text": "上六、敦臨。吉无咎。", "yao_ci_meaning": "篤実な態度で物事に臨む。吉であり、問題ない。", "changing_line_special_meaning": "寛大で、思いやりのある心で人に接しましょう。その篤実な人柄が、多くの人から慕われます。" },

    # 20. 風地観 (ふうちかん)
    { "hexagram_id": 20, "line_position": 1, "yao_ci_text": "初六、童観。小人无咎。君子吝。", "yao_ci_meaning": "子供のように、浅はかな見方をする。小人は問題ないが、君子にとっては恥ずべきこと。", "changing_line_special_meaning": "物事の表面しか見ていません。もっと深く、本質を見抜く努力が必要です。視野を広げましょう。" },
    { "hexagram_id": 20, "line_position": 2, "yao_ci_text": "六二、闚観。利女貞。", "yao_ci_meaning": "隙間から覗き見るような、狭い見方をする。女性にとっては良い。", "changing_line_special_meaning": "視野が狭くなっています。自分の殻に閉じこもらず、もっと広い世界に目を向けましょう。" },
    { "hexagram_id": 20, "line_position": 3, "yao_ci_text": "六三、観我生。進退。", "yao_ci_meaning": "自分のこれまでの生き方を観察し、進むべきか退くべきか判断する。", "changing_line_special_meaning": "これまでの人生を振り返り、自己分析をするべき時です。今後の身の振り方を、冷静に考えましょう。" },
    { "hexagram_id": 20, "line_position": 4, "yao_ci_text": "六四、観國之光。利用賓于王。", "yao_ci_meaning": "国の光、優れた文化を観察する。王の賓客として迎えられるのに良い。", "changing_line_special_meaning": "優れた人物や文化に触れ、見識を広めるべき時です。その経験が、あなたを大きく成長させます。" },
    { "hexagram_id": 20, "line_position": 5, "yao_ci_text": "九五、観我生。君子无咎。", "yao_ci_meaning": "自分の生き方が、人々の手本となる。君子であれば問題ない。", "changing_line_special_meaning": "あなたの言動は、多くの人から注目されています。手本となるような、立派な振る舞いを心がけましょう。" },
    { "hexagram_id": 20, "line_position": 6, "yao_ci_text": "上九、観其生。君子无咎。", "yao_ci_meaning": "人々の生き方を観察する。君子であれば問題ない。", "changing_line_special_meaning": "自分自身のことだけでなく、周りの人々の生き方からも学びましょう。客観的な視点が、新たな気づきを与えてくれます。" },

    # 21. 火雷噬嗑 (からいぜいごう)
    { "hexagram_id": 21, "line_position": 1, "yao_ci_text": "初九、屨校滅趾。无咎。", "yao_ci_meaning": "足枷をはめられ、足が見えなくなる。軽い罰で、問題ない。", "changing_line_special_meaning": "問題は、まだ初期段階です。今のうちに対処すれば、大きな問題にはなりません。早めの対応が肝心です。" },
    { "hexagram_id": 21, "line_position": 2, "yao_ci_text": "六二、噬膚滅鼻。无咎。", "yao_ci_meaning": "柔らかい肉を噛むように、簡単に解決できる。問題ない。", "changing_line_special_meaning": "障害は、それほど大きくありません。思い切って対処すれば、案外すんなりと解決するでしょう。" },
    { "hexagram_id": 21, "line_position": 3, "yao_ci_text": "六三、噬臘肉。遇毒。小吝。无咎。", "yao_ci_meaning": "干し肉を噛んで、毒にあたる。少し後悔するが、大きな問題はない。", "changing_line_special_meaning": "手強い相手や、厄介な問題に直面します。少し苦労しますが、乗り越えられない壁ではありません。" },
    { "hexagram_id": 21, "line_position": 4, "yao_ci_text": "九四、噬乾胏。得金矢。利艱貞。吉。", "yao_ci_meaning": "骨付きの干し肉を噛む。金と矢を得る。困難だが、正道を守れば吉。", "changing_line_special_meaning": "非常に困難な問題ですが、これを乗り越えれば、大きな利益と権威を得られます。諦めずに挑戦してください。" },
    { "hexagram_id": 21, "line_position": 5, "yao_ci_text": "六五、噬乾肉。得黄金。貞厲。无咎。", "yao_ci_meaning": "干し肉を噛む。黄金を得る。正道を守り、危機意識を持てば問題ない。", "changing_line_special_meaning": "比較的簡単な問題ですが、油断は禁物です。慎重に対処すれば、利益を得られるでしょう。" },
    { "hexagram_id": 21, "line_position": 6, "yao_ci_text": "上九、何校滅耳。凶。", "yao_ci_meaning": "首枷をはめられ、耳が聞こえなくなる。忠告を聞き入れず、凶。", "changing_line_special_meaning": "人の忠告に耳を貸さず、過ちを改めないため、最悪の事態を招きます。今すぐ、頑なな態度を改めるべきです。" },

    # 22. 山火賁 (さんかひ)
    { "hexagram_id": 22, "line_position": 1, "yao_ci_text": "初九、賁其趾。舎車而徒。", "yao_ci_meaning": "足元を飾る。車を捨てて、歩いていく。質素な態度が良い。", "changing_line_special_meaning": "見栄を張らず、地に足のついた行動を心がけましょう。実質を伴わない飾りは、何の役にも立ちません。" },
    { "hexagram_id": 22, "line_position": 2, "yao_ci_text": "六二、賁其須。", "yao_ci_meaning": "あごひげを飾る。目上の人に従って、自分を飾る。", "changing_line_special_meaning": "実力のある人や、目上の人を立てることで、あなた自身も引き立てられます。サポート役に徹するのが良いでしょう。" },
    { "hexagram_id": 22, "line_position": 3, "yao_ci_text": "九三、賁如濡如。永貞吉。", "yao_ci_meaning": "飾って、潤っている。長く正道を守れば吉。", "changing_line_special_meaning": "物質的にも精神的にも満たされ、華やかな時期です。この状態に溺れず、誠実さを保つことが大切です。" },
    { "hexagram_id": 22, "line_position": 4, "yao_ci_text": "六四、賁如皤如。白馬翰如。匪寇婚媾。", "yao_ci_meaning": "飾りがなく、白い。白馬に乗って現れるのは、敵ではなく、助け手である。", "changing_line_special_meaning": "飾り気のない、誠実な態度が、信頼できる協力者を呼び寄せます。真心をもって人と接しましょう。" },
    { "hexagram_id": 22, "line_position": 5, "yao_ci_text": "六五、賁于丘園。束帛戔戔。吝。終吉。", "yao_ci_meaning": "丘の上の庭園を飾るように、質素である。贈り物は少ないが、最終的には吉。", "changing_line_special_meaning": "華美な装飾よりも、質素で誠実な態度が評価されます。物質的な豊かさよりも、心の豊かさを大切に。" },
    { "hexagram_id": 22, "line_position": 6, "yao_ci_text": "上九、白賁。无咎。", "yao_ci_meaning": "飾りのない、ありのままの白さ。問題ない。", "changing_line_special_meaning": "全ての装飾を取り払い、本質に立ち返るべき時です。ありのままの、素朴な美しさが、最も価値があります。" },

    # 23. 山地剥 (さんちはく)
    { "hexagram_id": 23, "line_position": 1, "yao_ci_text": "初六、剥牀以足。蔑貞凶。", "yao_ci_meaning": "ベッドの足が剥がれ落ちる。正道を軽んじれば凶。", "changing_line_special_meaning": "崩壊は、まず足元から始まります。問題の小さな兆候を見逃さず、すぐに対処してください。" },
    { "hexagram_id": 23, "line_position": 2, "yao_ci_text": "六二、剥牀以辨。蔑貞凶。", "yao_ci_meaning": "ベッドの枠が剥がれ落ちる。正道を軽んじれば凶。", "changing_line_special_meaning": "事態はさらに悪化しています。もはや、根本的な対策を立てなければ、崩壊は免れません。" },
    { "hexagram_id": 23, "line_position": 3, "yao_ci_text": "六三、剥之。无咎。", "yao_ci_meaning": "小人たちを剥がし去る。そうすれば問題ない。", "changing_line_special_meaning": "周りにいる、悪影響を及ぼす人々との関係を断ち切るべきです。情に流されてはいけません。" },
    { "hexagram_id": 23, "line_position": 4, "yao_ci_text": "六四、剥牀以膚。凶。", "yao_ci_meaning": "ベッドの表面まで剥がれ落ちる。身に危険が迫っている。凶。", "changing_line_special_meaning": "災害が、いよいよ目前に迫っています。もはや、打つ手はありません。被害を最小限に抑えることだけを考えましょう。" },
    { "hexagram_id": 23, "line_position": 5, "yao_ci_text": "六五、貫魚。以宮人寵。无不利。", "yao_ci_meaning": "魚が貫かれるように、宮人が寵愛を受ける。何事もうまくいく。", "changing_line_special_meaning": "絶望的な状況の中で、唯一の陽爻として、リーダーシップを発揮する時です。人々をまとめ、導くことで、道が開けます。" },
    { "hexagram_id": 23, "line_position": 6, "yao_ci_text": "上九、碩果不食。君子得輿。小人剥廬。", "yao_ci_meaning": "大きな果実が、食べられずに残る。君子は人々の支持を得るが、小人は家を失う。", "changing_line_special_meaning": "崩壊の後に、新しい希望が生まれます。これまでの行いによって、未来は大きく分かれるでしょう。" },

    # 24. 地雷復 (ちらいふく)
    { "hexagram_id": 24, "line_position": 1, "yao_ci_text": "初九、不遠復。无祗悔。元吉。", "yao_ci_meaning": "遠くへ行かないうちに引き返す。後悔はない。大いに吉。", "changing_line_special_meaning": "間違いに気づいたら、すぐに引き返しましょう。早めの軌道修正が、大きな成功に繋がります。" },
    { "hexagram_id": 24, "line_position": 2, "yao_ci_text": "六二、休復。吉。", "yao_ci_meaning": "美しく引き返す。吉である。", "changing_line_special_meaning": "周りの善い人々に感化され、自然と正しい道に戻ることができます。素直な心が大切です。" },
    { "hexagram_id": 24, "line_position": 3, "yao_ci_text": "六三、頻復。厲无咎。", "yao_ci_meaning": "何度も道に迷い、引き返す。危ういが、問題はない。", "changing_line_special_meaning": "迷いが多く、方針が定まりません。しかし、その都度反省し、正しい道に戻ろうと努力すれば、大丈夫です。" },
    { "hexagram_id": 24, "line_position": 4, "yao_ci_text": "六四、中行獨復。", "yao_ci_meaning": "一人だけ、正しい道に引き返す。", "changing_line_special_meaning": "周りが間違った方向に進んでいても、あなただけは、勇気を持って正しい道を選びましょう。" },
    { "hexagram_id": 24, "line_position": 5, "yao_ci_text": "六五、敦復。无悔。", "yao_ci_meaning": "篤実に、真心をもって引き返す。後悔はない。", "changing_line_special_meaning": "真心をもって、自分の過ちを反省し、正しい道に戻りましょう。その誠実な態度は、必ず評価されます。" },
    { "hexagram_id": 24, "line_position": 6, "yao_ci_text": "上六、迷復。凶。有災眚。用行師。終有大敗。以其國君凶。至于十年不克征。", "yao_ci_meaning": "道に迷い、引き返せない。凶。災いがある。軍を動かせば大敗し、国君も凶。十年は再起不能。", "changing_line_special_meaning": "過ちを改める機会を逸し、最悪の事態を招きます。もはや、手遅れかもしれません。" },

    # 25. 天雷无妄 (てんらいむもう)
    { "hexagram_id": 25, "line_position": 1, "yao_ci_text": "初九、无妄。往吉。", "yao_ci_meaning": "自然のままでいなさい。進んでいけば吉。", "changing_line_special_meaning": "作為的なことをせず、自然の流れに身を任せるのが良い時です。素直な気持ちで進みましょう。" },
    { "hexagram_id": 25, "line_position": 2, "yao_ci_text": "六二、不耕穫。不菑畬。則利有攸往。", "yao_ci_meaning": "目先の利益を考えずに、やるべきことをやる。そうすれば、進むべき道が開ける。", "changing_line_special_meaning": "結果を期待せず、無心で物事に取り組みましょう。その純粋な姿勢が、良い結果を引き寄せます。" },
    { "hexagram_id": 25, "line_position": 3, "yao_ci_text": "六三、无妄之災。或繋之牛。行人之得。邑人之災。", "yao_ci_meaning": "予期せぬ災難。牛を繋いでおいたら、旅人に盗まれた。村人にとっては災難だ。", "changing_line_special_meaning": "思いがけないトラブルに巻き込まれる可能性があります。不可抗力なので、冷静に対処するしかありません。" },
    { "hexagram_id": 25, "line_position": 4, "yao_ci_text": "九四、可貞。无咎。", "yao_ci_meaning": "正しくあり続けることができる。問題ない。", "changing_line_special_meaning": "何があっても、誠実で正しい道を守り抜きましょう。その信念が、あなたを守ってくれます。" },
    { "hexagram_id": 25, "line_position": 5, "yao_ci_text": "九五、无妄之疾。勿藥有喜。", "yao_ci_meaning": "予期せぬ病気。薬を使わなくても、自然に治る。", "changing_line_special_meaning": "思いがけない問題が発生しますが、下手に動かず、自然に任せておけば、いつの間にか解決しているでしょう。" },
    { "hexagram_id": 25, "line_position": 6, "yao_ci_text": "上九、无妄。行有眚。无攸利。", "yao_ci_meaning": "自然のままでいるべき時に、行動すると災いがある。何の利益もない。", "changing_line_special_meaning": "今は、何もしないのが最善の策です。無理に行動を起こすと、かえって事態が悪化します。" },

    # 26. 山天大畜 (さんてんたいちく)
    { "hexagram_id": 26, "line_position": 1, "yao_ci_text": "初九、有厲。利已。", "yao_ci_meaning": "危険がある。進むのをやめるのが良い。", "changing_line_special_meaning": "障害があり、前に進むのは危険です。今は無理をせず、力を蓄えることに専念しましょう。" },
    { "hexagram_id": 26, "line_position": 2, "yao_ci_text": "九二、輿説輻。", "yao_ci_meaning": "車の部品が外れる。内部で対立が起こり、進めない。", "changing_line_special_meaning": "内部での意見の対立や、足並みの乱れが原因で、物事が停滞します。まずは、内部の結束を固めましょう。" },
    { "hexagram_id": 26, "line_position": 3, "yao_ci_text": "九三、良馬逐。利艱貞。日閑輿衛。利有攸往。", "yao_ci_meaning": "良い馬が走るように、進む。困難でも正しくあれ。日々訓練を怠らなければ、進むべき道が開ける。", "changing_line_special_meaning": "障害を乗り越え、物事が進み始めます。油断せず、日々の努力を続けることが、さらなる発展に繋がります。" },
    { "hexagram_id": 26, "line_position": 4, "yao_ci_text": "六四、童牛之牿。元吉。", "yao_ci_meaning": "子牛に角当てをするように、早いうちに災いの芽を摘んでおく。大いに吉。", "changing_line_special_meaning": "問題が小さいうちに、早めに対処しておくことが重要です。先手を打つことで、大きな災いを防げます。" },
    { "hexagram_id": 26, "line_position": 5, "yao_ci_text": "六五、豶豕之牙。吉。", "yao_ci_meaning": "去勢された豚の牙のように、危険がなくなった。吉。", "changing_line_special_meaning": "障害や危険が取り除かれ、安心して進める時です。これまでの努力が実を結びます。" },
    { "hexagram_id": 26, "line_position": 6, "yao_ci_text": "上九、何天之衢。亨。", "yao_ci_meaning": "天上の大通りを行くように、妨げるものがない。願いは通る。", "changing_line_special_meaning": "これまでの努力と蓄積が、大きな成果となって現れます。思う存分、その力を発揮してください。" },

    # 27. 山雷頤 (さんらいい)
    { "hexagram_id": 27, "line_position": 1, "yao_ci_text": "初九、舎爾靈龜。觀我朶頤。凶。", "yao_ci_meaning": "自分の霊亀を捨てて、他人の口元を羨ましげに見る。凶。", "changing_line_special_meaning": "自分自身の素晴らしい才能や長所を忘れ、他人を羨ましがってはいけません。自分に与えられたものを大切にしましょう。" },
    { "hexagram_id": 27, "line_position": 2, "yao_ci_text": "六二、顛頤。拂經。于丘頤。征凶。", "yao_ci_meaning": "逆さまに養う。道理に背いて、丘の上から養ってもらおうとする。進めば凶。", "changing_line_special_meaning": "実力のない者に養ってもらおうとしたり、楽して利益を得ようとしたりするのは、間違っています。自立する努力をしましょう。" },
    { "hexagram_id": 27, "line_position": 3, "yao_ci_text": "六三、拂頤。貞凶。十年勿用。无攸利。", "yao_ci_meaning": "養いの道に背く。正しくても凶。十年も用いられない。何の利益もない。", "changing_line_special_meaning": "快楽や欲望に溺れ、本来の目的を見失っています。このままでは、全てを失うことになるでしょう。" },
    { "hexagram_id": 27, "line_position": 4, "yao_ci_text": "六四、顛頤。吉。虎視眈眈。其欲逐逐。无咎。", "yao_ci_meaning": "逆さまに養う。虎が獲物を狙うように、人々のために尽くせば吉。問題ない。", "changing_line_special_meaning": "自分のことよりも、広く社会や人々のために尽くす時です。その奉仕の精神が、幸運を呼び込みます。" },
    { "hexagram_id": 27, "line_position": 5, "yao_ci_text": "六五、拂經。居貞吉。不可渉大川。", "yao_ci_meaning": "道理に背いているが、家にいて正しくしていれば吉。大きな事を始めるのはまだ早い。", "changing_line_special_meaning": "実力はまだ不十分です。今は大きな挑戦は避け、自分の足元を固めることに専念しましょう。" },
    { "hexagram_id": 27, "line_position": 6, "yao_ci_text": "上九、由頤。厲吉。利渉大川。", "yao_ci_meaning": "人々を養う立場になる。危ういが、吉。大きな事を成し遂げられる。", "changing_line_special_meaning": "多くの人々を養い、導く指導者となる時です。責任は重いですが、やりがいのある大きな仕事ができます。" },

    # 28. 沢風大過 (たくふうたいか)
    { "hexagram_id": 28, "line_position": 1, "yao_ci_text": "初六、藉用白茅。无咎。", "yao_ci_meaning": "白い茅を敷くように、慎重に行動する。問題ない。", "changing_line_special_meaning": "非常事態です。何事も、慎重すぎるくらい慎重に進めるべきです。細心の注意を払いましょう。" },
    { "hexagram_id": 28, "line_position": 2, "yao_ci_text": "九二、枯楊生稊。老夫得其女妻。无不利。", "yao_ci_meaning": "枯れた柳から芽が出るように、老夫が若い妻を得る。意外な組み合わせだが、うまくいく。", "changing_line_special_meaning": "一見、不釣り合いに見えることや、意外な組み合わせの中に、問題解決のヒントが隠されています。" },
    { "hexagram_id": 28, "line_position": 3, "yao_ci_text": "九三、棟橈。凶。", "yao_ci_meaning": "棟木がたわむ。凶。重荷に耐えきれず、崩壊寸前。", "changing_line_special_meaning": "限界を超えています。一人で問題を抱え込まず、周りに助けを求めましょう。このままでは、全てがダメになります。" },
    { "hexagram_id": 28, "line_position": 4, "yao_ci_text": "九四、棟隆。吉。有它吝。", "yao_ci_meaning": "棟木が盛り上がり、支えられる。吉。しかし、他のことに関わると後悔する。", "changing_line_special_meaning": "周りの助けを得て、危機を乗り越えることができます。しかし、調子に乗って他の問題に手を出すと、失敗します。" },
    { "hexagram_id": 28, "line_position": 5, "yao_ci_text": "九五、枯楊生華。老婦得其士夫。无咎无譽。", "yao_ci_meaning": "枯れた柳に花が咲くように、老婦が若い夫を得る。問題もないが、名誉もない。", "changing_line_special_meaning": "一時的に状況は持ち直しますが、根本的な解決にはなっていません。一時しのぎの策に過ぎないでしょう。" },
    { "hexagram_id": 28, "line_position": 6, "yao_ci_text": "上六、過渉滅頂。凶。无咎。", "yao_ci_meaning": "水の中を渡ろうとして、頭まで水に浸かる。凶。しかし、自己犠牲の精神であれば、咎められない。", "changing_line_special_meaning": "危険を顧みず、無謀な行動に出ます。失敗は免れませんが、その自己犠牲の精神は、評価されるかもしれません。" },

    # 29. 坎為水 (かんいすい)
    { "hexagram_id": 29, "line_position": 1, "yao_ci_text": "初六、習坎。入于坎窞。凶。", "yao_ci_meaning": "困難に次ぐ困難。穴の中の穴に入る。凶。", "changing_line_special_meaning": "次から次へと困難が訪れ、最悪の状況です。今は、ただ耐え忍ぶしかありません。" },
    { "hexagram_id": 29, "line_position": 2, "yao_ci_text": "九二、坎有險。求小得。", "yao_ci_meaning": "穴の中に危険がある。少しだけなら、得るものがある。", "changing_line_special_meaning": "困難な状況ですが、全てを失うわけではありません。小さな希望を見つけ、それを大切にしましょう。" },
    { "hexagram_id": 29, "line_position": 3, "yao_ci_text": "六三、來之坎坎。險且枕。入于坎窞。勿用。", "yao_ci_meaning": "行くも来るも、穴だらけ。危険で、安心できない。穴の中の穴に入る。何もしない方が良い。", "changing_line_special_meaning": "進むも退くも、困難な状況です。下手に動くと、さらに深みにはまります。今は、何もしないのが一番です。" },
    { "hexagram_id": 29, "line_position": 4, "yao_ci_text": "六四、樽酒簋貳。用缶。納約自牖。終无咎。", "yao_ci_meaning": "質素な酒と食べ物。誠意をもって、窓から差し出す。最終的には問題ない。", "changing_line_special_meaning": "困難な時こそ、誠実な心が試されます。真心をもって人と接すれば、必ず道は開けます。" },
    { "hexagram_id": 29, "line_position": 5, "yao_ci_text": "九五、坎不盈。祗既平。无咎。", "yao_ci_meaning": "穴に水が満ちない。やがて平らになる。問題ない。", "changing_line_special_meaning": "困難な状況は、もうすぐ終わりを告げます。希望の光が見えてきました。あと少しの辛抱です。" },
    { "hexagram_id": 29, "line_position": 6, "yao_ci_text": "上六、係用徽纆。寘于叢棘。三歳不得。凶。", "yao_ci_meaning": "縄で縛られ、いばらの中に置かれる。三年間も抜け出せない。凶。", "changing_line_special_meaning": "自ら招いた過ちによって、身動きが取れない状況に陥ります。この苦しみは、長く続くでしょう。" },

    # 30. 離為火 (りいか)
    { "hexagram_id": 30, "line_position": 1, "yao_ci_text": "初九、履錯然。敬之。无咎。", "yao_ci_meaning": "足元が乱れている。慎重に行動すれば、問題ない。", "changing_line_special_meaning": "浮足立っていて、注意力が散漫になっています。気を引き締め、慎重に行動してください。" },
    { "hexagram_id": 30, "line_position": 2, "yao_ci_text": "六二、黄離。元吉。", "yao_ci_meaning": "黄色い火。中庸の徳があり、大いに吉。", "changing_line_special_meaning": "あなたの知性や才能が、最も良い形で発揮される時です。自信を持って、物事に取り組んでください。" },
    { "hexagram_id": 30, "line_position": 3, "yao_ci_text": "九三、日昃之離。不鼓缶而歌。則大耋之嗟。凶。", "yao_ci_meaning": "夕日のような火。今を楽しめなければ、老人になって嘆くことになる。凶。", "changing_line_special_meaning": "人生の盛りは、あっという間に過ぎ去ります。今という時を大切に、楽しまなければ、後で後悔します。" },
    { "hexagram_id": 30, "line_position": 4, "yao_ci_text": "九四、突如其來如。焚如。死如。棄如。", "yao_ci_meaning": "突然やってきて、燃え尽き、死に、捨てられる。一過性の情熱。", "changing_line_special_meaning": "一時の感情の盛り上がりで、軽率な行動に出てはいけません。その情熱は、すぐに冷めてしまいます。" },
    { "hexagram_id": 30, "line_position": 5, "yao_ci_text": "六五、出涕沱若。戚嗟若。吉。", "yao_ci_meaning": "涙を流し、嘆き悲しむ。謙虚に反省すれば、吉。", "changing_line_special_meaning": "自分の過ちや至らなさを、素直に認めて反省しましょう。その謙虚な姿勢が、事態を好転させます。" },
    { "hexagram_id": 30, "line_position": 6, "yao_ci_text": "上九、王用出征。有嘉。折首。獲匪其醜。无咎。", "yao_ci_meaning": "王が出征する。首領を討ち取り、嘉される。抵抗しない者は許す。問題ない。", "changing_line_special_meaning": "悪の根源を断ち切るべき時です。ただし、関係のない人々を巻き込まないよう、冷静な判断が必要です。" },

    # 31. 沢山咸 (たくざんかん)
    { "hexagram_id": 31, "line_position": 1, "yao_ci_text": "初六、咸其拇。", "yao_ci_meaning": "足の親指に感じる。まだ行動に移す時ではない。", "changing_line_special_meaning": "心が動き始めていますが、まだ行動を起こすのは早すぎます。気持ちを落ち着けて、様子を見ましょう。" },
    { "hexagram_id": 31, "line_position": 2, "yao_ci_text": "六二、咸其腓。凶。居吉。", "yao_ci_meaning": "ふくらはぎに感じる。凶。じっとしていれば吉。", "changing_line_special_meaning": "そわそわして、落ち着きがありません。軽率に行動すると、失敗します。今は、じっとしているのが一番です。" },
    { "hexagram_id": 31, "line_position": 3, "yao_ci_text": "九三、咸其股。執其隨。往吝。", "yao_ci_meaning": "太ももに感じる。人に従おうとするが、進めば後悔する。", "changing_line_special_meaning": "感情に流されて、軽々しく人に従うべきではありません。自分の意志をしっかり持ちましょう。" },
    { "hexagram_id": 31, "line_position": 4, "yao_ci_text": "九四、貞吉。悔亡。憧憧往來。朋從爾思。", "yao_ci_meaning": "正しくしていれば吉。後悔はなくなる。心が揺れ動いても、仲間はあなたの思いに従う。", "changing_line_special_meaning": "迷いや不安があっても、正しい道を進み続ければ、必ず周りの人はあなたを理解し、ついてきてくれます。" },
    { "hexagram_id": 31, "line_position": 5, "yao_ci_text": "九五、咸其脢。无悔。", "yao_ci_meaning": "背中の肉に感じる。後悔はない。", "changing_line_special_meaning": "言葉ではなく、心で感じ、行動する時です。小手先のテクニックは通用しません。誠意が大切です。" },
    { "hexagram_id": 31, "line_position": 6, "yao_ci_text": "上六、咸其輔頰舌。", "yao_ci_meaning": "あご、頬、舌に感じる。口先だけの感応。", "changing_line_special_meaning": "口先だけで、調子の良いことばかりを言ってはいけません。言葉に行動が伴わなければ、誰からも信用されません。" },

    # 32. 雷風恒 (らいふうこう)
    { "hexagram_id": 32, "line_position": 1, "yao_ci_text": "初六、浚恒。貞凶。无攸利。", "yao_ci_meaning": "深く、長く続けようとしすぎる。正しくても凶。何の利益もない。", "changing_line_special_meaning": "最初から、あまりにも高すぎる目標を立ててはいけません。長続きせず、挫折してしまいます。" },
    { "hexagram_id": 32, "line_position": 2, "yao_ci_text": "九二、悔亡。", "yao_ci_meaning": "後悔はない。", "changing_line_special_meaning": "自分の能力をわきまえ、分相応の道を歩んでいるので、後悔することはありません。現状維持で順調です。" },
    { "hexagram_id": 32, "line_position": 3, "yao_ci_text": "九三、不恒其徳。或承之羞。貞吝。", "yao_ci_meaning": "徳を長く保てない。恥をかくことになる。正しくいても後悔する。", "changing_line_special_meaning": "気分にムラがあり、一貫性がありません。その日の気分で態度を変えていると、信用を失います。" },
    { "hexagram_id": 32, "line_position": 4, "yao_ci_text": "九四、田无禽。", "yao_ci_meaning": "狩りに行っても、獲物がいない。自分のいるべき場所を間違えている。", "changing_line_special_meaning": "あなたの能力や才能が、今の場所では活かされていません。自分に合った環境を探すべきです。" },
    { "hexagram_id": 32, "line_position": 5, "yao_ci_text": "六五、恒其徳。貞。婦人吉。夫子凶。", "yao_ci_meaning": "徳を長く保つ。女性は吉。男性は、人の意見を聞き入れないと凶。", "changing_line_special_meaning": "自分のやり方に固執せず、人の意見に耳を傾ける柔軟さが必要です。特に男性は、頑固になりがちなので注意。" },
    { "hexagram_id": 32, "line_position": 6, "yao_ci_text": "上六、振恒。凶。", "yao_ci_meaning": "絶えず動き回り、落ち着きがない。凶。", "changing_line_special_meaning": "一つのことに集中できず、落ち着きがありません。腰を据えて、じっくりと物事に取り組むべきです。" },

    # 33. 天山遯 (てんざんとん)
    { "hexagram_id": 33, "line_position": 1, "yao_ci_text": "初六、遯尾。厲。勿用有攸往。", "yao_ci_meaning": "退き逃れるのが遅れる。危険。進んではいけない。", "changing_line_special_meaning": "逃げ遅れて、危険な状況に陥ります。今は、とにかく身を守ることを最優先に考えてください。" },
    { "hexagram_id": 33, "line_position": 2, "yao_ci_text": "六二、執之用黄牛之革。莫之勝説。", "yao_ci_meaning": "黄色い牛の革で固く縛られる。誰も引き離すことはできない。", "changing_line_special_meaning": "しがらみに縛られ、身動きが取れません。今は、無理に動こうとせず、状況を受け入れるしかありません。" },
    { "hexagram_id": 33, "line_position": 3, "yao_ci_text": "九三、係遯。有疾厲。畜臣妾吉。", "yao_ci_meaning": "心惹かれるものがあり、逃れられない。病気のように危うい。部下や目下を養うなら吉。", "changing_line_special_meaning": "情にほだされて、退くべき時に退けません。私情を捨て、自分のやるべきことに集中しましょう。" },
    { "hexagram_id": 33, "line_position": 4, "yao_ci_text": "九四、好遯。君子吉。小人否。", "yao_ci_meaning": "好んで退き隠れる。君子は吉だが、小人はできない。", "changing_line_special_meaning": "俗世間のしがらみから、きっぱりと身を引くことができます。君子にとっては良いことですが、凡人には難しい決断です。" },
    { "hexagram_id": 33, "line_position": 5, "yao_ci_text": "九五、嘉遯。貞吉。", "yao_ci_meaning": "見事に退き隠れる。正しくしていれば吉。", "changing_line_special_meaning": "惜しまれながらも、美しい引き際で、その場を去ることができます。あなたの評価は、かえって高まるでしょう。" },
    { "hexagram_id": 33, "line_position": 6, "yao_ci_text": "上九、肥遯。无不利。", "yao_ci_meaning": "ゆったりと退き隠れる。何事もうまくいく。", "changing_line_special_meaning": "全てのしがらみから解放され、心穏やかに、悠々自適の生活を送ることができます。" },

    # 34. 雷天大壮 (らいてんたいそう)
    { "hexagram_id": 34, "line_position": 1, "yao_ci_text": "初九、壮于趾。征凶。有孚。", "yao_ci_meaning": "足に力が入りすぎる。進めば凶。誠意はあるのだが。", "changing_line_special_meaning": "やる気が空回りしています。勢いだけで進むと、必ず失敗します。まずは、冷静に計画を立てましょう。" },
    { "hexagram_id": 34, "line_position": 2, "yao_ci_text": "九二、貞吉。", "yao_ci_meaning": "正しくしていれば吉。", "changing_line_special_meaning": "力強く、安定した運気です。勢いに任せて暴走せず、正しい道を進むことを心がければ、うまくいきます。" },
    { "hexagram_id": 34, "line_position": 3, "yao_ci_text": "九三、小人用壮。君子用罔。貞厲。羝羊觸藩。羸其角。", "yao_ci_meaning": "小人は力を用い、君子は力を用いない。危うい。雄羊が垣根に角を引っ掛ける。", "changing_line_special_meaning": "力を過信し、無謀な行動に出てはいけません。自分の力を誇示しようとすると、かえって窮地に陥ります。" },
    { "hexagram_id": 34, "line_position": 4, "yao_ci_text": "九四、貞吉。悔亡。藩決不羸。壮于大輿之輹。", "yao_ci_meaning": "正しくしていれば吉。後悔はなくなる。垣根が壊れて、角が抜ける。大きな車の部品のように、力が発揮される。", "changing_line_special_meaning": "障害が取り除かれ、あなたの力が、いよいよ発揮される時です。これまでの努力が報われます。" },
    { "hexagram_id": 34, "line_position": 5, "yao_ci_text": "六五、喪羊于易。无悔。", "yao_ci_meaning": "たやすく羊を失う。後悔はない。", "changing_line_special_meaning": "力を失い、勢いがなくなりますが、それによって、かえって心穏やかになれます。執着を捨てることで、楽になれるでしょう。" },
    { "hexagram_id": 34, "line_position": 6, "yao_ci_text": "上六、羝羊觸藩。不能退。不能遂。无攸利。艱則吉。", "yao_ci_meaning": "雄羊が垣根に角を引っ掛け、退くことも進むこともできない。困難を覚悟すれば、吉。", "changing_line_special_meaning": "進退窮まり、どうしようもない状況です。ジタバタせず、腹をくくって、この困難な状況を受け入れましょう。" },

    # 35. 火地晋 (かちしん)
    { "hexagram_id": 35, "line_position": 1, "yao_ci_text": "初六、晋如摧如。貞吉。罔孚。裕无咎。", "yao_ci_meaning": "進もうとするが、妨げられる。正しくしていれば吉。信じられなくても、悠然としていれば問題ない。", "changing_line_special_meaning": "最初は障害が多く、なかなか前に進めません。周りに理解されなくても、焦らず、悠然と構えていましょう。" },
    { "hexagram_id": 35, "line_position": 2, "yao_ci_text": "六二、晋如愁如。貞吉。受茲介福。于其王母。", "yao_ci_meaning": "進もうとするが、憂いがある。正しくしていれば吉。大きな福を、王母から授かる。", "changing_line_special_meaning": "不安や心配事がありますが、誠実に行動すれば、目上の女性から、大きな引き立てを受けられます。" },
    { "hexagram_id": 35, "line_position": 3, "yao_ci_text": "六三、衆允。悔亡。", "yao_ci_meaning": "多くの人々から信頼される。後悔はない。", "changing_line_special_meaning": "あなたの誠実な人柄が、多くの人々から信頼されます。自信を持って、リーダーシップを発揮してください。" },
    { "hexagram_id": 35, "line_position": 4, "yao_ci_text": "九四、晋如鼫鼠。貞厲。", "yao_ci_meaning": "もぐらのように、こそこそと進む。正しくいても危うい。", "changing_line_special_meaning": "不正な手段で、利益を得ようとしてはいけません。たとえうまくいったとしても、必ず後でしっぺ返しを食らいます。" },
    { "hexagram_id": 35, "line_position": 5, "yao_ci_text": "六五、悔亡。失得勿恤。往吉。无不利。", "yao_ci_meaning": "後悔はない。損得を気にせず、進んでいけば吉。何事もうまくいく。", "changing_line_special_meaning": "目先の損得勘定で、一喜一憂してはいけません。大局的な視点に立って、自信を持って進みましょう。" },
    { "hexagram_id": 35, "line_position": 6, "yao_ci_text": "上九、晋其角。維用伐邑。厲吉无咎。貞吝。", "yao_ci_meaning": "角で進むように、強引に進む。内輪の不正を正すなら、危ういが吉。やり過ぎると後悔する。", "changing_line_special_meaning": "強引な手段も、時には必要です。ただし、それは内部の規律を正すためなど、正当な理由がある場合に限ります。" },

    # 36. 地火明夷 (ちかめいい)
    { "hexagram_id": 36, "line_position": 1, "yao_ci_text": "初九、明夷于飛。垂其翼。君子于行。三日不食。有攸往。主人有言。", "yao_ci_meaning": "飛びながら、明知が傷つけられる。翼を垂れて、難を避ける。君子は三日も食べずに逃げる。非難される。", "changing_line_special_meaning": "困難な状況から、いち早く逃れるべきです。周りから非難されても、今は身の安全を確保することが最優先です。" },
    { "hexagram_id": 36, "line_position": 2, "yao_ci_text": "六二、明夷。夷于左股。用拯馬壯。吉。", "yao_ci_meaning": "明知が傷つけられる。左股を傷つける。屈強な馬に助けられ、吉。", "changing_line_special_meaning": "困難な状況ですが、信頼できる助け手のおかげで、危機を脱することができます。感謝の気持ちを忘れずに。" },
    { "hexagram_id": 36, "line_position": 3, "yao_ci_text": "九三、明夷于南狩。得其大首。不可疾貞。", "yao_ci_meaning": "南に狩りをして、悪の首領を捕らえる。急いで改革しようとしてはいけない。", "changing_line_special_meaning": "問題の根本原因を突き止め、解決することができます。しかし、焦りは禁物です。時間をかけて、着実に改革を進めましょう。" },
    { "hexagram_id": 36, "line_position": 4, "yao_ci_text": "六四、入于左腹。獲明夷之心。于出門庭。", "yao_ci_meaning": "敵の懐深く入り込み、その本心を知る。そして、無事に脱出する。", "changing_line_special_meaning": "困難な状況の、まさに中心部に入り込みますが、そこで問題の本質を理解し、うまく立ち回ることができます。" },
    { "hexagram_id": 36, "line_position": 5, "yao_ci_text": "六五、箕子之明夷。利貞。", "yao_ci_meaning": "箕子のように、才能を隠し、愚か者のふりをする。正しくしていれば良い。", "changing_line_special_meaning": "今は、自分の才能や能力を隠し、目立たないようにしているのが賢明です。能ある鷹は爪を隠す、です。" },
    { "hexagram_id": 36, "line_position": 6, "yao_ci_text": "上六、不明晦。初登于天。後入于地。", "yao_ci_meaning": "光なく、暗い。最初は天に登るが、最後は地に落ちる。", "changing_line_special_meaning": "悪事が露見し、破滅します。最初はうまくいっているように見えても、最後には、全てを失うでしょう。" },

    # 37. 風火家人 (ふうかかじん)
    { "hexagram_id": 37, "line_position": 1, "yao_ci_text": "初九、閑有家。悔亡。", "yao_ci_meaning": "家をきちんと治める。後悔はない。", "changing_line_special_meaning": "まずは、自分の家庭や、身近なコミュニティのルールをしっかりと定め、秩序を保つことが大切です。" },
    { "hexagram_id": 37, "line_position": 2, "yao_ci_text": "六二、无攸遂。在中饋。貞吉。", "yao_ci_meaning": "自分の意志を押し通さず、家事やサポート役に徹する。正しくしていれば吉。", "changing_line_special_meaning": "自己主張を控え、縁の下の力持ちとして、周りの人をサポートする役割に徹しましょう。それが、全体の調和に繋がります。" },
    { "hexagram_id": 37, "line_position": 3, "yao_ci_text": "九三、家人嗃嗃。悔厲吉。婦子嘻嘻。終吝。", "yao_ci_meaning": "家族に厳しくしすぎる。後悔するが、最終的には吉。甘やかすと、後で後悔する。", "changing_line_special_meaning": "家庭や組織内の規律が緩んでいます。なあなあにせず、時には厳しく接することも必要です。" },
    { "hexagram_id": 37, "line_position": 4, "yao_ci_text": "六四、富家。大吉。", "yao_ci_meaning": "家を豊かにする。大いに吉。", "changing_line_special_meaning": "あなたの努力によって、家庭や組織は、物質的にも精神的にも、豊かになります。素晴らしいことです。" },
    { "hexagram_id": 37, "line_position": 5, "yao_ci_text": "九五、王假有家。勿恤。吉。", "yao_ci_meaning": "王が家を治めるように、人々を愛する。心配いらない。吉。", "changing_line_special_meaning": "リーダーとして、人々を愛し、信頼することが大切です。その真心は、必ず人々に伝わります。" },
    { "hexagram_id": 37, "line_position": 6, "yao_ci_text": "上九、有孚威如。終吉。", "yao_ci_meaning": "誠実で、威厳がある。最終的には吉。", "changing_line_special_meaning": "自分自身を厳しく律し、手本を示すことで、周りの人々も、自然とあなたについてきます。威厳と信頼を得るでしょう。" },

    # 38. 火沢睽 (かたくけい)
    { "hexagram_id": 38, "line_position": 1, "yao_ci_text": "初九、悔亡。喪馬勿逐。自復。見惡人。无咎。", "yao_ci_meaning": "後悔はない。馬がいなくなっても、追わずにいれば、自然に帰ってくる。悪人に会っても、問題ない。", "changing_line_special_meaning": "対立や誤解があっても、焦ってはいけません。冷静に、自然の流れに任せていれば、事態は好転します。" },
    { "hexagram_id": 38, "line_position": 2, "yao_ci_text": "九二、遇主于巷。无咎。", "yao_ci_meaning": "路地で主人に偶然会う。問題ない。", "changing_line_special_meaning": "対立している相手と、思いがけない場所で、ばったり会うかもしれません。しかし、それは和解のきっかけになります。" },
    { "hexagram_id": 38, "line_position": 3, "yao_ci_text": "六三、見輿曳。其牛掣。其人天且劓。无初有終。", "yao_ci_meaning": "車が進まず、牛も動かない。罪人のように、ひどい目に遭う。最初はダメだが、最後はうまくいく。", "changing_line_special_meaning": "疑心暗鬼に陥り、最悪の状況です。しかし、これを乗り越えれば、最終的には良い結果が待っています。" },
    { "hexagram_id": 38, "line_position": 4, "yao_ci_text": "九四、睽孤。遇元夫。交孚。厲无咎。", "yao_ci_meaning": "孤独で、孤立している。誠実な人に出会い、心を通わせる。危ういが、問題ない。", "changing_line_special_meaning": "孤立無援の状況ですが、誠実な協力者との出会いによって、道が開けます。信頼関係を大切に。" },
    { "hexagram_id": 38, "line_position": 5, "yao_ci_text": "六五、悔亡。厥宗噬膚。往何咎。", "yao_ci_meaning": "後悔はない。仲間が助けてくれる。進んでいけば、問題ない。", "changing_line_special_meaning": "対立が解消され、和解の時です。信頼できる仲間と共に、協力して進んでいきましょう。" },
    { "hexagram_id": 38, "line_position": 6, "yao_ci_text": "上九、睽孤。見豕負塗。載鬼一車。先張之弧。後説之弧。匪寇婚媾。往遇雨則吉。", "yao_ci_meaning": "孤独で、疑心暗鬼。泥だらけの豚や、鬼の車を見る。最初は弓を張るが、後で解く。敵ではなく、助け手。雨が降れば吉。", "changing_line_special_meaning": "疑いの心が晴れ、誤解が解ける時です。最初は敵だと思っていた相手が、実は味方だとわかります。" },

    # 39. 水山蹇 (すいざんけん)
    { "hexagram_id": 39, "line_position": 1, "yao_ci_text": "初六、往蹇來譽。", "yao_ci_meaning": "進めば困難、留まれば名誉。", "changing_line_special_meaning": "今は、無理に進むべき時ではありません。動かずに、静かにしているのが賢明です。" },
    { "hexagram_id": 39, "line_position": 2, "yao_ci_text": "六二、王臣蹇蹇。匪躬之故。", "yao_ci_meaning": "王のために、困難に次ぐ困難に立ち向かう。自分のためではない。", "changing_line_special_meaning": "自分の利益のためではなく、公のため、人のために、困難な役割を引き受けることになります。" },
    { "hexagram_id": 39, "line_position": 3, "yao_ci_text": "九三、往蹇來反。", "yao_ci_meaning": "進めば困難。引き返すべき。", "changing_line_special_meaning": "このまま進むのは、無謀です。勇気を持って、引き返す決断をしてください。" },
    { "hexagram_id": 39, "line_position": 4, "yao_ci_text": "六四、往蹇來連。", "yao_ci_meaning": "進めば困難。仲間と協力すれば、道は開ける。", "changing_line_special_meaning": "一人で悩んでいないで、周りの人と協力しましょう。助け合うことで、困難を乗り越えられます。" },
    { "hexagram_id": 39, "line_position": 5, "yao_ci_text": "九五、大蹇朋來。", "yao_ci_meaning": "大きな困難の中に、仲間が助けに来る。", "changing_line_special_meaning": "非常に困難な状況ですが、あなたの徳を慕って、多くの協力者が現れます。人との繋がりを大切に。" },
    { "hexagram_id": 39, "line_position": 6, "yao_ci_text": "上六、往蹇來碩。吉。利見大人。", "yao_ci_meaning": "進めば困難。留まれば、大きな成果がある。吉。徳の高い人に会うと良い。", "changing_line_special_meaning": "困難な状況から解放され、大きな成功を収めることができます。賢者の助言を求めると、さらに良いでしょう。" },

    # 40. 雷水解 (らいすいかい)
    { "hexagram_id": 40, "line_position": 1, "yao_ci_text": "初六、无咎。", "yao_ci_meaning": "問題ない。", "changing_line_special_meaning": "困難な状況が、解決に向かい始めました。静かに、事態の好転を待ちましょう。" },
    { "hexagram_id": 40, "line_position": 2, "yao_ci_text": "九二、田獲三狐。得黄矢。貞吉。", "yao_ci_meaning": "狩りで三匹の狐を捕らえ、黄金の矢を得る。正しくしていれば吉。", "changing_line_special_meaning": "邪魔なものや、不正を排除することができます。誠実に行動すれば、良い結果に繋がります。" },
    { "hexagram_id": 40, "line_position": 3, "yao_ci_text": "六三、負且乘。致寇至。貞吝。", "yao_ci_meaning": "荷物を背負いながら、車に乗る。分不相応なことをして、敵を招く。正しくいても後悔する。", "changing_line_special_meaning": "自分の実力以上の地位や富を求めると、嫉妬を買い、トラブルを招きます。分相応を心がけましょう。" },
    { "hexagram_id": 40, "line_position": 4, "yao_ci_text": "九四、解而拇。朋至斯孚。", "yao_ci_meaning": "足の親指を解き放つように、悪縁を断ち切る。そうすれば、信頼できる仲間が現れる。", "changing_line_special_meaning": "あなたにとって、良くない影響を与える人々との関係を、思い切って断ち切りましょう。そうすれば、新しい良い出会いがあります。" },
    { "hexagram_id": 40, "line_position": 5, "yao_ci_text": "六五、君子維有解。吉。有孚于小人。", "yao_ci_meaning": "君子が自ら解き放つ。吉。小人にも、誠意をもって接する。", "changing_line_special_meaning": "リーダーとして、自ら模範を示し、問題を解決する時です。分け隔てなく、誠実に人々と接しましょう。" },
    { "hexagram_id": 40, "line_position": 6, "yao_ci_text": "上六、公用射隼于高墉之上。獲之。无不利。", "yao_ci_meaning": "公が高い城壁の上の隼を射る。見事に仕留める。何事もうまくいく。", "changing_line_special_meaning": "困難な問題の、まさに元凶となっているものを、見事に取り除くことができます。あなたの手腕が高く評価されるでしょう。" },

    # 41. 山沢損 (さんたくそん)
    { "hexagram_id": 41, "line_position": 1, "yao_ci_text": "初九、已事遄往。无咎。酌損之。", "yao_ci_meaning": "自分の事を後回しにして、人のために尽くす。問題ない。ただし、やり過ぎないように。", "changing_line_special_meaning": "人のために、自己犠牲を払う時です。ただし、自分のことを、あまりにも疎かにしすぎないように、バランスが大切です。" },
    { "hexagram_id": 41, "line_position": 2, "yao_ci_text": "九二、利貞。征凶。弗損益之。", "yao_ci_meaning": "正しくしているのが良い。進めば凶。人を損なわず、自分に益する。", "changing_line_special_meaning": "無理に進むのはやめ、現状維持に努めましょう。人を助けることで、巡り巡って、自分自身が助けられます。" },
    { "hexagram_id": 41, "line_position": 3, "yao_ci_text": "六三、三人行。則損一人。一人行。則得其友。", "yao_ci_meaning": "三人が行けば、一人が損をする。一人が行けば、友を得る。", "changing_line_special_meaning": "複雑な人間関係は、トラブルの元です。単独行動をするか、本当に信頼できる人とだけ、行動を共にしましょう。" },
    { "hexagram_id": 41, "line_position": 4, "yao_ci_text": "六四、損其疾。使遄有喜。无咎。", "yao_ci_meaning": "自分の欠点を改める。そうすれば、すぐに喜びがある。問題ない。", "changing_line_special_meaning": "自分の悪いところや、欠点を、素直に認めて改めましょう。そうすれば、事態はすぐに好転します。" },
    { "hexagram_id": 41, "line_position": 5, "yao_ci_text": "六五、或益之。十朋之龜。弗克違。元吉。", "yao_ci_meaning": "大きな利益を得る。高価な亀の甲羅の占いも、これに逆らえない。大いに吉。", "changing_line_special_meaning": "これまでの誠実な行いが、大きな幸運となって、あなたに返ってきます。素晴らしい幸運期です。" },
    { "hexagram_id": 41, "line_position": 6, "yao_ci_text": "上九、弗損益之。无咎。貞吉。利有攸往。得臣无家。", "yao_ci_meaning": "もはや損なうことなく、人に益を与える。問題ない。正しくしていれば吉。多くの部下を得る。", "changing_line_special_meaning": "自己犠牲の段階は終わり、多くの人々に、利益や幸福を与える指導者となります。多くの人々が、あなたを慕って集まってくるでしょう。" },

    # 42. 風雷益 (ふうらいえき)
    { "hexagram_id": 42, "line_position": 1, "yao_ci_text": "初九、利用爲大作。元吉。无咎。", "yao_ci_meaning": "大きな事業を始めるのに良い。大いに吉。問題ない。", "changing_line_special_meaning": "新しいことを始める、絶好のチャンスです。思い切って、大きな目標に挑戦してみましょう。" },
    { "hexagram_id": 42, "line_position": 2, "yao_ci_text": "六二、或益之。十朋之龜。弗克違。永貞吉。王用享于帝。吉。", "yao_ci_meaning": "大きな利益を得る。高価な亀の甲羅の占いも、これに逆らえない。長く正しくしていれば吉。王が天帝を祀るように、感謝すれば吉。", "changing_line_special_meaning": "予期せぬ大きな幸運に恵まれます。この幸運に驕らず、感謝の気持ちを忘れなければ、長く続きます。" },
    { "hexagram_id": 42, "line_position": 3, "yao_ci_text": "六三、益之用凶事。无咎。有孚中行。告公用圭。", "yao_ci_meaning": "災害などの凶事に、自分の富を役立てる。問題ない。誠意をもって、公に尽くす。", "changing_line_special_meaning": "自分が得た利益を、社会や困っている人々のために役立てるべき時です。その善意が、さらなる幸運を呼び込みます。" },
    { "hexagram_id": 42, "line_position": 4, "yao_ci_text": "六四、中行。告公從。利用爲依遷國。", "yao_ci_meaning": "中庸の道を行く。公に告げて、従わせる。国を移すような、大きな計画にも良い。", "changing_line_special_meaning": "あなたの公平で、誠実な態度は、多くの人々の信頼を得ます。リーダーとして、大きなプロジェクトを成功させることができます。" },
    { "hexagram_id": 42, "line_position": 5, "yao_ci_text": "九五、有孚惠心。勿問元吉。有孚惠我徳。", "yao_ci_meaning": "誠意をもって、人々に恵みを与える。問うまでもなく、大いに吉。人々は、私の徳を信頼する。", "changing_line_special_meaning": "見返りを求めず、人々に愛情や恩恵を与えましょう。その無私の精神が、多くの人々から、深く尊敬されます。" },
    { "hexagram_id": 42, "line_position": 6, "yao_ci_text": "上九、莫益之。或擊之。立心勿恒。凶。", "yao_ci_meaning": "誰も、彼に利益を与えない。かえって、彼を攻撃する。心が定まらず、凶。", "changing_line_special_meaning": "強欲で、自分の利益ばかりを追求していると、周りの人々から、総スカンを食らいます。貪欲な心は、身を滅ぼします。" },

    # 43. 沢天夬 (たくてんかい)
    { "hexagram_id": 43, "line_position": 1, "yao_ci_text": "初九、壮于前趾。往不勝。爲咎。", "yao_ci_meaning": "足先に力が入りすぎる。進んでも勝てない。問題となる。", "changing_line_special_meaning": "力不足なのに、焦って前に進もうとしています。準備が整うまで、待つのが賢明です。" },
    { "hexagram_id": 43, "line_position": 2, "yao_ci_text": "九二、惕號。莫夜有戎。勿恤。", "yao_ci_meaning": "警戒して、叫ぶ。夜中に敵が来ても、心配いらない。", "changing_line_special_meaning": "常に警戒を怠らず、備えを万全にしておけば、不測の事態が起きても、冷静に対処できます。" },
    { "hexagram_id": 43, "line_position": 3, "yao_ci_text": "九三、壮于頄。有凶。君子夬夬。獨行遇雨。若濡有慍。无咎。", "yao_ci_meaning": "頬骨に力が入る。凶。君子は断固として、一人で行く。雨に濡れて、不満があっても、問題ない。", "changing_line_special_meaning": "周りの反対を押し切って、断固たる決意で、自分の道を進むべき時です。孤立しても、やり遂げなければなりません。" },
    { "hexagram_id": 43, "line_position": 4, "yao_ci_text": "九四、臀无膚。其行次且。牽羊悔亡。聞言不信。", "yao_ci_meaning": "尻に肉がなく、歩きにくい。羊に引かれるように、素直に従えば、後悔はない。忠告を聞き入れない。", "changing_line_special_meaning": "意地を張って、人の忠告を聞き入れません。頑固な態度は、あなたの立場を、ますます悪くするだけです。" },
    { "hexagram_id": 43, "line_position": 5, "yao_ci_text": "九五、莧陸夬夬。中行无咎。", "yao_ci_meaning": "雑草を抜き去るように、決然と処理する。中庸の道を行けば、問題ない。", "changing_line_special_meaning": "悪の根を、断固たる態度で、抜き去るべき時です。ただし、やり過ぎないように、冷静な判断が必要です。" },
    { "hexagram_id": 43, "line_position": 6, "yao_ci_text": "上六、无號。終有凶。", "yao_ci_meaning": "叫び声もない。最終的には、凶となる。", "changing_line_special_meaning": "悪が滅び去った後、油断していると、また新たな災いが忍び寄ります。最後まで、気を抜いてはいけません。" },

    # 44. 天風姤 (てんぷうこう)
    { "hexagram_id": 44, "line_position": 1, "yao_ci_text": "初六、繋于金柅。貞吉。有攸往。見凶。羸豕孚蹢躅。", "yao_ci_meaning": "金の車止めに繋ぐ。正しくしていれば吉。進めば凶。痩せた豚が、暴れ回る。", "changing_line_special_meaning": "悪しき誘惑や、良くない出会いの兆しがあります。関わらないように、しっかりと自制することが大切です。" },
    { "hexagram_id": 44, "line_position": 2, "yao_ci_text": "九二、包有魚。无咎。不利賓。", "yao_ci_meaning": "魚を包み隠す。問題ない。客には、見せない方が良い。", "changing_line_special_meaning": "問題の芽を、内々で処理することができます。事を荒立てず、穏便に済ませるのが良いでしょう。" },
    { "hexagram_id": 44, "line_position": 3, "yao_ci_text": "九三、臀无膚。其行次且。厲无大咎。", "yao_ci_meaning": "尻に肉がなく、歩きにくい。危ういが、大きな問題はない。", "changing_line_special_meaning": "誘惑に心が揺れ動き、落ち着きません。危険な状況ですが、何とか、一線を越えずに踏みとどまれます。" },
    { "hexagram_id": 44, "line_position": 4, "yao_ci_text": "九四、包无魚。起凶。", "yao_ci_meaning": "魚がいない。凶事が起こる。", "changing_line_special_meaning": "周りの人々から、孤立してしまいます。あなたの周りから、人が去っていくでしょう。" },
    { "hexagram_id": 44, "line_position": 5, "yao_ci_text": "九五、以杞包瓜。含章。有隕自天。", "yao_ci_meaning": "杞の木で瓜を包むように、才能を隠す。天から、思わぬ幸運が舞い降りる。", "changing_line_special_meaning": "自分の才能や美点を、ひけらかさないでください。その謙虚な姿勢が、かえって、大きな幸運を引き寄せます。" },
    { "hexagram_id": 44, "line_position": 6, "yao_ci_text": "上九、姤其角。吝。无咎。", "yao_ci_meaning": "角で出会う。孤高を保ち、人と交わらない。後悔するが、問題はない。", "changing_line_special_meaning": "悪しきものとの関わりを、きっぱりと断ち切ることができます。孤立しますが、災いを避けることができます。" },

    # 45. 沢地萃 (たくちすい)
    { "hexagram_id": 45, "line_position": 1, "yao_ci_text": "初六、有孚不終。乃亂乃萃。若號。一握爲笑。勿恤。往无咎。", "yao_ci_meaning": "誠意が長続きせず、混乱する。しかし、助けを求めれば、すぐに味方が現れる。心配いらない。進んで問題ない。", "changing_line_special_meaning": "最初は混乱しますが、素直に助けを求めれば、すぐに支援者が現れ、事態は好転します。" },
    { "hexagram_id": 45, "line_position": 2, "yao_ci_text": "六二、引吉。无咎。孚乃利用禴。", "yao_ci_meaning": "引き立てられて、吉。問題ない。誠意があれば、質素な祭りでも良い。", "changing_line_special_meaning": "誠実な人柄が認められ、良い方向へと導かれます。真心が、何よりも大切です。" },
    { "hexagram_id": 45, "line_position": 3, "yao_ci_text": "六三、萃如嗟如。无攸利。往无咎。小吝。", "yao_ci_meaning": "集まろうとするが、嘆き悲しむ。何の利益もない。しかし、進んでいけば、問題はない。少し後悔する。", "changing_line_special_meaning": "仲間外れにされ、孤立してしまいます。しかし、嘆いていないで、自分から心を開いていけば、道は開けます。" },
    { "hexagram_id": 45, "line_position": 4, "yao_ci_text": "九四、大吉。无咎。", "yao_ci_meaning": "大いに吉。問題ない。", "changing_line_special_meaning": "リーダーとして、多くの人々をまとめる役割を担います。その重責を、見事に果たすことができるでしょう。" },
    { "hexagram_id": 45, "line_position": 5, "yao_ci_text": "九五、萃有位。无咎。匪孚。元永貞。悔亡。", "yao_ci_meaning": "人々が集まる中心的な地位にいる。問題ない。人望だけではない。根本的な徳があれば、後悔はない。", "changing_line_special_meaning": "あなたは、人々が集まる中心にいます。人気だけでなく、確固たる実力と徳を身につけることで、その地位は盤石になります。" },
    { "hexagram_id": 45, "line_position": 6, "yao_ci_text": "上六、齎咨涕洟。无咎。", "yao_ci_meaning": "嘆き悲しみ、涙を流す。しかし、問題はない。", "changing_line_special_meaning": "人々のために、心を痛め、涙を流す。その深い愛情と、自己犠牲の精神は、咎められるものではありません。" },

    # 46. 地風升 (ちふうしょう)
    { "hexagram_id": 46, "line_position": 1, "yao_ci_text": "初六、允升。大吉。", "yao_ci_meaning": "順調に昇っていく。大いに吉。", "changing_line_special_meaning": "目上の人の引き立てを受け、物事は、とんとん拍子に進みます。絶好のスタートです。" },
    { "hexagram_id": 46, "line_position": 2, "yao_ci_text": "九二、孚乃利用禴。无咎。", "yao_ci_meaning": "誠意があれば、質素な祭りでも良い。問題ない。", "changing_line_special_meaning": "実力は、まだ少し足りませんが、誠実な人柄が、それを補ってくれます。真心をもって、物事にあたりましょう。" },
    { "hexagram_id": 46, "line_position": 3, "yao_ci_text": "九三、升虚邑。", "yao_ci_meaning": "何もない村を昇っていくように、妨げるものがない。", "changing_line_special_meaning": "何の障害もなく、スムーズに、物事が進展していきます。安心して、前に進んでください。" },
    { "hexagram_id": 46, "line_position": 4, "yao_ci_text": "六四、王用亨于岐山。吉无咎。", "yao_ci_meaning": "王が岐山で祭祀を行う。吉であり、問題ない。", "changing_line_special_meaning": "あなたのこれまでの努力が、神仏に通じ、認められる時です。感謝の気持ちを忘れずに。" },
    { "hexagram_id": 46, "line_position": 5, "yao_ci_text": "六五、貞吉。升階。", "yao_ci_meaning": "正しくしていれば吉。階段を昇るように、着実に昇進する。", "changing_line_special_meaning": "焦らず、一歩一歩、着実に進んでいきましょう。その地道な努力が、確実な成功へと繋がります。" },
    { "hexagram_id": 46, "line_position": 6, "yao_ci_text": "上六、冥升。利于不息之貞。", "yao_ci_meaning": "暗闇の中を昇っていく。絶え間なく、努力し続けることが大切。", "changing_line_special_meaning": "目標を見失い、がむしゃらに、努力を続けています。一度立ち止まり、自分の進むべき方向を、再確認しましょう。" },

    # 47. 沢水困 (たくすいこん)
    { "hexagram_id": 47, "line_position": 1, "yao_ci_text": "初六、臀困于株木。入于幽谷。三歳不覿。", "yao_ci_meaning": "切り株に座り込み、動けない。暗い谷に入り、三年間も、誰にも会えない。", "changing_line_special_meaning": "八方塞がりで、どうしようもない状況です。今は、ただ、ひたすら耐え忍ぶしかありません。" },
    { "hexagram_id": 47, "line_position": 2, "yao_ci_text": "九二、困于酒食。朱紱方來。利用亨祀。征凶。无咎。", "yao_ci_meaning": "酒食に困窮する。高官が助けに来る。祭祀を行うと良い。進めば凶。問題ない。", "changing_line_special_meaning": "生活に困窮しますが、目上の人からの助けがあります。感謝の気持ちを忘れず、今は、静かにしているのが良いでしょう。" },
    { "hexagram_id": 47, "line_position": 3, "yao_ci_text": "六三、困于石。據于蒺藜。入于其宮。不見其妻。凶。", "yao_ci_meaning": "石に阻まれ、いばらに囲まれる。家に帰っても、妻がいない。凶。", "changing_line_special_meaning": "次から次へと、困難が襲いかかり、安らげる場所がありません。非常に、苦しい状況です。" },
    { "hexagram_id": 47, "line_position": 4, "yao_ci_text": "九四、來徐徐。困于金車。吝。有終。", "yao_ci_meaning": "ゆっくりとやってくる。立派な車に乗っているが、困窮している。後悔するが、最後はうまくいく。", "changing_line_special_meaning": "見栄を張って、実力以上のことをしようとして、苦しんでいます。身の丈に合った行動をすれば、道は開けます。" },
    { "hexagram_id": 47, "line_position": 5, "yao_ci_text": "九五、劓刖。困于赤紱。乃徐有説。利用祭祀。", "yao_ci_meaning": "鼻や足を切られるような、ひどい目に遭う。高官の地位にいるが、困窮する。やがて、喜びがある。祭祀を行うと良い。", "changing_line_special_meaning": "高い地位にありながら、多くの困難に直面します。しかし、誠実に対応すれば、必ず乗り越えられます。" },
    { "hexagram_id": 47, "line_position": 6, "yao_ci_text": "上六、困于葛藟。于臲卼。曰動悔。有悔。征吉。", "yao_ci_meaning": "かずらに絡まれ、動けない。動けば後悔すると、反省する。しかし、思い切って進めば、吉。", "changing_line_special_meaning": "過去の失敗にとらわれ、身動きが取れなくなっています。後悔ばかりしていないで、勇気を出して、新しい一歩を踏み出しましょう。" },

    # 48. 水風井 (すいふうせい)
    { "hexagram_id": 48, "line_position": 1, "yao_ci_text": "初六、井泥不食。舊井无禽。", "yao_ci_meaning": "井戸の底の泥水は、飲めない。古い井戸には、鳥も来ない。", "changing_line_special_meaning": "あなたの才能や能力は、まだ、誰にも認められていません。今は、ただ、実力を磨く時です。" },
    { "hexagram_id": 48, "line_position": 2, "yao_ci_text": "九二、井谷射鮒。甕敝漏。", "yao_ci_meaning": "井戸の壁の穴から、鮒を射る。釣瓶が壊れて、水が漏れる。", "changing_line_special_meaning": "目先の小さな利益に、とらわれてはいけません。もっと、大局的な視点を持つべきです。" },
    { "hexagram_id": 48, "line_position": 3, "yao_ci_text": "九三、井渫不食。爲我心惻。可用汲。王明。並受其福。", "yao_ci_meaning": "井戸は綺麗なのに、誰も水を飲まない。心が痛む。この水は、汲むことができる。王が賢明であれば、共に福を受ける。", "changing_line_special_meaning": "あなたは、素晴らしい能力を持っているのに、それが、まだ世の中に認められていません。賢明なリーダーが現れるのを、待ちましょう。" },
    { "hexagram_id": 48, "line_position": 4, "yao_ci_text": "六四、井甃。无咎。", "yao_ci_meaning": "井戸の壁を修理する。問題ない。", "changing_line_special_meaning": "自分自身のメンテナンスや、能力の向上に、力を注ぐべき時です。自己投資が、将来の成功に繋がります。" },
    { "hexagram_id": 48, "line_position": 5, "yao_ci_text": "九五、井冽。寒泉食。", "yao_ci_meaning": "井戸の水が、清らかで冷たい。誰もが、この水を飲むことができる。", "changing_line_special_meaning": "あなたの素晴らしい才能や徳が、多くの人々の役に立ちます。思う存分、その力を発揮してください。" },
    { "hexagram_id": 48, "line_position": 6, "yao_ci_text": "上六、井收勿幕。有孚元吉。", "yao_ci_meaning": "井戸を、誰でも使えるように、蓋をしない。誠意があれば、大いに吉。", "changing_line_special_meaning": "自分の才能や利益を、独り占めにしてはいけません。多くの人々と、分かち合うことで、さらなる幸運が舞い込みます。" },

    # 49. 沢火革 (たくかかく)
    { "hexagram_id": 49, "line_position": 1, "yao_ci_text": "初九、鞏用黄牛之革。", "yao_ci_meaning": "黄色い牛の革で、固く縛る。まだ、変革の時ではない。", "changing_line_special_meaning": "まだ、変革の準備が整っていません。軽率に行動せず、今は、現状維持に努めましょう。" },
    { "hexagram_id": 49, "line_position": 2, "yao_ci_text": "六二、巳日乃革之。征吉。无咎。", "yao_ci_meaning": "時が満ちてから、変革する。進んでいけば、吉。問題ない。", "changing_line_special_meaning": "いよいよ、変革の時が来ました。十分に準備を整え、満を持して、行動を起こしましょう。" },
    { "hexagram_id": 49, "line_position": 3, "yao_ci_text": "九三、征凶。貞厲。革言三就。有孚。", "yao_ci_meaning": "進めば凶。正しくいても危うい。変革について、三度話し合って、誠意をもって臨むべき。", "changing_line_special_meaning": "焦って、変革を推し進めてはいけません。周りの人々と、十分に話し合い、合意を得ることが大切です。" },
    { "hexagram_id": 49, "line_position": 4, "yao_ci_text": "九四、悔亡。有孚。改命吉。", "yao_ci_meaning": "後悔はない。誠意をもって、天命を改める。吉。", "changing_line_special_meaning": "これまでの古い体制や、考え方を、根本から変える時です。あなたの改革は、多くの人々の支持を得るでしょう。" },
    { "hexagram_id": 49, "line_position": 5, "yao_ci_text": "九五、大人虎變。未占有孚。", "yao_ci_meaning": "大人が、虎の皮の模様のように、鮮やかに変わる。占うまでもなく、明らかである。", "changing_line_special_meaning": "あなたの変革は、誰の目にも明らかな、素晴らしい成果を上げます。リーダーシップを発揮してください。" },
    { "hexagram_id": 49, "line_position": 6, "yao_ci_text": "上六、君子豹變。小人革面。征凶。居貞吉。", "yao_ci_meaning": "君子は、豹の皮の模様のように、美しく変わる。小人は、表面だけを変える。進めば凶。留まれば吉。", "changing_line_special_meaning": "変革が、一段落した後は、その成果を、着実に定着させることが大切です。大きな改革は、もう必要ありません。" },

    # 50. 火風鼎 (かふうてい)
    { "hexagram_id": 50, "line_position": 1, "yao_ci_text": "初六、鼎顛趾。利出否。得妾以其子。无咎。", "yao_ci_meaning": "鼎がひっくり返る。悪いものを出すのに良い。子持ちの妾を得る。問題ない。", "changing_line_special_meaning": "古いものを捨て、新しいものを、取り入れるべき時です。過去の失敗も、将来の成功の糧となります。" },
    { "hexagram_id": 50, "line_position": 2, "yao_ci_text": "九二、鼎有實。我仇有疾。不我能即。吉。", "yao_ci_meaning": "鼎に、食べ物がいっぱい入っている。敵が、病気で、私を攻撃できない。吉。", "changing_line_special_meaning": "あなたは、実力も、才能も、十分に備わっています。周りの嫉妬や、妨害を気にせず、自信を持って進みましょう。" },
    { "hexagram_id": 50, "line_position": 3, "yao_ci_text": "九三、鼎耳革。其行塞。雉膏不食。方雨虧悔。終吉。", "yao_ci_meaning": "鼎の耳が、取れてしまう。進めない。美味しい料理も、食べられない。やがて、恵みの雨が降り、後悔は消え、最後は吉。", "changing_line_special_meaning": "あなたの才能が、正しく評価されず、活躍の機会を、失っています。しかし、諦めずに待てば、必ず、道は開けます。" },
    { "hexagram_id": 50, "line_position": 4, "yao_ci_text": "九四、鼎折足。覆公餗。其形渥。凶。", "yao_ci_meaning": "鼎の足が折れ、君主の料理が、ひっくり返る。ずぶ濡れになる。凶。", "changing_line_special_meaning": "重大な責任を、任されますが、その重圧に耐えきれず、大失敗を犯してしまいます。実力不足を、自覚すべきです。" },
    { "hexagram_id": 50, "line_position": 5, "yao_ci_text": "六五、鼎黄耳金鉉。利貞。", "yao_ci_meaning": "鼎に、黄色い耳と、金の鉉が付いている。正しくしているのが良い。", "changing_line_special_meaning": "謙虚な姿勢で、賢者の助言を、素直に聞き入れることで、物事は、順調に進みます。人の意見を、大切にしましょう。" },
    { "hexagram_id": 50, "line_position": 6, "yao_ci_text": "上九、鼎玉鉉。大吉。无不利。", "yao_ci_meaning": "鼎に、玉の鉉が付いている。大いに吉。何事も、うまくいく。", "changing_line_special_meaning": "あなたの知恵と、徳が、最高潮に達し、何をやっても、うまくいく、素晴らしい幸運期です。" },

    # 51. 震為雷 (しんいらい)
    { "hexagram_id": 51, "line_position": 1, "yao_ci_text": "初九、震來虩虩。後笑言啞啞。吉。", "yao_ci_meaning": "雷が鳴り響き、恐れおののく。しかし、後には、笑い声が響く。吉。", "changing_line_special_meaning": "最初は、驚くような出来事に、動揺しますが、冷静に対処すれば、かえって、良い結果に繋がります。" },
    { "hexagram_id": 51, "line_position": 2, "yao_ci_text": "六二、震來厲。億喪貝。躋于九陵。勿逐。七日得。", "yao_ci_meaning": "雷が来て、危うい。多くの財産を失う。高い丘に登って、難を避ける。追いかけてはならない。七日すれば、戻ってくる。", "changing_line_special_meaning": "突然のトラブルで、大きな損失を被ります。しかし、慌てず、冷静に、時が過ぎるのを待てば、失ったものは、取り戻せます。" },
    { "hexagram_id": 51, "line_position": 3, "yao_ci_text": "六三、震蘇蘇。震行无眚。", "yao_ci_meaning": "雷に、気力を失う。しかし、思い切って行動すれば、災いはない。", "changing_line_special_meaning": "動揺して、気力が、なえてしまいます。しかし、ここで、奮起して行動を起こせば、道は開けます。" },
    { "hexagram_id": 51, "line_position": 4, "yao_ci_text": "九四、震遂泥。", "yao_ci_meaning": "雷で、泥沼にはまる。", "changing_line_special_meaning": "度重なる衝撃で、身動きが取れない、最悪の状況に陥ります。今は、どうすることもできません。" },
    { "hexagram_id": 51, "line_position": 5, "yao_ci_text": "六五、震往來厲。億无喪。有事。", "yao_ci_meaning": "雷が、行ったり来たりして、危うい。しかし、損失はない。やるべきことがある。", "changing_line_special_meaning": "次から次へと、問題が発生し、気は休まりません。しかし、冷静に対処すれば、乗り越えられます。" },
    { "hexagram_id": 51, "line_position": 6, "yao_ci_text": "上六、震索索。視矍矍。征凶。震不于其躬。于其鄰。无咎。婚媾有言。", "yao_ci_meaning": "雷に、震え上がる。周りを、きょろきょろと見回す。進めば凶。災いは、自分ではなく、隣人に及ぶ。問題ない。結婚には、障害がある。", "changing_line_special_meaning": "動揺のあまり、パニックになっています。しかし、被害は、自分ではなく、周りの人に及びます。冷静さを、取り戻してください。" },

    # 52. 艮為山 (ごんいざん)
    { "hexagram_id": 52, "line_position": 1, "yao_ci_text": "初六、艮其趾。无咎。利永貞。", "yao_ci_meaning": "足が止まる。問題ない。長く、正しくしているのが良い。", "changing_line_special_meaning": "行動を、起こす前に、まずは、立ち止まって、よく考えるべきです。軽率な行動は、禁物です。" },
    { "hexagram_id": 52, "line_position": 2, "yao_ci_text": "六二、艮其腓。不拯其隨。其心不快。", "yao_ci_meaning": "ふくらはぎが止まる。助けようとしても、助けられない。心が、晴れない。", "changing_line_special_meaning": "思うように、体が動かず、もどかしい思いをします。無理に動こうとせず、今は、流れに任せましょう。" },
    { "hexagram_id": 52, "line_position": 3, "yao_ci_text": "九三、艮其限。列其夤。厲薰心。", "yao_ci_meaning": "腰が止まる。背骨が、引き裂かれるようだ。危険が、心に迫る。", "changing_line_special_meaning": "無理な姿勢を、強いられ、心身ともに、限界です。このままでは、倒れてしまいます。" },
    { "hexagram_id": 52, "line_position": 4, "yao_ci_text": "六四、艮其身。无咎。", "yao_ci_meaning": "上半身が止まる。問題ない。", "changing_line_special_meaning": "全ての動きを止め、心を、無にしましょう。静寂の中に、新たな発見があります。" },
    { "hexagram_id": 52, "line_position": 5, "yao_ci_text": "六五、艮其輔。言有序。悔亡。", "yao_ci_meaning": "あごが止まる。言葉に、秩序がある。後悔はない。", "changing_line_special_meaning": "余計なことは、言わないことです。言葉を、慎むことで、かえって、あなたの信頼は、高まります。" },
    { "hexagram_id": 52, "line_position": 6, "yao_ci_text": "上九、敦艮。吉。", "yao_ci_meaning": "篤実に、止まる。吉。", "changing_line_special_meaning": "自分の分を、わきまえ、満足することを知る。その、どっしりと、落ち着いた態度が、幸運を呼びます。" },

    # 53. 風山漸 (ふうざんぜん)
    { "hexagram_id": 53, "line_position": 1, "yao_ci_text": "初六、鴻漸于干。小子厲。有言。无咎。", "yao_ci_meaning": "鴻が、水際に進む。若い者は、危うい。非難されるが、問題ない。", "changing_line_special_meaning": "物事の、始まりの段階です。まだ、不安定で、周りから、とやかく言われますが、心配いりません。" },
    { "hexagram_id": 53, "line_position": 2, "yao_ci_text": "六二、鴻漸于磐。飲食衎衎。吉。", "yao_ci_meaning": "鴻が、大きな岩に進む。飲食を、楽しむ。吉。", "changing_line_special_meaning": "少し、安定した場所に進み、一息つくことができます。仲間と、楽しい時間を、過ごしましょう。" },
    { "hexagram_id": 53, "line_position": 3, "yao_ci_text": "九三、鴻漸于陸。夫征不復。婦孕不育。凶。利禦寇。", "yao_ci_meaning": "鴻が、陸地に進む。夫は、出征して帰らず、妻は、妊娠しても、育てられない。凶。敵を防ぐのに良い。", "changing_line_special_meaning": "調子に乗って、進みすぎると、危険です。自分の分を、わきまえ、足元を、しっかりと固めましょう。" },
    { "hexagram_id": 53, "line_position": 4, "yao_ci_text": "六四、鴻漸于木。或得其桷。无咎。", "yao_ci_meaning": "鴻が、木に進む。止まり木を、得るかもしれない。問題ない。", "changing_line_special_meaning": "不安定な状況ですが、仮の、足がかりを、見つけることができます。一時的な、安らぎを、得られるでしょう。" },
    { "hexagram_id": 53, "line_position": 5, "yao_ci_text": "九五、鴻漸于陵。婦三歳不孕。終莫之勝。吉。", "yao_ci_meaning": "鴻が、高い丘に進む。妻は、三年間、妊娠しない。しかし、最後は、誰も、これに勝てない。吉。", "changing_line_special_meaning": "目標達成までには、時間がかかり、多くの誤解を、受けるかもしれません。しかし、最後には、必ず、あなたの正しさが、証明されます。" },
    { "hexagram_id": 53, "line_position": 6, "yao_ci_text": "上九、鴻漸于逵。其羽可用爲儀。吉。", "yao_ci_meaning": "鴻が、天上の道に進む。その羽は、儀式の飾りに、使うことができる。吉。", "changing_line_special_meaning": "あなたは、人々の、手本となるような、素晴らしい高みに、到達します。その功績は、長く、称えられるでしょう。" },

    # 54. 雷沢帰妹 (らいたくきまい)
    { "hexagram_id": 54, "line_position": 1, "yao_ci_text": "初九、歸妹以娣。跛能履。征吉。", "yao_ci_meaning": "妹を、姉の付き添いとして、嫁がせる。不完全な状態だが、進んでいけば、吉。", "changing_line_special_meaning": "不本意な、スタートかもしれませんが、サポート役として、誠実に務めれば、道は開けます。" },
    { "hexagram_id": 54, "line_position": 2, "yao_ci_text": "九二、眇能視。利幽人之貞。", "yao_ci_meaning": "片目でも、見ることができる。静かに、正しくしているのが良い。", "changing_line_special_meaning": "恵まれない状況ですが、嘆いてはいけません。今の自分に、できることを、精一杯、やりましょう。" },
    { "hexagram_id": 54, "line_position": 3, "yao_ci_text": "六三、歸妹以須。反歸以娣。", "yao_ci_meaning": "自分を、安売りして、嫁ごうとする。結局、格下の扱いを、受けることになる。", "changing_line_special_meaning": "焦って、自分を、安売りしてはいけません。自分の価値を、信じ、堂々としていましょう。" },
    { "hexagram_id": 54, "line_position": 4, "yao_ci_text": "九四、歸妹愆期。遲歸有時。", "yao_ci_meaning": "結婚の時期を、逃してしまう。遅れても、良い時期が、必ず来る。", "changing_line_special_meaning": "チャンスを、逃してしまったと、焦る必要はありません。待っていれば、必ず、もっと良い機会が、巡ってきます。" },
    { "hexagram_id": 54, "line_position": 5, "yao_ci_text": "六五、帝乙歸妹。其君之袂。不如其娣之袂良。月幾望。吉。", "yao_ci_meaning": "帝乙が、妹を嫁がせる。正夫人の袖よりも、付き添いの袖の方が、立派である。月は、満月間近。吉。", "changing_line_special_meaning": "主役よりも、脇役の方が、注目を浴びる時です。謙虚な、サポート役が、幸運を呼び込みます。" },
    { "hexagram_id": 54, "line_position": 6, "yao_ci_text": "上六、女承筐无實。士刲羊无血。无攸利。", "yao_ci_meaning": "女性が、捧げ持つ籠には、何も入っていない。男性が、羊を割いても、血が出ない。何の利益もない。", "changing_line_special_meaning": "見かけだけで、中身が、伴っていません。実質のない関係は、何の、実りも、もたらさないでしょう。" },

    # 55. 雷火豊 (らいかほう)
    { "hexagram_id": 55, "line_position": 1, "yao_ci_text": "初九、遇其配主。雖旬无咎。往有尚。", "yao_ci_meaning": "自分に、ふさわしいパートナーに、出会う。十日間、協力しても、問題ない。進んでいけば、尊敬される。", "changing_line_special_meaning": "素晴らしい、パートナーとの出会いがあります。お互いに、協力し合うことで、大きな成果を、上げられるでしょう。" },
    { "hexagram_id": 55, "line_position": 2, "yao_ci_text": "六二、豊其蔀。日中見斗。往得疑疾。有孚發若。吉。", "yao_ci_meaning": "日よけが、厚すぎて、真昼なのに、星が見える。疑心暗鬼になる。誠意があれば、道は開ける。吉。", "changing_line_special_meaning": "周りの、嫉妬や、妨害によって、先が見えなくなっています。しかし、誠実な、あなたの心は、必ず、相手に通じます。" },
    { "hexagram_id": 55, "line_position": 3, "yao_ci_text": "九三、豊其沛。日中見沬。折其右肱。无咎。", "yao_ci_meaning": "日よけが、さらに厚くなる。真昼なのに、暗い。右腕を、折ってしまう。しかし、問題ない。", "changing_line_special_meaning": "有能な、部下や、協力者を、失ってしまいます。しかし、それは、あなたにとって、必要な試練です。心配いりません。" },
    { "hexagram_id": 55, "line_position": 4, "yao_ci_text": "九四、豊其蔀。日中見斗。遇其夷主。吉。", "yao_ci_meaning": "日よけが、厚い。真昼なのに、星が見える。自分と、対等なパートナーに、出会う。吉。", "changing_line_special_meaning": "困難な状況の中で、あなたを、理解してくれる、素晴らしいパートナーに、出会います。共に、困難を、乗り越えてください。" },
    { "hexagram_id": 55, "line_position": 5, "yao_ci_text": "六五、來章。有慶譽。吉。", "yao_ci_meaning": "賢者を、招き入れる。喜びと、名誉がある。吉。", "changing_line_special_meaning": "優れた才能を持つ人々が、あなたの周りに、集まってきます。彼らの力を、借りることで、大きな成功を、収めることができます。" },
    { "hexagram_id": 55, "line_position": 6, "yao_ci_text": "上六、豊其屋。蔀其家。闚其戸。闃其无人。三歳不覿。凶。", "yao_ci_meaning": "家を、豊かにしすぎる。家を、覆い隠してしまう。戸口から、覗いても、誰もいない。三年間、誰にも会えない。凶。", "changing_line_special_meaning": "富や、成功に、溺れ、周りの人々から、孤立してしまいます。謙虚さを、失った末路は、孤独です。" },

    # 56. 火山旅 (かざんりょ)
    { "hexagram_id": 56, "line_position": 1, "yao_ci_text": "初六、旅瑣瑣。斯其所取災。", "yao_ci_meaning": "旅先で、こせこせと、細かいことばかり、気にしている。それが、災いを、招く原因だ。", "changing_line_special_meaning": "慣れない環境で、細かいことばかり、気にしていると、かえって、トラブルを、引き寄せます。もっと、おおらかに、構えましょう。" },
    { "hexagram_id": 56, "line_position": 2, "yao_ci_text": "六二、旅即次。懐其資。得童僕貞。", "yao_ci_meaning": "旅先で、宿に着く。お金を、懐に入れている。誠実な、召使いを、得る。", "changing_line_special_meaning": "旅先で、心安らげる場所と、信頼できる、協力者を、得ることができます。安心して、旅を、続けてください。" },
    { "hexagram_id": 56, "line_position": 3, "yao_ci_text": "九三、旅焚其次。喪其童僕貞。厲。", "yao_ci_meaning": "旅先の宿が、火事になる。召使いを、失う。危うい。", "changing_line_special_meaning": "自分の、傲慢な態度が、原因で、安住の地と、信頼できる、協力者を、失ってしまいます。" },
    { "hexagram_id": 56, "line_position": 4, "yao_ci_text": "九四、旅于處。得其資斧。我心不快。", "yao_ci_meaning": "旅先で、仮の宿を得る。旅費と、武器を得る。しかし、心は、晴れない。", "changing_line_special_meaning": "一応の、安住の地は、確保できますが、心は、満たされません。まだ、本当の、居場所では、ないようです。" },
    { "hexagram_id": 56, "line_position": 5, "yao_ci_text": "六五、射雉。一矢亡。終以譽命。", "yao_ci_meaning": "雉を射る。一本の矢を、失う。しかし、最後は、名誉と、地位を、得る。", "changing_line_special_meaning": "最初は、少し、損をしますが、その、誠実な態度が、評価され、最終的には、大きな成功を、収めることができます。" },
    { "hexagram_id": 56, "line_position": 6, "yao_ci_text": "上九、鳥焚其巣。旅人先笑後號咷。喪牛于易。凶。", "yao_ci_meaning": "鳥が、自分の巣を、焼いてしまう。旅人は、最初は笑うが、後で、泣き叫ぶ。たやすく、牛を失う。凶。", "changing_line_special_meaning": "軽率で、傲慢な態度のせいで、全てを、失ってしまいます。最初は、良くても、最後は、破滅です。" },

    # 57. 巽為風 (そんいふう)
    { "hexagram_id": 57, "line_position": 1, "yao_ci_text": "初六、進退。利武人之貞。", "yao_ci_meaning": "進むか、退くか、迷う。軍人のように、規律正しく、決断するのが良い。", "changing_line_special_meaning": "方針が、定まらず、迷いが生じます。ぐずぐずしないで、リーダーの指示に、従いましょう。" },
    { "hexagram_id": 57, "line_position": 2, "yao_ci_text": "九二、巽在牀下。用史巫紛若。吉无咎。", "yao_ci_meaning": "ベッドの下に、隠れるように、謙虚である。史官や、巫女のように、神意を伺えば、吉。", "changing_line_special_meaning": "謙虚に、人の意見を、聞く姿勢が、大切です。専門家の、アドバイスを、求めましょう。" },
    { "hexagram_id": 57, "line_position": 3, "yao_ci_text": "九三、頻巽。吝。", "yao_ci_meaning": "何度も、方針を変える。後悔する。", "changing_line_special_meaning": "方針が、ころころと、変わり、一貫性がありません。これでは、誰からも、信用されません。" },
    { "hexagram_id": 57, "line_position": 4, "yao_ci_text": "六四、悔亡。田獲三品。", "yao_ci_meaning": "後悔はない。狩りで、多くの獲物を、得る。", "changing_line_special_meaning": "これまでの、地道な努力が、実を結び、大きな成果を、得ることができます。" },
    { "hexagram_id": 57, "line_position": 5, "yao_ci_text": "九五、貞吉。悔亡。无不利。无初有終。先庚三日。後庚三日。吉。", "yao_ci_meaning": "正しくしていれば、吉。後悔はない。何事も、うまくいく。始めは、悪くても、終わりは良い。十分に、準備をして、変革に臨めば、吉。", "changing_line_special_meaning": "物事を、始める前に、十分に、計画を練り、準備を、整えることが、成功の鍵です。" },
    { "hexagram_id": 57, "line_position": 6, "yao_ci_text": "上九、巽在牀下。喪其資斧。貞凶。", "yao_ci_meaning": "ベッドの下に、隠れるように、謙虚すぎる。財産と、武器を、失う。正しくいても、凶。", "changing_line_special_meaning": "あまりにも、へりくだりすぎると、かえって、自分の立場を、失ってしまいます。自信を、持つべきです。" },

    # 58. 兌為沢 (だいたく)
    { "hexagram_id": 58, "line_position": 1, "yao_ci_text": "初九、和兌。吉。", "yao_ci_meaning": "和やかに、喜ぶ。吉。", "changing_line_special_meaning": "周りの人々と、和やかに、喜びを、分かち合うことができます。穏やかで、楽しい時です。" },
    { "hexagram_id": 58, "line_position": 2, "yao_ci_text": "九二、孚兌。吉。悔亡。", "yao_ci_meaning": "誠意をもって、喜ぶ。吉。後悔はない。", "changing_line_special_meaning": "真心からの、喜びは、周りの人々にも、伝わります。誠実な、態度が、幸運を呼びます。" },
    { "hexagram_id": 58, "line_position": 3, "yao_ci_text": "六三、來兌。凶。", "yao_ci_meaning": "媚びへつらって、喜ばせようとする。凶。", "changing_line_special_meaning": "お世辞を、言ったり、人に、媚びへつらったりして、人気を、得ようとするのは、間違っています。" },
    { "hexagram_id": 58, "line_position": 4, "yao_ci_text": "九四、商兌未寧。介疾有喜。", "yao_ci_meaning": "喜びについて、話し合うが、まだ、決まらない。悪いものを、取り除けば、喜びがある。", "changing_line_special_meaning": "快楽に、溺れるか、正しい道を、進むか、迷っています。誘惑を、断ち切れば、本当の喜びを、得られます。" },
    { "hexagram_id": 58, "line_position": 5, "yao_ci_text": "九五、孚于剝。有厲。", "yao_ci_meaning": "剥ぎ取るような、危険なものを、信用する。危うい。", "changing_line_special_meaning": "口先の、甘い言葉を、信用してはいけません。あなたを、利用しようとする、危険な人物が、近づいてきます。" },
    { "hexagram_id": 58, "line_position": 6, "yao_ci_text": "上六、引兌。", "yao_ci_meaning": "人を、喜びに、引き込もうとする。", "changing_line_special_meaning": "言葉巧みに、人を、誘惑しようとします。しかし、その、浅はかな、たくらみは、すぐに見抜かれてしまうでしょう。" },

    # 59. 風水渙 (ふうすいかん)
    { "hexagram_id": 59, "line_position": 1, "yao_ci_text": "初六、用拯馬壯。吉。", "yao_ci_meaning": "屈強な馬に、助けられる。吉。", "changing_line_special_meaning": "困難な状況ですが、力強い、協力者の、おかげで、危機を、脱することができます。" },
    { "hexagram_id": 59, "line_position": 2, "yao_ci_text": "九二、渙奔其机。悔亡。", "yao_ci_meaning": "困難から、机に駆け寄り、難を避ける。後悔はない。", "changing_line_special_meaning": "危険を、感じたら、すぐに、安全な場所に、避難しましょう。早めの、決断が、身を助けます。" },
    { "hexagram_id": 59, "line_position": 3, "yao_ci_text": "六三、渙其躬。无悔。", "yao_ci_meaning": "自分の身を、顧みない。後悔はない。", "changing_line_special_meaning": "私利私欲を、捨て、公のために、尽くす時です。その、自己犠牲の精神は、必ず、報われます。" },
    { "hexagram_id": 59, "line_position": 4, "yao_ci_text": "六四、渙其群。元吉。渙有丘。匪夷所思。", "yao_ci_meaning": "仲間との、わだかまりが、解ける。大いに吉。小高い丘のように、人々が集まる。凡人には、思いもよらないことだ。", "changing_line_special_meaning": "バラバラだった、人々が、再び、一つに、まとまります。あなたの、リーダーシップが、高く、評価されるでしょう。" },
    { "hexagram_id": 59, "line_position": 5, "yao_ci_text": "九五、渙汗其大號。渙王居。无咎。", "yao_ci_meaning": "汗を流し、大号令を発する。王の居所を、開放する。問題ない。", "changing_line_special_meaning": "困難な状況を、乗り越えるために、リーダーとして、的確な、指示を、出すべき時です。財産を、人々のために、役立てましょう。" },
    { "hexagram_id": 59, "line_position": 6, "yao_ci_text": "上九、渙其血。去逖出。无咎。", "yao_ci_meaning": "血の災いから、遠く離れる。問題ない。", "changing_line_special_meaning": "危険な、状況や、場所から、完全に、離れることができます。ようやく、安心できるでしょう。" },

    # 60. 水沢節 (すいたくせつ)
    { "hexagram_id": 60, "line_position": 1, "yao_ci_text": "初九、不出戸庭。无咎。", "yao_ci_meaning": "戸口や、庭から、出ない。問題ない。", "changing_line_special_meaning": "今は、行動を、起こすべき時では、ありません。軽率に、動かず、状況を、静観しましょう。" },
    { "hexagram_id": 60, "line_position": 2, "yao_ci_text": "九二、不出門庭。凶。", "yao_ci_meaning": "門や、庭から、出ない。凶。", "changing_line_special_meaning": "チャンスが、来ているのに、行動を、起こさないため、好機を、逃してしまいます。" },
    { "hexagram_id": 60, "line_position": 3, "yao_ci_text": "六三、不節若。則嗟若。无咎。", "yao_ci_meaning": "節度を、守らない。嘆き悲しむことになる。しかし、問題はない。", "changing_line_special_meaning": "節度を、忘れて、楽しみに、溺れてしまいます。後で、後悔しますが、大きな、失敗には、なりません。" },
    { "hexagram_id": 60, "line_position": 4, "yao_ci_text": "六四、安節。亨。", "yao_ci_meaning": "自然な、節度を、守る。願いは、通る。", "changing_line_special_meaning": "無理をせず、自然体で、物事に、取り組むことで、かえって、うまくいきます。" },
    { "hexagram_id": 60, "line_position": 5, "yao_ci_text": "九五、甘節。吉。往有尚。", "yao_ci_meaning": "心地よい、節度を、守る。吉。進んでいけば、尊敬される。", "changing_line_special_meaning": "人々が、喜んで、従うような、適切な、ルールを、作ることができます。あなたの、リーダーシップが、評価されます。" },
    { "hexagram_id": 60, "line_position": 6, "yao_ci_text": "上六、苦節。貞凶。悔亡。", "yao_ci_meaning": "厳しすぎる、節度。正しくいても、凶。しかし、後悔は、なくなる。", "changing_line_special_meaning": "あまりにも、厳しすぎる、ルールは、かえって、人を、苦しめます。やり過ぎは、禁物です。" },

    # 61. 風沢中孚 (ふうたくちゅうふ)
    { "hexagram_id": 61, "line_position": 1, "yao_ci_text": "初九、虞吉。有他不燕。", "yao_ci_meaning": "準備を、しておけば、吉。他のことに、心が、移れば、安らかではない。", "changing_line_special_meaning": "誠実な、心で、物事に、臨むなら、あれこれと、心配する必要は、ありません。心を、落ち着けて、取り組みましょう。" },
    { "hexagram_id": 61, "line_position": 2, "yao_ci_text": "九二、鳴鶴在陰。其子和之。我有好爵。吾與爾靡之。", "yao_ci_meaning": "鶴が、物陰で鳴き、その子が、応える。良い酒が、ある。お前と、共に、楽しもう。", "changing_line_special_meaning": "あなたの、誠実な、思いは、必ず、相手に、通じます。心を開いて、語り合いましょう。" },
    { "hexagram_id": 61, "line_position": 3, "yao_ci_text": "六三、得敵。或鼓或罷。或泣或歌。", "yao_ci_meaning": "好敵手を、得る。ある時は、戦い、ある時は、休み、ある時は、泣き、ある時は、歌う。", "changing_line_special_meaning": "相手の、影響を、受けやすく、心が、不安定に、なっています。一貫した、態度を、保つことが、大切です。" },
    { "hexagram_id": 61, "line_position": 4, "yao_ci_text": "六四、月幾望。馬匹亡。无咎。", "yao_ci_meaning": "月は、満月間近。馬の、片方が、いなくなる。問題ない。", "changing_line_special_meaning": "目上の人を、敬い、謙虚な、態度を、心がけましょう。そうすれば、災いを、避けることができます。" },
    { "hexagram_id": 61, "line_position": 5, "yao_ci_text": "九五、有孚攣如。无咎。", "yao_ci_meaning": "誠意をもって、手を取り合う。問題ない。", "changing_line_special_meaning": "誠実な、リーダーシップで、人々を、一つに、まとめることができます。信頼関係が、成功の鍵です。" },
    { "hexagram_id": 61, "line_position": 6, "yao_ci_text": "上九、翰音登于天。貞凶。", "yao_ci_meaning": "鶏が、天に登ろうと、鳴き叫ぶ。正しくいても、凶。", "changing_line_special_meaning": "口先だけで、実力が、伴っていません。口ばかり、達者で、行動が、伴わなければ、誰からも、信用されません。" },

    # 62. 雷山小過 (らいざんしょうか)
    { "hexagram_id": 62, "line_position": 1, "yao_ci_text": "初六、飛鳥以凶。", "yao_ci_meaning": "鳥が、飛び立とうとして、凶。", "changing_line_special_meaning": "まだ、準備が、整っていないのに、焦って、行動を、起こしてはいけません。時期尚早です。" },
    { "hexagram_id": 62, "line_position": 2, "yao_ci_text": "六二、過其祖。遇其妣。不及其君。遇其臣。无咎。", "yao_ci_meaning": "祖父を、通り過ぎ、祖母に、会う。君主には、会えず、家臣に、会う。問題ない。", "changing_line_special_meaning": "本来の、目的は、達成できませんが、それに、準ずる、成果は、得られます。高望みは、しないことです。" },
    { "hexagram_id": 62, "line_position": 3, "yao_ci_text": "九三、弗過防之。從或戕之。凶。", "yao_ci_meaning": "行き過ぎを、防がない。かえって、殺されるかもしれない。凶。", "changing_line_special_meaning": "自分の、力を、過信し、忠告を、無視すると、痛い目に、遭います。謙虚に、なるべきです。" },
    { "hexagram_id": 62, "line_position": 4, "yao_ci_text": "九四、无咎。弗過遇之。往厲必戒。勿用永貞。", "yao_ci_meaning": "問題ない。行き過ぎず、慎重に、行動する。進めば、危険。長く、続けてはならない。", "changing_line_special_meaning": "謙虚な、態度を、保ち、慎重に、行動すれば、問題ありません。しかし、調子に乗って、前に、出過ぎては、いけません。" },
    { "hexagram_id": 62, "line_position": 5, "yao_ci_text": "六五、密雲不雨。自我西郊。公弋取彼在穴。", "yao_ci_meaning": "密雲が、立ち込めるが、雨は、降らない。公が、穴の中の、獲物を、取る。", "changing_line_special_meaning": "実力者が、下に、隠れています。目上の人は、その才能を、見出し、登用すべきです。" },
    { "hexagram_id": 62, "line_position": 6, "yao_ci_text": "上六、弗遇過之。飛鳥離之。凶。是謂災眚。", "yao_ci_meaning": "出会うべき人に、会えず、行き過ぎてしまう。飛ぶ鳥も、見放す。凶。これを、災いという。", "changing_line_special_meaning": "自分の、分を、わきまえず、高望み、しすぎたため、全てを、失ってしまいます。" },

    # 63. 水火既済 (すいかきせい)
    { "hexagram_id": 63, "line_position": 1, "yao_ci_text": "初九、曳其輪。濡其尾。无咎。", "yao_ci_meaning": "車輪を、引きずる。尾を、濡らす。問題ない。", "changing_line_special_meaning": "物事の、始めは、慎重に、進むべきです。勢いに、任せて、突っ走ると、失敗します。" },
    { "hexagram_id": 63, "line_position": 2, "yao_ci_text": "六二、婦喪其茀。勿逐。七日得。", "yao_ci_meaning": "婦人が、髪飾りを、なくす。追いかけては、いけない。七日すれば、戻ってくる。", "changing_line_special_meaning": "小さな、トラブルが、ありますが、慌てず、騒がず、どっしりと、構えていれば、自然に、解決します。" },
    { "hexagram_id": 63, "line_position": 3, "yao_ci_text": "九三、高宗伐鬼方。三歳克之。小人勿用。", "yao_ci_meaning": "高宗が、鬼方を、討伐する。三年かかって、勝利する。小人を、用いてはならない。", "changing_line_special_meaning": "大きな、目標を、達成するためには、時間と、労力が、かかります。焦らず、じっくりと、取り組みましょう。" },
    { "hexagram_id": 63, "line_position": 4, "yao_ci_text": "六四、繻有衣袽。終日戒。", "yao_ci_meaning": "立派な服も、ぼろきれで、備える。一日中、警戒する。", "changing_line_special_meaning": "順調な時こそ、油断は、禁物です。常に、最悪の事態を、想定し、備えを、怠らないでください。" },
    { "hexagram_id": 63, "line_position": 5, "yao_ci_text": "九五、東鄰殺牛。不如西鄰之禴祭。實受其福。", "yao_ci_meaning": "東の隣人が、牛を、殺して、盛大な、祭りをする。西の隣人の、質素な、祭りには、及ばない。誠意が、福を、受ける。", "changing_line_special_meaning": "見栄や、体裁よりも、真心が、大切です。誠実な、気持ちは、必ず、相手に、通じます。" },
    { "hexagram_id": 63, "line_position": 6, "yao_ci_text": "上六、濡其首。厲。", "yao_ci_meaning": "頭まで、水に、濡れる。危うい。", "changing_line_special_meaning": "調子に、乗りすぎて、深入りし、危険な、状況に、陥ります。引き際を、わきまえるべきです。" },

    # 64. 火水未済 (かすいびせい)
    { "hexagram_id": 64, "line_position": 1, "yao_ci_text": "初六、濡其尾。吝。", "yao_ci_meaning": "尾を、濡らす。後悔する。", "changing_line_special_meaning": "状況を、よく、見極めずに、軽率に、行動すると、失敗します。準備不足です。" },
    { "hexagram_id": 64, "line_position": 2, "yao_ci_text": "九二、曳其輪。貞吉。", "yao_ci_meaning": "車輪を、引きずる。正しくしていれば、吉。", "changing_line_special_meaning": "自分の、力を、過信せず、慎重に、物事を、進めるべきです。焦りは、禁物です。" },
    { "hexagram_id": 64, "line_position": 3, "yao_ci_text": "六三、未済。征凶。利渉大川。", "yao_ci_meaning": "まだ、完成していない。進めば、凶。大きな川を、渡るのに良い。", "changing_line_special_meaning": "実力が、伴わないまま、大きな、挑戦を、するのは、無謀です。しかし、覚悟を、決めて、臨むなら、道は、開けるかもしれません。" },
    { "hexagram_id": 64, "line_position": 4, "yao_ci_text": "九四、貞吉。悔亡。震用伐鬼方。三歳有賞于大國。", "yao_ci_meaning": "正しくしていれば、吉。後悔はない。奮起して、鬼方を、討伐する。三年で、大手柄を、立てる。", "changing_line_special_meaning": "困難な、目標に、対して、不屈の、闘志で、立ち向かう時です。その、努力は、必ず、報われます。" },
    { "hexagram_id": 64, "line_position": 5, "yao_ci_text": "六五、貞吉。无悔。君子之光。有孚。吉。", "yao_ci_meaning": "正しくしていれば、吉。後悔はない。君子の、光。誠意が、あれば、吉。", "changing_line_special_meaning": "あなたの、誠実な、人柄と、これまでの、努力が、認められ、物事は、完成へと、向かいます。素晴らしい、成果を、得られるでしょう。" },
    { "hexagram_id": 64, "line_position": 6, "yao_ci_text": "上九、有孚于飲酒。无咎。濡其首。有孚失是。", "yao_ci_meaning": "酒を、飲むのに、誠意がある。問題ない。しかし、頭まで、濡れるほど、飲むと、誠意を、失う。", "changing_line_special_meaning": "目標を、達成し、祝杯を、あげるのは、良いことです。しかし、調子に、乗りすぎて、羽目を、外しすぎないように、注意してください。" }
]