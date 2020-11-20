# HIKAKIN TV コピペ 表示ライブラリ
Python library to output the HIKAKINTV appearance for each age and each year.  
各年齢・各年のHIKAKIN TV の様子を出力するライブラリ。

>【27歳のヒカキンによるHIKAKIN TV】
>
>♪HIKAKIN TV〜 2nd Wednesday〜(毎日は無理なので月一の第二水曜日だけになった)
>
>ぶっぶっ(できなくなった) へろう ごずめず(YouTubeは2057年にGoz-Mezに改名しました) どうも、開發光です(本名) 今日はもう寝ます(19時)

Twitterで検索したものの中から複数の HIKAKIN TV をピックアップしています。

## 仕様
ライブラリと表記されていますが、単体でも起動可能です。  
一部の入力ではランダムで結果が異なることがあります。

- コマンドラインから起動  
引数を与えると引数の年齢の HIKAKIN TV を表示します。
引数がない場合は標準入力の年齢の HIKAKIN TV を表示します。</br></br>
入力がキーワードの場合、キーワードに対応した HIKAKIN TV が表示されます。（「時代劇」→ 時代劇の HIKAKIN TV ）</br>キーワードに当てはまらない場合は全ての HIKAKIN TV の中からランダムに HIKAKIN TV を表示します。</br></br>
なお、コマンドラインからしか出すことができない隠し HIKAKIN TV があります。

- 外部から呼び出す  
「関数の説明」にある関数が使用できます。</br>
使用時はhikakinTVフォルダごと作業ディレクトリに保存し、プログラム中に下記のコードを入力してください。
```python
from hikakinTV import hikakinTV
```


## 関数の説明
`hikakin_age`  
入力された年齢に対応する HIKAKIN TV を返します。  
入力がキーワードの場合、キーワードに対応した HIKAKIN TV を返します。（「時代劇」→ 時代劇の HIKAKIN TV ）  
キーワードに当てはまらない場合は全ての HIKAKIN TV の中からランダムに HIKAKIN TV を返します。

`hikakin_year`  
入力された西暦に対応する HIKAKIN TV を返します。  
入力がキーワードの場合、キーワードに対応した HIKAKIN TV を返します。（「時代劇」→ 時代劇の HIKAKIN TV ）  
キーワードに当てはまらない場合は全ての HIKAKIN TV の中からランダムに HIKAKIN TV を返します。

`random_all`  
全ての HIKAKIN TV の中からランダムに HIKAKIN TV を返します。

`random_noNum`  
特定の年齢に対応しないものの中から（時代劇のHIKAKIN TVなど）ランダムに HIKAKIN TV を返します。

