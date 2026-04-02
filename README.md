# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--02_07:41:13_UTC-green)

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

**Latest saved flight:** 2026-04-02 07:41:13 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-02 07:41:13 UTC

- **10,401** saved flights
- **6,106** unique routes
- **111** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **10,401** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **127,855.2 tonnes** estimated CO2 emissions
- **7,411,896 km** total distance flown
- **851 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 470 |
| 2 | Ryanair | 390 |
| 3 | IndiGo | 280 |
| 4 | EJA | 215 |
| 5 | American Airlines | 188 |
| 6 | Lufthansa | 167 |
| 7 | Southwest Airlines | 164 |
| 8 | ENY | 139 |
| 9 | AXM | 111 |
| 10 | Vueling | 111 |
| 11 | LATAM Airlines | 106 |
| 12 | LXJ | 100 |
| 13 | QLK | 95 |
| 14 | All Nippon Airways | 91 |
| 15 | Delta Air Lines | 86 |
| 16 | WIF | 81 |
| 17 | Swiss International | 74 |
| 18 | Alaska Airlines | 72 |
| 19 | VIV | 72 |
| 20 | AZU | 71 |
| 21 | Japan Airlines | 70 |
| 22 | AXB | 67 |
| 23 | EDV | 66 |
| 24 | United Airlines | 66 |
| 25 | Cathay Pacific | 64 |
| 26 | Avianca | 60 |
| 27 | BRC | 58 |
| 28 | EJU | 57 |
| 29 | easyJet | 57 |
| 30 | ANZ | 55 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 8541 |
| 2 | 🇦🇺 AU | 874 |
| 3 | 🇮🇳 IN | 852 |
| 4 | 🇪🇸 ES | 782 |
| 5 | 🇩🇪 DE | 545 |
| 6 | 🇧🇷 BR | 542 |
| 7 | 🇯🇵 JP | 530 |
| 8 | 🇨🇴 CO | 524 |
| 9 | 🇨🇦 CA | 510 |
| 10 | 🇮🇹 IT | 451 |
| 11 | 🇲🇽 MX | 379 |
| 12 | 🇬🇧 GB | 360 |
| 13 | 🇫🇷 FR | 310 |
| 14 | 🇳🇴 NO | 263 |
| 15 | 🇳🇿 NZ | 258 |
| 16 | 🇲🇾 MY | 249 |
| 17 | 🇬🇷 GR | 238 |
| 18 | 🇨🇭 CH | 235 |
| 19 | 🇿🇦 ZA | 209 |
| 20 | 🇬🇹 GT | 209 |
| 21 | 🇵🇭 PH | 202 |
| 22 | 🇰🇷 KR | 182 |
| 23 | 🇹🇷 TR | 163 |
| 24 | 🇮🇩 ID | 130 |
| 25 | 🇵🇱 PL | 128 |
| 26 | 🇲🇴 MO | 121 |
| 27 | 🇹🇭 TH | 120 |
| 28 | 🇲🇦 MA | 119 |
| 29 | 🇲🇪 ME | 100 |
| 30 | 🇧🇸 BS | 96 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 252 |
| 2 | Indira Gandhi International Airport |  | IN | 191 |
| 3 | Tokyo International Airport |  | JP | 190 |
| 4 | Denver International Airport |  | US | 189 |
| 5 | El Dorado International Airport |  | CO | 173 |
| 6 | Frankfurt am Main International Airport |  | DE | 169 |
| 7 | Harry Reid International Airport |  | US | 149 |
| 8 | Guaymaral Airport |  | CO | 148 |
| 9 | La Aurora Airport |  | GT | 146 |
| 10 | Sydney Kingsford Smith International Airport |  | AU | 130 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 126 |
| 12 | Macau International Airport |  | MO | 121 |
| 13 | Zurich Airport |  | CH | 116 |
| 14 | Eleftherios Venizelos International Airport |  | GR | 114 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 106 |
| 16 | Chicago O'Hare International Airport |  | US | 105 |
| 17 | Reno/Tahoe International Airport |  | US | 95 |
| 18 | Atizapan De Zaragoza Airport |  | MX | 93 |
| 19 | Madrid Barajas International Airport |  | ES | 93 |
| 20 | Kuala Lumpur International Airport |  | MY | 93 |
| 21 | Charlotte/Douglas International Airport |  | US | 92 |
| 22 | Tenerife Norte Airport |  | ES | 92 |
| 23 | Bengaluru International Airport |  | IN | 92 |
| 24 | Ninoy Aquino International Airport |  | PH | 91 |
| 25 | Daniel K Inouye International Airport |  | US | 81 |
| 26 | Congonhas Airport |  | BR | 81 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 80 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 79 |
| 29 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 76 |
| 30 | Malpensa International Airport |  | IT | 75 |
| 31 | Salt Lake City International Airport |  | US | 75 |
| 32 | Austin-Bergstrom International Airport |  | US | 72 |
| 33 | Vitoria/Foronda Airport |  | ES | 72 |
| 34 | Barcelona International Airport |  | ES | 72 |
| 35 | Seattle-Tacoma International Airport |  | US | 72 |
| 36 | Pune Airport |  | IN | 71 |
| 37 | Charles de Gaulle International Airport |  | FR | 69 |
| 38 | Miami International Airport |  | US | 67 |
| 39 | Gimpo International Airport |  | KR | 67 |
| 40 | Calgary International Airport |  | CA | 67 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 59 | 27m | - | - |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 48 | 14m | 114 km | 94.1 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 46 | 1h 7m | 706 km | 560.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 39 | 24m | 225 km | 151.3 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 34 | 30m | 304 km | 178.2 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 31 | 1h 44m | 1,156 km | 618.4 t |
| 7 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 31 | 4m | - | - |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 30 | 30m | - | - |
| 9 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 30 | 23m | 99 km | 51.4 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 29 | 20m | 165 km | 82.5 t |
| 11 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 29 | 53m | 556 km | 278.0 t |
| 12 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 29 | 26m | 152 km | 75.8 t |
| 13 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 27 | 15m | 206 km | 96.0 t |
| 14 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 27 | 1h 26m | 910 km | 423.7 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 25 | 30m | 369 km | 159.1 t |
| 16 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 23 | 28m | 275 km | 109.0 t |
| 17 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 23 | 1h 43m | 1,423 km | 564.5 t |
| 18 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 23 | 53m | 546 km | 216.5 t |
| 19 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 22 | 8m | - | - |
| 20 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 21 | 1h 10m | 770 km | 279.0 t |
| 21 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 21 | 1h 58m | 1,304 km | 472.4 t |
| 22 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 19 | 1h 1m | 723 km | 236.9 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 18 | 11m | 127 km | 39.4 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 17 | 20m | 250 km | 73.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 16 | 1h 46m | 1,290 km | 356.0 t |
| 26 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 16 | 32m | - | - |
| 27 | Brisbane International Airport (YBBN) | Maryborough Airport (YMYB) | 16 | 28m | 212 km | 58.5 t |
| 28 | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 16 | 18m | 26 km | 7.2 t |
| 29 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 15 | 23m | 252 km | 65.1 t |
| 30 | Auckland International Airport (NZAA) | Omarama Glider Airport (NZOA) | 15 | 1h 17m | 924 km | 239.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DHDAL | DHD | Oerlinghausen Airport (EDLO) | Hameln-Pyrmont Airport (EDVW) | 2026-04-02 07:19 UTC | 2026-04-02 07:41 UTC | 22m |
| HBXBO | HBX | St Stephan Airport (LSTS) | Bern Belp Airport (LSZB) | 2026-04-02 07:06 UTC | 2026-04-02 07:40 UTC | 33m |
| HBZVS | HBZ | Courchevel Airport (LFLJ) | Muenster Aero Airport (LSPU) | 2026-04-02 05:54 UTC | 2026-04-02 07:29 UTC | 1h 34m |
| N488RJ |  | Harry Reid International Airport (KLAS) | Phoenix Sky Harbor International Airport (KPHX) | 2026-04-02 06:40 UTC | 2026-04-02 07:20 UTC | 40m |
| ENT1PK | ENT | Pisa / San Giusto - Galileo Galilei International Airport (LIRP) | Zurich Airport (LSZH) | 2026-04-02 06:24 UTC | 2026-04-02 07:14 UTC | 49m |
| AUR201 | AUR | Alderney Airport (EGJA) | Guernsey Airport (EGJB) | 2026-04-02 07:00 UTC | 2026-04-02 07:11 UTC | 11m |
| CPA335 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-04-02 00:01 UTC | 2026-04-02 07:10 UTC | 7h 9m |
| UAE37N | Emirates | Amsterdam Airport Schiphol (EHAM) | Macau International Airport (VMMC) | 2026-04-01 14:16 UTC | 2026-04-02 07:04 UTC | 16h 47m |
| BAW31 | British Airways | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-04-01 18:45 UTC | 2026-04-02 06:56 UTC | 12h 11m |
| HBXBO | HBX | St Stephan Airport (LSTS) | Reichenbach Air Base (LSGR) | 2026-04-02 06:23 UTC | 2026-04-02 06:55 UTC | 31m |
| ZUMNT | ZUM | Lanseria Airport (FALA) | Pilanesberg International Airport (FAPN) | 2026-04-02 06:23 UTC | 2026-04-02 06:54 UTC | 31m |
| OECCE | OEC | Urbe Airport (LIRU) | Urbe Airport (LIRU) | 2026-04-02 06:43 UTC | 2026-04-02 06:53 UTC | 10m |
| IGO497 | IndiGo | Bengaluru International Airport (VOBL) | Kalka Airport (VI71) | 2026-04-02 03:28 UTC | 2026-04-02 06:50 UTC | 3h 21m |
| UPS2 | UPS | Cologne Bonn Airport (EDDK) | Macau International Airport (VMMC) | 2026-04-01 19:56 UTC | 2026-04-02 06:48 UTC | 10h 51m |
| HBZUW | HBZ | Sion Airport (LSGS) | Sion Airport (LSGS) | 2026-04-02 06:36 UTC | 2026-04-02 06:47 UTC | 10m |
| WIF1X | WIF | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 2026-04-02 06:43 UTC | 2026-04-02 06:47 UTC | 3m |
| AAO13 | AAO | Ciampino Airport (LIRA) | Tivat Airport (LYTV) | 2026-04-02 05:59 UTC | 2026-04-02 06:47 UTC | 47m |
| IGO7304 | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 2026-04-02 05:31 UTC | 2026-04-02 06:47 UTC | 1h 15m |
| IGO239V | IndiGo | Indira Gandhi International Airport (VIDP) | VEDG (VEDG) | 2026-04-02 05:11 UTC | 2026-04-02 06:46 UTC | 1h 34m |
| DLH796 | Lufthansa | Frankfurt am Main International Airport (EDDF) | Macau International Airport (VMMC) | 2026-04-01 19:53 UTC | 2026-04-02 06:45 UTC | 10h 52m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
