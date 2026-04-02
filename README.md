# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--02_19:53:07_UTC-green)

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

**Latest saved flight:** 2026-04-02 19:53:07 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-02 19:53:07 UTC

- **11,889** saved flights
- **6,818** unique routes
- **111** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **11,889** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **146,657.9 tonnes** estimated CO2 emissions
- **8,501,906 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 510 |
| 2 | Ryanair | 473 |
| 3 | IndiGo | 328 |
| 4 | EJA | 233 |
| 5 | American Airlines | 213 |
| 6 | Lufthansa | 194 |
| 7 | Southwest Airlines | 178 |
| 8 | ENY | 150 |
| 9 | Vueling | 129 |
| 10 | AXM | 120 |
| 11 | LATAM Airlines | 119 |
| 12 | LXJ | 112 |
| 13 | All Nippon Airways | 103 |
| 14 | QLK | 99 |
| 15 | WIF | 95 |
| 16 | Swiss International | 94 |
| 17 | Delta Air Lines | 91 |
| 18 | AZU | 87 |
| 19 | VIV | 86 |
| 20 | AXB | 80 |
| 21 | Japan Airlines | 77 |
| 22 | Alaska Airlines | 76 |
| 23 | easyJet | 74 |
| 24 | United Airlines | 74 |
| 25 | EDV | 73 |
| 26 | EJU | 73 |
| 27 | BRC | 70 |
| 28 | Cathay Pacific | 70 |
| 29 | Avianca | 68 |
| 30 | GLO | 65 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 9543 |
| 2 | 🇮🇳 IN | 1014 |
| 3 | 🇪🇸 ES | 948 |
| 4 | 🇦🇺 AU | 904 |
| 5 | 🇩🇪 DE | 664 |
| 6 | 🇧🇷 BR | 652 |
| 7 | 🇯🇵 JP | 595 |
| 8 | 🇨🇴 CO | 583 |
| 9 | 🇨🇦 CA | 551 |
| 10 | 🇮🇹 IT | 546 |
| 11 | 🇬🇧 GB | 457 |
| 12 | 🇲🇽 MX | 424 |
| 13 | 🇫🇷 FR | 398 |
| 14 | 🇬🇷 GR | 301 |
| 15 | 🇳🇴 NO | 300 |
| 16 | 🇨🇭 CH | 293 |
| 17 | 🇲🇾 MY | 273 |
| 18 | 🇳🇿 NZ | 260 |
| 19 | 🇿🇦 ZA | 237 |
| 20 | 🇬🇹 GT | 226 |
| 21 | 🇵🇭 PH | 216 |
| 22 | 🇹🇷 TR | 210 |
| 23 | 🇰🇷 KR | 204 |
| 24 | 🇵🇱 PL | 172 |
| 25 | 🇹🇭 TH | 150 |
| 26 | 🇮🇩 ID | 143 |
| 27 | 🇲🇦 MA | 143 |
| 28 | 🇲🇴 MO | 135 |
| 29 | 🇳🇱 NL | 120 |
| 30 | 🇲🇪 ME | 118 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 281 |
| 2 | Indira Gandhi International Airport |  | IN | 218 |
| 3 | Tokyo International Airport |  | JP | 213 |
| 4 | Denver International Airport |  | US | 210 |
| 5 | El Dorado International Airport |  | CO | 199 |
| 6 | Frankfurt am Main International Airport |  | DE | 184 |
| 7 | Harry Reid International Airport |  | US | 163 |
| 8 | La Aurora Airport |  | GT | 158 |
| 9 | Guaymaral Airport |  | CO | 152 |
| 10 | Zurich Airport |  | CH | 146 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 138 |
| 12 | Macau International Airport |  | MO | 135 |
| 13 | Sydney Kingsford Smith International Airport |  | AU | 133 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 132 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 119 |
| 16 | Bengaluru International Airport |  | IN | 114 |
| 17 | Chicago O'Hare International Airport |  | US | 113 |
| 18 | Madrid Barajas International Airport |  | ES | 108 |
| 19 | Charlotte/Douglas International Airport |  | US | 107 |
| 20 | Atizapan De Zaragoza Airport |  | MX | 105 |
| 21 | Tenerife Norte Airport |  | ES | 105 |
| 22 | Kuala Lumpur International Airport |  | MY | 104 |
| 23 | Congonhas Airport |  | BR | 101 |
| 24 | Ninoy Aquino International Airport |  | PH | 97 |
| 25 | Reno/Tahoe International Airport |  | US | 96 |
| 26 | Netaji Subhash Chandra Bose International Airport |  | IN | 92 |
| 27 | Malpensa International Airport |  | IT | 90 |
| 28 | Vitoria/Foronda Airport |  | ES | 90 |
| 29 | Daniel K Inouye International Airport |  | US | 88 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 87 |
| 31 | Charles de Gaulle International Airport |  | FR | 86 |
| 32 | Barcelona International Airport |  | ES | 84 |
| 33 | Salt Lake City International Airport |  | US | 84 |
| 34 | Pune Airport |  | IN | 80 |
| 35 | Austin-Bergstrom International Airport |  | US | 79 |
| 36 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 79 |
| 37 | Bodø Airport |  | NO | 78 |
| 38 | Seattle-Tacoma International Airport |  | US | 76 |
| 39 | Gimpo International Airport |  | KR | 75 |
| 40 | George Bush Intcntl/Houston Airport |  | US | 75 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 60 | 27m | - | - |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 56 | 14m | 114 km | 109.8 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 52 | 1h 7m | 706 km | 633.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 42 | 24m | 225 km | 162.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 40 | 29m | 304 km | 209.7 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 37 | 1h 46m | 1,156 km | 738.1 t |
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
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 19 | 13m | 99 km | 32.6 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 18 | 20m | 147 km | 45.6 t |
| 27 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 18 | 33m | - | - |
| 28 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 18 | 26m | 69 km | 21.5 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 17 | 44m | 452 km | 132.5 t |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 17 | 19m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N27DX |  | Republic Airport (KFRG) | Laguardia Airport (KLGA) | 2026-04-02 19:38 UTC | 2026-04-02 19:53 UTC | 14m |
| N243TX |  | San Antonio International Airport (KSAT) | Austin-Bergstrom International Airport (KAUS) | 2026-04-02 19:29 UTC | 2026-04-02 19:52 UTC | 22m |
| SYS48 | SYS | RAF Shawbury (EGOS) | RAF Shawbury (EGOS) | 2026-04-02 19:16 UTC | 2026-04-02 19:44 UTC | 28m |
| FH734 |  | Santa Rosa Nolf Airport (KNGS) | Santa Rosa Nolf Airport (KNGS) | 2026-04-02 19:06 UTC | 2026-04-02 19:41 UTC | 35m |
| N92486 |  | Porterville Municipal Airport (KPTV) | Meadows Field (KBFL) | 2026-04-02 19:09 UTC | 2026-04-02 19:41 UTC | 31m |
| N1345P |  | Chickasha Municipal Airport (KCHK) | Anadarko Municipal Airport (KF68) | 2026-04-02 19:28 UTC | 2026-04-02 19:40 UTC | 11m |
| EJA572 | EJA | Monterey Regional Airport (KMRY) | Moffett Federal Airfield (KNUQ) | 2026-04-02 19:17 UTC | 2026-04-02 19:31 UTC | 14m |
| SIL1705 | SIL | Ted Stevens Anchorage International Airport (PANC) | Kenai Municipal Airport (PAEN) | 2026-04-02 19:11 UTC | 2026-04-02 19:26 UTC | 14m |
| N4888C |  | Williams Field (5MI7) | Jackson County/Reynolds Field (KJXN) | 2026-04-02 19:15 UTC | 2026-04-02 19:25 UTC | 9m |
| SHINR42 | SHI | Austin-Bergstrom International Airport (KAUS) | Hawken Air One Airport (62TA) | 2026-04-02 19:01 UTC | 2026-04-02 19:25 UTC | 23m |
| LXJ320 | LXJ | San Antonio International Airport (KSAT) | K36U (K36U) | 2026-04-02 17:00 UTC | 2026-04-02 19:22 UTC | 2h 21m |
| N2135K |  | Indianapolis Executive Airport (KTYQ) | Monroe County Airport (KBMG) | 2026-04-02 18:22 UTC | 2026-04-02 19:17 UTC | 55m |
| N303ZZ |  | Centennial Airport (KAPA) | Colorado Plains Regional Airport (KAKO) | 2026-04-02 18:47 UTC | 2026-04-02 19:16 UTC | 28m |
|  |  | Portage County Airport (KPOV) | Portage County Airport (KPOV) | 2026-04-02 19:15 UTC | 2026-04-02 19:15 UTC | 0m |
| RN110 |  | Triple B Airpark (FL81) | Evergreen Regional/Middleton Field (KGZH) | 2026-04-02 18:57 UTC | 2026-04-02 19:15 UTC | 18m |
| GLO1555 | GLO | Pinto Martins International Airport (SBFZ) | Professor Urbano Ernesto Stumpf Airport (SBSJ) | 2026-04-02 15:59 UTC | 2026-04-02 19:13 UTC | 3h 13m |
| WZZ4295 | Wizz Air | John Paul II International Airport Kraków-Balice Airport (EPKK) | Malpensa International Airport (LIMC) | 2026-04-02 17:33 UTC | 2026-04-02 19:13 UTC | 1h 39m |
| N65435 |  | 24TX (24TX) | 5TS4 (5TS4) | 2026-04-02 18:14 UTC | 2026-04-02 19:12 UTC | 57m |
| N665M |  | Palo Alto Airport (KPAO) | Tracy Municipal Airport (KTCY) | 2026-04-02 18:39 UTC | 2026-04-02 19:12 UTC | 32m |
| TAUNT41 | TAU | 75OK (75OK) | Blackwell-Tonkawa Municipal Airport (KBKN) | 2026-04-02 19:02 UTC | 2026-04-02 19:11 UTC | 8m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
