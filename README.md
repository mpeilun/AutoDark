<img style="width:64px" src="https://user-images.githubusercontent.com/13403218/228272332-fbbe0d8a-752b-40f5-ac9b-59f02e2d3924.png" />

# AutoDark

AutoDark 是一個可以自動調整顯示器亮度的程式。透過對螢幕進行截圖並分析截得的圖片來判斷是否需要調整亮度。

## 環境設定

AutoDark 使用 Python3 進行開發，需安裝以下套件：

- `pillow`
- `numpy`
- `pystray`
- `screen_brightness_control`
- `mss`

## 如何使用

1. 開啟命令列視窗
2. 輸入 `python autodark.py` 開啟程式
3. 程式開啟後會在系統列出現一個 icon，可透過 icon 選單進行關閉程式
4. 程式每秒會透過 `mss` 套件進行螢幕截圖，判斷是否需要調整亮度

## 注意事項

- AutoDark 只能適用於 Windows 系統
- 程式需要使用管理員權限執行，否則無法正常調整螢幕亮度
- 當系統有多個顯示器時，請確認 `sbc.list_monitors()` 回傳的資訊與實際狀況相符，並且自行更改 `monitors[1]` 為欲調整亮度的顯示器編號

## License

AutoDark 使用 MIT License 開放原始碼。 

Idea icons created by Good Ware - [Flaticon](https://media.flaticon.com/license/license.pdf)
