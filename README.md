# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--02_11:40:03_UTC-green)

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

**Latest saved flight:** 2026-04-02 11:40:03 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-02 11:40:03 UTC

- **10,761** saved flights
- **6,260** unique routes
- **111** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **10,761** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **133,528.7 tonnes** estimated CO2 emissions
- **7,740,793 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 470 |
| 2 | Ryanair | 418 |
| 3 | IndiGo | 306 |
| 4 | EJA | 215 |
| 5 | American Airlines | 188 |
| 6 | Lufthansa | 176 |
| 7 | Southwest Airlines | 164 |
| 8 | ENY | 139 |
| 9 | Vueling | 117 |
| 10 | AXM | 116 |
| 11 | LATAM Airlines | 107 |
| 12 | All Nippon Airways | 103 |
| 13 | LXJ | 100 |
| 14 | QLK | 99 |
| 15 | Delta Air Lines | 86 |
| 16 | WIF | 85 |
| 17 | Swiss International | 84 |
| 18 | Japan Airlines | 77 |
| 19 | AXB | 75 |
| 20 | AZU | 73 |
| 21 | Alaska Airlines | 72 |
| 22 | VIV | 72 |
| 23 | Cathay Pacific | 66 |
| 24 | EDV | 66 |
| 25 | United Airlines | 66 |
| 26 | easyJet | 64 |
| 27 | EJU | 62 |
| 28 | Avianca | 60 |
| 29 | BRC | 58 |
| 30 | ANZ | 56 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 8563 |
| 2 | 🇮🇳 IN | 940 |
| 3 | 🇦🇺 AU | 900 |
| 4 | 🇪🇸 ES | 834 |
| 5 | 🇩🇪 DE | 596 |
| 6 | 🇯🇵 JP | 588 |
| 7 | 🇧🇷 BR | 555 |
| 8 | 🇨🇴 CO | 524 |
| 9 | 🇨🇦 CA | 513 |
| 10 | 🇮🇹 IT | 477 |
| 11 | 🇬🇧 GB | 392 |
| 12 | 🇲🇽 MX | 379 |
| 13 | 🇫🇷 FR | 342 |
| 14 | 🇳🇴 NO | 274 |
| 15 | 🇬🇷 GR | 267 |
| 16 | 🇲🇾 MY | 264 |
| 17 | 🇳🇿 NZ | 260 |
| 18 | 🇨🇭 CH | 256 |
| 19 | 🇿🇦 ZA | 223 |
| 20 | 🇵🇭 PH | 212 |
| 21 | 🇬🇹 GT | 209 |
| 22 | 🇰🇷 KR | 203 |
| 23 | 🇹🇷 TR | 179 |
| 24 | 🇵🇱 PL | 141 |
| 25 | 🇹🇭 TH | 140 |
| 26 | 🇮🇩 ID | 139 |
| 27 | 🇲🇴 MO | 129 |
| 28 | 🇲🇦 MA | 125 |
| 29 | 🇲🇪 ME | 105 |
| 30 | 🇳🇱 NL | 101 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 252 |
| 2 | Tokyo International Airport |  | JP | 213 |
| 3 | Indira Gandhi International Airport |  | IN | 203 |
| 4 | Denver International Airport |  | US | 189 |
| 5 | Frankfurt am Main International Airport |  | DE | 176 |
| 6 | El Dorado International Airport |  | CO | 173 |
| 7 | Harry Reid International Airport |  | US | 150 |
| 8 | Guaymaral Airport |  | CO | 148 |
| 9 | La Aurora Airport |  | GT | 146 |
| 10 | Sydney Kingsford Smith International Airport |  | AU | 132 |
| 11 | Macau International Airport |  | MO | 129 |
| 12 | Eleftherios Venizelos International Airport |  | GR | 126 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 126 |
| 14 | Zurich Airport |  | CH | 125 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 106 |
| 16 | Bengaluru International Airport |  | IN | 106 |
| 17 | Chicago O'Hare International Airport |  | US | 105 |
| 18 | Kuala Lumpur International Airport |  | MY | 100 |
| 19 | Tenerife Norte Airport |  | ES | 98 |
| 20 | Madrid Barajas International Airport |  | ES | 97 |
| 21 | Reno/Tahoe International Airport |  | US | 95 |
| 22 | Ninoy Aquino International Airport |  | PH | 95 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 93 |
| 24 | Charlotte/Douglas International Airport |  | US | 92 |
| 25 | Netaji Subhash Chandra Bose International Airport |  | IN | 87 |
| 26 | Congonhas Airport |  | BR | 84 |
| 27 | Malpensa International Airport |  | IT | 81 |
| 28 | Daniel K Inouye International Airport |  | US | 81 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 80 |
| 30 | Vitoria/Foronda Airport |  | ES | 78 |
| 31 | Charles de Gaulle International Airport |  | FR | 76 |
| 32 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 76 |
| 33 | Gimpo International Airport |  | KR | 75 |
| 34 | Pune Airport |  | IN | 75 |
| 35 | Barcelona International Airport |  | ES | 75 |
| 36 | Salt Lake City International Airport |  | US | 75 |
| 37 | Austin-Bergstrom International Airport |  | US | 72 |
| 38 | Seattle-Tacoma International Airport |  | US | 72 |
| 39 | Bodø Airport |  | NO | 71 |
| 40 | Miami International Airport |  | US | 67 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 59 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 52 | 1h 7m | 706 km | 633.1 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 48 | 14m | 114 km | 94.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 42 | 24m | 225 km | 162.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 40 | 29m | 304 km | 209.7 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 34 | 1h 46m | 1,156 km | 678.3 t |
| 7 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 33 | 4m | - | - |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 32 | 30m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 32 | 20m | 165 km | 91.0 t |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 30 | 23m | 99 km | 51.4 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 29 | 1h 26m | 910 km | 455.1 t |
| 12 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 29 | 53m | 556 km | 278.0 t |
| 13 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 29 | 26m | 152 km | 75.8 t |
| 14 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 27 | 15m | 206 km | 96.0 t |
| 15 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 26 | 53m | 546 km | 244.8 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 25 | 30m | 369 km | 159.1 t |
| 17 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 24 | 28m | 275 km | 113.7 t |
| 18 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 24 | 1h 42m | 1,423 km | 589.0 t |
| 19 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 22 | 1h 10m | 770 km | 292.3 t |
| 20 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 22 | 8m | - | - |
| 21 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 21 | 1h 58m | 1,304 km | 472.4 t |
| 22 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 20 | 23m | 252 km | 86.8 t |
| 23 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 19 | 1h 1m | 723 km | 236.9 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 19 | 11m | 127 km | 41.6 t |
| 25 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 18 | 33m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 17 | 44m | 452 km | 132.5 t |
| 27 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 17 | 20m | 250 km | 73.4 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 16 | 20m | 147 km | 40.5 t |
| 29 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 16 | 1h 46m | 1,290 km | 356.0 t |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 16 | 19m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ABB854 | ABB | Liege Airport (EBLG) | Macau International Airport (VMMC) | 2026-04-01 23:48 UTC | 2026-04-02 11:40 UTC | 11h 51m |
| MAC828Q | MAC | Charles de Gaulle International Airport (LFPG) | Kenitra Airport (GMMY) | 2026-04-02 09:05 UTC | 2026-04-02 11:22 UTC | 2h 16m |
| TCF637 | TCF | Melbourne Orlando International Airport (KMLB) | Fellsmere Airport (4FL3) | 2026-04-02 10:51 UTC | 2026-04-02 11:18 UTC | 27m |
| FGTYF | FGT | Saint-Yan Airport (LFLN) | Lyon-Bron Airport (LFLY) | 2026-04-02 10:53 UTC | 2026-04-02 11:18 UTC | 24m |
| SEH3TK | SEH | Eleftherios Venizelos International Airport (LGAV) | Olimboi Airport (LG56) | 2026-04-02 10:49 UTC | 2026-04-02 11:11 UTC | 21m |
| OKBIS | OKB | Letnany Airport (LKLT) | Letnany Airport (LKLT) | 2026-04-02 10:47 UTC | 2026-04-02 11:08 UTC | 21m |
| DHK813 | DHK | Leipzig Halle Airport (EDDP) | Macau International Airport (VMMC) | 2026-04-02 00:14 UTC | 2026-04-02 11:03 UTC | 10h 49m |
| VOE3GE | VOE | Bordeaux-Merignac (BA 106) Airport (LFBD) | Son Bonet Airport (LESB) | 2026-04-02 09:53 UTC | 2026-04-02 10:59 UTC | 1h 6m |
| EXS9BY | EXS | Manchester Airport (EGCC) | Tivat Airport (LYTV) | 2026-04-02 08:24 UTC | 2026-04-02 10:56 UTC | 2h 31m |
| HBKFI | HBK | Lausanne-la Blecherette Airport (LSGL) | Bad Ragaz Airport (LSZE) | 2026-04-02 09:31 UTC | 2026-04-02 10:55 UTC | 1h 24m |
| JANET11 | JAN | Harry Reid International Airport (KLAS) | NV11 (NV11) | 2026-04-02 10:39 UTC | 2026-04-02 10:52 UTC | 13m |
| AEE242 | AEE | Eleftherios Venizelos International Airport (LGAV) | Ikaria Airport (LGIK) | 2026-04-02 10:21 UTC | 2026-04-02 10:50 UTC | 28m |
| IBEPP | Iberia | Vergiate Airport (LILG) | Muenster Aero Airport (LSPU) | 2026-04-02 10:30 UTC | 2026-04-02 10:49 UTC | 18m |
| MAS1276 | Malaysia Airlines | Kuala Lumpur International Airport (WMKK) | Termeloh Airport (WMBE) | 2026-04-02 10:32 UTC | 2026-04-02 10:46 UTC | 13m |
| IGO6724 | IndiGo | Agartala Airport (VEAT) | Shillong Airport (VEBI) | 2026-04-02 10:21 UTC | 2026-04-02 10:44 UTC | 22m |
| IFJ31T | IFJ | Cascais Airport (LPCS) | Cascais Airport (LPCS) | 2026-04-02 10:23 UTC | 2026-04-02 10:44 UTC | 21m |
| ANA683 | All Nippon Airways | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 2026-04-02 09:51 UTC | 2026-04-02 10:43 UTC | 51m |
| VLG53JQ | Vueling | Melsbroek Air Base (EBMB) | Castellón De La Plana Airport (LECN) | 2026-04-02 09:06 UTC | 2026-04-02 10:42 UTC | 1h 35m |
| IGO2016 | IndiGo | Juhu Aerodrome (VAJJ) | Salem Airport (VOSM) | 2026-04-02 09:13 UTC | 2026-04-02 10:40 UTC | 1h 26m |
| RSC22SD | RSC | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 2026-04-02 10:30 UTC | 2026-04-02 10:37 UTC | 6m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
