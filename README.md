# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--15_09:51:51_UTC-green)

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

**Latest saved flight:** 2026-05-15 09:51:51 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-15 09:51:51 UTC

- **82,836** saved flights
- **29,976** unique routes
- **129** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **82,836** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,021,253.9 tonnes** estimated CO2 emissions
- **59,203,126 km** total distance flown
- **866 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3548 |
| 2 | SkyWest Airlines | 3066 |
| 3 | IndiGo | 1806 |
| 4 | EJA | 1554 |
| 5 | American Airlines | 1277 |
| 6 | Southwest Airlines | 1211 |
| 7 | Lufthansa | 1065 |
| 8 | ENY | 1034 |
| 9 | Delta Air Lines | 906 |
| 10 | Vueling | 785 |
| 11 | LATAM Airlines | 752 |
| 12 | AXM | 749 |
| 13 | WIF | 717 |
| 14 | AZU | 653 |
| 15 | All Nippon Airways | 652 |
| 16 | Swiss International | 644 |
| 17 | QLK | 615 |
| 18 | LXJ | 601 |
| 19 | Alaska Airlines | 587 |
| 20 | easyJet | 546 |
| 21 | EJU | 530 |
| 22 | AEE | 526 |
| 23 | Cathay Pacific | 518 |
| 24 | VIV | 494 |
| 25 | Air France | 487 |
| 26 | Japan Airlines | 468 |
| 27 | AXB | 442 |
| 28 | CXK | 432 |
| 29 | MXY | 410 |
| 30 | AIQ | 409 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 67657 |
| 2 | 🇪🇸 ES | 5875 |
| 3 | 🇮🇳 IN | 5645 |
| 4 | 🇦🇺 AU | 5322 |
| 5 | 🇩🇪 DE | 4637 |
| 6 | 🇧🇷 BR | 4582 |
| 7 | 🇮🇹 IT | 4572 |
| 8 | 🇯🇵 JP | 4195 |
| 9 | 🇨🇦 CA | 4124 |
| 10 | 🇬🇧 GB | 3533 |
| 11 | 🇫🇷 FR | 3292 |
| 12 | 🇨🇴 CO | 2756 |
| 13 | 🇲🇽 MX | 2506 |
| 14 | 🇬🇷 GR | 2408 |
| 15 | 🇳🇴 NO | 2312 |
| 16 | 🇨🇭 CH | 2210 |
| 17 | 🇲🇾 MY | 1883 |
| 18 | 🇿🇦 ZA | 1562 |
| 19 | 🇹🇷 TR | 1468 |
| 20 | 🇳🇿 NZ | 1463 |
| 21 | 🇹🇭 TH | 1448 |
| 22 | 🇵🇱 PL | 1382 |
| 23 | 🇵🇭 PH | 1308 |
| 24 | 🇰🇷 KR | 1272 |
| 25 | 🇬🇹 GT | 1256 |
| 26 | 🇲🇦 MA | 964 |
| 27 | 🇲🇴 MO | 952 |
| 28 | 🇲🇪 ME | 881 |
| 29 | 🇳🇱 NL | 854 |
| 30 | 🇭🇷 HR | 738 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1822 |
| 2 | Tokyo International Airport |  | JP | 1406 |
| 3 | Denver International Airport |  | US | 1388 |
| 4 | Indira Gandhi International Airport |  | IN | 1199 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1174 |
| 6 | Frankfurt am Main International Airport |  | DE | 1076 |
| 7 | Harry Reid International Airport |  | US | 1033 |
| 8 | Zurich Airport |  | CH | 986 |
| 9 | Macau International Airport |  | MO | 952 |
| 10 | La Aurora Airport |  | GT | 951 |
| 11 | Guaymaral Airport |  | CO | 925 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 923 |
| 13 | El Dorado International Airport |  | CO | 889 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 829 |
| 15 | Chicago O'Hare International Airport |  | US | 803 |
| 16 | Madrid Barajas International Airport |  | ES | 755 |
| 17 | Kuala Lumpur International Airport |  | MY | 749 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 720 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 699 |
| 20 | Malpensa International Airport |  | IT | 696 |
| 21 | Bengaluru International Airport |  | IN | 693 |
| 22 | Salt Lake City International Airport |  | US | 684 |
| 23 | Capua Airport |  | IT | 675 |
| 24 | Charles de Gaulle International Airport |  | FR | 650 |
| 25 | Charlotte/Douglas International Airport |  | US | 645 |
| 26 | Congonhas Airport |  | BR | 644 |
| 27 | Tenerife Norte Airport |  | ES | 603 |
| 28 | Daniel K Inouye International Airport |  | US | 601 |
| 29 | Ninoy Aquino International Airport |  | PH | 598 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 589 |
| 31 | Barcelona International Airport |  | ES | 556 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 555 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 554 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 535 |
| 35 | Vitoria/Foronda Airport |  | ES | 523 |
| 36 | Don Mueang International Airport |  | TH | 522 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 520 |
| 38 | Amsterdam Airport Schiphol |  | NL | 516 |
| 39 | O. R. Tambo International Airport |  | ZA | 491 |
| 40 | Calgary International Airport |  | CA | 485 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 385 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 299 | 21m | 244 km | 1,259.0 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 273 | 1h 8m | 706 km | 3,323.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 237 | 24m | 225 km | 919.4 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 222 | 28m | 304 km | 1,163.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 221 | 1h 26m | 910 km | 3,468.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 212 | 14m | 114 km | 415.8 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 211 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 196 | 31m | - | - |
| 10 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 188 | 1h 11m | 770 km | 2,497.4 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 188 | 19m | 165 km | 534.8 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 172 | 26m | 275 km | 815.0 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 142 | 20m | 99 km | 243.2 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 139 | 44m | 452 km | 1,083.3 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 128 | 31m | 369 km | 814.8 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 124 | 27m | 152 km | 324.1 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 123 | 27m | 215 km | 455.5 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 121 | 20m | 147 km | 306.2 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 119 | 14m | 154 km | 315.3 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 116 | 20m | 250 km | 501.1 t |
| 21 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 115 | 23m | 55 km | 109.3 t |
| 22 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 113 | 1h 2m | 695 km | 1,354.5 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 110 | 57m | 493 km | 935.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 107 | 1h 43m | 1,423 km | 2,625.9 t |
| 26 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |
| 27 | Bodø Airport (ENBO) | ENEN (ENEN) | 105 | 13m | - | - |
| 28 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 104 | 18m | 144 km | 258.7 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 103 | 12m | - | - |
| 30 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| GLO1000 | GLO | Congonhas Airport (SBSP) | Parati Airport (SDTK) | 2026-05-15 09:33 UTC | 2026-05-15 09:51 UTC | 18m |
| FLJ63T | FLJ | Dublin Airport (EIDW) | Madrid Barajas International Airport (LEMD) | 2026-05-15 07:56 UTC | 2026-05-15 09:47 UTC | 1h 51m |
| JST419 | JST | Gold Coast Airport (YBCG) | Sydney Kingsford Smith International Airport (YSSY) | 2026-05-15 08:40 UTC | 2026-05-15 09:44 UTC | 1h 3m |
| QTR63G | Qatar Airways | Henri Coanda International Airport (LROP) | Queen Alia International Airport (OJAI) | 2026-05-15 08:04 UTC | 2026-05-15 09:40 UTC | 1h 36m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-05-15 08:48 UTC | 2026-05-15 09:32 UTC | 44m |
| N930U |  | Hanover County Municipal Airport (KOFP) | Richmond International Airport (KRIC) | 2026-05-15 09:23 UTC | 2026-05-15 09:29 UTC | 6m |
| BLVF | BLV | Shek Kong Air Base (VHSK) | Chek Lap Kok International Airport (VHHH) | 2026-05-15 09:18 UTC | 2026-05-15 09:22 UTC | 4m |
| SWR339H | Swiss International | Luxembourg-Findel International Airport (ELLX) | Zurich Airport (LSZH) | 2026-05-15 08:40 UTC | 2026-05-15 09:22 UTC | 42m |
| UAE3U | Emirates | Al Hamra Airport (OMAH) | Queen Alia International Airport (OJAI) | 2026-05-15 06:14 UTC | 2026-05-15 09:22 UTC | 3h 8m |
| CHX04 | CHX | Celle Airport (ETHC) | Uelzen Airport (EDVU) | 2026-05-15 09:01 UTC | 2026-05-15 09:16 UTC | 15m |
| AM280 |  | Sydney Kingsford Smith International Airport (YSSY) | Adaminaby Airport (YADI) | 2026-05-15 08:31 UTC | 2026-05-15 09:13 UTC | 41m |
| THY6248 | Turkish Airlines | Ataturk International Airport (LTBA) | Macau International Airport (VMMC) | 2026-05-14 19:43 UTC | 2026-05-15 09:08 UTC | 13h 24m |
| IGO7425 | IndiGo | Indira Gandhi International Airport (VIDP) | Pantnagar Airport (VIPT) | 2026-05-15 08:31 UTC | 2026-05-15 09:03 UTC | 32m |
| VOE89ZU | VOE | Paris-Orly Airport (LFPO) | Tarbes Laloubere Airport (LFDT) | 2026-05-15 08:12 UTC | 2026-05-15 09:03 UTC | 51m |
| CSH852 | CSH | Taipei Songshan Airport (RCSS) | Macau International Airport (VMMC) | 2026-05-15 03:31 UTC | 2026-05-15 09:03 UTC | 5h 31m |
| FIN99 | Finnair | Helsinki Vantaa Airport (EFHK) | Macau International Airport (VMMC) | 2026-05-14 21:41 UTC | 2026-05-15 09:01 UTC | 11h 20m |
| AFL912 | AFL | Trabzon International Airport (LTCG) | Queen Alia International Airport (OJAI) | 2026-05-15 07:26 UTC | 2026-05-15 08:58 UTC | 1h 32m |
| SPNTH | SPN | Deblin Military Air Base (EPDE) | Deblin Military Air Base (EPDE) | 2026-05-15 08:52 UTC | 2026-05-15 08:58 UTC | 6m |
| AFR188 | Air France | Charles de Gaulle International Airport (LFPG) | Macau International Airport (VMMC) | 2026-05-14 21:50 UTC | 2026-05-15 08:57 UTC | 11h 7m |
| NOZ2FH | Norwegian Air | Oslo Gardermoen Airport (ENGM) | Sørkjosen Airport (ENSR) | 2026-05-15 07:26 UTC | 2026-05-15 08:56 UTC | 1h 30m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
