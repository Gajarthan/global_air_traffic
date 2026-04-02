# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--02_15:21:31_UTC-green)

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

**Latest saved flight:** 2026-04-02 15:21:31 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-02 15:21:31 UTC

- **11,164** saved flights
- **6,457** unique routes
- **111** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **11,164** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **138,280.6 tonnes** estimated CO2 emissions
- **8,016,266 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 472 |
| 2 | Ryanair | 445 |
| 3 | IndiGo | 318 |
| 4 | EJA | 216 |
| 5 | American Airlines | 192 |
| 6 | Lufthansa | 188 |
| 7 | Southwest Airlines | 168 |
| 8 | ENY | 142 |
| 9 | Vueling | 121 |
| 10 | AXM | 120 |
| 11 | LATAM Airlines | 115 |
| 12 | All Nippon Airways | 103 |
| 13 | LXJ | 102 |
| 14 | QLK | 99 |
| 15 | WIF | 92 |
| 16 | Swiss International | 89 |
| 17 | Delta Air Lines | 87 |
| 18 | AZU | 79 |
| 19 | AXB | 78 |
| 20 | Japan Airlines | 77 |
| 21 | VIV | 77 |
| 22 | Alaska Airlines | 72 |
| 23 | Cathay Pacific | 69 |
| 24 | easyJet | 68 |
| 25 | EDV | 67 |
| 26 | United Airlines | 67 |
| 27 | EJU | 65 |
| 28 | Avianca | 64 |
| 29 | BRC | 64 |
| 30 | GLO | 58 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 8781 |
| 2 | 🇮🇳 IN | 980 |
| 3 | 🇦🇺 AU | 904 |
| 4 | 🇪🇸 ES | 881 |
| 5 | 🇩🇪 DE | 640 |
| 6 | 🇧🇷 BR | 596 |
| 7 | 🇯🇵 JP | 593 |
| 8 | 🇨🇴 CO | 553 |
| 9 | 🇨🇦 CA | 521 |
| 10 | 🇮🇹 IT | 507 |
| 11 | 🇬🇧 GB | 426 |
| 12 | 🇲🇽 MX | 398 |
| 13 | 🇫🇷 FR | 364 |
| 14 | 🇳🇴 NO | 294 |
| 15 | 🇬🇷 GR | 280 |
| 16 | 🇨🇭 CH | 274 |
| 17 | 🇲🇾 MY | 272 |
| 18 | 🇳🇿 NZ | 260 |
| 19 | 🇿🇦 ZA | 229 |
| 20 | 🇵🇭 PH | 216 |
| 21 | 🇬🇹 GT | 215 |
| 22 | 🇰🇷 KR | 204 |
| 23 | 🇹🇷 TR | 185 |
| 24 | 🇵🇱 PL | 156 |
| 25 | 🇹🇭 TH | 146 |
| 26 | 🇮🇩 ID | 143 |
| 27 | 🇲🇴 MO | 134 |
| 28 | 🇲🇦 MA | 133 |
| 29 | 🇳🇱 NL | 114 |
| 30 | 🇲🇪 ME | 112 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 257 |
| 2 | Tokyo International Airport |  | JP | 213 |
| 3 | Indira Gandhi International Airport |  | IN | 211 |
| 4 | Denver International Airport |  | US | 191 |
| 5 | El Dorado International Airport |  | CO | 187 |
| 6 | Frankfurt am Main International Airport |  | DE | 180 |
| 7 | Harry Reid International Airport |  | US | 154 |
| 8 | Guaymaral Airport |  | CO | 150 |
| 9 | La Aurora Airport |  | GT | 150 |
| 10 | Macau International Airport |  | MO | 134 |
| 11 | Sydney Kingsford Smith International Airport |  | AU | 133 |
| 12 | Zurich Airport |  | CH | 130 |
| 13 | Eleftherios Venizelos International Airport |  | GR | 129 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 126 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 111 |
| 16 | Bengaluru International Airport |  | IN | 109 |
| 17 | Chicago O'Hare International Airport |  | US | 106 |
| 18 | Kuala Lumpur International Airport |  | MY | 104 |
| 19 | Tenerife Norte Airport |  | ES | 101 |
| 20 | Madrid Barajas International Airport |  | ES | 99 |
| 21 | Atizapan De Zaragoza Airport |  | MX | 98 |
| 22 | Ninoy Aquino International Airport |  | PH | 97 |
| 23 | Charlotte/Douglas International Airport |  | US | 95 |
| 24 | Reno/Tahoe International Airport |  | US | 95 |
| 25 | Netaji Subhash Chandra Bose International Airport |  | IN | 91 |
| 26 | Congonhas Airport |  | BR | 90 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 86 |
| 28 | Malpensa International Airport |  | IT | 83 |
| 29 | Daniel K Inouye International Airport |  | US | 82 |
| 30 | Vitoria/Foronda Airport |  | ES | 81 |
| 31 | Barcelona International Airport |  | ES | 79 |
| 32 | Charles de Gaulle International Airport |  | FR | 78 |
| 33 | Pune Airport |  | IN | 78 |
| 34 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 77 |
| 35 | Bodø Airport |  | NO | 76 |
| 36 | Gimpo International Airport |  | KR | 75 |
| 37 | Salt Lake City International Airport |  | US | 75 |
| 38 | Austin-Bergstrom International Airport |  | US | 72 |
| 39 | Seattle-Tacoma International Airport |  | US | 72 |
| 40 | Amsterdam Airport Schiphol |  | NL | 70 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 59 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 52 | 1h 7m | 706 km | 633.1 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 52 | 14m | 114 km | 102.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 42 | 24m | 225 km | 162.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 40 | 29m | 304 km | 209.7 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 36 | 1h 46m | 1,156 km | 718.2 t |
| 7 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 35 | 4m | - | - |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 33 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 33 | 20m | 165 km | 93.9 t |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 30 | 23m | 99 km | 51.4 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 29 | 1h 26m | 910 km | 455.1 t |
| 12 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 29 | 53m | 556 km | 278.0 t |
| 13 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 29 | 26m | 152 km | 75.8 t |
| 14 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 28 | 15m | 206 km | 99.5 t |
| 15 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 26 | 53m | 546 km | 244.8 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 25 | 30m | 369 km | 159.1 t |
| 17 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 24 | 28m | 275 km | 113.7 t |
| 18 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 24 | 1h 42m | 1,423 km | 589.0 t |
| 19 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 23 | 8m | - | - |
| 20 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 22 | 1h 10m | 770 km | 292.3 t |
| 21 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 22 | 1h 57m | 1,304 km | 494.9 t |
| 22 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 21 | 23m | 252 km | 91.2 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 21 | 11m | 127 km | 46.0 t |
| 24 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 19 | 1h 1m | 723 km | 236.9 t |
| 25 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 18 | 33m | - | - |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 17 | 20m | 147 km | 43.0 t |
| 27 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 17 | 44m | 452 km | 132.5 t |
| 28 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 17 | 13m | 99 km | 29.1 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 17 | 19m | - | - |
| 30 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 17 | 8h 31m | 38 km | 11.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LLN103 | LLN | Perot Field/Fort Worth Alliance Airport (KAFW) | Decatur Municipal Airport (KLUD) | 2026-04-02 14:58 UTC | 2026-04-02 15:21 UTC | 23m |
| N374BL |  | Winter Haven Regional Airport (KGIF) | Bartow Executive Airport (KBOW) | 2026-04-02 14:01 UTC | 2026-04-02 15:21 UTC | 1h 20m |
| N358EA |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-04-02 14:29 UTC | 2026-04-02 15:19 UTC | 50m |
| N331JK |  | Centennial Airport (KAPA) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-04-02 13:49 UTC | 2026-04-02 15:18 UTC | 1h 28m |
| IGREI | IGR | Cuneo / Levaldigi Airport (LIMZ) | Sollieres Sardieres Airport (LFKD) | 2026-04-02 15:03 UTC | 2026-04-02 15:16 UTC | 13m |
| N3030E |  | Burlington/Alamance Regional Airport (KBUY) | K5W8 (K5W8) | 2026-04-02 14:53 UTC | 2026-04-02 15:14 UTC | 21m |
| N1111B |  | Orlando North Airpark (FA83) | Back Achers Airport (8FL3) | 2026-04-02 14:54 UTC | 2026-04-02 15:12 UTC | 17m |
| N618DS |  | Deland Municipal-Sidney H Taylor Field (KDED) | Deland Municipal-Sidney H Taylor Field (KDED) | 2026-04-02 14:53 UTC | 2026-04-02 15:11 UTC | 17m |
| N2949V |  | City Of Colorado Springs Municipal Airport (KCOS) | High Plains Airport Airport (CD15) | 2026-04-02 14:44 UTC | 2026-04-02 15:07 UTC | 22m |
| CFDYL | CFD | Vancouver International Airport (CYVR) | Victoria International Airport (CYYJ) | 2026-04-02 14:34 UTC | 2026-04-02 15:03 UTC | 29m |
| ARCAS46 | ARC | Danaher Airport (7TX0) | TX20 (TX20) | 2026-04-02 14:47 UTC | 2026-04-02 15:02 UTC | 15m |
| S1251 |  | Cox's Bazar Airport (VGCB) | Cox's Bazar Airport (VGCB) | 2026-04-02 14:53 UTC | 2026-04-02 14:58 UTC | 4m |
| ASP812 | ASP | Vancouver International Airport (CYVR) | Boeing Field/King County International Airport (KBFI) | 2026-04-02 14:02 UTC | 2026-04-02 14:57 UTC | 54m |
| WCC55 | WCC | John Wayne/Orange County Airport (KSNA) | Bermuda Dunes Airport (KUDD) | 2026-04-02 14:37 UTC | 2026-04-02 14:56 UTC | 18m |
| N65PX |  | Charlotte/Monroe Executive Airport (KEQY) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-04-02 14:08 UTC | 2026-04-02 14:55 UTC | 46m |
| N64423 |  | Denton Enterprise Airport (KDTO) | Sherman Municipal Airport (KSWI) | 2026-04-02 14:29 UTC | 2026-04-02 14:54 UTC | 24m |
| N2230D |  | Phoenix Deer Valley Airport (KDVT) | Montezuma Airport (19AZ) | 2026-04-02 14:24 UTC | 2026-04-02 14:49 UTC | 24m |
| CPA336 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-04-02 07:35 UTC | 2026-04-02 14:48 UTC | 7h 13m |
| UBG119 | UBG | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 2026-04-02 14:13 UTC | 2026-04-02 14:46 UTC | 33m |
| MTN8310 | MTN | Newark Liberty International Airport (KEWR) | General Edward Lawrence Logan International Airport (KBOS) | 2026-04-02 13:34 UTC | 2026-04-02 14:46 UTC | 1h 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
