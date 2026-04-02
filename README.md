# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--02_18:20:52_UTC-green)

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

**Latest saved flight:** 2026-04-02 18:20:52 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-02 18:20:52 UTC

- **11,643** saved flights
- **6,687** unique routes
- **111** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **11,643** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **143,499.2 tonnes** estimated CO2 emissions
- **8,318,795 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 492 |
| 2 | Ryanair | 465 |
| 3 | IndiGo | 328 |
| 4 | EJA | 226 |
| 5 | American Airlines | 206 |
| 6 | Lufthansa | 194 |
| 7 | Southwest Airlines | 173 |
| 8 | ENY | 147 |
| 9 | Vueling | 127 |
| 10 | AXM | 120 |
| 11 | LATAM Airlines | 117 |
| 12 | LXJ | 110 |
| 13 | All Nippon Airways | 103 |
| 14 | QLK | 99 |
| 15 | WIF | 95 |
| 16 | Swiss International | 94 |
| 17 | Delta Air Lines | 89 |
| 18 | AZU | 83 |
| 19 | AXB | 80 |
| 20 | VIV | 80 |
| 21 | Japan Airlines | 77 |
| 22 | Alaska Airlines | 74 |
| 23 | EJU | 71 |
| 24 | easyJet | 71 |
| 25 | BRC | 70 |
| 26 | Cathay Pacific | 70 |
| 27 | EDV | 70 |
| 28 | United Airlines | 69 |
| 29 | Avianca | 68 |
| 30 | GLO | 63 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 9245 |
| 2 | 🇮🇳 IN | 1011 |
| 3 | 🇪🇸 ES | 924 |
| 4 | 🇦🇺 AU | 904 |
| 5 | 🇩🇪 DE | 658 |
| 6 | 🇧🇷 BR | 633 |
| 7 | 🇯🇵 JP | 593 |
| 8 | 🇨🇴 CO | 577 |
| 9 | 🇨🇦 CA | 537 |
| 10 | 🇮🇹 IT | 536 |
| 11 | 🇬🇧 GB | 443 |
| 12 | 🇲🇽 MX | 412 |
| 13 | 🇫🇷 FR | 393 |
| 14 | 🇳🇴 NO | 300 |
| 15 | 🇬🇷 GR | 297 |
| 16 | 🇨🇭 CH | 287 |
| 17 | 🇲🇾 MY | 272 |
| 18 | 🇳🇿 NZ | 260 |
| 19 | 🇿🇦 ZA | 233 |
| 20 | 🇬🇹 GT | 226 |
| 21 | 🇵🇭 PH | 216 |
| 22 | 🇰🇷 KR | 204 |
| 23 | 🇹🇷 TR | 200 |
| 24 | 🇵🇱 PL | 170 |
| 25 | 🇹🇭 TH | 150 |
| 26 | 🇮🇩 ID | 143 |
| 27 | 🇲🇦 MA | 139 |
| 28 | 🇲🇴 MO | 135 |
| 29 | 🇳🇱 NL | 120 |
| 30 | 🇲🇪 ME | 116 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 272 |
| 2 | Indira Gandhi International Airport |  | IN | 217 |
| 3 | Tokyo International Airport |  | JP | 213 |
| 4 | Denver International Airport |  | US | 201 |
| 5 | El Dorado International Airport |  | CO | 196 |
| 6 | Frankfurt am Main International Airport |  | DE | 184 |
| 7 | Harry Reid International Airport |  | US | 160 |
| 8 | La Aurora Airport |  | GT | 158 |
| 9 | Guaymaral Airport |  | CO | 152 |
| 10 | Zurich Airport |  | CH | 140 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 135 |
| 12 | Macau International Airport |  | MO | 135 |
| 13 | Sydney Kingsford Smith International Airport |  | AU | 133 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 130 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 116 |
| 16 | Bengaluru International Airport |  | IN | 114 |
| 17 | Chicago O'Hare International Airport |  | US | 113 |
| 18 | Charlotte/Douglas International Airport |  | US | 104 |
| 19 | Tenerife Norte Airport |  | ES | 104 |
| 20 | Kuala Lumpur International Airport |  | MY | 104 |
| 21 | Madrid Barajas International Airport |  | ES | 103 |
| 22 | Atizapan De Zaragoza Airport |  | MX | 100 |
| 23 | Congonhas Airport |  | BR | 99 |
| 24 | Ninoy Aquino International Airport |  | PH | 97 |
| 25 | Reno/Tahoe International Airport |  | US | 96 |
| 26 | Netaji Subhash Chandra Bose International Airport |  | IN | 92 |
| 27 | Malpensa International Airport |  | IT | 89 |
| 28 | Vitoria/Foronda Airport |  | ES | 88 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 86 |
| 30 | Daniel K Inouye International Airport |  | US | 85 |
| 31 | Charles de Gaulle International Airport |  | FR | 85 |
| 32 | Barcelona International Airport |  | ES | 84 |
| 33 | Pune Airport |  | IN | 79 |
| 34 | Salt Lake City International Airport |  | US | 78 |
| 35 | Bodø Airport |  | NO | 78 |
| 36 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 77 |
| 37 | Austin-Bergstrom International Airport |  | US | 76 |
| 38 | Gimpo International Airport |  | KR | 75 |
| 39 | Seattle-Tacoma International Airport |  | US | 75 |
| 40 | Amsterdam Airport Schiphol |  | NL | 74 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 60 | 27m | - | - |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 54 | 14m | 114 km | 105.9 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 52 | 1h 7m | 706 km | 633.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 42 | 24m | 225 km | 162.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 40 | 29m | 304 km | 209.7 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 36 | 1h 46m | 1,156 km | 718.2 t |
| 7 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 34 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 33 | 20m | 165 km | 93.9 t |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 31 | 23m | 99 km | 53.1 t |
| 11 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 30 | 26m | 152 km | 78.4 t |
| 12 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 29 | 15m | 206 km | 103.1 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 29 | 1h 26m | 910 km | 455.1 t |
| 14 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 29 | 53m | 556 km | 278.0 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 28 | 29m | 275 km | 132.7 t |
| 16 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 26 | 1h 42m | 1,423 km | 638.1 t |
| 17 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 26 | 53m | 546 km | 244.8 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 25 | 30m | 369 km | 159.1 t |
| 19 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 24 | 8m | - | - |
| 20 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 22 | 1h 10m | 770 km | 292.3 t |
| 21 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 22 | 1h 57m | 1,304 km | 494.9 t |
| 22 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 21 | 23m | 252 km | 91.2 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 21 | 11m | 127 km | 46.0 t |
| 24 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 20 | 1h 1m | 723 km | 249.3 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 19 | 13m | 99 km | 32.6 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 18 | 20m | 147 km | 45.6 t |
| 27 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 18 | 33m | - | - |
| 28 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 17 | 44m | 452 km | 132.5 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 17 | 19m | - | - |
| 30 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 17 | 8h 31m | 38 km | 11.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N363K |  | Palo Alto Airport (KPAO) | Palo Alto Airport (KPAO) | 2026-04-02 17:46 UTC | 2026-04-02 18:20 UTC | 34m |
| N945G |  | Palo Alto Airport (KPAO) | Palo Alto Airport (KPAO) | 2026-04-02 18:03 UTC | 2026-04-02 18:19 UTC | 15m |
| FUSON91 | FUS | Laughlin Afb Aux Nr 1 Airport (KT70) | 6TA4 (6TA4) | 2026-04-02 17:47 UTC | 2026-04-02 18:15 UTC | 28m |
| BRG650 | BRG | Ralph Wien Memorial Airport (PAOT) | Selawik Airport (PASK) | 2026-04-02 17:43 UTC | 2026-04-02 18:11 UTC | 27m |
| N856SR |  | Aero Valley Airport (K52F) | Aero Valley Airport (K52F) | 2026-04-02 17:52 UTC | 2026-04-02 18:07 UTC | 14m |
| SCU29 | SCU | Tulsa International Airport (KTUL) | Tulsa International Airport (KTUL) | 2026-04-02 17:48 UTC | 2026-04-02 18:03 UTC | 14m |
| N739UQ |  | K5T6 (K5T6) | Las Cruces International Airport (KLRU) | 2026-04-02 16:54 UTC | 2026-04-02 17:57 UTC | 1h 3m |
| N819EE |  | K5T6 (K5T6) | Telluride Regional Airport (KTEX) | 2026-04-02 16:08 UTC | 2026-04-02 17:56 UTC | 1h 48m |
| ROKT41 | ROK | Pensacola Nas (Forrest Sherman Field) Airport (KNPA) | Bird Nest Airport (4MS5) | 2026-04-02 17:33 UTC | 2026-04-02 17:53 UTC | 19m |
| N5158J |  | Cheyenne Regional/Jerry Olson Field (KCYS) | Skyview Airpark (WY05) | 2026-04-02 17:41 UTC | 2026-04-02 17:53 UTC | 11m |
| N716GS |  | Page Field (KFMY) | Booneville/Baldwyn Airport (K8M1) | 2026-04-02 16:22 UTC | 2026-04-02 17:53 UTC | 1h 30m |
| N51222 |  | Bartow Executive Airport (KBOW) | Bartow Executive Airport (KBOW) | 2026-04-02 17:51 UTC | 2026-04-02 17:51 UTC | 0m |
| N643SA |  | Addison Airport (KADS) | TX81 (TX81) | 2026-04-02 17:28 UTC | 2026-04-02 17:48 UTC | 20m |
| TAHOE51 | TAH | Randolph Afb Airport (KRND) | Bailey Airport (2TS8) | 2026-04-02 17:30 UTC | 2026-04-02 17:44 UTC | 14m |
| BRCAT20 | BRC | 81NM (81NM) | Skeen Ranch Airport (82NM) | 2026-04-02 17:15 UTC | 2026-04-02 17:42 UTC | 27m |
| CPA3295 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-04-02 02:54 UTC | 2026-04-02 17:41 UTC | 14h 46m |
| N31EP |  | Phoenix Deer Valley Airport (KDVT) | Montezuma Airport (19AZ) | 2026-04-02 17:22 UTC | 2026-04-02 17:41 UTC | 19m |
| PAT752 | PAT | Los Alamitos Army Air Field (KSLI) | Jacqueline Cochran Regional Airport (KTRM) | 2026-04-02 17:07 UTC | 2026-04-02 17:39 UTC | 32m |
| BRCAT12 | BRC | Roswell Air Center Airport (KROW) | Skeen Ranch Airport (82NM) | 2026-04-02 16:50 UTC | 2026-04-02 17:34 UTC | 44m |
| XE1180 |  | Harry Reid International Airport (KLAS) | Santa Monica Municipal Airport (KSMO) | 2026-04-02 16:32 UTC | 2026-04-02 17:32 UTC | 1h 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
