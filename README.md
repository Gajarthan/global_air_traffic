# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--01_13:46:26_UTC-green)

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

**Latest saved flight:** 2026-04-01 13:46:26 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-01 13:46:26 UTC

- **8,726** saved flights
- **5,334** unique routes
- **107** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **8,726** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **106,623.9 tonnes** estimated CO2 emissions
- **6,181,095 km** total distance flown
- **844 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 391 |
| 2 | Ryanair | 338 |
| 3 | IndiGo | 251 |
| 4 | EJA | 175 |
| 5 | American Airlines | 154 |
| 6 | Lufthansa | 149 |
| 7 | Southwest Airlines | 134 |
| 8 | ENY | 117 |
| 9 | AXM | 102 |
| 10 | Vueling | 96 |
| 11 | LATAM Airlines | 87 |
| 12 | All Nippon Airways | 79 |
| 13 | LXJ | 73 |
| 14 | Delta Air Lines | 72 |
| 15 | QLK | 70 |
| 16 | WIF | 69 |
| 17 | Swiss International | 66 |
| 18 | AXB | 61 |
| 19 | Japan Airlines | 60 |
| 20 | AZU | 59 |
| 21 | VIV | 59 |
| 22 | Alaska Airlines | 56 |
| 23 | United Airlines | 54 |
| 24 | EDV | 53 |
| 25 | easyJet | 50 |
| 26 | Avianca | 49 |
| 27 | BRC | 49 |
| 28 | Cathay Pacific | 49 |
| 29 | EJU | 48 |
| 30 | JST | 46 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 7111 |
| 2 | 🇮🇳 IN | 771 |
| 3 | 🇦🇺 AU | 696 |
| 4 | 🇪🇸 ES | 691 |
| 5 | 🇩🇪 DE | 480 |
| 6 | 🇯🇵 JP | 459 |
| 7 | 🇧🇷 BR | 429 |
| 8 | 🇨🇴 CO | 398 |
| 9 | 🇨🇦 CA | 395 |
| 10 | 🇮🇹 IT | 394 |
| 11 | 🇬🇧 GB | 308 |
| 12 | 🇲🇽 MX | 302 |
| 13 | 🇫🇷 FR | 262 |
| 14 | 🇳🇴 NO | 228 |
| 15 | 🇲🇾 MY | 228 |
| 16 | 🇨🇭 CH | 209 |
| 17 | 🇬🇷 GR | 206 |
| 18 | 🇳🇿 NZ | 197 |
| 19 | 🇿🇦 ZA | 189 |
| 20 | 🇬🇹 GT | 174 |
| 21 | 🇵🇭 PH | 166 |
| 22 | 🇰🇷 KR | 157 |
| 23 | 🇹🇷 TR | 152 |
| 24 | 🇮🇩 ID | 119 |
| 25 | 🇹🇭 TH | 111 |
| 26 | 🇵🇱 PL | 106 |
| 27 | 🇲🇦 MA | 102 |
| 28 | 🇲🇴 MO | 90 |
| 29 | 🇲🇪 ME | 82 |
| 30 | 🇳🇱 NL | 81 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 201 |
| 2 | Indira Gandhi International Airport |  | IN | 168 |
| 3 | Tokyo International Airport |  | JP | 165 |
| 4 | Denver International Airport |  | US | 155 |
| 5 | Frankfurt am Main International Airport |  | DE | 150 |
| 6 | El Dorado International Airport |  | CO | 138 |
| 7 | Harry Reid International Airport |  | US | 123 |
| 8 | La Aurora Airport |  | GT | 122 |
| 9 | Phoenix Sky Harbor International Airport |  | US | 108 |
| 10 | Zurich Airport |  | CH | 103 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 97 |
| 12 | Sydney Kingsford Smith International Airport |  | AU | 97 |
| 13 | Guaymaral Airport |  | CO | 97 |
| 14 | Macau International Airport |  | MO | 90 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 89 |
| 16 | Tenerife Norte Airport |  | ES | 88 |
| 17 | Chicago O'Hare International Airport |  | US | 86 |
| 18 | Bengaluru International Airport |  | IN | 84 |
| 19 | Kuala Lumpur International Airport |  | MY | 84 |
| 20 | Madrid Barajas International Airport |  | ES | 79 |
| 21 | Reno/Tahoe International Airport |  | US | 77 |
| 22 | Ninoy Aquino International Airport |  | PH | 75 |
| 23 | Charlotte/Douglas International Airport |  | US | 72 |
| 24 | Netaji Subhash Chandra Bose International Airport |  | IN | 71 |
| 25 | Malpensa International Airport |  | IT | 68 |
| 26 | Atizapan De Zaragoza Airport |  | MX | 68 |
| 27 | Daniel K Inouye International Airport |  | US | 67 |
| 28 | Pune Airport |  | IN | 66 |
| 29 | Vitoria/Foronda Airport |  | ES | 64 |
| 30 | Salt Lake City International Airport |  | US | 64 |
| 31 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 63 |
| 32 | Congonhas Airport |  | BR | 62 |
| 33 | Barcelona International Airport |  | ES | 62 |
| 34 | Charles de Gaulle International Airport |  | FR | 61 |
| 35 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 61 |
| 36 | Gimpo International Airport |  | KR | 60 |
| 37 | Seattle-Tacoma International Airport |  | US | 60 |
| 38 | Miami International Airport |  | US | 58 |
| 39 | Bodø Airport |  | NO | 56 |
| 40 | O. R. Tambo International Airport |  | ZA | 54 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 40 | 1h 7m | 706 km | 487.0 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 39 | 14m | 114 km | 76.5 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 38 | 28m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 34 | 24m | 225 km | 131.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 30 | 30m | 304 km | 157.3 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 29 | 1h 45m | 1,156 km | 578.5 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 29 | 30m | - | - |
| 8 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 26 | 4m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 25 | 20m | 165 km | 71.1 t |
| 10 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 25 | 27m | 152 km | 65.3 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 24 | 15m | 206 km | 85.3 t |
| 12 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 24 | 23m | 99 km | 41.1 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 23 | 1h 26m | 910 km | 360.9 t |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 21 | 28m | 275 km | 99.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 21 | 1h 42m | 1,423 km | 515.4 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 21 | 30m | 369 km | 133.7 t |
| 17 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 20 | 52m | 556 km | 191.7 t |
| 18 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 19 | 53m | 546 km | 178.9 t |
| 19 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 18 | 1h 1m | 723 km | 224.4 t |
| 20 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 18 | 1h 10m | 770 km | 239.1 t |
| 21 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 18 | 8m | - | - |
| 22 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 17 | 11m | 127 km | 37.2 t |
| 23 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 15 | 23m | 252 km | 65.1 t |
| 24 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 15 | 20m | - | - |
| 25 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 15 | 28m | 69 km | 17.9 t |
| 26 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 15 | 20m | 250 km | 64.8 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 15 | 1h 56m | 1,304 km | 337.5 t |
| 28 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 14 | 1h 45m | 1,290 km | 311.5 t |
| 29 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 14 | 32m | - | - |
| 30 | Melbourne International Airport (YMML) | Long Hill Airport (YLHL) | 14 | 34m | 431 km | 104.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N886CB |  | Spicewood Airport (K88R) | Austin Executive Airport (KEDC) | 2026-04-01 13:32 UTC | 2026-04-01 13:46 UTC | 14m |
| N243SD |  | Brookings Regional Airport (KBKX) | Brookings Regional Airport (KBKX) | 2026-04-01 12:43 UTC | 2026-04-01 13:29 UTC | 45m |
| N813TB |  | St Pete-Clearwater International Airport (KPIE) | Plant City Airport (KPCM) | 2026-04-01 12:57 UTC | 2026-04-01 13:25 UTC | 28m |
| DESAS | DES | Bonn-Hangelar Airport (EDKB) | Koblenz-Winningen Airport (EDRK) | 2026-04-01 13:01 UTC | 2026-04-01 13:23 UTC | 21m |
| EWG5SP | EWG | Berlin Brandenburg Airport (EDDB) | Palma De Mallorca Airport (LEPA) | 2026-04-01 11:23 UTC | 2026-04-01 13:20 UTC | 1h 57m |
| EWG4BN | EWG | Dusseldorf International Airport (EDDL) | Palma De Mallorca Airport (LEPA) | 2026-04-01 10:58 UTC | 2026-04-01 13:17 UTC | 2h 19m |
| HBZTO | HBZ | Meiringen Airport (LSMM) | Meiringen Airport (LSMM) | 2026-04-01 13:13 UTC | 2026-04-01 13:17 UTC | 3m |
| D9195 |  | Chateau-Arnoux-Saint-Auban Airport (LFMX) | Fayence Airport (LFMF) | 2026-04-01 12:30 UTC | 2026-04-01 13:11 UTC | 41m |
| DKDXT | DKD | St Etienne En Devoluy Airport (LFNY) | Fayence Airport (LFMF) | 2026-04-01 12:58 UTC | 2026-04-01 13:10 UTC | 12m |
| LVGQW | LVG | San Fernando Airport (SADF) | SUGA (SUGA) | 2026-04-01 12:46 UTC | 2026-04-01 13:07 UTC | 21m |
| GEIV02 | GEI | Santos Dumont Airport (SBRJ) | Base de Aviacao de Taubate Airport (SBTA) | 2026-04-01 12:19 UTC | 2026-04-01 13:02 UTC | 42m |
| N846AA |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-04-01 12:57 UTC | 2026-04-01 13:02 UTC | 4m |
| CXK442 | CXK | Rocky Mountain Metro Airport (KBJC) | Rocky Mountain Metro Airport (KBJC) | 2026-04-01 12:39 UTC | 2026-04-01 13:00 UTC | 21m |
| N365LP |  | Flying Cloud Airport (KFCM) | Lincoln Airport (KLNK) | 2026-04-01 12:06 UTC | 2026-04-01 12:58 UTC | 51m |
| ANA868 | All Nippon Airways | Gimpo International Airport (RKSS) | Tokyo International Airport (RJTT) | 2026-04-01 11:09 UTC | 2026-04-01 12:56 UTC | 1h 46m |
| N905NY |  | Capitan FAP Carlos Martinez De Pinillos International Airport (SPRU) | Quiruvilca Airport (SPQR) | 2026-04-01 12:45 UTC | 2026-04-01 12:56 UTC | 11m |
| GLF6 | GLF | Savannah/Hilton Head International Airport (KSAV) | Brunswick Golden Isles Airport (KBQK) | 2026-04-01 12:33 UTC | 2026-04-01 12:56 UTC | 23m |
| CPA801 | Cathay Pacific | Chicago O'Hare International Airport (KORD) | Macau International Airport (VMMC) | 2026-03-31 22:26 UTC | 2026-04-01 12:56 UTC | 14h 30m |
| HBLWA | HBL | St Gallen Altenrhein Airport (LSZR) | Mengen-Hohentengen Airport (EDTM) | 2026-04-01 12:28 UTC | 2026-04-01 12:55 UTC | 26m |
| RYR9KJ | Ryanair | Budapest Ferenc Liszt International Airport (LHBP) | Malpensa International Airport (LIMC) | 2026-04-01 11:28 UTC | 2026-04-01 12:53 UTC | 1h 25m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
