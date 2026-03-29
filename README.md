# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--29_14:31:54_UTC-green)

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

**Latest saved flight:** 2026-03-29 14:31:54 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-29 14:31:54 UTC

- **2,045** saved flights
- **1,617** unique routes
- **88** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **2,045** saved routes in the archive
- **1h 22m** average flight duration

### Carbon Footprint Estimate

- **28,266.2 tonnes** estimated CO2 emissions
- **1,638,622 km** total distance flown
- **932 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 91 |
| 2 | Ryanair | 71 |
| 3 | IndiGo | 62 |
| 4 | Southwest Airlines | 40 |
| 5 | American Airlines | 35 |
| 6 | AXM | 35 |
| 7 | Lufthansa | 35 |
| 8 | EJA | 35 |
| 9 | ENY | 31 |
| 10 | Delta Air Lines | 22 |
| 11 | United Airlines | 22 |
| 12 | All Nippon Airways | 20 |
| 13 | Cathay Pacific | 20 |
| 14 | Vueling | 20 |
| 15 | LATAM Airlines | 19 |
| 16 | Japan Airlines | 18 |
| 17 | BRC | 17 |
| 18 | LXJ | 17 |
| 19 | Avianca | 14 |
| 20 | AXB | 14 |
| 21 | SFR | 14 |
| 22 | VIV | 14 |
| 23 | VOE | 14 |
| 24 | APG | 13 |
| 25 | Alaska Airlines | 13 |
| 26 | QLK | 13 |
| 27 | Swiss International | 13 |
| 28 | EDV | 12 |
| 29 | AEE | 11 |
| 30 | ARE | 11 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 1673 |
| 2 | 🇮🇳 IN | 173 |
| 3 | 🇪🇸 ES | 157 |
| 4 | 🇯🇵 JP | 132 |
| 5 | 🇦🇺 AU | 123 |
| 6 | 🇨🇴 CO | 121 |
| 7 | 🇩🇪 DE | 104 |
| 8 | 🇮🇹 IT | 78 |
| 9 | 🇬🇧 GB | 78 |
| 10 | 🇲🇾 MY | 73 |
| 11 | 🇧🇷 BR | 73 |
| 12 | 🇨🇦 CA | 72 |
| 13 | 🇲🇽 MX | 71 |
| 14 | 🇿🇦 ZA | 70 |
| 15 | 🇵🇭 PH | 61 |
| 16 | 🇬🇹 GT | 60 |
| 17 | 🇫🇷 FR | 50 |
| 18 | 🇬🇷 GR | 44 |
| 19 | 🇨🇭 CH | 42 |
| 20 | 🇹🇭 TH | 42 |
| 21 | 🇹🇷 TR | 38 |
| 22 | 🇮🇩 ID | 33 |
| 23 | 🇳🇴 NO | 33 |
| 24 | 🇲🇴 MO | 29 |
| 25 | 🇵🇱 PL | 29 |
| 26 | 🇰🇷 KR | 26 |
| 27 | 🇫🇮 FI | 26 |
| 28 | 🇲🇦 MA | 23 |
| 29 | 🇲🇪 ME | 23 |
| 30 | 🇳🇿 NZ | 22 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 45 |
| 2 | Tokyo International Airport |  | JP | 44 |
| 3 | El Dorado International Airport |  | CO | 43 |
| 4 | Frankfurt am Main International Airport |  | DE | 39 |
| 5 | La Aurora Airport |  | GT | 38 |
| 6 | Indira Gandhi International Airport |  | IN | 37 |
| 7 | Denver International Airport |  | US | 35 |
| 8 | Guaymaral Airport |  | CO | 32 |
| 9 | Macau International Airport |  | MO | 29 |
| 10 | Kuala Lumpur International Airport |  | MY | 29 |
| 11 | Tenerife Norte Airport |  | ES | 26 |
| 12 | O. R. Tambo International Airport |  | ZA | 26 |
| 13 | Ninoy Aquino International Airport |  | PH | 25 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 24 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 24 |
| 16 | Chicago O'Hare International Airport |  | US | 23 |
| 17 | Zurich Airport |  | CH | 23 |
| 18 | Netaji Subhash Chandra Bose International Airport |  | IN | 23 |
| 19 | Harry Reid International Airport |  | US | 22 |
| 20 | Vitoria/Foronda Airport |  | ES | 20 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 19 |
| 22 | Atizapan De Zaragoza Airport |  | MX | 19 |
| 23 | Eleftherios Venizelos International Airport |  | GR | 18 |
| 24 | Miami International Airport |  | US | 17 |
| 25 | Zhuhai Airport |  | CN | 17 |
| 26 | Madrid Barajas International Airport |  | ES | 17 |
| 27 | Charles de Gaulle International Airport |  | FR | 17 |
| 28 | Bengaluru International Airport |  | IN | 17 |
| 29 | Don Mueang International Airport |  | TH | 16 |
| 30 | Wasig Airport |  | PH | 16 |
| 31 | VGZR |  |  | 16 |
| 32 | Amsterdam Airport Schiphol |  | NL | 16 |
| 33 | Salt Lake City International Airport |  | US | 16 |
| 34 | Newcastle Airport |  | ZA | 16 |
| 35 | Soekarno-Hatta International Airport |  | ID | 15 |
| 36 | Los Angeles International Airport |  | US | 15 |
| 37 | Seattle-Tacoma International Airport |  | US | 15 |
| 38 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 15 |
| 39 | Helsinki Vantaa Airport |  | FI | 14 |
| 40 | Perales Airport |  | CO | 14 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 14 | 23m | 225 km | 54.3 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 14 | 14m | 114 km | 27.5 t |
| 3 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 13 | 20m | 250 km | 56.2 t |
| 4 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 13 | 26m | - | - |
| 5 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 10 | 30m | - | - |
| 6 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 10 | 24m | 99 km | 17.1 t |
| 7 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 9 | 22m | 252 km | 39.1 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 9 | 1h 7m | 706 km | 109.6 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 8 | 30m | 275 km | 37.9 t |
| 10 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 8 | 1h 40m | 1,423 km | 196.3 t |
| 11 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 8 | 26m | 152 km | 20.9 t |
| 12 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 7 | 28m | 304 km | 36.7 t |
| 13 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 6 | 14m | 206 km | 21.3 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 6 | 52m | 546 km | 56.5 t |
| 15 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 6 | 13m | 99 km | 10.3 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Sepulot Airport (WBKO) | 6 | 2h 4m | 1,652 km | 171.0 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 6 | 22m | 165 km | 17.1 t |
| 18 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 6 | 8h 51m | 38 km | 3.9 t |
| 19 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 6 | 1h 27m | 910 km | 94.2 t |
| 20 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 6 | 17m | 55 km | 5.7 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 5 | 29m | 369 km | 31.8 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 5 | 11m | 127 km | 10.9 t |
| 23 | O. R. Tambo International Airport (FAOR) | Durnacol Airport (FADH) | 5 | 22m | 275 km | 23.7 t |
| 24 | Melbourne International Airport (YMML) | Long Hill Airport (YLHL) | 5 | 36m | 431 km | 37.2 t |
| 25 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 5 | 27m | 69 km | 6.0 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 5 | 1h 55m | 1,304 km | 112.5 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pathankot Air Force Station (VIPK) | 4 | 42m | 431 km | 29.8 t |
| 28 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 4 | 1h 15m | 723 km | 49.9 t |
| 29 | Tokyo International Airport (RJTT) | Akeno Airport (RJOE) | 4 | 30m | 305 km | 21.0 t |
| 30 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 4 | 1h 10m | 770 km | 53.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N97SW |  | Harry Reid International Airport (KLAS) | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | 2026-03-29 10:59 UTC | 2026-03-29 14:31 UTC | 3h 32m |
| N402AM |  | Waukegan Ntl Airport (KUGN) | Dane County Regional/Truax Field (KMSN) | 2026-03-29 13:36 UTC | 2026-03-29 14:30 UTC | 54m |
| SFY3DB | SFY | Gloucestershire Airport (EGBJ) | Oxford (Kidlington) Airport (EGTK) | 2026-03-29 13:31 UTC | 2026-03-29 14:28 UTC | 56m |
| N8148M |  | Savannah/Hilton Head International Airport (KSAV) | Hilton Head Airport (KHXD) | 2026-03-29 14:10 UTC | 2026-03-29 14:27 UTC | 17m |
| N831MT |  | Boise Air Trml/Gowen Field (KBOI) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-03-29 12:52 UTC | 2026-03-29 14:18 UTC | 1h 25m |
| N367BW |  | K61B (K61B) | Grand Canyon West Airport (K1G4) | 2026-03-29 13:45 UTC | 2026-03-29 14:14 UTC | 28m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-03-29 13:58 UTC | 2026-03-29 14:10 UTC | 12m |
| N585CH |  | Central Il Regional/Bloomington-Normal Airport (KBMI) | Frasca Field (KC16) | 2026-03-29 13:45 UTC | 2026-03-29 14:08 UTC | 22m |
| N4953G |  | Casper/Natrona County International Airport (KCPR) | Casper/Natrona County International Airport (KCPR) | 2026-03-29 13:51 UTC | 2026-03-29 14:07 UTC | 15m |
| N4715K |  | Steamboat Springs/Bob Adams Field (KSBS) | Yampa Valley Airport (KHDN) | 2026-03-29 13:45 UTC | 2026-03-29 14:06 UTC | 20m |
| CPA393 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-03-29 06:23 UTC | 2026-03-29 13:59 UTC | 7h 35m |
| N682AC |  | Toy Airpark (15XS) | Bb Airpark (TE88) | 2026-03-29 13:47 UTC | 2026-03-29 13:57 UTC | 9m |
| N72HH |  | Oelde Bergeler Airport (EDLU) | Meinerzhagen Airport (EDKZ) | 2026-03-29 13:21 UTC | 2026-03-29 13:55 UTC | 33m |
| COS142B | COS | La Esperanza Airport (MNEP) | El Bluff Airport (MNFF) | 2026-03-29 13:45 UTC | 2026-03-29 13:54 UTC | 9m |
| N886AB |  | Denton Enterprise Airport (KDTO) | Bridgeport Municipal Airport (KXBP) | 2026-03-29 13:16 UTC | 2026-03-29 13:53 UTC | 36m |
| N35377 |  | Arnold Palmer Regional Airport (KLBE) | Rostraver Airport (KFWQ) | 2026-03-29 13:38 UTC | 2026-03-29 13:52 UTC | 14m |
| N3653R |  | North Las Vegas Airport (KVGT) | Caas Airport (NV98) | 2026-03-29 13:31 UTC | 2026-03-29 13:52 UTC | 21m |
| HK5100G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-03-29 13:14 UTC | 2026-03-29 13:50 UTC | 36m |
| AAL2897 | American Airlines | Dallas-Fort Worth International Airport (KDFW) | St Louis Lambert International Airport (KSTL) | 2026-03-29 12:35 UTC | 2026-03-29 13:50 UTC | 1h 14m |
| ICY99 | ICY | Elmendorf Afb Airport (PAED) | Elmendorf Afb Airport (PAED) | 2026-03-29 13:11 UTC | 2026-03-29 13:50 UTC | 38m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
