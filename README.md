# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--16_13:55:39_UTC-green)

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

**Latest saved flight:** 2026-05-16 13:55:39 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-16 13:55:39 UTC

- **84,660** saved flights
- **30,465** unique routes
- **130** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **84,660** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,044,611.1 tonnes** estimated CO2 emissions
- **60,557,164 km** total distance flown
- **867 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3625 |
| 2 | SkyWest Airlines | 3127 |
| 3 | IndiGo | 1829 |
| 4 | EJA | 1594 |
| 5 | American Airlines | 1301 |
| 6 | Southwest Airlines | 1238 |
| 7 | Lufthansa | 1076 |
| 8 | ENY | 1053 |
| 9 | Delta Air Lines | 922 |
| 10 | Vueling | 802 |
| 11 | AXM | 769 |
| 12 | LATAM Airlines | 768 |
| 13 | WIF | 732 |
| 14 | AZU | 661 |
| 15 | All Nippon Airways | 659 |
| 16 | Swiss International | 657 |
| 17 | LXJ | 620 |
| 18 | QLK | 620 |
| 19 | Alaska Airlines | 599 |
| 20 | easyJet | 557 |
| 21 | EJU | 538 |
| 22 | AEE | 533 |
| 23 | Cathay Pacific | 533 |
| 24 | VIV | 505 |
| 25 | Air France | 497 |
| 26 | Japan Airlines | 474 |
| 27 | AXB | 448 |
| 28 | CXK | 447 |
| 29 | MXY | 422 |
| 30 | AIQ | 417 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 69289 |
| 2 | 🇪🇸 ES | 5981 |
| 3 | 🇮🇳 IN | 5723 |
| 4 | 🇦🇺 AU | 5410 |
| 5 | 🇩🇪 DE | 4715 |
| 6 | 🇮🇹 IT | 4673 |
| 7 | 🇧🇷 BR | 4655 |
| 8 | 🇯🇵 JP | 4258 |
| 9 | 🇨🇦 CA | 4207 |
| 10 | 🇬🇧 GB | 3615 |
| 11 | 🇫🇷 FR | 3367 |
| 12 | 🇨🇴 CO | 2834 |
| 13 | 🇲🇽 MX | 2566 |
| 14 | 🇬🇷 GR | 2461 |
| 15 | 🇳🇴 NO | 2362 |
| 16 | 🇨🇭 CH | 2231 |
| 17 | 🇲🇾 MY | 1929 |
| 18 | 🇿🇦 ZA | 1598 |
| 19 | 🇹🇷 TR | 1511 |
| 20 | 🇳🇿 NZ | 1490 |
| 21 | 🇹🇭 TH | 1474 |
| 22 | 🇵🇱 PL | 1410 |
| 23 | 🇵🇭 PH | 1330 |
| 24 | 🇰🇷 KR | 1312 |
| 25 | 🇬🇹 GT | 1274 |
| 26 | 🇲🇦 MA | 982 |
| 27 | 🇲🇴 MO | 982 |
| 28 | 🇲🇪 ME | 887 |
| 29 | 🇳🇱 NL | 861 |
| 30 | 🇭🇷 HR | 756 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1849 |
| 2 | Tokyo International Airport |  | JP | 1423 |
| 3 | Denver International Airport |  | US | 1419 |
| 4 | Indira Gandhi International Airport |  | IN | 1222 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1187 |
| 6 | Frankfurt am Main International Airport |  | DE | 1090 |
| 7 | Harry Reid International Airport |  | US | 1067 |
| 8 | Zurich Airport |  | CH | 1005 |
| 9 | Macau International Airport |  | MO | 982 |
| 10 | La Aurora Airport |  | GT | 966 |
| 11 | Guaymaral Airport |  | CO | 954 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 938 |
| 13 | El Dorado International Airport |  | CO | 912 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 850 |
| 15 | Chicago O'Hare International Airport |  | US | 817 |
| 16 | Madrid Barajas International Airport |  | ES | 771 |
| 17 | Kuala Lumpur International Airport |  | MY | 766 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 730 |
| 19 | Malpensa International Airport |  | IT | 707 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 706 |
| 21 | Salt Lake City International Airport |  | US | 704 |
| 22 | Bengaluru International Airport |  | IN | 698 |
| 23 | Capua Airport |  | IT | 690 |
| 24 | Charles de Gaulle International Airport |  | FR | 662 |
| 25 | Charlotte/Douglas International Airport |  | US | 657 |
| 26 | Congonhas Airport |  | BR | 657 |
| 27 | Daniel K Inouye International Airport |  | US | 617 |
| 28 | Tenerife Norte Airport |  | ES | 614 |
| 29 | Ninoy Aquino International Airport |  | PH | 609 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 594 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 570 |
| 32 | Barcelona International Airport |  | ES | 565 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 564 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 548 |
| 35 | Vitoria/Foronda Airport |  | ES | 536 |
| 36 | Don Mueang International Airport |  | TH | 534 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 533 |
| 38 | Amsterdam Airport Schiphol |  | NL | 522 |
| 39 | O. R. Tambo International Airport |  | ZA | 504 |
| 40 | Calgary International Airport |  | CA | 494 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 395 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 313 | 21m | 244 km | 1,318.0 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 275 | 1h 7m | 706 km | 3,348.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 240 | 24m | 225 km | 931.1 t |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 225 | 1h 26m | 910 km | 3,530.8 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 224 | 28m | 304 km | 1,174.3 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 218 | 14m | 114 km | 427.6 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 215 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 199 | 31m | - | - |
| 10 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 193 | 1h 11m | 770 km | 2,563.9 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 192 | 19m | 165 km | 546.1 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 177 | 26m | 275 km | 838.7 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 144 | 20m | 99 km | 246.7 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 133 | 31m | 369 km | 846.6 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 126 | 27m | 215 km | 466.7 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 126 | 27m | 152 km | 329.3 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 123 | 20m | 147 km | 311.3 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 122 | 14m | 154 km | 323.3 t |
| 20 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 120 | 23m | 55 km | 114.1 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 119 | 20m | 250 km | 514.0 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 115 | 1h 2m | 695 km | 1,378.5 t |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 108 | 1h 43m | 1,423 km | 2,650.5 t |
| 26 | Bodø Airport (ENBO) | ENEN (ENEN) | 108 | 13m | - | - |
| 27 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 107 | 18m | 144 km | 266.2 t |
| 28 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 104 | 12m | - | - |
| 30 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 101 | 1h 41m | 1,156 km | 2,014.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N9758H |  | Solberg/Hunterdon Airport (KN51) | Lancaster Airport (KLNS) | 2026-05-16 13:09 UTC | 2026-05-16 13:55 UTC | 45m |
| TCHGE | TCH | Trabzon International Airport (LTCG) | Trabzon International Airport (LTCG) | 2026-05-16 13:43 UTC | 2026-05-16 13:53 UTC | 10m |
| VAR447 | VAR | Phoenix Goodyear Airport (KGYR) | Buckeye Municipal Airport (KBXK) | 2026-05-16 13:22 UTC | 2026-05-16 13:51 UTC | 29m |
| GTI9449 | GTI | RAF Fairford (EGVA) | Zhuhai Airport (ZGSD) | 2026-05-16 01:56 UTC | 2026-05-16 13:50 UTC | 11h 53m |
| ENSAIO83 | ENS | Aeroclube de Itapolis Airport (SDIO) | Mirassol Airport (SDMH) | 2026-05-16 13:32 UTC | 2026-05-16 13:46 UTC | 13m |
| N2418R |  | Lake City Gateway Airport (KLCQ) | Flying C Farm Airport (FD16) | 2026-05-16 12:16 UTC | 2026-05-16 13:45 UTC | 1h 29m |
| N902TV |  | Leesburg Executive Airport (KJYO) | Lancaster Airport (KLNS) | 2026-05-16 12:57 UTC | 2026-05-16 13:36 UTC | 39m |
| N292SP |  | Ocean County Airport (KMJX) | Ocean County Airport (KMJX) | 2026-05-16 13:13 UTC | 2026-05-16 13:35 UTC | 22m |
| N103FD |  | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-05-16 12:44 UTC | 2026-05-16 13:34 UTC | 50m |
| AUB140 | AUB | Auburn University Regional Airport (KAUO) | Lanett Regional Airport (K7A3) | 2026-05-16 12:34 UTC | 2026-05-16 13:32 UTC | 57m |
| N4174B |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-05-16 13:00 UTC | 2026-05-16 13:29 UTC | 28m |
| N618VC |  | Republic Airport (KFRG) | Bridgeport/Sikorsky Airport (KBDR) | 2026-05-16 13:00 UTC | 2026-05-16 13:27 UTC | 26m |
| 5YJSK |  | Naivasha Airport (HKNV) | Jomo Kenyatta International Airport (HKJK) | 2026-05-16 13:26 UTC | 2026-05-16 13:26 UTC | 0m |
| N508HS |  | KL38 (KL38) | KL38 (KL38) | 2026-05-16 13:07 UTC | 2026-05-16 13:26 UTC | 19m |
| N695SU |  | Huber Airport (39MI) | Huber Airport (39MI) | 2026-05-16 13:22 UTC | 2026-05-16 13:22 UTC | 0m |
| NOJ88 | NOJ | Saint John Airport (CYSJ) | Bangor International Airport (KBGR) | 2026-05-16 12:54 UTC | 2026-05-16 13:22 UTC | 28m |
| N8286E |  | Albuquerque International Sunport Airport (KABQ) | NM74 (NM74) | 2026-05-16 12:45 UTC | 2026-05-16 13:19 UTC | 34m |
| N3555L |  | Prineville Airport (KS39) | Prineville Airport (KS39) | 2026-05-16 13:03 UTC | 2026-05-16 13:15 UTC | 12m |
| N847MH |  | Nellis Afb Airport (KLSV) | Harry Reid International Airport (KLAS) | 2026-05-16 13:02 UTC | 2026-05-16 13:12 UTC | 10m |
| GCMAK | GCM | Elstree Airfield (EGTR) | Elstree Airfield (EGTR) | 2026-05-16 13:11 UTC | 2026-05-16 13:12 UTC | 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
