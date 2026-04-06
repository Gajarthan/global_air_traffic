# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--06_19:36:24_UTC-green)

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

**Latest saved flight:** 2026-04-06 19:36:24 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-06 19:36:24 UTC

- **20,531** saved flights
- **10,263** unique routes
- **116** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **20,531** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **257,648.4 tonnes** estimated CO2 emissions
- **14,936,136 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 887 |
| 2 | Ryanair | 854 |
| 3 | IndiGo | 579 |
| 4 | American Airlines | 394 |
| 5 | EJA | 381 |
| 6 | Southwest Airlines | 289 |
| 7 | ENY | 275 |
| 8 | Lufthansa | 264 |
| 9 | Vueling | 222 |
| 10 | LATAM Airlines | 213 |
| 11 | AXM | 198 |
| 12 | Delta Air Lines | 178 |
| 13 | All Nippon Airways | 176 |
| 14 | LXJ | 175 |
| 15 | QLK | 164 |
| 16 | AZU | 160 |
| 17 | Swiss International | 152 |
| 18 | VIV | 152 |
| 19 | easyJet | 141 |
| 20 | United Airlines | 140 |
| 21 | Alaska Airlines | 135 |
| 22 | EJU | 134 |
| 23 | Japan Airlines | 134 |
| 24 | Avianca | 133 |
| 25 | AEE | 127 |
| 26 | WIF | 126 |
| 27 | EDV | 122 |
| 28 | AXB | 118 |
| 29 | Air France | 111 |
| 30 | BRC | 109 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 16101 |
| 2 | 🇮🇳 IN | 1767 |
| 3 | 🇪🇸 ES | 1646 |
| 4 | 🇦🇺 AU | 1411 |
| 5 | 🇧🇷 BR | 1172 |
| 6 | 🇨🇴 CO | 1122 |
| 7 | 🇯🇵 JP | 1090 |
| 8 | 🇩🇪 DE | 1028 |
| 9 | 🇮🇹 IT | 1016 |
| 10 | 🇨🇦 CA | 899 |
| 11 | 🇬🇧 GB | 815 |
| 12 | 🇫🇷 FR | 756 |
| 13 | 🇲🇽 MX | 700 |
| 14 | 🇬🇷 GR | 579 |
| 15 | 🇨🇭 CH | 563 |
| 16 | 🇲🇾 MY | 464 |
| 17 | 🇬🇹 GT | 462 |
| 18 | 🇿🇦 ZA | 459 |
| 19 | 🇳🇴 NO | 431 |
| 20 | 🇳🇿 NZ | 416 |
| 21 | 🇹🇷 TR | 402 |
| 22 | 🇵🇭 PH | 380 |
| 23 | 🇰🇷 KR | 351 |
| 24 | 🇹🇭 TH | 307 |
| 25 | 🇵🇱 PL | 301 |
| 26 | 🇲🇦 MA | 253 |
| 27 | 🇧🇸 BS | 227 |
| 28 | 🇲🇪 ME | 217 |
| 29 | 🇮🇩 ID | 214 |
| 30 | 🇳🇱 NL | 208 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 503 |
| 2 | El Dorado International Airport |  | CO | 420 |
| 3 | Tokyo International Airport |  | JP | 377 |
| 4 | Denver International Airport |  | US | 373 |
| 5 | Indira Gandhi International Airport |  | IN | 362 |
| 6 | La Aurora Airport |  | GT | 317 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 274 |
| 8 | Harry Reid International Airport |  | US | 268 |
| 9 | Zurich Airport |  | CH | 253 |
| 10 | Frankfurt am Main International Airport |  | DE | 235 |
| 11 | Chicago O'Hare International Airport |  | US | 223 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 222 |
| 13 | Guaymaral Airport |  | CO | 222 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 216 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 204 |
| 16 | Macau International Airport |  | MO | 200 |
| 17 | Bengaluru International Airport |  | IN | 199 |
| 18 | Charlotte/Douglas International Airport |  | US | 198 |
| 19 | Madrid Barajas International Airport |  | ES | 191 |
| 20 | Tenerife Norte Airport |  | ES | 189 |
| 21 | Atizapan De Zaragoza Airport |  | MX | 184 |
| 22 | Congonhas Airport |  | BR | 174 |
| 23 | Ninoy Aquino International Airport |  | PH | 172 |
| 24 | Salt Lake City International Airport |  | US | 164 |
| 25 | Reno/Tahoe International Airport |  | US | 162 |
| 26 | Kuala Lumpur International Airport |  | MY | 161 |
| 27 | Malpensa International Airport |  | IT | 157 |
| 28 | Daniel K Inouye International Airport |  | US | 156 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 154 |
| 30 | Charles de Gaulle International Airport |  | FR | 152 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 148 |
| 32 | Vitoria/Foronda Airport |  | ES | 145 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 144 |
| 34 | Miami International Airport |  | US | 143 |
| 35 | O. R. Tambo International Airport |  | ZA | 143 |
| 36 | Barcelona International Airport |  | ES | 136 |
| 37 | General Edward Lawrence Logan International Airport |  | US | 135 |
| 38 | Pune Airport |  | IN | 135 |
| 39 | George Bush Intcntl/Houston Airport |  | US | 133 |
| 40 | Seattle-Tacoma International Airport |  | US | 130 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 95 | 1h 8m | 706 km | 1,156.6 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 90 | 14m | 114 km | 176.5 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 81 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 74 | 24m | 225 km | 287.1 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 69 | 28m | 304 km | 361.7 t |
| 6 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 68 | 22m | 99 km | 116.5 t |
| 7 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 65 | 27m | 152 km | 169.9 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 60 | 1h 27m | 910 km | 941.5 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 58 | 31m | - | - |
| 10 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 57 | 1h 43m | 1,156 km | 1,137.1 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 55 | 16m | 206 km | 195.5 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 48 | 27m | 275 km | 227.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 46 | 19m | 165 km | 130.8 t |
| 14 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 15 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 44 | 23m | 252 km | 191.0 t |
| 16 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 44 | 1h 12m | 770 km | 584.5 t |
| 17 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 42 | 55m | 546 km | 395.4 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 42 | 52m | 556 km | 402.6 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 41 | 30m | 369 km | 261.0 t |
| 20 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 40 | 10m | - | - |
| 21 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 39 | 4m | - | - |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 39 | 20m | 250 km | 168.5 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 38 | 1h 43m | 1,423 km | 932.6 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 38 | 13m | 99 km | 65.2 t |
| 25 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 36 | 46m | 452 km | 280.6 t |
| 26 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 27 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 35 | 58m | 723 km | 436.3 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 32 | 12m | 15 km | 8.4 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 31 | 20m | 147 km | 78.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N61PF |  | Kalaeloa (John Rodgers Field) Airport (PHJR) | Kalaeloa (John Rodgers Field) Airport (PHJR) | 2026-04-06 19:23 UTC | 2026-04-06 19:36 UTC | 13m |
| N816SW |  | Merrill Field (PAMR) | Merrill Field (PAMR) | 2026-04-06 18:48 UTC | 2026-04-06 19:35 UTC | 46m |
| N4649U |  | Ted Stevens Anchorage International Airport (PANC) | Fire Island Airport (6AK5) | 2026-04-06 19:11 UTC | 2026-04-06 19:25 UTC | 13m |
| N21167 |  | Easton/Newnam Field (KESN) | Cambridge-Dorchester Regional Airport (KCGE) | 2026-04-06 19:13 UTC | 2026-04-06 19:25 UTC | 11m |
| HK4907 |  | Juan H White Airport (SKCU) | Ernesto Cortissoz International Airport (SKBQ) | 2026-04-06 18:56 UTC | 2026-04-06 19:23 UTC | 27m |
| LIFELN2 | LIF | City Of Colorado Springs Municipal Airport (KCOS) | Desiderata Ranch Airport (30CO) | 2026-04-06 18:54 UTC | 2026-04-06 19:22 UTC | 27m |
| N53TE |  | 3MI5 (3MI5) | Ann Arbor Municipal Airport (KARB) | 2026-04-06 18:45 UTC | 2026-04-06 19:20 UTC | 34m |
| N372HB |  | City Of Colorado Springs Municipal Airport (KCOS) | Lone Tree Ranch Airport (35CO) | 2026-04-06 18:45 UTC | 2026-04-06 19:17 UTC | 31m |
| N558TC |  | 84OL (84OL) | Hartsfield/Jackson Atlanta International Airport (KATL) | 2026-04-06 17:51 UTC | 2026-04-06 19:15 UTC | 1h 24m |
| DHK373 | DHK | Cincinnati/Northern Kentucky International Airport (KCVG) | Brussels Airport (EBBR) | 2026-04-06 11:51 UTC | 2026-04-06 19:13 UTC | 7h 22m |
| N309EB |  | Brandywine Regional Airport (KOQN) | DE12 (DE12) | 2026-04-06 18:27 UTC | 2026-04-06 19:13 UTC | 46m |
| HK3544G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-04-06 18:40 UTC | 2026-04-06 19:13 UTC | 32m |
| N307AG |  | Provo Municipal Airport (KPVU) | Provo Municipal Airport (KPVU) | 2026-04-06 19:05 UTC | 2026-04-06 19:13 UTC | 7m |
| N280C |  | Erie-Ottawa International Airport (KPCW) | Linville-Edom Airport (2VG3) | 2026-04-06 18:38 UTC | 2026-04-06 19:13 UTC | 34m |
| EXD83 | EXD | Sao Joao da Boa Vista Airport (SDJV) | Campo Fontenelle Airport (SBYS) | 2026-04-06 17:57 UTC | 2026-04-06 19:12 UTC | 1h 15m |
| HK5100G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-04-06 18:54 UTC | 2026-04-06 19:12 UTC | 17m |
| CXK184 | CXK | Montgomery-Gibbs Executive Airport (KMYF) | Riverside Airport (KRAL) | 2026-04-06 17:49 UTC | 2026-04-06 19:11 UTC | 1h 21m |
| BKN25 | BKN | 7IS9 (7IS9) | IL18 (IL18) | 2026-04-06 19:00 UTC | 2026-04-06 19:08 UTC | 8m |
| N27DX |  | Republic Airport (KFRG) | Laguardia Airport (KLGA) | 2026-04-06 18:53 UTC | 2026-04-06 19:08 UTC | 14m |
| N900NT |  | Orlando Executive Airport (KORL) | Charlotte/Douglas International Airport (KCLT) | 2026-04-06 18:01 UTC | 2026-04-06 19:07 UTC | 1h 6m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
