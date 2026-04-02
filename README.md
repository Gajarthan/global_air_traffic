# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--02_20:38:49_UTC-green)

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

**Latest saved flight:** 2026-04-02 20:38:49 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-02 20:38:49 UTC

- **12,022** saved flights
- **6,896** unique routes
- **111** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **12,022** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **148,974.1 tonnes** estimated CO2 emissions
- **8,636,179 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 524 |
| 2 | Ryanair | 477 |
| 3 | IndiGo | 328 |
| 4 | EJA | 235 |
| 5 | American Airlines | 216 |
| 6 | Lufthansa | 194 |
| 7 | Southwest Airlines | 180 |
| 8 | ENY | 155 |
| 9 | Vueling | 129 |
| 10 | LATAM Airlines | 122 |
| 11 | AXM | 120 |
| 12 | LXJ | 114 |
| 13 | All Nippon Airways | 103 |
| 14 | QLK | 99 |
| 15 | Swiss International | 95 |
| 16 | WIF | 95 |
| 17 | Delta Air Lines | 92 |
| 18 | AZU | 87 |
| 19 | VIV | 87 |
| 20 | AXB | 81 |
| 21 | Alaska Airlines | 79 |
| 22 | Japan Airlines | 77 |
| 23 | United Airlines | 76 |
| 24 | EDV | 75 |
| 25 | easyJet | 75 |
| 26 | Cathay Pacific | 73 |
| 27 | EJU | 73 |
| 28 | Avianca | 70 |
| 29 | BRC | 70 |
| 30 | GLO | 66 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 9695 |
| 2 | 🇮🇳 IN | 1016 |
| 3 | 🇪🇸 ES | 950 |
| 4 | 🇦🇺 AU | 906 |
| 5 | 🇩🇪 DE | 667 |
| 6 | 🇧🇷 BR | 660 |
| 7 | 🇨🇴 CO | 595 |
| 8 | 🇯🇵 JP | 595 |
| 9 | 🇨🇦 CA | 555 |
| 10 | 🇮🇹 IT | 549 |
| 11 | 🇬🇧 GB | 460 |
| 12 | 🇲🇽 MX | 434 |
| 13 | 🇫🇷 FR | 398 |
| 14 | 🇬🇷 GR | 305 |
| 15 | 🇳🇴 NO | 301 |
| 16 | 🇨🇭 CH | 296 |
| 17 | 🇲🇾 MY | 273 |
| 18 | 🇳🇿 NZ | 266 |
| 19 | 🇿🇦 ZA | 237 |
| 20 | 🇬🇹 GT | 230 |
| 21 | 🇵🇭 PH | 216 |
| 22 | 🇹🇷 TR | 211 |
| 23 | 🇰🇷 KR | 204 |
| 24 | 🇵🇱 PL | 173 |
| 25 | 🇹🇭 TH | 150 |
| 26 | 🇲🇦 MA | 144 |
| 27 | 🇮🇩 ID | 143 |
| 28 | 🇲🇴 MO | 137 |
| 29 | 🇳🇱 NL | 120 |
| 30 | 🇲🇪 ME | 120 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 287 |
| 2 | Indira Gandhi International Airport |  | IN | 219 |
| 3 | Denver International Airport |  | US | 215 |
| 4 | Tokyo International Airport |  | JP | 213 |
| 5 | El Dorado International Airport |  | CO | 204 |
| 6 | Frankfurt am Main International Airport |  | DE | 184 |
| 7 | Harry Reid International Airport |  | US | 163 |
| 8 | La Aurora Airport |  | GT | 160 |
| 9 | Guaymaral Airport |  | CO | 153 |
| 10 | Zurich Airport |  | CH | 147 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 138 |
| 12 | Macau International Airport |  | MO | 137 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 135 |
| 14 | Sydney Kingsford Smith International Airport |  | AU | 133 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 119 |
| 16 | Chicago O'Hare International Airport |  | US | 115 |
| 17 | Bengaluru International Airport |  | IN | 114 |
| 18 | Madrid Barajas International Airport |  | ES | 108 |
| 19 | Atizapan De Zaragoza Airport |  | MX | 107 |
| 20 | Charlotte/Douglas International Airport |  | US | 107 |
| 21 | Tenerife Norte Airport |  | ES | 106 |
| 22 | Kuala Lumpur International Airport |  | MY | 104 |
| 23 | Congonhas Airport |  | BR | 102 |
| 24 | Ninoy Aquino International Airport |  | PH | 97 |
| 25 | Reno/Tahoe International Airport |  | US | 96 |
| 26 | Netaji Subhash Chandra Bose International Airport |  | IN | 92 |
| 27 | Malpensa International Airport |  | IT | 90 |
| 28 | Daniel K Inouye International Airport |  | US | 90 |
| 29 | Vitoria/Foronda Airport |  | ES | 90 |
| 30 | Salt Lake City International Airport |  | US | 90 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 88 |
| 32 | Charles de Gaulle International Airport |  | FR | 86 |
| 33 | Barcelona International Airport |  | ES | 85 |
| 34 | Austin-Bergstrom International Airport |  | US | 81 |
| 35 | Pune Airport |  | IN | 81 |
| 36 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 81 |
| 37 | Seattle-Tacoma International Airport |  | US | 78 |
| 38 | Bodø Airport |  | NO | 78 |
| 39 | George Bush Intcntl/Houston Airport |  | US | 77 |
| 40 | Gimpo International Airport |  | KR | 75 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 60 | 27m | - | - |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 56 | 14m | 114 km | 109.8 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 52 | 1h 7m | 706 km | 633.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 42 | 24m | 225 km | 162.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 40 | 29m | 304 km | 209.7 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 38 | 1h 46m | 1,156 km | 758.1 t |
| 7 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 34 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 33 | 20m | 165 km | 93.9 t |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 31 | 23m | 99 km | 53.1 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 30 | 15m | 206 km | 106.7 t |
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
| CPA843 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-04-02 06:03 UTC | 2026-04-02 20:38 UTC | 14h 35m |
| BCS692 | BCS | Leipzig Halle Airport (EDDP) | Zhuhai Airport (ZGSD) | 2026-04-02 09:26 UTC | 2026-04-02 20:34 UTC | 11h 8m |
| N750GJ |  | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-04-02 18:14 UTC | 2026-04-02 20:33 UTC | 2h 18m |
| CPA829 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Zhuhai Airport (ZGSD) | 2026-04-02 06:13 UTC | 2026-04-02 20:33 UTC | 14h 19m |
| CXK1057 | CXK | Mesa Gateway Airport (KIWA) | Coolidge Municipal Airport (KP08) | 2026-04-02 19:43 UTC | 2026-04-02 20:30 UTC | 46m |
| N669NE |  | Placerville Airport (KPVF) | Auburn Municipal Airport (KAUN) | 2026-04-02 19:38 UTC | 2026-04-02 20:23 UTC | 44m |
| BRG594 | BRG | Ralph Wien Memorial Airport (PAOT) | Kivalina Airport (PAVL) | 2026-04-02 19:54 UTC | 2026-04-02 20:22 UTC | 28m |
| CREEP31 | CRE | 75OK (75OK) | Ramey 1 Airport (0OK8) | 2026-04-02 19:52 UTC | 2026-04-02 20:22 UTC | 29m |
| CPA811 | Cathay Pacific | General Edward Lawrence Logan International Airport (KBOS) | Macau International Airport (VMMC) | 2026-04-02 05:59 UTC | 2026-04-02 20:22 UTC | 14h 22m |
| 00 |  | Eielson Afb Airport (PAEI) | Eielson Afb Airport (PAEI) | 2026-04-02 19:48 UTC | 2026-04-02 20:20 UTC | 31m |
| ARCAS11 | ARC | 4TA5 (4TA5) | K14F (K14F) | 2026-04-02 20:01 UTC | 2026-04-02 20:18 UTC | 16m |
| N935RK |  | University Of Illinois/Willard Airport (KCMI) | 4IN8 (4IN8) | 2026-04-02 19:40 UTC | 2026-04-02 20:14 UTC | 33m |
| OAI | OAI | Aeropelican Airport (YPEC) | Aeropelican Airport (YPEC) | 2026-04-02 19:55 UTC | 2026-04-02 20:14 UTC | 18m |
| ERU29 | ERU | Prescott Regional/Ernest A Love Field (KPRC) | 42AZ (42AZ) | 2026-04-02 20:08 UTC | 2026-04-02 20:13 UTC | 5m |
| UAE9842 | Emirates | Al Maktoum International Airport (OMDW) | Zhuhai Airport (ZGSD) | 2026-04-02 14:05 UTC | 2026-04-02 20:12 UTC | 6h 6m |
| N892AE |  | Austin-Bergstrom International Airport (KAUS) | Mills Field (KK22) | 2026-04-02 18:12 UTC | 2026-04-02 20:09 UTC | 1h 56m |
| IFJ32T | IFJ | Cascais Airport (LPCS) | Cascais Airport (LPCS) | 2026-04-02 19:20 UTC | 2026-04-02 20:09 UTC | 48m |
| NSZ48U | NSZ | Budapest Ferenc Liszt International Airport (LHBP) | Stockholm-Arlanda Airport (ESSA) | 2026-04-02 18:21 UTC | 2026-04-02 20:08 UTC | 1h 47m |
| N83KB |  | French Valley Airport (KF70) | Desert Air Sky Ranch Airport (63CA) | 2026-04-02 19:41 UTC | 2026-04-02 20:08 UTC | 26m |
| TGCYE | TGC | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 2026-04-02 19:43 UTC | 2026-04-02 20:06 UTC | 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
