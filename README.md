# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--29_18:10:08_UTC-green)

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

**Latest saved flight:** 2026-03-29 18:10:08 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-29 18:10:08 UTC

- **2,685** saved flights
- **2,063** unique routes
- **93** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **2,685** saved routes in the archive
- **1h 20m** average flight duration

### Carbon Footprint Estimate

- **35,957.4 tonnes** estimated CO2 emissions
- **2,084,485 km** total distance flown
- **907 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 120 |
| 2 | Ryanair | 91 |
| 3 | IndiGo | 77 |
| 4 | EJA | 54 |
| 5 | American Airlines | 49 |
| 6 | Lufthansa | 49 |
| 7 | Southwest Airlines | 49 |
| 8 | ENY | 42 |
| 9 | AXM | 38 |
| 10 | Delta Air Lines | 30 |
| 11 | Vueling | 28 |
| 12 | LXJ | 26 |
| 13 | LATAM Airlines | 26 |
| 14 | United Airlines | 23 |
| 15 | Cathay Pacific | 21 |
| 16 | All Nippon Airways | 20 |
| 17 | Avianca | 19 |
| 18 | Swiss International | 19 |
| 19 | AXB | 18 |
| 20 | Japan Airlines | 18 |
| 21 | BRC | 17 |
| 22 | VIV | 17 |
| 23 | WIF | 17 |
| 24 | ARE | 16 |
| 25 | EDV | 16 |
| 26 | VOE | 16 |
| 27 | Alaska Airlines | 15 |
| 28 | SFR | 15 |
| 29 | AEE | 14 |
| 30 | APG | 14 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 2258 |
| 2 | 🇪🇸 ES | 217 |
| 3 | 🇮🇳 IN | 212 |
| 4 | 🇨🇴 CO | 167 |
| 5 | 🇩🇪 DE | 145 |
| 6 | 🇯🇵 JP | 132 |
| 7 | 🇦🇺 AU | 125 |
| 8 | 🇧🇷 BR | 118 |
| 9 | 🇮🇹 IT | 110 |
| 10 | 🇨🇦 CA | 108 |
| 11 | 🇬🇧 GB | 96 |
| 12 | 🇲🇽 MX | 93 |
| 13 | 🇿🇦 ZA | 82 |
| 14 | 🇲🇾 MY | 81 |
| 15 | 🇬🇹 GT | 81 |
| 16 | 🇫🇷 FR | 80 |
| 17 | 🇨🇭 CH | 66 |
| 18 | 🇵🇭 PH | 63 |
| 19 | 🇬🇷 GR | 56 |
| 20 | 🇳🇴 NO | 55 |
| 21 | 🇹🇷 TR | 46 |
| 22 | 🇹🇭 TH | 44 |
| 23 | 🇵🇱 PL | 39 |
| 24 | 🇧🇸 BS | 36 |
| 25 | 🇮🇩 ID | 35 |
| 26 | 🇫🇮 FI | 35 |
| 27 | 🇲🇦 MA | 34 |
| 28 | 🇲🇴 MO | 32 |
| 29 | 🇳🇱 NL | 27 |
| 30 | 🇰🇷 KR | 26 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 61 |
| 2 | El Dorado International Airport |  | CO | 58 |
| 3 | La Aurora Airport |  | GT | 51 |
| 4 | Frankfurt am Main International Airport |  | DE | 50 |
| 5 | Guaymaral Airport |  | CO | 48 |
| 6 | Indira Gandhi International Airport |  | IN | 47 |
| 7 | Denver International Airport |  | US | 45 |
| 8 | Tokyo International Airport |  | JP | 44 |
| 9 | Tenerife Norte Airport |  | ES | 37 |
| 10 | Kuala Lumpur International Airport |  | MY | 33 |
| 11 | Zurich Airport |  | CH | 32 |
| 12 | Macau International Airport |  | MO | 32 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 31 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 31 |
| 15 | Harry Reid International Airport |  | US | 30 |
| 16 | O. R. Tambo International Airport |  | ZA | 29 |
| 17 | Chicago O'Hare International Airport |  | US | 28 |
| 18 | Ninoy Aquino International Airport |  | PH | 26 |
| 19 | Vitoria/Foronda Airport |  | ES | 25 |
| 20 | Netaji Subhash Chandra Bose International Airport |  | IN | 25 |
| 21 | Atizapan De Zaragoza Airport |  | MX | 24 |
| 22 | Eleftherios Venizelos International Airport |  | GR | 23 |
| 23 | Charlotte/Douglas International Airport |  | US | 23 |
| 24 | Miami International Airport |  | US | 23 |
| 25 | Madrid Barajas International Airport |  | ES | 23 |
| 26 | Charles de Gaulle International Airport |  | FR | 23 |
| 27 | Salt Lake City International Airport |  | US | 23 |
| 28 | Amsterdam Airport Schiphol |  | NL | 22 |
| 29 | Bengaluru International Airport |  | IN | 21 |
| 30 | VGZR |  |  | 21 |
| 31 | Centennial Airport |  | US | 20 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 19 |
| 33 | Reno/Tahoe International Airport |  | US | 19 |
| 34 | Sydney Kingsford Smith International Airport |  | AU | 19 |
| 35 | George Bush Intcntl/Houston Airport |  | US | 19 |
| 36 | John Paul II International Airport Kraków-Balice Airport |  | PL | 19 |
| 37 | CO86 |  |  | 18 |
| 38 | Helsinki Vantaa Airport |  | FI | 18 |
| 39 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 18 |
| 40 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 18 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 19 | 25m | - | - |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 17 | 14m | 114 km | 33.3 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 14 | 23m | 225 km | 54.3 t |
| 4 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 14 | 24m | 99 km | 24.0 t |
| 5 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 13 | 20m | 250 km | 56.2 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 12 | 30m | - | - |
| 7 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 11 | 1h 39m | 1,423 km | 270.0 t |
| 8 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 11 | 24m | 152 km | 28.7 t |
| 9 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 10 | 12m | 99 km | 17.1 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 9 | 29m | 275 km | 42.6 t |
| 11 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 9 | 22m | 252 km | 39.1 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 9 | 1h 7m | 706 km | 109.6 t |
| 13 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 8 | 14m | 206 km | 28.4 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 8 | 22m | 165 km | 22.8 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 7 | 28m | 304 km | 36.7 t |
| 16 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 7 | 1h 44m | 1,290 km | 155.8 t |
| 17 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 7 | 52m | 136 km | 16.4 t |
| 18 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 7 | 34m | 69 km | 8.4 t |
| 19 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 6 | 52m | 546 km | 56.5 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Sepulot Airport (WBKO) | 6 | 2h 4m | 1,652 km | 171.0 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 6 | 11m | 127 km | 13.1 t |
| 22 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 6 | 8h 51m | 38 km | 3.9 t |
| 23 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 6 | 1h 27m | 910 km | 94.2 t |
| 24 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 6 | 17m | 55 km | 5.7 t |
| 25 | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 6 | 12m | - | - |
| 26 | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 6 | 14m | - | - |
| 27 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 6 | 4m | - | - |
| 28 | Phoenix Sky Harbor International Airport (KPHX) | Reno/Tahoe International Airport (KRNO) | 5 | 1h 20m | 967 km | 83.4 t |
| 29 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 5 | 29m | 369 km | 31.8 t |
| 30 | VGZR (VGZR) | Lengpui Airport (VELP) | 5 | 22m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CLX7956 | CLX | Luxembourg-Findel International Airport (ELLX) | Macau International Airport (VMMC) | 2026-03-29 04:00 UTC | 2026-03-29 18:10 UTC | 14h 9m |
| ACA1046 | Air Canada | Vancouver International Airport (CYVR) | Yucca Valley Airport (KL22) | 2026-03-29 15:45 UTC | 2026-03-29 18:09 UTC | 2h 24m |
| N107MR |  | Meriden Markham Municipal Airport (KMMK) | Tweed/New Haven Airport (KHVN) | 2026-03-29 17:50 UTC | 2026-03-29 18:02 UTC | 11m |
| N485DL |  | Rocky Mountain Metro Airport (KBJC) | Erie Municipal Airport (KEIK) | 2026-03-29 17:26 UTC | 2026-03-29 18:00 UTC | 34m |
| N216LT |  | Dupage Airport (KDPA) | Ruder Airport (59IL) | 2026-03-29 17:36 UTC | 2026-03-29 17:57 UTC | 21m |
| N938GC |  | Charleston Afb/International Airport (KCHS) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-03-29 17:04 UTC | 2026-03-29 17:55 UTC | 51m |
| N909YR |  | Scottsdale Airport (KSDL) | Sedona Airport (KSEZ) | 2026-03-29 17:35 UTC | 2026-03-29 17:52 UTC | 17m |
| AFL1137 | AFL | Sochi International Airport (URSS) | Sheremetyevo International Airport (UUEE) | 2026-03-29 14:59 UTC | 2026-03-29 17:51 UTC | 2h 52m |
| DRAGO741 | DRA | Annecy-Haute-Savoie-Mont Blanc Airport (LFLP) | Sallanches Airport (LFHZ) | 2026-03-29 17:25 UTC | 2026-03-29 17:50 UTC | 24m |
| N895CA |  | Aztec Municipal Airport (KN19) | Phoenix Sky Harbor International Airport (KPHX) | 2026-03-29 16:55 UTC | 2026-03-29 17:49 UTC | 53m |
| N1Y |  | Naples Municipal Airport (KAPF) | Southwest Florida International Airport (KRSW) | 2026-03-29 16:50 UTC | 2026-03-29 17:45 UTC | 54m |
| TGCCC | TGC | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 2026-03-29 17:21 UTC | 2026-03-29 17:45 UTC | 23m |
| MFX558 | MFX | Indira Gandhi International Airport (VIDP) | Sheremetyevo International Airport (UUEE) | 2026-03-29 07:01 UTC | 2026-03-29 17:44 UTC | 10h 43m |
| N216AF |  | Montgomery-Gibbs Executive Airport (KMYF) | Banning Municipal Airport (KBNG) | 2026-03-29 17:01 UTC | 2026-03-29 17:43 UTC | 41m |
| N417JS |  | Earl Barnickel Airport (IL88) | Willadae Farms Airport (4LL7) | 2026-03-29 17:20 UTC | 2026-03-29 17:38 UTC | 17m |
| N815SS |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-03-29 16:02 UTC | 2026-03-29 17:38 UTC | 1h 36m |
| AFL2137 | AFL | Sheremetyevo International Airport (UUEE) | Sheremetyevo International Airport (UUEE) | 2026-03-29 17:36 UTC | 2026-03-29 17:36 UTC | 0m |
| CGFDE | CGF | Montréal / St-Hubert Airport (CYHU) | Montréal / St-Hubert Airport (CYHU) | 2026-03-29 16:50 UTC | 2026-03-29 17:32 UTC | 42m |
| CST797 | CST | Norwood Memorial Airport (KOWD) | Caledonia County Airport (KCDA) | 2026-03-29 16:51 UTC | 2026-03-29 17:32 UTC | 40m |
| N342FG |  | Rocky Mountain Metro Airport (KBJC) | Vance Brand Airport (KLMO) | 2026-03-29 17:08 UTC | 2026-03-29 17:31 UTC | 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
