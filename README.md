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

### FLAG
```
KOMJAR25{Brut3_F0rc3_5JqXUmMFjVeW8AuDcq9rR0aaQ}
```
