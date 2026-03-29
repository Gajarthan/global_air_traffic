# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--29_19:23:16_UTC-green)

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

**Latest saved flight:** 2026-03-29 19:23:16 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-29 19:23:16 UTC

- **2,953** saved flights
- **2,248** unique routes
- **93** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **2,953** saved routes in the archive
- **1h 20m** average flight duration

### Carbon Footprint Estimate

- **39,149.0 tonnes** estimated CO2 emissions
- **2,269,506 km** total distance flown
- **900 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 145 |
| 2 | Ryanair | 102 |
| 3 | IndiGo | 79 |
| 4 | EJA | 64 |
| 5 | Southwest Airlines | 58 |
| 6 | American Airlines | 57 |
| 7 | Lufthansa | 52 |
| 8 | ENY | 47 |
| 9 | AXM | 38 |
| 10 | Delta Air Lines | 32 |
| 11 | Vueling | 30 |
| 12 | LXJ | 28 |
| 13 | LATAM Airlines | 28 |
| 14 | United Airlines | 25 |
| 15 | VIV | 23 |
| 16 | Avianca | 22 |
| 17 | Cathay Pacific | 21 |
| 18 | Swiss International | 21 |
| 19 | WIF | 21 |
| 20 | All Nippon Airways | 20 |
| 21 | ARE | 19 |
| 22 | AXB | 19 |
| 23 | EDV | 18 |
| 24 | Japan Airlines | 18 |
| 25 | BRC | 17 |
| 26 | VOE | 17 |
| 27 | AEE | 16 |
| 28 | SFR | 16 |
| 29 | Alaska Airlines | 15 |
| 30 | Finnair | 15 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 2568 |
| 2 | 🇪🇸 ES | 241 |
| 3 | 🇮🇳 IN | 219 |
| 4 | 🇨🇴 CO | 191 |
| 5 | 🇩🇪 DE | 155 |
| 6 | 🇯🇵 JP | 132 |
| 7 | 🇦🇺 AU | 125 |
| 8 | 🇧🇷 BR | 125 |
| 9 | 🇮🇹 IT | 122 |
| 10 | 🇨🇦 CA | 117 |
| 11 | 🇲🇽 MX | 111 |
| 12 | 🇬🇧 GB | 108 |
| 13 | 🇬🇹 GT | 88 |
| 14 | 🇫🇷 FR | 85 |
| 15 | 🇿🇦 ZA | 84 |
| 16 | 🇲🇾 MY | 81 |
| 17 | 🇨🇭 CH | 72 |
| 18 | 🇳🇴 NO | 65 |
| 19 | 🇬🇷 GR | 64 |
| 20 | 🇵🇭 PH | 63 |
| 21 | 🇹🇷 TR | 46 |
| 22 | 🇹🇭 TH | 45 |
| 23 | 🇵🇱 PL | 41 |
| 24 | 🇧🇸 BS | 39 |
| 25 | 🇫🇮 FI | 38 |
| 26 | 🇮🇩 ID | 37 |
| 27 | 🇲🇦 MA | 35 |
| 28 | 🇲🇴 MO | 32 |
| 29 | 🇳🇱 NL | 28 |
| 30 | 🇰🇷 KR | 26 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 72 |
| 2 | El Dorado International Airport |  | CO | 67 |
| 3 | La Aurora Airport |  | GT | 56 |
| 4 | Denver International Airport |  | US | 54 |
| 5 | Frankfurt am Main International Airport |  | DE | 54 |
| 6 | Guaymaral Airport |  | CO | 51 |
| 7 | Indira Gandhi International Airport |  | IN | 48 |
| 8 | Tokyo International Airport |  | JP | 44 |
| 9 | Tenerife Norte Airport |  | ES | 43 |
| 10 | Hartsfield/Jackson Atlanta International Airport |  | US | 37 |
| 11 | Chicago O'Hare International Airport |  | US | 36 |
| 12 | Harry Reid International Airport |  | US | 36 |
| 13 | Zurich Airport |  | CH | 36 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 35 |
| 15 | Kuala Lumpur International Airport |  | MY | 33 |
| 16 | Macau International Airport |  | MO | 32 |
| 17 | Atizapan De Zaragoza Airport |  | MX | 30 |
| 18 | O. R. Tambo International Airport |  | ZA | 30 |
| 19 | Madrid Barajas International Airport |  | ES | 27 |
| 20 | Vitoria/Foronda Airport |  | ES | 27 |
| 21 | Salt Lake City International Airport |  | US | 27 |
| 22 | Eleftherios Venizelos International Airport |  | GR | 26 |
| 23 | Charlotte/Douglas International Airport |  | US | 26 |
| 24 | Ninoy Aquino International Airport |  | PH | 26 |
| 25 | Reno/Tahoe International Airport |  | US | 25 |
| 26 | Netaji Subhash Chandra Bose International Airport |  | IN | 25 |
| 27 | Miami International Airport |  | US | 24 |
| 28 | Charles de Gaulle International Airport |  | FR | 23 |
| 29 | Bengaluru International Airport |  | IN | 23 |
| 30 | Amsterdam Airport Schiphol |  | NL | 23 |
| 31 | Perales Airport |  | CO | 22 |
| 32 | George Bush Intcntl/Houston Airport |  | US | 22 |
| 33 | Centennial Airport |  | US | 22 |
| 34 | CO86 |  |  | 21 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 21 |
| 36 | VGZR |  |  | 21 |
| 37 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 21 |
| 38 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 20 |
| 39 | Los Angeles International Airport |  | US | 19 |
| 40 | Yampa Valley Airport |  | US | 19 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 22 | 14m | 114 km | 43.1 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 20 | 26m | - | - |
| 3 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 15 | 26m | 99 km | 25.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 14 | 23m | 225 km | 54.3 t |
| 5 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 14 | 25m | 152 km | 36.6 t |
| 6 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 13 | 20m | 250 km | 56.2 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 12 | 30m | - | - |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 11 | 1h 39m | 1,423 km | 270.0 t |
| 9 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 10 | 12m | 99 km | 17.1 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 9 | 29m | 275 km | 42.6 t |
| 11 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 9 | 22m | 252 km | 39.1 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 9 | 1h 7m | 706 km | 109.6 t |
| 13 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 9 | 30m | 69 km | 10.8 t |
| 14 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 8 | 14m | 206 km | 28.4 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 8 | 22m | 165 km | 22.8 t |
| 16 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 8 | 52m | 136 km | 18.8 t |
| 17 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 8 | 1h 55m | 1,304 km | 180.0 t |
| 18 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 7 | 28m | 304 km | 36.7 t |
| 19 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 7 | 1h 44m | 1,290 km | 155.8 t |
| 20 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 7 | 18m | 55 km | 6.7 t |
| 21 | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 7 | 12m | - | - |
| 22 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 6 | 52m | 546 km | 56.5 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Sepulot Airport (WBKO) | 6 | 2h 4m | 1,652 km | 171.0 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 6 | 11m | 127 km | 13.1 t |
| 25 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 6 | 8h 51m | 38 km | 3.9 t |
| 26 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 6 | 1h 27m | 910 km | 94.2 t |
| 27 | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 6 | 14m | - | - |
| 28 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 6 | 4m | - | - |
| 29 | Dallas-Fort Worth International Airport (KDFW) | CO86 (CO86) | 5 | 1h 49m | - | - |
| 30 | Phoenix Sky Harbor International Airport (KPHX) | Reno/Tahoe International Airport (KRNO) | 5 | 1h 20m | 967 km | 83.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N102UC |  | Palo Alto Airport (KPAO) | Palo Alto Airport (KPAO) | 2026-03-29 18:16 UTC | 2026-03-29 19:23 UTC | 1h 6m |
| N306PP |  | Auburn Municipal Airport (KS50) | Auburn Municipal Airport (KS50) | 2026-03-29 19:07 UTC | 2026-03-29 19:21 UTC | 14m |
| N107PJ |  | Santa Barbara Municipal Airport (KSBA) | Gnoss Field (KDVO) | 2026-03-29 18:31 UTC | 2026-03-29 19:18 UTC | 47m |
| N172EL |  | Watsonville Municipal Airport (KWVI) | Palo Alto Airport (KPAO) | 2026-03-29 18:49 UTC | 2026-03-29 19:11 UTC | 22m |
| N60244 |  | North Las Vegas Airport (KVGT) | Creech Afb Airport (KINS) | 2026-03-29 18:16 UTC | 2026-03-29 19:08 UTC | 51m |
| JUMP3 | JUM | Eloy Municipal Airport (KE60) | Eloy Municipal Airport (KE60) | 2026-03-29 18:59 UTC | 2026-03-29 19:07 UTC | 8m |
| AFL2131 | AFL | Sheremetyevo International Airport (UUEE) | Sheremetyevo International Airport (UUEE) | 2026-03-29 19:07 UTC | 2026-03-29 19:07 UTC | 0m |
| OKC26 | OKC | Tampa International Airport (KTPA) | St Paul Downtown Holman Field (KSTP) | 2026-03-29 15:56 UTC | 2026-03-29 19:04 UTC | 3h 8m |
| OTIS32 | OTI | Easley Acres Airport (33NC) | Ingalls Field (KHSP) | 2026-03-29 16:34 UTC | 2026-03-29 19:01 UTC | 2h 27m |
| N400AY |  | Sacramento Mather Airport (KMHR) | Truckee-Tahoe Airport (KTRK) | 2026-03-29 18:41 UTC | 2026-03-29 19:00 UTC | 19m |
| N446BL |  | Johnston Regional Airport (KJNX) | Johnston Regional Airport (KJNX) | 2026-03-29 18:37 UTC | 2026-03-29 18:59 UTC | 22m |
| N534ME |  | Youngstown Elser Metro Airport (K4G4) | OH27 (OH27) | 2026-03-29 18:53 UTC | 2026-03-29 18:56 UTC | 3m |
| N74KM |  | Austin Executive Airport (KEDC) | Santiago Cattle Company Airport (XS78) | 2026-03-29 18:32 UTC | 2026-03-29 18:56 UTC | 24m |
| BRG661 | BRG | Point Hope Airport (PAPO) | Kivalina Airport (PAVL) | 2026-03-29 18:29 UTC | 2026-03-29 18:55 UTC | 26m |
| LYM3802 | LYM | Dallas-Fort Worth International Airport (KDFW) | Greenville Mid-Delta Airport (KGLH) | 2026-03-29 18:02 UTC | 2026-03-29 18:53 UTC | 50m |
| N801JA |  | Mesquite Airport (K67L) | Mesquite Airport (K67L) | 2026-03-29 18:41 UTC | 2026-03-29 18:53 UTC | 11m |
| N5932U |  | Camp Bullis Als (Cals) Airport (9TX5) | Camp Bullis Als (Cals) Airport (9TX5) | 2026-03-29 18:32 UTC | 2026-03-29 18:51 UTC | 18m |
| WIF3F | WIF | Bergen Airport Flesland (ENBR) | Haugesund Airport (ENHD) | 2026-03-29 18:34 UTC | 2026-03-29 18:50 UTC | 15m |
| VAR518 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Deer Valley Airport (KDVT) | 2026-03-29 18:16 UTC | 2026-03-29 18:48 UTC | 32m |
| VOE81UT | VOE | Madrid Barajas International Airport (LEMD) | La Morgal Airport (LEMR) | 2026-03-29 18:08 UTC | 2026-03-29 18:46 UTC | 38m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
