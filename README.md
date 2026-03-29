# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--29_02:09:03_UTC-green)

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

**2026-03-29 02:09:03 UTC**

- **6,057** aircraft tracked
- **5,493** currently in the air
- **564** on the ground
- **88** countries
- **100** airports with traffic
- **50** airlines identified
- **77** flight routes (last 2h)
- **1h 12m** average flight duration

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Southwest Airlines | 437 |
| 2 | American Airlines | 400 |
| 3 | United Airlines | 369 |
| 4 | Delta Air Lines | 323 |
| 5 | SkyWest Airlines | 154 |
| 6 | Alaska Airlines | 135 |
| 7 | JetBlue | 130 |
| 8 | Air Canada | 104 |
| 9 | FFT | 101 |
| 10 | IndiGo | 86 |
| 11 | ENY | 75 |
| 12 | All Nippon Airways | 68 |
| 13 | WJA | 65 |
| 14 | NKS | 58 |
| 15 | Japan Airlines | 48 |
| 16 | Turkish Airlines | 46 |
| 17 | JST | 44 |
| 18 | Air India | 43 |
| 19 | Republic Airways | 43 |
| 20 | JIA | 39 |
| 21 | Virgin Australia | 37 |
| 22 | Qantas | 36 |
| 23 | ANZ | 35 |
| 24 | AAY | 34 |
| 25 | Cathay Pacific | 33 |
| 26 | EVA Air | 33 |
| 27 | Korean Air | 32 |
| 28 | MXY | 30 |
| 29 | POE | 30 |
| 30 | VOI | 29 |

## Top Countries (by aircraft registration)

| # | Country | Aircraft |
|---:|---------|--------:|
| 1 | 🇺🇸 United States | 3550 |
| 2 | 🇨🇦 Canada | 351 |
| 3 | 🇦🇺 Australia | 313 |
| 4 | 🇨🇳 China | 210 |
| 5 | 🇯🇵 Japan | 196 |
| 6 | 🇮🇳 India | 173 |
| 7 | 🇹🇷 Turkey | 115 |
| 8 | 🏳️ Republic of Korea | 94 |
| 9 | 🇳🇿 New Zealand | 91 |
| 10 | 🇲🇽 Mexico | 73 |
| 11 | 🇬🇧 United Kingdom | 68 |
| 12 | 🇹🇼 Taiwan | 65 |
| 13 | 🇧🇷 Brazil | 48 |
| 14 | 🇲🇾 Malaysia | 46 |
| 15 | 🇫🇷 France | 42 |
| 16 | 🇩🇪 Germany | 39 |
| 17 | 🇵🇭 Philippines | 39 |
| 18 | 🇹🇭 Thailand | 37 |
| 19 | 🇮🇩 Indonesia | 35 |
| 20 | 🇦🇪 United Arab Emirates | 34 |
| 21 | 🇸🇬 Singapore | 33 |
| 22 | 🏳️ Panama | 23 |
| 23 | 🇪🇸 Spain | 22 |
| 24 | 🏳️ Russian Federation | 22 |
| 25 | 🇮🇪 Ireland | 22 |
| 26 | 🏳️ Viet Nam | 21 |
| 27 | 🇨🇱 Chile | 20 |
| 28 | 🇪🇬 Egypt | 17 |
| 29 | 🇪🇹 Ethiopia | 13 |
| 30 | 🇨🇭 Switzerland | 13 |

## Busiest Airports (aircraft on ground)

| # | Airport | City | Country | Aircraft |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport | Dallas-Fort Worth | US | 37 |
| 2 | Tokyo International Airport | Tokyo | JP | 29 |
| 3 | Hartsfield/Jackson Atlanta International Airport | Atlanta | US | 26 |
| 4 | Phoenix Sky Harbor International Airport | Phoenix | US | 24 |
| 5 | San Francisco International Airport | San Francisco | US | 17 |
| 6 | Sydney Kingsford Smith International Airport | Sydney | AU | 17 |
| 7 | Toronto Pearson International Airport | Mississauga | CA | 17 |
| 8 | John F Kennedy International Airport | New York | US | 15 |
| 9 | Denver International Airport | Denver | US | 15 |
| 10 | Harry Reid International Airport | Las Vegas | US | 15 |
| 11 | Chicago O'Hare International Airport | Chicago | US | 13 |
| 12 | Chek Lap Kok International Airport | Hong Kong | HK | 13 |
| 13 | Calgary International Airport | Calgary | CA | 12 |
| 14 | Nashville International Airport | Nashville | US | 11 |
| 15 | Salt Lake City International Airport | Salt Lake City | US | 10 |
| 16 | Vancouver International Airport | Richmond | CA | 9 |
| 17 | Orlando International Airport | Orlando | US | 9 |
| 18 | Washington Dulles International Airport | Washington | US | 9 |
| 19 | St Louis Lambert International Airport | St Louis | US | 8 |
| 20 | Narita International Airport | Tokyo | JP | 8 |
| 21 | Newark Liberty International Airport | Newark | US | 8 |
| 22 | Indira Gandhi International Airport | New Delhi | IN | 7 |
| 23 | Chhatrapati Shivaji International Airport | Mumbai | IN | 7 |
| 24 | Chicago Midway International Airport | Chicago | US | 7 |
| 25 | El Dorado International Airport | Bogota | CO | 7 |
| 26 | General Edward Lawrence Logan International Airport | Boston | US | 7 |
| 27 | Austin-Bergstrom International Airport | Austin | US | 6 |
| 28 | Los Angeles International Airport | Los Angeles | US | 6 |
| 29 | Norman Y Mineta San Jose International Airport | San Jose | US | 5 |
| 30 | Wellington International Airport | Wellington | NZ | 5 |
| 31 | Laguardia Airport | New York | US | 5 |
| 32 | Ted Stevens Anchorage International Airport | Anchorage | US | 5 |
| 33 | Montréal-Pierre Elliott Trudeau International Airport | Dorval | CA | 5 |
| 34 | Perth International Airport | Perth | AU | 5 |
| 35 | Tampa International Airport | Tampa | US | 4 |
| 36 | London Gatwick Airport | London | GB | 4 |
| 37 | Cancun International Airport | Cancun | MX | 4 |
| 38 | Melbourne International Airport | Melbourne | AU | 4 |
| 39 | General Mariano Escobedo International Airport | Monterrey | MX | 4 |
| 40 | San Diego International Airport | San Diego | US | 4 |

## Top Routes (last 2 hours)

| # | From | To | Flights | Avg Duration |
|---:|------|-----|--------:|------------:|
| 1 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 3 | 24m |
| 2 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2 | 14m |
| 3 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 2 | 20m |
| 4 | Daniel K Inouye International Airport (PHNL) | Kahului Airport (PHOG) | 2 | 14m |
| 5 | Taupo Airport (NZAP) | Taupo Airport (NZAP) | 2 | 22m |
| 6 | Liege Airport (EBLG) | Zhuhai Airport (ZGSD) | 1 | 12h 9m |
| 7 | El Dorado International Airport (SKBO) | Alberto Lleras Camargo Airport (SKSO) | 1 | 18m |
| 8 | Quetzalcoatl International Airport (MMNL) | Atizapan De Zaragoza Airport (MMJC) | 1 | 1h 16m |
| 9 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 1 | 1h 55m |
| 10 | Del Norte International Airport (MMAN) | General Servando Canales International Airport (MMMA) | 1 | 28m |
| 11 | Incheon International Airport (RKSI) | Matsumoto Airport (RJAF) | 1 | 1h 7m |
| 12 | Incheon International Airport (RKSI) | G 802 Airport (RKD1) | 1 | 25m |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 1 | 21m |
| 14 | Kuala Lumpur International Airport (WMKK) | Sepulot Airport (WBKO) | 1 | 2h 5m |
| 15 | Diosdado Macapagal International Airport (RPLC) | Mamburao Airport (RPUM) | 1 | 31m |
| 16 | Ninoy Aquino International Airport (RPLL) | Naga Airport (RPUN) | 1 | 26m |
| 17 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 1 | 11h 2m |
| 18 | Bengaluru International Airport (VOBL) | Macau International Airport (VMMC) | 1 | 4h 29m |
| 19 | Gold Coast Airport (YBCG) | Dalby Airport (YDAY) | 1 | 1h 24m |
| 20 | Cessnock Airport (YCNK) | Tamworth Airport (YSTW) | 1 | 51m |
| 21 | Brisbane International Airport (YBBN) | Childers Airport (YCDS) | 1 | 31m |
| 22 | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 1 | 15m |
| 23 | Brisbane International Airport (YBBN) | Monduran Airport (YMUA) | 1 | 33m |
| 24 | Sydney Kingsford Smith International Airport (YSSY) | Sunshine Coast Airport (YBMC) | 1 | 1h 21m |
| 25 | Brisbane International Airport (YBBN) | Braidwood Airport (YBAO) | 1 | 1h 13m |
| 26 | Sydney Bankstown Airport (YSBK) | Walcha Airport (YWCH) | 1 | 51m |
| 27 | Sydney Kingsford Smith International Airport (YSSY) | Glenorchy Airport (NZGY) | 1 | 2h 24m |
| 28 | Pune Airport (VAPO) | Karad Airport (VA1M) | 1 | 10m |
| 29 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 1 | 54m |
| 30 | Tokyo International Airport (RJTT) | Kumamoto Airport (RJFT) | 1 | 1h 20m |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N916ET |  | Denton Enterprise Airport (KDTO) | Denton Enterprise Airport (KDTO) | 2026-03-29 01:08 UTC | 2026-03-29 01:57 UTC | 48m |
| TRP7 | TRP | St Mary's County Regional Airport (K2W6) | Joint Base Andrews Airport (KADW) | 2026-03-29 01:27 UTC | 2026-03-29 01:46 UTC | 18m |
| BRG2682 | BRG | Noatak Airport (PAWN) | Kivalina Airport (PAVL) | 2026-03-29 01:02 UTC | 2026-03-29 01:29 UTC | 26m |
| QTR8766 | Qatar Airways | Liege Airport (EBLG) | Zhuhai Airport (ZGSD) | 2026-03-28 13:14 UTC | 2026-03-29 01:23 UTC | 12h 9m |
| BFP | BFP | Cessnock Airport (YCNK) | Tamworth Airport (YSTW) | 2026-03-29 00:30 UTC | 2026-03-29 01:22 UTC | 51m |
| N618VA |  | San Luis Obispo County Regional Airport (KSBP) | Van Nuys Airport (KVNY) | 2026-03-29 00:27 UTC | 2026-03-29 01:17 UTC | 50m |
| OXW | OXW | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-03-29 00:54 UTC | 2026-03-29 01:09 UTC | 15m |
| N607FJ |  | Ted Stevens Anchorage International Airport (PANC) | Kenai Municipal Airport (PAEN) | 2026-03-29 00:10 UTC | 2026-03-29 01:08 UTC | 58m |
| CPA632 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-03-28 14:02 UTC | 2026-03-29 01:05 UTC | 11h 2m |
| N24775 |  | University Airport (KEDU) | Tracy Municipal Airport (KTCY) | 2026-03-29 00:23 UTC | 2026-03-29 01:02 UTC | 39m |
| ZKTTL | ZKT | Taupo Airport (NZAP) | Taupo Airport (NZAP) | 2026-03-29 00:36 UTC | 2026-03-29 01:01 UTC | 24m |
| N959UA |  | Merrill Field (PAMR) | Homer Airport (PAHO) | 2026-03-28 23:50 UTC | 2026-03-29 00:59 UTC | 1h 9m |
| SKW4913 | SkyWest Airlines | Phoenix Sky Harbor International Airport (KPHX) | Indian Hills Airpark (2AZ1) | 2026-03-29 00:29 UTC | 2026-03-29 00:54 UTC | 24m |
| CFH24 | CFH | Sydney Bankstown Airport (YSBK) | Walcha Airport (YWCH) | 2026-03-29 00:00 UTC | 2026-03-29 00:52 UTC | 51m |
| AXM6051 | AXM | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 2026-03-29 00:27 UTC | 2026-03-29 00:48 UTC | 21m |
| CEB821 | CEB | Ninoy Aquino International Airport (RPLL) | Naga Airport (RPUN) | 2026-03-29 00:21 UTC | 2026-03-29 00:48 UTC | 26m |
| EJA343 | EJA | Dallas Love Field (KDAL) | Dallas-Fort Worth International Airport (KDFW) | 2026-03-29 00:26 UTC | 2026-03-29 00:46 UTC | 19m |
| XFL539 | XFL | Cancun International Airport (MMUN) | General Servando Canales International Airport (MMMA) | 2026-03-28 23:04 UTC | 2026-03-29 00:42 UTC | 1h 38m |
| GLT4 | GLT | Spirit Of St Louis Airport (KSUS) | Piedmont Municipal Airport (KPYN) | 2026-03-29 00:21 UTC | 2026-03-29 00:42 UTC | 20m |
| CPA624 | Cathay Pacific | Bengaluru International Airport (VOBL) | Macau International Airport (VMMC) | 2026-03-28 20:12 UTC | 2026-03-29 00:41 UTC | 4h 29m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
