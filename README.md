# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--02_21:46:33_UTC-green)

![Flight Map](images/flight_map.png)

## About

Historical archive of saved air traffic routes collected from the [OpenSky Network](https://opensky-network.org/) API. This repository keeps appending completed flights to `data/flights/` and rebuilds the visuals from the full archive.

**Data Source:** Saved route files in `data/flights/` (originally fetched from OpenSky `/flights/all`)

**Update Frequency:** Every 5 minutes via GitHub Actions

**How it works:**
- Fetches recently completed routes from OpenSky
- Saves each route as a JSON file in `data/flights/`
- Rebuilds aggregate statistics from all saved historical routes
- Generates a historical route map and archive summary
- Generates daily reports, weekly leaderboards, and timelapse GIFs

## Route Timelapse

![Timelapse](images/timelapse.gif)

## Archive Snapshot

**Latest saved flight:** 2026-04-02 21:46:33 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-02 21:46:33 UTC

- **12,205** saved flights
- **6,986** unique routes
- **111** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **12,205** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **151,477.2 tonnes** estimated CO2 emissions
- **8,781,288 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 540 |
| 2 | Ryanair | 481 |
| 3 | IndiGo | 329 |
| 4 | EJA | 240 |
| 5 | American Airlines | 225 |
| 6 | Lufthansa | 194 |
| 7 | Southwest Airlines | 183 |
| 8 | ENY | 160 |
| 9 | Vueling | 131 |
| 10 | LATAM Airlines | 125 |
| 11 | AXM | 120 |
| 12 | LXJ | 114 |
| 13 | All Nippon Airways | 103 |
| 14 | QLK | 101 |
| 15 | Delta Air Lines | 95 |
| 16 | Swiss International | 95 |
| 17 | WIF | 95 |
| 18 | AZU | 89 |
| 19 | VIV | 89 |
| 20 | United Airlines | 82 |
| 21 | Alaska Airlines | 81 |
| 22 | AXB | 81 |
| 23 | Japan Airlines | 77 |
| 24 | EDV | 76 |
| 25 | Cathay Pacific | 75 |
| 26 | easyJet | 75 |
| 27 | EJU | 73 |
| 28 | BRC | 71 |
| 29 | Avianca | 70 |
| 30 | GLO | 66 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 9918 |
| 2 | 🇮🇳 IN | 1020 |
| 3 | 🇪🇸 ES | 955 |
| 4 | 🇦🇺 AU | 918 |
| 5 | 🇧🇷 BR | 674 |
| 6 | 🇩🇪 DE | 670 |
| 7 | 🇨🇴 CO | 604 |
| 8 | 🇯🇵 JP | 597 |
| 9 | 🇨🇦 CA | 566 |
| 10 | 🇮🇹 IT | 555 |
| 11 | 🇬🇧 GB | 461 |
| 12 | 🇲🇽 MX | 442 |
| 13 | 🇫🇷 FR | 398 |
| 14 | 🇬🇷 GR | 305 |
| 15 | 🇳🇴 NO | 301 |
| 16 | 🇨🇭 CH | 296 |
| 17 | 🇳🇿 NZ | 274 |
| 18 | 🇲🇾 MY | 273 |
| 19 | 🇿🇦 ZA | 237 |
| 20 | 🇬🇹 GT | 231 |
| 21 | 🇵🇭 PH | 216 |
| 22 | 🇹🇷 TR | 213 |
| 23 | 🇰🇷 KR | 204 |
| 24 | 🇵🇱 PL | 176 |
| 25 | 🇹🇭 TH | 150 |
| 26 | 🇲🇦 MA | 145 |
| 27 | 🇮🇩 ID | 143 |
| 28 | 🇲🇴 MO | 142 |
| 29 | 🇧🇸 BS | 122 |
| 30 | 🇲🇪 ME | 121 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 298 |
| 2 | Denver International Airport |  | US | 224 |
| 3 | Indira Gandhi International Airport |  | IN | 221 |
| 4 | Tokyo International Airport |  | JP | 213 |
| 5 | El Dorado International Airport |  | CO | 209 |
| 6 | Frankfurt am Main International Airport |  | DE | 184 |
| 7 | Harry Reid International Airport |  | US | 165 |
| 8 | La Aurora Airport |  | GT | 161 |
| 9 | Guaymaral Airport |  | CO | 153 |
| 10 | Zurich Airport |  | CH | 147 |
| 11 | Macau International Airport |  | MO | 142 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 140 |
| 13 | Eleftherios Venizelos International Airport |  | GR | 138 |
| 14 | Sydney Kingsford Smith International Airport |  | AU | 135 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 120 |
| 16 | Chicago O'Hare International Airport |  | US | 118 |
| 17 | Bengaluru International Airport |  | IN | 114 |
| 18 | Atizapan De Zaragoza Airport |  | MX | 108 |
| 19 | Madrid Barajas International Airport |  | ES | 108 |
| 20 | Charlotte/Douglas International Airport |  | US | 107 |
| 21 | Tenerife Norte Airport |  | ES | 106 |
| 22 | Kuala Lumpur International Airport |  | MY | 104 |
| 23 | Congonhas Airport |  | BR | 104 |
| 24 | Reno/Tahoe International Airport |  | US | 97 |
| 25 | Ninoy Aquino International Airport |  | PH | 97 |
| 26 | Vitoria/Foronda Airport |  | ES | 92 |
| 27 | Netaji Subhash Chandra Bose International Airport |  | IN | 92 |
| 28 | Salt Lake City International Airport |  | US | 92 |
| 29 | Daniel K Inouye International Airport |  | US | 91 |
| 30 | Malpensa International Airport |  | IT | 90 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 89 |
| 32 | Barcelona International Airport |  | ES | 87 |
| 33 | Charles de Gaulle International Airport |  | FR | 86 |
| 34 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 83 |
| 35 | Pune Airport |  | IN | 82 |
| 36 | Austin-Bergstrom International Airport |  | US | 81 |
| 37 | Seattle-Tacoma International Airport |  | US | 81 |
| 38 | George Bush Intcntl/Houston Airport |  | US | 78 |
| 39 | Bodø Airport |  | NO | 78 |
| 40 | Miami International Airport |  | US | 76 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 60 | 27m | - | - |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 58 | 14m | 114 km | 113.8 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 52 | 1h 7m | 706 km | 633.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 42 | 24m | 225 km | 162.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 40 | 29m | 304 km | 209.7 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 38 | 1h 46m | 1,156 km | 758.1 t |
| 7 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 34 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 33 | 20m | 165 km | 93.9 t |
| 10 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 31 | 15m | 206 km | 110.2 t |
| 11 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 31 | 23m | 99 km | 53.1 t |
| 12 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 30 | 26m | 152 km | 78.4 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 29 | 29m | 275 km | 137.4 t |
| 14 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 29 | 1h 26m | 910 km | 455.1 t |
| 15 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 29 | 53m | 556 km | 278.0 t |
| 16 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 26 | 1h 42m | 1,423 km | 638.1 t |
| 17 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 26 | 53m | 546 km | 244.8 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 25 | 30m | 369 km | 159.1 t |
| 19 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 25 | 1h 56m | 1,304 km | 562.4 t |
| 20 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 24 | 8m | - | - |
| 21 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 22 | 1h 10m | 770 km | 292.3 t |
| 22 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 21 | 23m | 252 km | 91.2 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 21 | 11m | 127 km | 46.0 t |
| 24 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 20 | 1h 1m | 723 km | 249.3 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 20 | 13m | 99 km | 34.3 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 18 | 20m | 147 km | 45.6 t |
| 27 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 18 | 33m | - | - |
| 28 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 18 | 26m | 69 km | 21.5 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 17 | 44m | 452 km | 132.5 t |
| 30 | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 17 | 44m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CXK505 | CXK | Wiley Post Airport (KPWA) | El Reno Regional Airport (KRQO) | 2026-04-02 21:03 UTC | 2026-04-02 21:46 UTC | 43m |
| CPA698 | Cathay Pacific | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-04-02 17:42 UTC | 2026-04-02 21:41 UTC | 3h 58m |
| LOOT18 | LOO | Flysooner Field (OK50) | William R Pogue Municipal Airport (KOWP) | 2026-04-02 21:15 UTC | 2026-04-02 21:39 UTC | 24m |
| CPA292 | Cathay Pacific | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Macau International Airport (VMMC) | 2026-04-02 11:16 UTC | 2026-04-02 21:34 UTC | 10h 18m |
| N741AE |  | Vr Airstrip (2OK0) | Tinker Afb Airport (KTIK) | 2026-04-02 21:16 UTC | 2026-04-02 21:34 UTC | 18m |
| TKJ9EF | TKJ | Dusseldorf International Airport (EDDL) | Istanbul Airport (LTFM) | 2026-04-02 19:04 UTC | 2026-04-02 21:33 UTC | 2h 29m |
| N460CA |  | Palo Alto Airport (KPAO) | Tracy Municipal Airport (KTCY) | 2026-04-02 21:01 UTC | 2026-04-02 21:31 UTC | 29m |
| N78AS |  | Centennial Airport (KAPA) | Limon Municipal Airport (KLIC) | 2026-04-02 21:00 UTC | 2026-04-02 21:30 UTC | 29m |
| N852S |  | Charles M Schulz/Sonoma County Airport (KSTS) | Petaluma Municipal Airport (KO69) | 2026-04-02 21:21 UTC | 2026-04-02 21:29 UTC | 7m |
| VOZ908 | Virgin Australia | Brisbane International Airport (YBBN) | Sydney Kingsford Smith International Airport (YSSY) | 2026-04-02 20:13 UTC | 2026-04-02 21:28 UTC | 1h 14m |
| BCS696 | BCS | Leipzig Halle Airport (EDDP) | Macau International Airport (VMMC) | 2026-04-02 10:15 UTC | 2026-04-02 21:26 UTC | 11h 10m |
| N73KG |  | Phoenix Deer Valley Airport (KDVT) | 2AZ7 (2AZ7) | 2026-04-02 21:17 UTC | 2026-04-02 21:23 UTC | 6m |
| AM339 |  | Melbourne Essendon Airport (YMEN) | Strathbogie Airport (YSBG) | 2026-04-02 21:02 UTC | 2026-04-02 21:20 UTC | 18m |
| N737MF |  | Sacramento Executive Airport (KSAC) | Franklin Field (KF72) | 2026-04-02 20:47 UTC | 2026-04-02 21:19 UTC | 32m |
| N5470W |  | Camp Bullis Als (Cals) Airport (9TX5) | Kestrel Airpark (K1T7) | 2026-04-02 20:24 UTC | 2026-04-02 21:19 UTC | 55m |
| N18ZD |  | Glendale Regional Airport (KGEU) | Sequoia Field (KD86) | 2026-04-02 20:04 UTC | 2026-04-02 21:18 UTC | 1h 14m |
| GARMN12 | GAR | New Century Aircenter Airport (KIXD) | Landmark Mfg Corporation Airport (1MO4) | 2026-04-02 20:18 UTC | 2026-04-02 21:17 UTC | 58m |
| AIC314 | Air India | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-04-02 17:03 UTC | 2026-04-02 21:14 UTC | 4h 11m |
| VOZ630 | Virgin Australia | Sydney Kingsford Smith International Airport (YSSY) | Collector Airport (YCLT) | 2026-04-02 20:45 UTC | 2026-04-02 21:14 UTC | 29m |
| JINX31 | JIN | Randolph Afb Airport (KRND) | Tee Pee Creek Airport (8TE0) | 2026-04-02 20:40 UTC | 2026-04-02 21:13 UTC | 33m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
