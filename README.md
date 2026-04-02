# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--02_13:30:23_UTC-green)

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

**Latest saved flight:** 2026-04-02 13:30:23 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-02 13:30:23 UTC

- **10,882** saved flights
- **6,307** unique routes
- **111** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **10,882** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **135,068.6 tonnes** estimated CO2 emissions
- **7,830,064 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 470 |
| 2 | Ryanair | 431 |
| 3 | IndiGo | 311 |
| 4 | EJA | 215 |
| 5 | American Airlines | 189 |
| 6 | Lufthansa | 177 |
| 7 | Southwest Airlines | 164 |
| 8 | ENY | 139 |
| 9 | Vueling | 119 |
| 10 | AXM | 117 |
| 11 | LATAM Airlines | 110 |
| 12 | All Nippon Airways | 103 |
| 13 | LXJ | 101 |
| 14 | QLK | 99 |
| 15 | WIF | 90 |
| 16 | Delta Air Lines | 86 |
| 17 | Swiss International | 84 |
| 18 | AXB | 77 |
| 19 | Japan Airlines | 77 |
| 20 | AZU | 74 |
| 21 | Alaska Airlines | 72 |
| 22 | VIV | 72 |
| 23 | Cathay Pacific | 68 |
| 24 | EDV | 66 |
| 25 | United Airlines | 66 |
| 26 | easyJet | 65 |
| 27 | EJU | 63 |
| 28 | Avianca | 61 |
| 29 | BRC | 58 |
| 30 | AEE | 56 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 8605 |
| 2 | 🇮🇳 IN | 957 |
| 3 | 🇦🇺 AU | 904 |
| 4 | 🇪🇸 ES | 860 |
| 5 | 🇩🇪 DE | 609 |
| 6 | 🇯🇵 JP | 591 |
| 7 | 🇧🇷 BR | 563 |
| 8 | 🇨🇴 CO | 534 |
| 9 | 🇨🇦 CA | 515 |
| 10 | 🇮🇹 IT | 488 |
| 11 | 🇬🇧 GB | 403 |
| 12 | 🇲🇽 MX | 381 |
| 13 | 🇫🇷 FR | 350 |
| 14 | 🇳🇴 NO | 285 |
| 15 | 🇬🇷 GR | 270 |
| 16 | 🇲🇾 MY | 266 |
| 17 | 🇨🇭 CH | 260 |
| 18 | 🇳🇿 NZ | 260 |
| 19 | 🇿🇦 ZA | 227 |
| 20 | 🇵🇭 PH | 212 |
| 21 | 🇬🇹 GT | 209 |
| 22 | 🇰🇷 KR | 204 |
| 23 | 🇹🇷 TR | 180 |
| 24 | 🇵🇱 PL | 146 |
| 25 | 🇹🇭 TH | 144 |
| 26 | 🇮🇩 ID | 143 |
| 27 | 🇲🇴 MO | 133 |
| 28 | 🇲🇦 MA | 127 |
| 29 | 🇲🇪 ME | 108 |
| 30 | 🇳🇱 NL | 105 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 252 |
| 2 | Tokyo International Airport |  | JP | 213 |
| 3 | Indira Gandhi International Airport |  | IN | 206 |
| 4 | Denver International Airport |  | US | 189 |
| 5 | El Dorado International Airport |  | CO | 178 |
| 6 | Frankfurt am Main International Airport |  | DE | 178 |
| 7 | Harry Reid International Airport |  | US | 151 |
| 8 | Guaymaral Airport |  | CO | 149 |
| 9 | La Aurora Airport |  | GT | 146 |
| 10 | Macau International Airport |  | MO | 133 |
| 11 | Sydney Kingsford Smith International Airport |  | AU | 133 |
| 12 | Eleftherios Venizelos International Airport |  | GR | 127 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 126 |
| 14 | Zurich Airport |  | CH | 125 |
| 15 | Bengaluru International Airport |  | IN | 107 |
| 16 | Hartsfield/Jackson Atlanta International Airport |  | US | 106 |
| 17 | Chicago O'Hare International Airport |  | US | 106 |
| 18 | Kuala Lumpur International Airport |  | MY | 101 |
| 19 | Tenerife Norte Airport |  | ES | 100 |
| 20 | Madrid Barajas International Airport |  | ES | 98 |
| 21 | Reno/Tahoe International Airport |  | US | 95 |
| 22 | Ninoy Aquino International Airport |  | PH | 95 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 93 |
| 24 | Charlotte/Douglas International Airport |  | US | 93 |
| 25 | Netaji Subhash Chandra Bose International Airport |  | IN | 90 |
| 26 | Congonhas Airport |  | BR | 84 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 83 |
| 28 | Malpensa International Airport |  | IT | 82 |
| 29 | Daniel K Inouye International Airport |  | US | 82 |
| 30 | Vitoria/Foronda Airport |  | ES | 80 |
| 31 | Barcelona International Airport |  | ES | 78 |
| 32 | Charles de Gaulle International Airport |  | FR | 76 |
| 33 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 76 |
| 34 | Gimpo International Airport |  | KR | 75 |
| 35 | Pune Airport |  | IN | 75 |
| 36 | Salt Lake City International Airport |  | US | 75 |
| 37 | Bodø Airport |  | NO | 74 |
| 38 | Austin-Bergstrom International Airport |  | US | 72 |
| 39 | Seattle-Tacoma International Airport |  | US | 72 |
| 40 | Miami International Airport |  | US | 67 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 59 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 52 | 1h 7m | 706 km | 633.1 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 51 | 14m | 114 km | 100.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 42 | 24m | 225 km | 162.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 40 | 29m | 304 km | 209.7 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 34 | 1h 46m | 1,156 km | 678.3 t |
| 7 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 34 | 4m | - | - |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 32 | 30m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 32 | 20m | 165 km | 91.0 t |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 30 | 23m | 99 km | 51.4 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 29 | 1h 26m | 910 km | 455.1 t |
| 12 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 29 | 53m | 556 km | 278.0 t |
| 13 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 29 | 26m | 152 km | 75.8 t |
| 14 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 28 | 15m | 206 km | 99.5 t |
| 15 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 26 | 53m | 546 km | 244.8 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 25 | 30m | 369 km | 159.1 t |
| 17 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 24 | 28m | 275 km | 113.7 t |
| 18 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 24 | 1h 42m | 1,423 km | 589.0 t |
| 19 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 22 | 1h 10m | 770 km | 292.3 t |
| 20 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 22 | 8m | - | - |
| 21 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 21 | 1h 58m | 1,304 km | 472.4 t |
| 22 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 20 | 23m | 252 km | 86.8 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 20 | 11m | 127 km | 43.8 t |
| 24 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 19 | 1h 1m | 723 km | 236.9 t |
| 25 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 18 | 33m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 17 | 44m | 452 km | 132.5 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 17 | 19m | - | - |
| 28 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 17 | 20m | 250 km | 73.4 t |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 16 | 20m | 147 km | 40.5 t |
| 30 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 16 | 1h 46m | 1,290 km | 356.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N718LU |  | Lynchburg Regional/Preston Glenn Field (KLYH) | Richmond International Airport (KRIC) | 2026-04-02 12:48 UTC | 2026-04-02 13:30 UTC | 42m |
| WEY42G | WEY | Cascais Airport (LPCS) | Sintra Airport (LPST) | 2026-04-02 12:40 UTC | 2026-04-02 13:30 UTC | 49m |
| HNL14A | HNL | De Kooy Airport (EHKD) | Rotterdam Airport (EHRD) | 2026-04-02 12:57 UTC | 2026-04-02 13:24 UTC | 27m |
| TGJAK | TGJ | Matehuala Airport (MM67) | Matehuala Airport (MM67) | 2026-04-02 13:11 UTC | 2026-04-02 13:22 UTC | 11m |
| CCA186 | Air China | Taiwan Taoyuan International Airport (RCTP) | Macau International Airport (VMMC) | 2026-04-02 05:08 UTC | 2026-04-02 13:21 UTC | 8h 13m |
| SPGTT | SPG | Mielec Airport (EPML) | Mielec Airport (EPML) | 2026-04-02 13:01 UTC | 2026-04-02 13:16 UTC | 15m |
| CPA332 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-04-02 05:17 UTC | 2026-04-02 13:15 UTC | 7h 58m |
| N38549 |  | Laconia Municipal Airport (KLCI) | Laconia Municipal Airport (KLCI) | 2026-04-02 12:54 UTC | 2026-04-02 13:10 UTC | 16m |
| DHK524 | DHK | Malpensa International Airport (LIMC) | Macau International Airport (VMMC) | 2026-04-02 02:26 UTC | 2026-04-02 13:09 UTC | 10h 43m |
| LJC6 | LJC | Gloucestershire Airport (EGBJ) | Guernsey Airport (EGJB) | 2026-04-02 12:25 UTC | 2026-04-02 13:09 UTC | 43m |
| DFELI | DFE | Thalmassing-Waizenhofen Airport (EDPW) | Thalmassing-Waizenhofen Airport (EDPW) | 2026-04-02 12:21 UTC | 2026-04-02 13:08 UTC | 46m |
| N20292 |  | Hinton Field (NC72) | Spencer Field (7NC9) | 2026-04-02 12:32 UTC | 2026-04-02 13:01 UTC | 29m |
| AM234 |  | Sydney Kingsford Smith International Airport (YSSY) | Nambucca Heads Airport (YNHS) | 2026-04-02 12:24 UTC | 2026-04-02 12:58 UTC | 34m |
| N5158J |  | Cheyenne Regional/Jerry Olson Field (KCYS) | WY59 (WY59) | 2026-04-02 12:34 UTC | 2026-04-02 12:58 UTC | 23m |
| N3363E |  | Casper/Natrona County International Airport (KCPR) | Casper/Natrona County International Airport (KCPR) | 2026-04-02 12:42 UTC | 2026-04-02 12:57 UTC | 15m |
| ICBAS | ICB | Trento / Mattarello Airport (LIDT) | Trento / Mattarello Airport (LIDT) | 2026-04-02 12:51 UTC | 2026-04-02 12:56 UTC | 5m |
| CXK538 | CXK | Clark Regional Airport (KJVY) | Clark Regional Airport (KJVY) | 2026-04-02 12:47 UTC | 2026-04-02 12:55 UTC | 7m |
| WIF66D | WIF | Bodø Airport (ENBO) | Mo i Rana Airport Rossvoll (ENRA) | 2026-04-02 12:33 UTC | 2026-04-02 12:47 UTC | 14m |
| WIF3B | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-04-02 12:18 UTC | 2026-04-02 12:46 UTC | 28m |
| DESRT3 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-04-02 12:30 UTC | 2026-04-02 12:46 UTC | 15m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
