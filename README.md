# Jarkom-Modul-1-2025-IT-54

| No | Nama                              | NRP         |
|----|-----------------------------------|-------------|
| 1  | Salsa Bil Ulla         | 5027241052 |
| 2  | Hafiz Ramadhan   | 5027241096  |

## Soal 14
```
nc 10.15.43.32 3401
```

#### Q1: How many packets are recorded in the pcapng file? (Format: int)
```
> 500358
```
Buka Wireshark dan buka `shortbf.pcapng`, maka akan terlihat jumlah paket di kanan bawah.
<img width="361" height="152" alt="image" src="https://github.com/user-attachments/assets/d18b4e20-1793-4f7b-8b43-062f9290f121" />

#### Q2: What are the user that successfully logged in? (Format: user:pass)
```
> n1enna:y4v4nn4_k3m3nt4r1
```
Masukkan `http contains "success"` pada kolom filter.
<img width="990" height="197" alt="image" src="https://github.com/user-attachments/assets/206c5bcb-0f1c-4f63-b532-d3bb6e1d0eb2" />
Lalu klik kanan packet untuk `Follow HTTP Stream`.
<img width="687" height="123" alt="image" src="https://github.com/user-attachments/assets/90dd813b-f262-474b-94d1-e8ed96d4fc46" />\

#### Q3: In which stream were the credentials found? (Format: int)
```
> 41824
```
Pada details, scroll ke bagian `Tranmission Control Protocol` hingga menemukan `Stream index`.
<img width="827" height="406" alt="image" src="https://github.com/user-attachments/assets/214503b2-7e89-4e5a-b38b-9d683bd02f9a" />

#### Q4: What tools are used for brute force? (Format: Hydra v1.8.0-dev)
```
> Fuzz Faster U Fool v2.1.0-dev
```
Klik kanan pada packet, lalu `Follow HTTP Stream`, tools tertera pada `User-Agent`.
<img width="505" height="136" alt="image" src="https://github.com/user-attachments/assets/4b7db386-02ee-4f37-9f7e-446cda380bad" />

#### FLAG
```
KOMJAR25{Brut3_F0rc3_5JqXUmMFjVeW8AuDcq9rR0aaQ}
```

## Soal 15
```
nc 10.15.43.32 3402
```

#### Q1: What device does Melkor use? (Format: string)
```
> Keyboard
```
Pada details di salah satu packet, tertera jika usage menggunakan USB Keyboard.
<img width="842" height="307" alt="image" src="https://github.com/user-attachments/assets/e4d83c97-be48-464b-8898-476608ba2129" />

#### Q2: What did Melkor write? (Format: string)
```
> UGx6X3ByMHYxZGVfeTB1cl91czNybjRtZV80bmRfcDRzc3cwcmQ=
```
Ketik `usb.transfer_type == 0x01` pada filter, lalu simpan sebagai `plain text` melalui `File`.
> awok.txt
<img width="1087" height="168" alt="image" src="https://github.com/user-attachments/assets/59435fff-f487-4733-b883-f7182cb717e2" />
Buat script dengan `nano [nama script].py` untuk membaca hasil file log `.txt` yang berisikan data HID berbentuk hex.
> awokdecode.py
<img width="1108" height="480" alt="image" src="https://github.com/user-attachments/assets/3227401e-158c-4129-9b8d-095d62096f8e" />
Jalankan `python3 [nama script].py` dan hasil sudah muncul di output langsung.
<img width="926" height="200" alt="image" src="https://github.com/user-attachments/assets/2aca6e00-4755-48f3-9691-d393dcd94af0" />

#### Q3: What is Melkor's secret message? (Format: string)
```
> Plz_pr0v1de_y0ur_us3rn4me_4nd_p4ssw0rd
```
Dari hasil script tadi, di-decode dengan tools `CyberChef From Base64`.
<img width="1597" height="412" alt="image" src="https://github.com/user-attachments/assets/a43ea62b-a1d6-46b1-82af-2f1919e43f10" />

#### FLAG
```
KOMJAR25{K3yb0ard_W4rr10r_V9IxfCMHIM9BsNAY34P4AN2L4}
```

## Soal 16
```
nc
```

#### Q1: 
```
> 
```

#### Q2: 
```
> 
```

#### Q3: 
```
> 
```

#### Q4: 
```
> 
```

#### FLAG
```

```

## Soal 16
```
nc
```

#### Q1: 
```
> 
```

#### Q2: 
```
> 
```

#### Q3: 
```
> 
```

#### Q4: 
```
> 
```

#### FLAG
```

```

