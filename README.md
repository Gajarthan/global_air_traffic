# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_08:53:28_UTC-green)

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

**Latest saved flight:** 2026-04-05 08:53:28 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-05 08:53:28 UTC

- **17,529** saved flights
- **9,101** unique routes
- **114** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **17,529** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **220,746.8 tonnes** estimated CO2 emissions
- **12,796,914 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 769 |
| 2 | Ryanair | 703 |
| 3 | IndiGo | 498 |
| 4 | EJA | 328 |
| 5 | American Airlines | 323 |
| 6 | Lufthansa | 247 |
| 7 | Southwest Airlines | 247 |
| 8 | ENY | 234 |
| 9 | Vueling | 196 |
| 10 | LATAM Airlines | 184 |
| 11 | AXM | 175 |
| 12 | All Nippon Airways | 154 |
| 13 | QLK | 153 |
| 14 | Delta Air Lines | 150 |
| 15 | LXJ | 149 |
| 16 | AZU | 131 |
| 17 | VIV | 131 |
| 18 | Swiss International | 128 |
| 19 | Alaska Airlines | 123 |
| 20 | Japan Airlines | 119 |
| 21 | United Airlines | 116 |
| 22 | Avianca | 113 |
| 23 | EJU | 110 |
| 24 | easyJet | 110 |
| 25 | AEE | 109 |
| 26 | AXB | 108 |
| 27 | EDV | 108 |
| 28 | WIF | 102 |
| 29 | BRC | 101 |
| 30 | Cathay Pacific | 100 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 13910 |
| 2 | 🇮🇳 IN | 1523 |
| 3 | 🇪🇸 ES | 1440 |
| 4 | 🇦🇺 AU | 1294 |
| 5 | 🇧🇷 BR | 1000 |
| 6 | 🇯🇵 JP | 947 |
| 7 | 🇩🇪 DE | 909 |
| 8 | 🇨🇴 CO | 905 |
| 9 | 🇮🇹 IT | 801 |
| 10 | 🇨🇦 CA | 780 |
| 11 | 🇬🇧 GB | 669 |
| 12 | 🇫🇷 FR | 626 |
| 13 | 🇲🇽 MX | 608 |
| 14 | 🇬🇷 GR | 481 |
| 15 | 🇨🇭 CH | 454 |
| 16 | 🇲🇾 MY | 398 |
| 17 | 🇳🇿 NZ | 394 |
| 18 | 🇿🇦 ZA | 363 |
| 19 | 🇵🇭 PH | 344 |
| 20 | 🇳🇴 NO | 341 |
| 21 | 🇬🇹 GT | 337 |
| 22 | 🇹🇷 TR | 321 |
| 23 | 🇰🇷 KR | 316 |
| 24 | 🇹🇭 TH | 248 |
| 25 | 🇵🇱 PL | 242 |
| 26 | 🇲🇦 MA | 211 |
| 27 | 🇮🇩 ID | 197 |
| 28 | 🇧🇸 BS | 191 |
| 29 | 🇲🇴 MO | 186 |
| 30 | 🇲🇪 ME | 180 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 420 |
| 2 | El Dorado International Airport |  | CO | 343 |
| 3 | Denver International Airport |  | US | 327 |
| 4 | Tokyo International Airport |  | JP | 327 |
| 5 | Indira Gandhi International Airport |  | IN | 317 |
| 6 | La Aurora Airport |  | GT | 237 |
| 7 | Harry Reid International Airport |  | US | 232 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 226 |
| 9 | Frankfurt am Main International Airport |  | DE | 219 |
| 10 | Zurich Airport |  | CH | 209 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 189 |
| 12 | Sydney Kingsford Smith International Airport |  | AU | 189 |
| 13 | Macau International Airport |  | MO | 186 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 182 |
| 15 | Guaymaral Airport |  | CO | 182 |
| 16 | Chicago O'Hare International Airport |  | US | 172 |
| 17 | Bengaluru International Airport |  | IN | 171 |
| 18 | Charlotte/Douglas International Airport |  | US | 165 |
| 19 | Madrid Barajas International Airport |  | ES | 165 |
| 20 | Atizapan De Zaragoza Airport |  | MX | 157 |
| 21 | Ninoy Aquino International Airport |  | PH | 157 |
| 22 | Congonhas Airport |  | BR | 154 |
| 23 | Tenerife Norte Airport |  | ES | 152 |
| 24 | Daniel K Inouye International Airport |  | US | 144 |
| 25 | Salt Lake City International Airport |  | US | 142 |
| 26 | Kuala Lumpur International Airport |  | MY | 140 |
| 27 | Netaji Subhash Chandra Bose International Airport |  | IN | 138 |
| 28 | Reno/Tahoe International Airport |  | US | 136 |
| 29 | Malpensa International Airport |  | IT | 135 |
| 30 | Vitoria/Foronda Airport |  | ES | 132 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 129 |
| 32 | Charles de Gaulle International Airport |  | FR | 125 |
| 33 | Miami International Airport |  | US | 123 |
| 34 | Barcelona International Airport |  | ES | 122 |
| 35 | George Bush Intcntl/Houston Airport |  | US | 117 |
| 36 | Pune Airport |  | IN | 117 |
| 37 | Seattle-Tacoma International Airport |  | US | 114 |
| 38 | General Edward Lawrence Logan International Airport |  | US | 112 |
| 39 | John Paul II International Airport Kraków-Balice Airport |  | PL | 112 |
| 40 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 110 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 81 | 1h 8m | 706 km | 986.2 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 79 | 14m | 114 km | 154.9 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 69 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 68 | 24m | 225 km | 263.8 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 62 | 29m | 304 km | 325.0 t |
| 6 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 53 | 27m | 152 km | 138.5 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 52 | 31m | - | - |
| 8 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 51 | 1h 45m | 1,156 km | 1,017.4 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 51 | 1h 27m | 910 km | 800.3 t |
| 10 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 49 | 16m | 206 km | 174.2 t |
| 11 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 46 | 22m | 99 km | 78.8 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 43 | 28m | 275 km | 203.8 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 39 | 19m | 165 km | 110.9 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 38 | 1h 11m | 770 km | 504.8 t |
| 15 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 38 | 1h 54m | 1,304 km | 854.9 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 37 | 30m | 369 km | 235.5 t |
| 17 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 37 | 52m | 556 km | 354.7 t |
| 18 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 36 | 54m | 546 km | 338.9 t |
| 19 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 20 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 33 | 1h 43m | 1,423 km | 809.9 t |
| 21 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 32 | 23m | 252 km | 138.9 t |
| 22 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 32 | 58m | 723 km | 398.9 t |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 32 | 46m | 452 km | 249.4 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 30 | 13m | 99 km | 51.4 t |
| 25 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 30 | 9m | - | - |
| 26 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 29 | 11m | 127 km | 63.5 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 27 | 20m | 147 km | 68.3 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 26 | 1h 23m | 961 km | 431.0 t |
| 29 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 25 | 16m | 183 km | 78.8 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 24 | 12m | 15 km | 6.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| OKBIT | OKB | Letnany Airport (LKLT) | Medlanky Airport (LKCM) | 2026-04-05 07:54 UTC | 2026-04-05 08:53 UTC | 59m |
| FIN99 | Finnair | Helsinki Vantaa Airport (EFHK) | Macau International Airport (VMMC) | 2026-04-04 21:48 UTC | 2026-04-05 08:52 UTC | 11h 4m |
| CPA256 | Cathay Pacific | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-04-04 21:12 UTC | 2026-04-05 08:51 UTC | 11h 38m |
| N187QS |  | Westchester County Airport (KHPN) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-05 00:40 UTC | 2026-04-05 08:49 UTC | 8h 9m |
| HLC260 | HLC | Osan Air Base (RKSO) | Osan Air Base (RKSO) | 2026-04-05 08:36 UTC | 2026-04-05 08:49 UTC | 12m |
| HKC393 | HKC | Budapest Ferenc Liszt International Airport (LHBP) | Macau International Airport (VMMC) | 2026-04-04 22:15 UTC | 2026-04-05 08:43 UTC | 10h 28m |
| SWR7AK | Swiss International | Nice-Cote d'Azur Airport (LFMN) | Zurich Airport (LSZH) | 2026-04-05 07:48 UTC | 2026-04-05 08:39 UTC | 51m |
| HBZVU | HBZ | Muenster Aero Airport (LSPU) | Raron Airport (LSTA) | 2026-04-05 06:38 UTC | 2026-04-05 08:38 UTC | 2h 0m |
| DRAGO74 | DRA | Courchevel Airport (LFLJ) | Sallanches Airport (LFHZ) | 2026-04-05 08:10 UTC | 2026-04-05 08:14 UTC | 3m |
| N364EA |  | Glendale Regional Airport (KGEU) | Indian Hills Airpark (2AZ1) | 2026-04-05 07:12 UTC | 2026-04-05 08:13 UTC | 1h 1m |
| AXM429 | AXM | Kuala Lumpur International Airport (WMKK) | Sultan Syarif Kasim Ii (Simpang Tiga) Airport (WIBB) | 2026-04-05 07:47 UTC | 2026-04-05 08:08 UTC | 20m |
| OAL3ML | OAL | Milos Airport (LGML) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-05 07:35 UTC | 2026-04-05 08:05 UTC | 29m |
|  |  | Rothenburg o. d. T. Airport (EDFR) | Rothenburg o. d. T. Airport (EDFR) | 2026-04-05 08:05 UTC | 2026-04-05 08:05 UTC | 0m |
| AXM278 | AXM | Kuala Lumpur International Airport (WMKK) | Anduki Airport (WBAK) | 2026-04-05 06:10 UTC | 2026-04-05 08:02 UTC | 1h 51m |
| DLH1MK | Lufthansa | Munich International Airport (EDDM) | Hamburg Airport (EDDH) | 2026-04-05 06:56 UTC | 2026-04-05 07:59 UTC | 1h 3m |
| DRAGO74 | DRA | Sallanches Airport (LFHZ) | Sallanches Airport (LFHZ) | 2026-04-05 07:36 UTC | 2026-04-05 07:59 UTC | 23m |
| AXB1498 | AXB | Bengaluru International Airport (VOBL) | Chandigarh Airport (VICG) | 2026-04-05 05:15 UTC | 2026-04-05 07:56 UTC | 2h 41m |
| CNF616 | CNF | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 2026-04-05 07:41 UTC | 2026-04-05 07:55 UTC | 14m |
| OEFDN | OEF | Rothenburg o. d. T. Airport (EDFR) | Rothenburg o. d. T. Airport (EDFR) | 2026-04-05 07:31 UTC | 2026-04-05 07:55 UTC | 24m |
| VLG7KA | Vueling | Sevilla Airport (LEZL) | Vitoria/Foronda Airport (LEVT) | 2026-04-05 07:01 UTC | 2026-04-05 07:55 UTC | 53m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
