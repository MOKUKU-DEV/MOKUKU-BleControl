

### Transfer Data (to display) (BLE UUID: beb5483e-36e1-4688-b7f5-ea07361b26a8):

1. length 5 uint8_t array :

| 1 | 2 | 3 | 4 | 5 |
|---|-----|------|---------|----|
| 1 | VEL | RPM_A | RPM_B | GAS |

2. length 10 uint8_t array :

| 1 | 2 | 3 | 4 | 5 | 6 | 7| 8| 9| 10 | 11|
|---|-----|------|---------|----|---|-----|------|---------|----|----|
| 1 | VEL | RPM_A | RPM_B | GAS | TIMESTAMP_1 | TIMESTAMP_2 | TIMESTAMP_3 | TIMESTAMP_4 | BACKLIGHT | COMMAND |

<details>
  <summary>command list</summary>

* 10 : toggle stereo mode
* 43 : left click
* 53 : right click
* 66 : left ota update
* 67 : right ota update

</details>

### Transfer Message (BLE UUID: d222e154-1a80-4e71-9a63-2aa2c0ce0a8c)

1. Wifi Name :

| 1 | 2 | 3 - N |
|---|---|-------|
| 7 | string length | string (wifi name) |

2. Wifi Password :

| 1 | 2 | 3 - N |
|---|---|-------|
| 8 | string length | string (wifi password) |

3. List all elements in a folder :

| 1 | 2 | 3 - N |
|---|---|-------|
| 60 | string length | string (target directory path) |

4. Return SD card information (used space / total space) :

| 1 |
|---|
| 61 |

5. Delete a file :

| 1 | 2 | 3 - N |
|---|---|-------|
| 62 | string length | string (target file path) |

6. Direct Command :

| 1 | 2 |
|---|---|
| 1 | command id |

7. Obtain Software Version :

| 1 |
|---|
| 3 |


### For downloading file from MOKUKU (txt only)

1. send open file request **id(1 byte), string_len(1 byte, n<255), string(n bytes)**
  * MOKUKU will return file message : **id(1 byte, =65), ret(1 byte), file_key(4 bytes), file_size(4 bytes)**
2. Then we could request for file data : **id(1 byte, =66), data_size(1 byte, <255), file_key(4 bytes), begin_position(4 bytes)**
  * MOKUKU will return the data **id(1 byte, =66), data_size(1 byte, n<255), begin_position(4 bytes), data(n bytes)**

### For uploading file to MOKUKU (txt only)

1. send open file request **id(1 byte), string_len(1 byte, n<255), string(n bytes)**
  * MOKUKU will return file message : **id(1 byte, =63), ret(1 byte), file_key(4 bytes), file_size(4 bytes, =0)**
2. Then we could begin to send file data : **id(1 byte, =64), data_size(1 byte, n<255), file_key(4 bytes), begin_position(4 bytes), data(n bytes)**
  * send a zero sized message to indicate file end.
  * MOKUKU will return its current file position : **id(1 byte, =64), file_key(4 bytes), current_position(4 bytes)**

### For DIY config file

```
PANEL_TYPE_INVALID = 0,
PANEL_TYPE_VEL = 1,
PANEL_TYPE_RPM = 2,
PANEL_TYPE_GRAVITY = 3,
PANEL_TYPE_PITCHROLL = 4,
PANEL_TYPE_FUEL = 5,
PANEL_TYPE_LENGTH = 6,
PANEL_TYPE_DURATION = 7,
PANEL_TYPE_TRAJECTORY = 8,
PANEL_TYPE_TIME = 9,
PANEL_TYPE_MUSIC = 10,
```
example config file in `assets/config.txt`

1. hide a panel (i) : `i, 45`:
  * example : `1, 45`
2. show a panel (i) : `i, 46`:
  * example : `1, 46`
3. clean all added element of panel (i):  `i, 44`
  * example : `1, 44`
4. set the data value range of panel (i): `i, 40, min_value, max_value`, (only valid for velocity and rpm pages : 00 & 01 pages)
  * example : `1, 40, 0, 100`
5. add text element to panel (i) at position (x, y) (origin at the center), with font size: `i, 41, x, y, font_size, text`
  * example : `1, 41, 0, 61, 60, CPU %`
  * available font sizes are : 28, 48, 60, 80, 120, 140, 160.
