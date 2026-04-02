# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--02_10:44:13_UTC-green)

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

**Latest saved flight:** 2026-04-02 10:44:13 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-02 10:44:13 UTC

- **10,685** saved flights
- **6,228** unique routes
- **111** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **10,685** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **132,234.8 tonnes** estimated CO2 emissions
- **7,665,786 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 470 |
| 2 | Ryanair | 416 |
| 3 | IndiGo | 302 |
| 4 | EJA | 215 |
| 5 | American Airlines | 188 |
| 6 | Lufthansa | 175 |
| 7 | Southwest Airlines | 164 |
| 8 | ENY | 139 |
| 9 | AXM | 116 |
| 10 | Vueling | 115 |
| 11 | LATAM Airlines | 107 |
| 12 | All Nippon Airways | 100 |
| 13 | LXJ | 100 |
| 14 | QLK | 99 |
| 15 | Delta Air Lines | 86 |
| 16 | WIF | 85 |
| 17 | Swiss International | 83 |
| 18 | Japan Airlines | 75 |
| 19 | AXB | 73 |
| 20 | Alaska Airlines | 72 |
| 21 | AZU | 72 |
| 22 | VIV | 72 |
| 23 | Cathay Pacific | 66 |
| 24 | EDV | 66 |
| 25 | United Airlines | 66 |
| 26 | EJU | 61 |
| 27 | Avianca | 60 |
| 28 | easyJet | 60 |
| 29 | BRC | 58 |
| 30 | ANZ | 56 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 8556 |
| 2 | 🇮🇳 IN | 923 |
| 3 | 🇦🇺 AU | 898 |
| 4 | 🇪🇸 ES | 819 |
| 5 | 🇩🇪 DE | 584 |
| 6 | 🇯🇵 JP | 572 |
| 7 | 🇧🇷 BR | 546 |
| 8 | 🇨🇴 CO | 524 |
| 9 | 🇨🇦 CA | 513 |
| 10 | 🇮🇹 IT | 475 |
| 11 | 🇬🇧 GB | 384 |
| 12 | 🇲🇽 MX | 379 |
| 13 | 🇫🇷 FR | 335 |
| 14 | 🇳🇴 NO | 274 |
| 15 | 🇬🇷 GR | 261 |
| 16 | 🇲🇾 MY | 260 |
| 17 | 🇳🇿 NZ | 260 |
| 18 | 🇨🇭 CH | 251 |
| 19 | 🇿🇦 ZA | 219 |
| 20 | 🇵🇭 PH | 212 |
| 21 | 🇬🇹 GT | 209 |
| 22 | 🇰🇷 KR | 195 |
| 23 | 🇹🇷 TR | 174 |
| 24 | 🇵🇱 PL | 139 |
| 25 | 🇮🇩 ID | 139 |
| 26 | 🇹🇭 TH | 138 |
| 27 | 🇲🇴 MO | 127 |
| 28 | 🇲🇦 MA | 122 |
| 29 | 🇲🇪 ME | 103 |
| 30 | 🇳🇱 NL | 101 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 252 |
| 2 | Tokyo International Airport |  | JP | 207 |
| 3 | Indira Gandhi International Airport |  | IN | 202 |
| 4 | Denver International Airport |  | US | 189 |
| 5 | Frankfurt am Main International Airport |  | DE | 175 |
| 6 | El Dorado International Airport |  | CO | 173 |
| 7 | Harry Reid International Airport |  | US | 149 |
| 8 | Guaymaral Airport |  | CO | 148 |
| 9 | La Aurora Airport |  | GT | 146 |
| 10 | Sydney Kingsford Smith International Airport |  | AU | 132 |
| 11 | Macau International Airport |  | MO | 127 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 126 |
| 13 | Zurich Airport |  | CH | 124 |
| 14 | Eleftherios Venizelos International Airport |  | GR | 123 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 106 |
| 16 | Chicago O'Hare International Airport |  | US | 105 |
| 17 | Bengaluru International Airport |  | IN | 102 |
| 18 | Kuala Lumpur International Airport |  | MY | 98 |
| 19 | Madrid Barajas International Airport |  | ES | 96 |
| 20 | Reno/Tahoe International Airport |  | US | 95 |
| 21 | Ninoy Aquino International Airport |  | PH | 95 |
| 22 | Atizapan De Zaragoza Airport |  | MX | 93 |
| 23 | Tenerife Norte Airport |  | ES | 93 |
| 24 | Charlotte/Douglas International Airport |  | US | 92 |
| 25 | Netaji Subhash Chandra Bose International Airport |  | IN | 87 |
| 26 | Congonhas Airport |  | BR | 82 |
| 27 | Malpensa International Airport |  | IT | 81 |
| 28 | Daniel K Inouye International Airport |  | US | 81 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 80 |
| 30 | Vitoria/Foronda Airport |  | ES | 78 |
| 31 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 76 |
| 32 | Charles de Gaulle International Airport |  | FR | 75 |
| 33 | Salt Lake City International Airport |  | US | 75 |
| 34 | Pune Airport |  | IN | 74 |
| 35 | Barcelona International Airport |  | ES | 74 |
| 36 | Gimpo International Airport |  | KR | 73 |
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
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 39 | 29m | 304 km | 204.4 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 33 | 1h 44m | 1,156 km | 658.3 t |
| 7 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 33 | 4m | - | - |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 31 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 31 | 20m | 165 km | 88.2 t |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 30 | 23m | 99 km | 51.4 t |
| 11 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 29 | 53m | 556 km | 278.0 t |
| 12 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 29 | 26m | 152 km | 75.8 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 28 | 1h 26m | 910 km | 439.4 t |
| 14 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 27 | 15m | 206 km | 96.0 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 25 | 30m | 369 km | 159.1 t |
| 16 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 24 | 28m | 275 km | 113.7 t |
| 17 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 24 | 1h 42m | 1,423 km | 589.0 t |
| 18 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 24 | 53m | 546 km | 226.0 t |
| 19 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 22 | 1h 10m | 770 km | 292.3 t |
| 20 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 22 | 8m | - | - |
| 21 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 21 | 1h 58m | 1,304 km | 472.4 t |
| 22 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 19 | 23m | 252 km | 82.5 t |
| 23 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 19 | 1h 1m | 723 km | 236.9 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 19 | 11m | 127 km | 41.6 t |
| 25 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 18 | 33m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 17 | 44m | 452 km | 132.5 t |
| 27 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 17 | 20m | 250 km | 73.4 t |
| 28 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 16 | 1h 46m | 1,290 km | 356.0 t |
| 29 | Brisbane International Airport (YBBN) | Maryborough Airport (YMYB) | 16 | 28m | 212 km | 58.5 t |
| 30 | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 16 | 18m | 26 km | 7.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| IFJ31T | IFJ | Cascais Airport (LPCS) | Cascais Airport (LPCS) | 2026-04-02 10:23 UTC | 2026-04-02 10:44 UTC | 21m |
| EWG6W | EWG | Berlin Brandenburg Airport (EDDB) | Meschede-Schuren Airport (EDKM) | 2026-04-02 09:24 UTC | 2026-04-02 10:21 UTC | 57m |
| EZY9097 | easyJet | London Gatwick Airport (EGKK) | Durham Tees Valley Airport (EGNV) | 2026-04-02 08:06 UTC | 2026-04-02 10:12 UTC | 2h 6m |
| IGO7015 | IndiGo | Chhatrapati Shivaji International Airport (VABB) | Mysore Airport (VOMY) | 2026-04-02 05:12 UTC | 2026-04-02 10:10 UTC | 4h 58m |
| RYR2UM | Ryanair | Belfast International Airport (EGAA) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-02 07:31 UTC | 2026-04-02 10:04 UTC | 2h 33m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-04-02 09:09 UTC | 2026-04-02 10:03 UTC | 54m |
| AFR11ZB | Air France | Charles de Gaulle International Airport (LFPG) | Stockholm-Arlanda Airport (ESSA) | 2026-04-02 07:50 UTC | 2026-04-02 10:02 UTC | 2h 11m |
| DHTAF | DHT | Frankfurt-Egelsbach Airport (EDFE) | Frankfurt-Egelsbach Airport (EDFE) | 2026-04-02 09:40 UTC | 2026-04-02 09:57 UTC | 16m |
| SEH4LQ | SEH | Eleftherios Venizelos International Airport (LGAV) | Syros Airport (LGSO) | 2026-04-02 09:45 UTC | 2026-04-02 09:55 UTC | 10m |
| NAY66 | NAY | Gran Canaria Airport (GCLP) | Tenerife Norte Airport (GCXO) | 2026-04-02 09:38 UTC | 2026-04-02 09:53 UTC | 15m |
| SEH1SM | SEH | Eleftherios Venizelos International Airport (LGAV) | Ikaria Airport (LGIK) | 2026-04-02 09:25 UTC | 2026-04-02 09:53 UTC | 27m |
| RYR1CW | Ryanair | Diagoras Airport (LGRP) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-02 07:34 UTC | 2026-04-02 09:53 UTC | 2h 18m |
| ICBAS | ICB | Trento / Mattarello Airport (LIDT) | Trento / Mattarello Airport (LIDT) | 2026-04-02 09:47 UTC | 2026-04-02 09:52 UTC | 5m |
| OEFDD | OEF | Urbe Airport (LIRU) | Guidonia Airport (LIRG) | 2026-04-02 09:36 UTC | 2026-04-02 09:51 UTC | 15m |
| AKJ554U | AKJ | Bengaluru International Airport (VOBL) | Biju Patnaik Airport (VEBS) | 2026-04-02 08:20 UTC | 2026-04-02 09:49 UTC | 1h 29m |
| FIN4BX | Finnair | Helsinki Vantaa Airport (EFHK) | Kittila Airport (EFKT) | 2026-04-02 08:45 UTC | 2026-04-02 09:49 UTC | 1h 3m |
| RYR1963 | Ryanair | Memmingen Allgau Airport (EDJA) | Sepurine Training Base (LD57) | 2026-04-02 08:57 UTC | 2026-04-02 09:48 UTC | 50m |
| SWR1CA | Swiss International | Václav Havel Airport (LKPR) | Zurich Airport (LSZH) | 2026-04-02 08:54 UTC | 2026-04-02 09:47 UTC | 53m |
| THY6DT | Turkish Airlines | Ataturk International Airport (LTBA) | Karain Airport (LTXE) | 2026-04-02 09:09 UTC | 2026-04-02 09:47 UTC | 38m |
| XU2597 |  | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 2026-04-02 09:10 UTC | 2026-04-02 09:46 UTC | 36m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
