# YABIP
_yet another batch image processor_  
アプリ名は未定です。  
いまのところ"Gahen"(仮)です。  
画像一括変換装置、「画変」です。


## ('v') できること
簡単な画像編集ができます。
- たて/よこ縮小
- みぎ/ひだり回転
- たて/よこ連結
- 減色(pngquant)
- PNG/JPG/BMP変換


## ('o') つかいかた
画像ファイルを各パネルにドロップしてください。  
「連結」は2枚以上必要です。  
「減色」はPNGのみ対応しています。  
「減色」→「変換」は変な感じになるのでやめてください。


## ('-') くわしく
- よこ縮小  
横サイズを指定して画像を縮小します。  
縦サイズと比率は自動的に調整されます。  

- たて縮小  
画像の縦サイズを指定します。  
拡大はできません。縮小専用です。  

- ひだり回転  
画像を反時計回りに90度回転します。  
つまり左回転です。  

- みぎ回転  
画像を反時計回りに270度回転します。  
上が右に、右が下に、下が左に、左が上に。  

- よこ結合  
画像を横方向に連結します。  
異なる大きさの画像同士の場合、最も小さな画像にあわせて縮小されます。  

- たて結合  
画像を縦方向に連結します。  
"つかんだ"ファイルが基準になります。  

- 容量削減(pngquant)  
画像の色を減らして容量を削減します。  
色が減るので画質が下がります。PNG専用。  

- 出力形式選択  
出力画像のフォーマットを指定します。  
ちなみに、このパネルにドロップすると何もせずに変換されます。  


## ('~') ちゅうい
この場所に"pngquant.exe"を置くこと。  
_APP\_PATH/resources/pngquant/pngquant.exe_  


pngquant  
[https://pngquant.org/](https://pngquant.org/)  


### TODO
- [ ] 「常に最前面で表示」機能をつけたい
- [ ] どこでもドラッグ機能をつけたい
- [ ] ましなUIにする
- [ ] アプリ名やアイコンも仮のやつだから、ちゃんとする