# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--29_15:01:56_UTC-green)

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

**Latest saved flight:** 2026-03-29 15:01:56 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-29 15:01:56 UTC

- **2,117** saved flights
- **1,669** unique routes
- **89** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **2,117** saved routes in the archive
- **1h 22m** average flight duration

### Carbon Footprint Estimate

- **29,171.6 tonnes** estimated CO2 emissions
- **1,691,107 km** total distance flown
- **929 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 92 |
| 2 | Ryanair | 74 |
| 3 | IndiGo | 65 |
| 4 | Southwest Airlines | 41 |
| 5 | Lufthansa | 38 |
| 6 | AXM | 37 |
| 7 | American Airlines | 36 |
| 8 | EJA | 35 |
| 9 | ENY | 32 |
| 10 | Delta Air Lines | 23 |
| 11 | United Airlines | 22 |
| 12 | Cathay Pacific | 21 |
| 13 | Vueling | 21 |
| 14 | All Nippon Airways | 20 |
| 15 | LATAM Airlines | 20 |
| 16 | Japan Airlines | 18 |
| 17 | BRC | 17 |
| 18 | LXJ | 17 |
| 19 | Swiss International | 16 |
| 20 | Avianca | 15 |
| 21 | AXB | 15 |
| 22 | VIV | 15 |
| 23 | SFR | 14 |
| 24 | VOE | 14 |
| 25 | APG | 13 |
| 26 | Alaska Airlines | 13 |
| 27 | QLK | 13 |
| 28 | EDV | 12 |
| 29 | AEE | 11 |
| 30 | AIQ | 11 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 1710 |
| 2 | 🇮🇳 IN | 182 |
| 3 | 🇪🇸 ES | 167 |
| 4 | 🇯🇵 JP | 132 |
| 5 | 🇨🇴 CO | 128 |
| 6 | 🇦🇺 AU | 125 |
| 7 | 🇩🇪 DE | 110 |
| 8 | 🇮🇹 IT | 81 |
| 9 | 🇧🇷 BR | 81 |
| 10 | 🇬🇧 GB | 80 |
| 11 | 🇲🇾 MY | 77 |
| 12 | 🇨🇦 CA | 74 |
| 13 | 🇲🇽 MX | 73 |
| 14 | 🇿🇦 ZA | 72 |
| 15 | 🇵🇭 PH | 61 |
| 16 | 🇬🇹 GT | 60 |
| 17 | 🇫🇷 FR | 57 |
| 18 | 🇨🇭 CH | 48 |
| 19 | 🇬🇷 GR | 44 |
| 20 | 🇹🇭 TH | 44 |
| 21 | 🇹🇷 TR | 39 |
| 22 | 🇳🇴 NO | 36 |
| 23 | 🇮🇩 ID | 33 |
| 24 | 🇲🇴 MO | 29 |
| 25 | 🇵🇱 PL | 29 |
| 26 | 🇫🇮 FI | 28 |
| 27 | 🇰🇷 KR | 26 |
| 28 | 🇲🇦 MA | 26 |
| 29 | 🇲🇪 ME | 23 |
| 30 | 🇧🇸 BS | 23 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 46 |
| 2 | El Dorado International Airport |  | CO | 46 |
| 3 | Tokyo International Airport |  | JP | 44 |
| 4 | Frankfurt am Main International Airport |  | DE | 42 |
| 5 | Indira Gandhi International Airport |  | IN | 40 |
| 6 | La Aurora Airport |  | GT | 38 |
| 7 | Denver International Airport |  | US | 35 |
| 8 | Guaymaral Airport |  | CO | 34 |
| 9 | Kuala Lumpur International Airport |  | MY | 31 |
| 10 | Macau International Airport |  | MO | 29 |
| 11 | Tenerife Norte Airport |  | ES | 28 |
| 12 | O. R. Tambo International Airport |  | ZA | 27 |
| 13 | Zurich Airport |  | CH | 26 |
| 14 | Ninoy Aquino International Airport |  | PH | 25 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 24 |
| 16 | Chicago O'Hare International Airport |  | US | 24 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 24 |
| 18 | Harry Reid International Airport |  | US | 23 |
| 19 | Netaji Subhash Chandra Bose International Airport |  | IN | 23 |
| 20 | Vitoria/Foronda Airport |  | ES | 20 |
| 21 | Charles de Gaulle International Airport |  | FR | 19 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 19 |
| 23 | VGZR |  |  | 19 |
| 24 | Atizapan De Zaragoza Airport |  | MX | 19 |
| 25 | Eleftherios Venizelos International Airport |  | GR | 18 |
| 26 | Madrid Barajas International Airport |  | ES | 18 |
| 27 | Bengaluru International Airport |  | IN | 18 |
| 28 | Amsterdam Airport Schiphol |  | NL | 18 |
| 29 | Miami International Airport |  | US | 17 |
| 30 | Zhuhai Airport |  | CN | 17 |
| 31 | Don Mueang International Airport |  | TH | 17 |
| 32 | Wasig Airport |  | PH | 16 |
| 33 | Salt Lake City International Airport |  | US | 16 |
| 34 | Newcastle Airport |  | ZA | 16 |
| 35 | Soekarno-Hatta International Airport |  | ID | 15 |
| 36 | Los Angeles International Airport |  | US | 15 |
| 37 | Helsinki Vantaa Airport |  | FI | 15 |
| 38 | Seattle-Tacoma International Airport |  | US | 15 |
| 39 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 15 |
| 40 | Perales Airport |  | CO | 14 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 14 | 23m | 225 km | 54.3 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 14 | 14m | 114 km | 27.5 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 14 | 26m | - | - |
| 4 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 13 | 20m | 250 km | 56.2 t |
| 5 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 12 | 30m | - | - |
| 6 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 10 | 24m | 99 km | 17.1 t |
| 7 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 9 | 1h 39m | 1,423 km | 220.9 t |
| 8 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 9 | 22m | 252 km | 39.1 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 9 | 1h 7m | 706 km | 109.6 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 8 | 30m | 275 km | 37.9 t |
| 11 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 8 | 12m | 99 km | 13.7 t |
| 12 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 8 | 26m | 152 km | 20.9 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 7 | 28m | 304 km | 36.7 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 7 | 21m | 165 km | 19.9 t |
| 15 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 6 | 14m | 206 km | 21.3 t |
| 16 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 6 | 52m | 546 km | 56.5 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Sepulot Airport (WBKO) | 6 | 2h 4m | 1,652 km | 171.0 t |
| 18 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 6 | 8h 51m | 38 km | 3.9 t |
| 19 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 6 | 1h 27m | 910 km | 94.2 t |
| 20 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 6 | 17m | 55 km | 5.7 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 5 | 29m | 369 km | 31.8 t |
| 22 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 5 | 1h 44m | 1,290 km | 111.3 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 5 | 11m | 127 km | 10.9 t |
| 24 | O. R. Tambo International Airport (FAOR) | Durnacol Airport (FADH) | 5 | 22m | 275 km | 23.7 t |
| 25 | Melbourne International Airport (YMML) | Long Hill Airport (YLHL) | 5 | 36m | 431 km | 37.2 t |
| 26 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 5 | 27m | 69 km | 6.0 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 5 | 1h 55m | 1,304 km | 112.5 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pathankot Air Force Station (VIPK) | 4 | 42m | 431 km | 29.8 t |
| 29 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 4 | 2h 9m | 1,156 km | 79.8 t |
| 30 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 4 | 1h 15m | 723 km | 49.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N13715 |  | Dupage Airport (KDPA) | Ruder Airport (59IL) | 2026-03-29 14:45 UTC | 2026-03-29 15:01 UTC | 16m |
| N172RR |  | Westfield-Barnes Regional Airport (KBAF) | Tweed/New Haven Airport (KHVN) | 2026-03-29 14:20 UTC | 2026-03-29 14:56 UTC | 36m |
|  |  | Knoxville Downtown Island Airport (KDKX) | Landing At River's Edge Airport (98TN) | 2026-03-29 14:41 UTC | 2026-03-29 14:55 UTC | 13m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-03-29 14:31 UTC | 2026-03-29 14:52 UTC | 21m |
| CPA479 | Cathay Pacific | Taiwan Taoyuan International Airport (RCTP) | Chek Lap Kok International Airport (VHHH) | 2026-03-29 13:20 UTC | 2026-03-29 14:50 UTC | 1h 30m |
| N157CT |  | Skylark Field (KILE) | Varisco Airport (13TE) | 2026-03-29 14:11 UTC | 2026-03-29 14:48 UTC | 37m |
| N97SW |  | Harry Reid International Airport (KLAS) | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | 2026-03-29 10:59 UTC | 2026-03-29 14:31 UTC | 3h 32m |
| N402AM |  | Waukegan Ntl Airport (KUGN) | Dane County Regional/Truax Field (KMSN) | 2026-03-29 13:36 UTC | 2026-03-29 14:30 UTC | 54m |
| N3356V |  | Cleveland Regional Jetport Airport (KRZR) | Cleveland Regional Jetport Airport (KRZR) | 2026-03-29 14:27 UTC | 2026-03-29 14:29 UTC | 2m |
| SFY3DB | SFY | Gloucestershire Airport (EGBJ) | Oxford (Kidlington) Airport (EGTK) | 2026-03-29 13:31 UTC | 2026-03-29 14:28 UTC | 56m |
| N8148M |  | Savannah/Hilton Head International Airport (KSAV) | Hilton Head Airport (KHXD) | 2026-03-29 14:10 UTC | 2026-03-29 14:27 UTC | 17m |
| N212CP |  | Grant County Airport (KW99) | Grant County Airport (KW99) | 2026-03-29 13:48 UTC | 2026-03-29 14:23 UTC | 35m |
| QHD813 | QHD | Dekalb-Peachtree Airport (KPDK) | Austin-Bergstrom International Airport (KAUS) | 2026-03-29 11:51 UTC | 2026-03-29 14:18 UTC | 2h 26m |
| N831MT |  | Boise Air Trml/Gowen Field (KBOI) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-03-29 12:52 UTC | 2026-03-29 14:18 UTC | 1h 25m |
| AXM6046 | AXM | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 2026-03-29 13:56 UTC | 2026-03-29 14:17 UTC | 20m |
| RYR4618 | Ryanair | Stockholm-Arlanda Airport (ESSA) | Slavonski Jelas Airport (LDOR) | 2026-03-29 12:09 UTC | 2026-03-29 14:16 UTC | 2h 7m |
| N367BW |  | K61B (K61B) | Grand Canyon West Airport (K1G4) | 2026-03-29 13:45 UTC | 2026-03-29 14:14 UTC | 28m |
| DLH3LC | Lufthansa | Frankfurt am Main International Airport (EDDF) | Hannover Airport (EDDV) | 2026-03-29 13:35 UTC | 2026-03-29 14:12 UTC | 36m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-03-29 13:58 UTC | 2026-03-29 14:10 UTC | 12m |
| FIN1TJ | Finnair | Helsinki Vantaa Airport (EFHK) | Vaasa Airport (EFVA) | 2026-03-29 13:25 UTC | 2026-03-29 14:10 UTC | 44m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
