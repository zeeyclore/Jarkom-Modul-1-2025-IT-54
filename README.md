# Jarkom-Modul-1-2025-K54

| No | Nama                              | NRP         |
|----|-----------------------------------|-------------|
| 1  | Salsa Bil Ulla         | 5027241052 |
| 2  | Hafiz Ramadhan   | 5027241096  |

## Soal 1
![Gambar1](images/img_1.png)
Untuk nomor 1 kurang lebih sama seperti yang ada pada modul GNS3, yaitu menambah/memasukkan:
- Eru: router(ervn-debi)
- 2 Switch/Gateway
- 4 Ainur/Client (Melkor, Manwe, Varda, Ulmo)

## Soal 2
Agar Eru bisa mengakses internet, kita tambahkan:
```
auto eth0
iface eth0 inet dhcp
```
![Gambar2](images/img_2.png)
pada network config nya.

![Gambar2](images/img_2_1.png)

Bisa dilihat Eru sudah bisa melakukan ping ke google.

# Soal 3
Agar client dapat terhubung satu sama lain, kita ubah network config pada Eru terlebih dahulu:
```
auto eth0
iface eth0 inet dhcp

auto eth1
iface eth1 inet static
	address 192.238.1.1
	netmask 255.255.255.0

auto eth2
iface eth2 inet static
	address [Prefix IP].2.1
	netmask 255.255.255.0
```
Lalu untuk masing masing client, kita tambahkan juga kedalam network confignya:
- Melkor
```
auto eth0
iface eth0 inet static
	address 192.238.1.2
	netmask 255.255.255.0
	gateway 192.238.1.1
```
- Manwe
```
auto eth0
iface eth0 inet static
	address 192.238.1.3
	netmask 255.255.255.0
	gateway 192.238.1.1
```
- Varda
```
auto eth0
iface eth0 inet static
	address 192.238.2.2
	netmask 255.255.255.0
	gateway 192.238.2.1
```
- Ulmo
```
auto eth0
iface eth0 inet static
	address 192.238.2.3
	netmask 255.255.255.0
	gateway 192.238.2.1
```

Sekarang, seharusnya client sudah dapat terhubung satu sama lain, bisa kita lihat beberapa contoh dibawah ini:

![Gambar31](images/img_3_1.png)

Bisa dilihat Melkor sudah bisa tersambung ke Ulmo.

![Gambar32](images/img_3_2.png)

Varda juga sudah dapat terhubung ke Manwe.

![Gambar33](images/img_3_3.png)

Ulmo dan Manwe juga sudah bisa.

## Soal 4
Agar setiap client dapat tersambung ke internet, lakukan:

![Gambar41](images/img_4_1.png)

```
cat /etc/resolv.conf
```

untuk melihat isi file konfigurasi DNS resolver di Eru.

Lalu gunakan:
```
echo nameserver 192.168.122.1 > /etc/resolv.conf
```

pada setiap client, untuk mengarahkan semua permintaan DNS ke DNS NAT-nya GNS3

setelah itu gunakan:
```
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE -s 192.238.0.0/16
```

Sekarang setiap client sudah dapat tersambung ke internet

![Gambar42](images/img_4_2.png)


## Soal 14
```
nc 10.15.43.32 3401
```
#### FLAG
```
KOMJAR25{Brut3_F0rc3_5JqXUmMFjVeW8AuDcq9rR0aaQ}
```
<img width="1057" height="534" alt="image" src="https://github.com/user-attachments/assets/a94cb403-7904-4f09-926f-ff031b4d27b9" />

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
<img width="687" height="123" alt="image" src="https://github.com/user-attachments/assets/90dd813b-f262-474b-94d1-e8ed96d4fc46" />

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

## Soal 15
```
nc 10.15.43.32 3402
```
#### FLAG
```
KOMJAR25{K3yb0ard_W4rr10r_V9IxfCMHIM9BsNAY34P4AN2L4}
```
<img width="1249" height="459" alt="image" src="https://github.com/user-attachments/assets/241177d6-2777-4c56-abaf-3fcbb644db0e" />

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
<img width="1087" height="168" alt="image" src="https://github.com/user-attachments/assets/59435fff-f487-4733-b883-f7182cb717e2" />
> [awok.txt](https://github.com/zeeyclore/Jarkom-Modul-1-2025-K54/blob/main/awok.txt)

Buat script dengan `nano [nama script].py` untuk membaca hasil file log `.txt` yang berisikan data HID berbentuk hex.
<img width="1108" height="480" alt="image" src="https://github.com/user-attachments/assets/3227401e-158c-4129-9b8d-095d62096f8e" />
> [awokdecode.py](https://github.com/zeeyclore/Jarkom-Modul-1-2025-K54/blob/main/awokdecode.py)

Jalankan `python3 [nama script].py` dan hasil sudah muncul di output langsung.
<img width="926" height="200" alt="image" src="https://github.com/user-attachments/assets/2aca6e00-4755-48f3-9691-d393dcd94af0" />

#### Q3: What is Melkor's secret message? (Format: string)
```
> Plz_pr0v1de_y0ur_us3rn4me_4nd_p4ssw0rd
```
Dari hasil script tadi, di-decode dengan tools `CyberChef From Base64`.
<img width="1597" height="412" alt="image" src="https://github.com/user-attachments/assets/a43ea62b-a1d6-46b1-82af-2f1919e43f10" />

## Soal 16
```
nc 10.15.43.32 3403
```
#### FLAG
```
KOMJAR25{Y0u_4r3_4_g00d_4nalyz3r_N9uTF98Yt2wXd1FKlRK3hsdkr}
```
<img width="1466" height="876" alt="image" src="https://github.com/user-attachments/assets/4ce4126f-0d1d-4e20-998f-f252792e02d7" />

#### Q1: What credential did the attacker use to log in? (Format: user:pass)
```
> ind@psg420.com:{6r_6e#TfT1p
```
Ketik `ftp || ftp-data` pada kolom filter, lalu informasi terkait user dan pass akan terlihat.
<img width="1164" height="281" alt="image" src="https://github.com/user-attachments/assets/30a0d68f-a998-42eb-b5a9-30ebbe6be0c9" />

#### Q2: How many files are suspected of containing malware? (Format: int)
```
> 5
```
Ketik `ftp.request.command == "RETR"` pada kolom filter untuk memunculkan file-file yang kemungkinan berbahaya.
<img width="1920" height="285" alt="image" src="https://github.com/user-attachments/assets/7b45d932-71e6-4f44-b334-57849a4d9973" />

#### Q3: What is the hash of the first file (q.exe)? (Format: sha256)
```
> ca34b0926cdc3242bbfad1c4a0b42cc2750d90db9a272d92cfb6cb7034d2a3bd
```
Cari port dari tiap file `.exe` tadi dengan `tshark -r MelkorPlan1.pcap -Y "ftp-data" -T fields -e tcp.srcport -e tcp.dstport | sort -u | tail -5` agar mudah untuk ekspor nantinya.
<img width="1451" height="151" alt="image" src="https://github.com/user-attachments/assets/73a7f58a-94fa-4be6-8921-61354e19941f" />

Jalankan `tshark -r MelkorPlan1.pcap -Y "tcp.port == 51889 && tcp.len > 0" -T fields -e tcp.payload | xxd -r -p > q_exe_final.bin` di terminal, lalu jalankan `sha256sum q_exe_final.bin` untuk mendapatkan hasil hash `q.exe`.
<img width="1467" height="175" alt="image" src="https://github.com/user-attachments/assets/fb949722-724a-4e44-947e-a7826005d8d5" />

#### Q4: What is the hash of the second file (w.exe)? (Format: sha256)
```
> 08eb941447078ef2c6ad8d91bb2f52256c09657ecd3d5344023edccf7291e9fc
```
Jalankan `tshark -r MelkorPlan1.pcap -Y "tcp.port == 59785 && tcp.len > 0" -T fields -e tcp.payload | xxd -r -p > w_exe_final.bin` di terminal, lalu jalankan `sha256sum w_exe_final.bin` untuk mendapatkan hasil hash `w.exe`.
<img width="1470" height="159" alt="image" src="https://github.com/user-attachments/assets/cff78d90-433c-4362-8a60-9eedfe96ac36" />

#### Q5: What is the hash of the third file (e.exe)? (Format: sha256)
```
> 32e1b3732cd779af1bf7730d0ec8a7a87a084319f6a0870dc7362a15ddbd3199
```
Jalankan `tshark -r MelkorPlan1.pcap -Y "tcp.port == 59785 && tcp.len > 0" -T fields -e tcp.payload | xxd -r -p > e_exe_final.bin` di terminal, lalu jalankan `sha256sum e_exe_final.bin` untuk mendapatkan hasil hash `e.exe`.
<img width="1470" height="159" alt="image" src="https://github.com/user-attachments/assets/b55d7efc-2830-4f25-90b0-ea7d3ad00879" />

#### Q6: What is the hash of the fourth file (r.exe)? (Format: sha256)
```
> 4ebd58007ee933a0a8348aee2922904a7110b7fb6a316b1c7fb2c6677e613884
```
Jalankan `tshark -r MelkorPlan1.pcap -Y "tcp.port == 59785 && tcp.len > 0" -T fields -e tcp.payload | xxd -r -p > r_exe_final.bin` di terminal, lalu jalankan `sha256sum r_exe_final.bin` untuk mendapatkan hasil hash `r.exe`.
<img width="1470" height="159" alt="image" src="https://github.com/user-attachments/assets/5ec1f288-5321-460e-b06e-1b5f1ae880c1" />

#### Q7: What is the hash of the fifth file (t.exe)? (Format: sha256)
```
> 10ce4b79180a2ddd924fdc95951d968191af2ee3b7dfc96dd6a5714dbeae613a
```
Jalankan `tshark -r MelkorPlan1.pcap -Y "tcp.port == 59785 && tcp.len > 0" -T fields -e tcp.payload | xxd -r -p > t_exe_final.bin` di terminal, lalu jalankan `sha256sum t_exe_final.bin` untuk mendapatkan hasil hash `t.exe`.
<img width="1470" height="159" alt="image" src="https://github.com/user-attachments/assets/f3879f77-c4a9-4bc3-aa39-d5b321888193" />

## Soal 17
```
nc 10.15.43.32 3404
```
#### FLAG
```
KOMJAR25{M4ster_4n4lyzer_IUP0UnMxzseaMoArxrNlbTRTZ}
```
<img width="1415" height="511" alt="image" src="https://github.com/user-attachments/assets/476e7a32-7795-465e-a261-010099e631c4" />

#### Q1: What is the name of the first suspicious file? (Format: file.exe)
```
> Invoice&MSO-Request.doc
```
Jalankan `tshark -r MelkorPlan2.pcap --export-objects http,all_files ls -la all_files/` lalu file yang terdownload akan otomatis terlihat dan yang pertama adalah `Invoice&MSO-Request.doc`.
<img width="1446" height="223" alt="image" src="https://github.com/user-attachments/assets/b5bce701-cf6a-4e05-9677-3480148b6269" />
<img width="1417" height="170" alt="image" src="https://github.com/user-attachments/assets/3f979922-06cd-4733-8a19-9c369cc233b0" />

#### Q2: What is the name of the second suspicious file? (Format: file.exe)
```
> knr.exe
```
Hasil dapat terlihat dari command di `Q1`.
<img width="1417" height="170" alt="image" src="https://github.com/user-attachments/assets/3f979922-06cd-4733-8a19-9c369cc233b0" />

#### Q3: What is the hash of the second suspicious file (knr.exe)? (Format: sha256)
```
> 749e161661290e8a2d190b1a66469744127bc25bf46e5d0c6f2e835f4b92db18
```
Jalankan `sha256sum knr.exe`.
<img width="1293" height="162" alt="image" src="https://github.com/user-attachments/assets/d195af41-86dd-42ee-96de-1a47466d80ec" />

## Soal 18
```
nc 10.15.43.32 3405
```
#### FLAG
```
KOMJAR25{Y0u_4re_g0dl1ke_4qZjUyll3QSeU81aIRWVst5DP}
```
<img width="1464" height="673" alt="image" src="https://github.com/user-attachments/assets/90344a89-439f-4934-9d40-dca73103e02a" />

#### Q1: How many files are suspected of containing malware? (Format: int)
```
> 2
```
Jalankan `ls -la http_files/ smb_files/` maka akan terlihat ada 2 file `.exe` dengan awalan `WINDOWS` dan nama file mencurigakan.
<img width="1209" height="132" alt="image" src="https://github.com/user-attachments/assets/27893365-a1af-4878-b769-39fa3bd6962c" />
<img width="1462" height="219" alt="image" src="https://github.com/user-attachments/assets/97f9159e-90a4-4770-ad68-376b240fff0d" />

#### Q2: What is the name of the first malicious file? (Format: file.exe)
```
> d0p2nc6ka3f_fixhohlycj4ovqfcy_smchzo_ub83urjpphrwahjwhv_o5c0fvf6.exe
```
Dari hasil command di `Q1` sudah menunjukkan nama file aneh.
<img width="1462" height="219" alt="image" src="https://github.com/user-attachments/assets/97f9159e-90a4-4770-ad68-376b240fff0d" />

#### Q3: Apa nama file berbahaya yang kedua? (Format: file.exe)
```
> oiku9bu68cxqenfmcsos2aek6t07_guuisgxhllixv8dx2eemqddnhyh46l8n_di.exe
```
Dari hasil command di `Q1` sudah menunjukkan nama file aneh.
<img width="1462" height="219" alt="image" src="https://github.com/user-attachments/assets/97f9159e-90a4-4770-ad68-376b240fff0d" />

#### Q4: What is the hash of the first malicious file? (Format: sha256)
```
> 59896ae5f3edcb999243c7bfdc0b17eb7fe28f3a66259d797386ea470c010040
```
Jalankan `sha256sum "smb_files/%5cWINDOWS%Scd0p2nc6ka3f_fixhohlycj4ovqfcy_smchzo_ub83urjpphrwahjwhv_o5c0fvf6.exe"` di terminal, hash akan langsung ter-print.
<img width="1468" height="106" alt="image" src="https://github.com/user-attachments/assets/63eca46c-e751-416d-b982-9eef05a1161c" />

#### Q5: What is the hash of the second malicious file? (Format: sha256)
```
> cf99990bee6c378cbf56239b3cc88276eec348d82740f84e9d5c343751f82560
```
Jalankan `sha256sum "smb_files/%5cWINDOWS%Scoiku9bu68cxqenfmcsos2aek6t07_guuisgxhllixv8dx2eemqddnhyh46l8n_di.exe"` di terminal, hash akan langsung ter-print.
<img width="1468" height="103" alt="image" src="https://github.com/user-attachments/assets/ab928dde-e096-48d4-af86-2a4ce198451f" />

## Soal 19
```
nc 10.15.43.32 3406
```
#### FLAG
```
KOMJAR25{Y0u_4re_J4rk0m_G0d_kBdVLljgIyR9nnyqSFd3cjC87}
```
<img width="1468" height="471" alt="image" src="https://github.com/user-attachments/assets/c6ea7daf-8c74-4766-99db-caaea4c941ca" />

#### Q1: Who sent the threatening message? (Format: string (name))
```
> Your Life
```
Jalankan `smtp.req.command == "MAIL"` agar menampilkan seluruh pesan dari log. Pesan paling banyak berasal dari akun `YourLife[...]@[...].com`.
<img width="1920" height="363" alt="image" src="https://github.com/user-attachments/assets/d50c44e2-b460-4355-93bb-086ab6d3028d" />

Jika melakukan `Follow TCP Stream` akan terlihat isi dari log tersebut dan nama utama dari email tersebut adalah `Your Life`.
<img width="647" height="79" alt="image" src="https://github.com/user-attachments/assets/b1be254e-a302-49c5-b7ce-8eb807737d17" />

#### Q2: How much ransom did the attacker demand ($)? (Format: int)
```
> 1600
```
Masih dengan cara yang sama dari `Q1`, jumlah uang yang diinginkan oleh attacker disebutkan di dalam pesan.
<img width="699" height="96" alt="image" src="https://github.com/user-attachments/assets/b86811e0-e7e8-46e3-9f2b-4b0eeb7632c2" />

#### Q3: What is the attacker's bitcoin wallet? (Format: string)
```
> 1CWHmuF8dHt7HBGx5RKKLgg9QA2GmE3UyL
```
Masih dengan cara yang sama dari `Q1`, dompet bitcoin attacker disebutkan di dalam pesan.
<img width="699" height="96" alt="image" src="https://github.com/user-attachments/assets/5c0371f4-b927-4671-abab-6e4368d36305" />

## Soal 20
```
nc 10.15.43.32 3407
```
#### FLAG
```
KOMJAR25{B3ware_0f_M4lw4re_AGCe0yhAX9U82C38E4Ow72nEP}
```
<img width="1366" height="472" alt="image" src="https://github.com/user-attachments/assets/1b90124d-403d-4c08-91e5-eabcbedf3131" />

#### Q1: What encryption method is used? (Format: string)
```
> TLS
```
Dalam folder zip terdapat 2 file yaitu `MelkorPlan5.pcap` dan `keyslogfile.txt`. Saat dibuka, `keyslogfile.txt` menunjukkan teks `CLIENT RANDOM` yang biasa digunakan untuk decrypt TLS traffic di Wireshark.
<img width="1460" height="644" alt="image" src="https://github.com/user-attachments/assets/4d4d97e0-e4ae-4077-bac1-1485b80f295e" />

#### Q2: What is the name of the malicious file placed by the attacker? (Format: file.exe)
```
> invest_20.dll
```
Setelah membuka `MelkorPlan5.pcap` pada Wireshark, lakukan `CTRL + SHIFT + P` atau dapat pergi ke `Edit` pada pojok kiri atas lalu ke `Preferences..`. Lalu ke `Protocols` dan cari `TLS`. Pada `(Pre)-Master-Secret log filename`, lakukan `Browse...` dan cari file `keyslogfile.txt` di komputer. Setelah itu bisa langsung `Apply` dan klik `OK`.
<img width="1017" height="725" alt="image" src="https://github.com/user-attachments/assets/f75cd0d0-afd1-4871-bfb8-ae5e868ddda8" />

Nanti packet number `165` akan berubah yang tadinya `TLSv1.2` menjadi `HTTP`. Info terbuka menunjukkan `GET /invest_20.dll HTTP/1.1` yang di mana adalah file malicous.
<img width="1159" height="83" alt="image" src="https://github.com/user-attachments/assets/74bff8d4-d484-4d31-a9a4-44894304193d" />
<img width="1157" height="81" alt="image" src="https://github.com/user-attachments/assets/bac57670-5ecb-42ce-9a75-eacece6dc9b4" />

#### Q3: What is the hash of the file containing the malware? (Format: sha256)
```
>  31cf42b2a7c5c558f44cfc67684cc344c17d4946d3a1e0b2cecb8eb58173cb2f
```
Jalankan `tshark -r MelkorPlan5.pcap -o tls.keylog_file:keyslogfile.txt -Y "ip.addr==94.103.84.245 and tcp.port==50074" --export-objects http,export_folder` di terminal.
<img width="1464" height="225" alt="image" src="https://github.com/user-attachments/assets/89c3955c-20db-49bb-8a98-442784efd4ef" />

Lalu jalankan `sha256sum invest_20.dll
<img width="975" height="63" alt="image" src="https://github.com/user-attachments/assets/4bd0dc95-b85c-406b-9931-84798813f38f" />
