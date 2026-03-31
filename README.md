# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--31_06:40:31_UTC-green)

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

**Latest saved flight:** 2026-03-31 06:40:31 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-31 06:40:31 UTC

- **6,036** saved flights
- **4,037** unique routes
- **104** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **6,036** saved routes in the archive
- **1h 17m** average flight duration

### Carbon Footprint Estimate

- **75,940.6 tonnes** estimated CO2 emissions
- **4,402,352 km** total distance flown
- **870 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 312 |
| 2 | Ryanair | 212 |
| 3 | IndiGo | 156 |
| 4 | EJA | 129 |
| 5 | American Airlines | 121 |
| 6 | Southwest Airlines | 101 |
| 7 | ENY | 93 |
| 8 | Lufthansa | 82 |
| 9 | LATAM Airlines | 68 |
| 10 | AXM | 62 |
| 11 | LXJ | 57 |
| 12 | Delta Air Lines | 55 |
| 13 | Vueling | 55 |
| 14 | QLK | 50 |
| 15 | All Nippon Airways | 47 |
| 16 | Cathay Pacific | 47 |
| 17 | United Airlines | 46 |
| 18 | VIV | 46 |
| 19 | WIF | 44 |
| 20 | AZU | 43 |
| 21 | Japan Airlines | 41 |
| 22 | Alaska Airlines | 39 |
| 23 | EDV | 39 |
| 24 | Swiss International | 39 |
| 25 | Avianca | 37 |
| 26 | AXB | 37 |
| 27 | MXY | 33 |
| 28 | VOE | 31 |
| 29 | EJU | 30 |
| 30 | GLO | 29 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 5344 |
| 2 | 🇮🇳 IN | 463 |
| 3 | 🇦🇺 AU | 448 |
| 4 | 🇪🇸 ES | 415 |
| 5 | 🇧🇷 BR | 314 |
| 6 | 🇯🇵 JP | 291 |
| 7 | 🇨🇴 CO | 288 |
| 8 | 🇨🇦 CA | 269 |
| 9 | 🇮🇹 IT | 267 |
| 10 | 🇩🇪 DE | 250 |
| 11 | 🇲🇽 MX | 228 |
| 12 | 🇬🇧 GB | 185 |
| 13 | 🇫🇷 FR | 172 |
| 14 | 🇳🇴 NO | 147 |
| 15 | 🇲🇾 MY | 137 |
| 16 | 🇬🇹 GT | 132 |
| 17 | 🇿🇦 ZA | 127 |
| 18 | 🇨🇭 CH | 126 |
| 19 | 🇬🇷 GR | 123 |
| 20 | 🇵🇭 PH | 120 |
| 21 | 🇳🇿 NZ | 116 |
| 22 | 🇹🇷 TR | 93 |
| 23 | 🇹🇭 TH | 83 |
| 24 | 🇲🇴 MO | 76 |
| 25 | 🇲🇦 MA | 70 |
| 26 | 🇮🇩 ID | 68 |
| 27 | 🇵🇱 PL | 66 |
| 28 | 🇧🇸 BS | 60 |
| 29 | 🇰🇷 KR | 57 |
| 30 | 🇲🇪 ME | 50 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 162 |
| 2 | Denver International Airport |  | US | 122 |
| 3 | Indira Gandhi International Airport |  | IN | 105 |
| 4 | El Dorado International Airport |  | CO | 105 |
| 5 | Tokyo International Airport |  | JP | 101 |
| 6 | La Aurora Airport |  | GT | 90 |
| 7 | Frankfurt am Main International Airport |  | DE | 84 |
| 8 | Harry Reid International Airport |  | US | 81 |
| 9 | Chicago O'Hare International Airport |  | US | 76 |
| 10 | Macau International Airport |  | MO | 76 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 75 |
| 12 | Sydney Kingsford Smith International Airport |  | AU | 72 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 66 |
| 14 | Zurich Airport |  | CH | 66 |
| 15 | Guaymaral Airport |  | CO | 65 |
| 16 | Tenerife Norte Airport |  | ES | 62 |
| 17 | Reno/Tahoe International Airport |  | US | 58 |
| 18 | Eleftherios Venizelos International Airport |  | GR | 57 |
| 19 | Bengaluru International Airport |  | IN | 54 |
| 20 | Ninoy Aquino International Airport |  | PH | 54 |
| 21 | Atizapan De Zaragoza Airport |  | MX | 53 |
| 22 | Charlotte/Douglas International Airport |  | US | 50 |
| 23 | Madrid Barajas International Airport |  | ES | 50 |
| 24 | Salt Lake City International Airport |  | US | 49 |
| 25 | Kuala Lumpur International Airport |  | MY | 49 |
| 26 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 49 |
| 27 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 48 |
| 28 | Malpensa International Airport |  | IT | 47 |
| 29 | Miami International Airport |  | US | 46 |
| 30 | Charles de Gaulle International Airport |  | FR | 46 |
| 31 | Congonhas Airport |  | BR | 45 |
| 32 | Seattle-Tacoma International Airport |  | US | 44 |
| 33 | Centennial Airport |  | US | 43 |
| 34 | Daniel K Inouye International Airport |  | US | 42 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 42 |
| 36 | O. R. Tambo International Airport |  | ZA | 42 |
| 37 | Vitoria/Foronda Airport |  | ES | 41 |
| 38 | George Bush Intcntl/Houston Airport |  | US | 41 |
| 39 | Netaji Subhash Chandra Bose International Airport |  | IN | 41 |
| 40 | Los Angeles International Airport |  | US | 39 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 28 | 14m | 114 km | 54.9 t |
| 2 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 25 | 24m | 225 km | 97.0 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 25 | 27m | - | - |
| 4 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 21 | 26m | 152 km | 54.9 t |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 19 | 1h 7m | 706 km | 231.3 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 19 | 30m | - | - |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 19 | 24m | 99 km | 32.5 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 17 | 1h 41m | 1,423 km | 417.2 t |
| 9 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 16 | 15m | 206 km | 56.9 t |
| 10 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 16 | 4m | - | - |
| 11 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 15 | 1h 50m | 1,156 km | 299.2 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 15 | 21m | 165 km | 42.7 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 14 | 1h 25m | 910 km | 219.7 t |
| 14 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 14 | 30m | 369 km | 89.1 t |
| 15 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 14 | 51m | 556 km | 134.2 t |
| 16 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 13 | 29m | 275 km | 61.6 t |
| 17 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 13 | 23m | 252 km | 56.4 t |
| 18 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 13 | 1h 10m | 770 km | 172.7 t |
| 19 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 13 | 28m | 69 km | 15.5 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 13 | 20m | 250 km | 56.2 t |
| 21 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 12 | 28m | 304 km | 62.9 t |
| 22 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 12 | 53m | 546 km | 113.0 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 12 | 11m | 127 km | 26.3 t |
| 24 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 12 | 8h 41m | 38 km | 7.8 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 12 | 1h 56m | 1,304 km | 270.0 t |
| 26 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 11 | 1h 2m | 723 km | 137.1 t |
| 27 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 11 | 12m | 99 km | 18.9 t |
| 28 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 11 | 1h 46m | 1,290 km | 244.8 t |
| 29 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 11 | 30m | - | - |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 11 | 52m | 136 km | 25.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N7318F |  | Palo Alto Airport (KPAO) | Palo Alto Airport (KPAO) | 2026-03-31 05:38 UTC | 2026-03-31 06:40 UTC | 1h 2m |
| RSCU209 | RSC | Sydney Kingsford Smith International Airport (YSSY) | Sydney Kingsford Smith International Airport (YSSY) | 2026-03-31 06:24 UTC | 2026-03-31 06:34 UTC | 10m |
| YGP | YGP | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-03-31 05:42 UTC | 2026-03-31 06:25 UTC | 42m |
| ZGI | ZGI | Bacchus Marsh Airport (YBSS) | Bacchus Marsh Airport (YBSS) | 2026-03-31 05:16 UTC | 2026-03-31 06:14 UTC | 58m |
| AAL1886 | American Airlines | Pittsburgh International Airport (KPIT) | Harry Reid International Airport (KLAS) | 2026-03-31 01:55 UTC | 2026-03-31 06:12 UTC | 4h 17m |
| FD567 |  | Adelaide International Airport (YPAD) | Snowtown Airport (YSNT) | 2026-03-31 05:28 UTC | 2026-03-31 05:52 UTC | 24m |
| DLH6VV | Lufthansa | Frankfurt am Main International Airport (EDDF) | Hannover Airport (EDDV) | 2026-03-31 05:09 UTC | 2026-03-31 05:50 UTC | 40m |
| OAL062 | OAL | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 2026-03-31 05:25 UTC | 2026-03-31 05:48 UTC | 23m |
| DLA2MA | DLA | Trieste / Ronchi Dei Legionari (LIPQ) | Frankfurt am Main International Airport (EDDF) | 2026-03-31 04:31 UTC | 2026-03-31 05:44 UTC | 1h 12m |
| J886KT |  | Gading Wonosari Airport (WI1G) | Gading Wonosari Airport (WI1G) | 2026-03-31 05:43 UTC | 2026-03-31 05:44 UTC | 0m |
| HSEFS | HSE | Bang Pra Airport (VTBT) | Bang Pra Airport (VTBT) | 2026-03-31 05:12 UTC | 2026-03-31 05:40 UTC | 27m |
| VOZ656 | Virgin Australia | Sydney Kingsford Smith International Airport (YSSY) | Collector Airport (YCLT) | 2026-03-31 05:11 UTC | 2026-03-31 05:38 UTC | 27m |
| ANE2481 | ANE | Menorca Airport (LEMH) | Palma De Mallorca Airport (LEPA) | 2026-03-31 05:23 UTC | 2026-03-31 05:35 UTC | 12m |
| FIN50C | Finnair | Helsinki Vantaa Airport (EFHK) | Hamburg Airport (EDDH) | 2026-03-31 03:56 UTC | 2026-03-31 05:34 UTC | 1h 38m |
| JST656 | JST | Brisbane International Airport (YBBN) | Braidwood Airport (YBAO) | 2026-03-31 04:22 UTC | 2026-03-31 05:34 UTC | 1h 11m |
| AM324 |  | Melbourne Essendon Airport (YMEN) | Dadswells Bridge Airport (YCFF) | 2026-03-31 05:01 UTC | 2026-03-31 05:33 UTC | 32m |
| ZSASN | ZSA | Lanseria Airport (FALA) | Ventersdorp Airport (FAVE) | 2026-03-31 04:59 UTC | 2026-03-31 05:30 UTC | 30m |
| KLM89W | KLM Royal Dutch | Amsterdam Airport Schiphol (EHAM) | Brussels Airport (EBBR) | 2026-03-31 05:08 UTC | 2026-03-31 05:29 UTC | 21m |
| FJW31H | FJW | Dendron Airport (FADO) | Rand Airport (FAGM) | 2026-03-31 04:52 UTC | 2026-03-31 05:27 UTC | 35m |
| JST749 | JST | Sydney Kingsford Smith International Airport (YSSY) | Cape Barren Island Airport (YCBN) | 2026-03-31 04:27 UTC | 2026-03-31 05:26 UTC | 59m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
