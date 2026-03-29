# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--29_06:03:48_UTC-green)

![Flight Map](images/flight_map.png)

## About

Real-time tracking of global air traffic using the [OpenSky Network](https://opensky-network.org/) API. This repository automatically fetches live aircraft positions worldwide and generates visualizations and statistics.

**Data Source:** OpenSky Network REST API (`/states/all`)

**Update Frequency:** Every 5 minutes via GitHub Actions

**How it works:**
- Fetches all aircraft transponder data globally
- Maps on-ground aircraft to nearest airports (28,000+ airport database)
- Identifies airlines from ICAO callsign prefixes
- Generates a live flight map and summary statistics

## Live Snapshot

**2026-03-29 06:03:48 UTC**

- **4,978** aircraft tracked
- **4,422** currently in the air
- **556** on the ground
- **90** countries
- **100** airports with traffic
- **50** airlines identified
- **58** flight routes (last 2h)
- **1h 25m** average flight duration

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 329 |
| 2 | Turkish Airlines | 135 |
| 3 | Southwest Airlines | 121 |
| 4 | American Airlines | 109 |
| 5 | United Airlines | 96 |
| 6 | Delta Air Lines | 95 |
| 7 | Lufthansa | 95 |
| 8 | Air France | 95 |
| 9 | IndiGo | 93 |
| 10 | EJU | 93 |
| 11 | easyJet | 83 |
| 12 | KLM Royal Dutch | 73 |
| 13 | Vueling | 71 |
| 14 | British Airways | 63 |
| 15 | Alaska Airlines | 57 |
| 16 | All Nippon Airways | 54 |
| 17 | EWG | 53 |
| 18 | Swiss International | 53 |
| 19 | Air India | 52 |
| 20 | Qantas | 48 |
| 21 | Scandinavian Airlines | 46 |
| 22 | Japan Airlines | 45 |
| 23 | Wizz Air | 40 |
| 24 | Virgin Australia | 39 |
| 25 | FFT | 37 |
| 26 | Cathay Pacific | 37 |
| 27 | JetBlue | 36 |
| 28 | JST | 36 |
| 29 | SXS | 36 |
| 30 | Austrian Airlines | 35 |

## Top Countries (by aircraft registration)

| # | Country | Aircraft |
|---:|---------|--------:|
| 1 | 🇺🇸 United States | 1013 |
| 2 | 🇦🇺 Australia | 289 |
| 3 | 🇬🇧 United Kingdom | 249 |
| 4 | 🇮🇪 Ireland | 235 |
| 5 | 🇹🇷 Turkey | 233 |
| 6 | 🇨🇳 China | 214 |
| 7 | 🇮🇳 India | 190 |
| 8 | 🇩🇪 Germany | 190 |
| 9 | 🇯🇵 Japan | 182 |
| 10 | 🇪🇸 Spain | 164 |
| 11 | 🏳️ Malta | 162 |
| 12 | 🇫🇷 France | 149 |
| 13 | 🇨🇦 Canada | 132 |
| 14 | 🇦🇹 Austria | 127 |
| 15 | 🏳️ Republic of Korea | 99 |
| 16 | 🏳️ Kingdom of the Netherlands | 97 |
| 17 | 🇨🇭 Switzerland | 82 |
| 18 | 🇵🇱 Poland | 78 |
| 19 | 🇹🇼 Taiwan | 64 |
| 20 | 🇸🇪 Sweden | 59 |
| 21 | 🏳️ Hungary | 53 |
| 22 | 🇹🇭 Thailand | 50 |
| 23 | 🇳🇿 New Zealand | 46 |
| 24 | 🇲🇾 Malaysia | 46 |
| 25 | 🇦🇪 United Arab Emirates | 45 |
| 26 | 🏳️ Greece | 43 |
| 27 | 🇵🇹 Portugal | 41 |
| 28 | 🇮🇩 Indonesia | 38 |
| 29 | 🇲🇽 Mexico | 35 |
| 30 | 🇫🇮 Finland | 34 |

## Busiest Airports (aircraft on ground)

| # | Airport | City | Country | Aircraft |
|---:|---------|------|---------|--------:|
| 1 | Tokyo International Airport | Tokyo | JP | 24 |
| 2 | Zurich Airport | Zurich | CH | 21 |
| 3 | San Francisco International Airport | San Francisco | US | 21 |
| 4 | Chek Lap Kok International Airport | Hong Kong | HK | 18 |
| 5 | Los Angeles International Airport | Los Angeles | US | 17 |
| 6 | Frankfurt am Main International Airport | Frankfurt am Main | DE | 17 |
| 7 | Phoenix Sky Harbor International Airport | Phoenix | US | 16 |
| 8 | Calgary International Airport | Calgary | CA | 15 |
| 9 | Harry Reid International Airport | Las Vegas | US | 14 |
| 10 | Indira Gandhi International Airport | New Delhi | IN | 13 |
| 11 | London Gatwick Airport | London | GB | 13 |
| 12 | Vienna International Airport | Vienna | AT | 13 |
| 13 | Paris-Orly Airport | Paris | FR | 11 |
| 14 | Denver International Airport | Denver | US | 11 |
| 15 | Malpensa International Airport | Milan | IT | 10 |
| 16 | Sydney Kingsford Smith International Airport | Sydney | AU | 10 |
| 17 | Netaji Subhash Chandra Bose International Airport | Kolkata | IN | 9 |
| 18 | Eleftherios Venizelos International Airport | Athens | GR | 9 |
| 19 | Toronto Pearson International Airport | Mississauga | CA | 9 |
| 20 | Vancouver International Airport | Richmond | CA | 8 |
| 21 | Perth International Airport | Perth | AU | 8 |
| 22 | Narita International Airport | Tokyo | JP | 7 |
| 23 | Chhatrapati Shivaji International Airport | Mumbai | IN | 7 |
| 24 | Stockholm-Arlanda Airport | Stockholm | SE | 7 |
| 25 | Charles de Gaulle International Airport | Paris | FR | 7 |
| 26 | Melbourne International Airport | Melbourne | AU | 7 |
| 27 | General Edward Lawrence Logan International Airport | Boston | US | 6 |
| 28 | Tallinn Airport | Tallinn | EE | 6 |
| 29 | John F Kennedy International Airport | New York | US | 6 |
| 30 | Kaohsiung International Airport | Kaohsiung City | TW | 6 |
| 31 | Seattle-Tacoma International Airport | Seattle | US | 6 |
| 32 | Amsterdam Airport Schiphol | Amsterdam | NL | 6 |
| 33 | Laguardia Airport | New York | US | 5 |
| 34 | Manchester Airport | Manchester | GB | 5 |
| 35 | Norman Y Mineta San Jose International Airport | San Jose | US | 5 |
| 36 | Orlando International Airport | Orlando | US | 5 |
| 37 | Salt Lake City International Airport | Salt Lake City | US | 4 |
| 38 | San Diego International Airport | San Diego | US | 4 |
| 39 | Helsinki Vantaa Airport | Helsinki | FI | 4 |
| 40 | Bristol International Airport | Bristol | GB | 4 |

## Top Routes (last 2 hours)

| # | From | To | Flights | Avg Duration |
|---:|------|-----|--------:|------------:|
| 1 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 2 | 12m |
| 2 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 2 | 1h 40m |
| 3 | Marina Municipal Airport (KOAR) | San Carlos Airport (KSQL) | 2 | 18m |
| 4 | Miami International Airport (KMIA) | Atizapan De Zaragoza Airport (MMJC) | 1 | 4h 59m |
| 5 | Chhatrapati Shivaji International Airport (VABB) | Purnea Airport (VEPU) | 1 | 1h 59m |
| 6 | Eleftherios Venizelos International Airport (LGAV) | Olimboi Airport (LG56) | 1 | 25m |
| 7 | Eleftherios Venizelos International Airport (LGAV) | Ikaria Airport (LGIK) | 1 | 29m |
| 8 | John Paul II International Airport Kraków-Balice Airport (EPKK) | Otocac Airport (LDRO) | 1 | 54m |
| 9 | Torino / Caselle International Airport (LIMF) | Oristano / Fenosu Airport (LIER) | 1 | 50m |
| 10 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 1 | 26m |
| 11 | Ulu Bernam Airport (WMBF) | Batu Pahat Airport (WMAB) | 1 | 23m |
| 12 | Kuala Lumpur International Airport (WMKK) | Sepulot Airport (WBKO) | 1 | 2h 2m |
| 13 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 1 | 23m |
| 14 | Ninoy Aquino International Airport (RPLL) | Romblon Airport (RPVU) | 1 | 25m |
| 15 | Beijing Capital International Airport (ZBAA) | Macau International Airport (VMMC) | 1 | 2h 44m |
| 16 | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 1 | 14h 35m |
| 17 | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 1 | 11h 55m |
| 18 | Wollongong Airport (YWOL) | Wollongong Airport (YWOL) | 1 | 11m |
| 19 | YSMB (YSMB) | Sydney Bankstown Airport (YSBK) | 1 | 18m |
| 20 | Narrabri Airport (YNBR) | Collarenebri Airport (YCBR) | 1 | 21m |
| 21 | Brisbane International Airport (YBBN) | Pacific Haven Airport (YPAC) | 1 | 34m |
| 22 | Sydney Kingsford Smith International Airport (YSSY) | Bunyan Airfield (YBUY) | 1 | 42m |
| 23 | Sydney Kingsford Smith International Airport (YSSY) | Ballina Byron Gateway Airport (YBNA) | 1 | 1h 8m |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 1 | 52m |
| 25 | Indira Gandhi International Airport (VIDP) | Zhuhai Airport (ZGSD) | 1 | 4h 18m |
| 26 | Bengaluru International Airport (VOBL) | Arkonam Airport (VOAR) | 1 | 22m |
| 27 | Chhatrapati Shivaji International Airport (VABB) | Tirupati Airport (VOTP) | 1 | 1h 12m |
| 28 | Matsumoto Airport (RJAF) | Matsumoto Airport (RJAF) | 1 | 10m |
| 29 | Nagoya Airport (RJNA) | Yamagata Airport (RJSC) | 1 | 36m |
| 30 | Fukuoka Airport (RJFF) | Takamatsu Airport (RJOT) | 1 | 29m |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N496AE |  | Spirit Of St Louis Airport (KSUS) | Spirit Of St Louis Airport (KSUS) | 2026-03-29 05:19 UTC | 2026-03-29 05:49 UTC | 30m |
| N851MB |  | Greeley-Weld County Airport (KGXY) | Buckley Space Force Base Airport (KBKF) | 2026-03-29 05:12 UTC | 2026-03-29 05:36 UTC | 23m |
| XSN82 | XSN | Marina Municipal Airport (KOAR) | San Carlos Airport (KSQL) | 2026-03-29 05:12 UTC | 2026-03-29 05:31 UTC | 18m |
| XSN06 | XSN | Marina Municipal Airport (KOAR) | San Carlos Airport (KSQL) | 2026-03-29 05:10 UTC | 2026-03-29 05:28 UTC | 17m |
| CPA841 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-03-28 14:40 UTC | 2026-03-29 05:15 UTC | 14h 35m |
| ESF612 | ESF | Miami International Airport (KMIA) | Atizapan De Zaragoza Airport (MMJC) | 2026-03-29 00:11 UTC | 2026-03-29 05:11 UTC | 4h 59m |
| CFH3 | CFH | YSMB (YSMB) | Sydney Bankstown Airport (YSBK) | 2026-03-29 04:51 UTC | 2026-03-29 05:10 UTC | 18m |
| IGO1721 | IndiGo | Indira Gandhi International Airport (VIDP) | Zhuhai Airport (ZGSD) | 2026-03-29 00:48 UTC | 2026-03-29 05:07 UTC | 4h 18m |
| JA02NA |  | Matsumoto Airport (RJAF) | Matsumoto Airport (RJAF) | 2026-03-29 04:52 UTC | 2026-03-29 05:03 UTC | 10m |
| CPA238 | Cathay Pacific | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-03-28 17:05 UTC | 2026-03-29 05:01 UTC | 11h 55m |
| CRN711 | CRN | Vancouver International Airport (CYVR) | Banff Airport (CYBA) | 2026-03-29 04:03 UTC | 2026-03-29 04:56 UTC | 52m |
| RYR40HE | Ryanair | Torino / Caselle International Airport (LIMF) | Oristano / Fenosu Airport (LIER) | 2026-03-29 04:03 UTC | 2026-03-29 04:54 UTC | 50m |
| N915SH |  | Joe Foss Field (KFSD) | Gregory Municipal/Flynn Field (K9D1) | 2026-03-29 04:23 UTC | 2026-03-29 04:53 UTC | 30m |
| AAL559 | American Airlines | Phoenix Sky Harbor International Airport (KPHX) | Harry Reid International Airport (KLAS) | 2026-03-29 04:00 UTC | 2026-03-29 04:52 UTC | 51m |
| CRK305 | CRK | Beijing Capital International Airport (ZBAA) | Macau International Airport (VMMC) | 2026-03-29 02:02 UTC | 2026-03-29 04:47 UTC | 2h 44m |
| FD212 |  | Narrabri Airport (YNBR) | Collarenebri Airport (YCBR) | 2026-03-29 04:25 UTC | 2026-03-29 04:47 UTC | 21m |
| EMD1 | EMD | Wichita Dwight D Eisenhower Ntl Airport (KICT) | 7Up Ranch Airport (75KS) | 2026-03-29 04:14 UTC | 2026-03-29 04:43 UTC | 29m |
| ARR352 | ARR | William P Hobby Airport (KHOU) | Wildwood Airport (XA91) | 2026-03-29 04:25 UTC | 2026-03-29 04:41 UTC | 16m |
| RYR7273 | Ryanair | John Paul II International Airport Kraków-Balice Airport (EPKK) | Otocac Airport (LDRO) | 2026-03-29 03:46 UTC | 2026-03-29 04:41 UTC | 54m |
| LR455 |  | Brisbane International Airport (YBBN) | Pacific Haven Airport (YPAC) | 2026-03-29 04:05 UTC | 2026-03-29 04:39 UTC | 34m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
