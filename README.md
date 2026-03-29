# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--29_18:55:27_UTC-green)

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

**Latest saved flight:** 2026-03-29 18:55:27 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-29 18:55:27 UTC

- **2,828** saved flights
- **2,157** unique routes
- **93** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **2,828** saved routes in the archive
- **1h 20m** average flight duration

### Carbon Footprint Estimate

- **37,847.7 tonnes** estimated CO2 emissions
- **2,194,069 km** total distance flown
- **906 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 134 |
| 2 | Ryanair | 97 |
| 3 | IndiGo | 79 |
| 4 | EJA | 59 |
| 5 | American Airlines | 55 |
| 6 | Southwest Airlines | 53 |
| 7 | Lufthansa | 50 |
| 8 | ENY | 45 |
| 9 | AXM | 38 |
| 10 | Delta Air Lines | 30 |
| 11 | Vueling | 30 |
| 12 | LXJ | 27 |
| 13 | LATAM Airlines | 27 |
| 14 | United Airlines | 25 |
| 15 | Avianca | 21 |
| 16 | Cathay Pacific | 21 |
| 17 | Swiss International | 21 |
| 18 | All Nippon Airways | 20 |
| 19 | VIV | 19 |
| 20 | AXB | 18 |
| 21 | Japan Airlines | 18 |
| 22 | WIF | 18 |
| 23 | ARE | 17 |
| 24 | BRC | 17 |
| 25 | EDV | 17 |
| 26 | VOE | 16 |
| 27 | AEE | 15 |
| 28 | Alaska Airlines | 15 |
| 29 | Finnair | 15 |
| 30 | SFR | 15 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 2414 |
| 2 | 🇪🇸 ES | 234 |
| 3 | 🇮🇳 IN | 217 |
| 4 | 🇨🇴 CO | 179 |
| 5 | 🇩🇪 DE | 150 |
| 6 | 🇯🇵 JP | 132 |
| 7 | 🇦🇺 AU | 125 |
| 8 | 🇧🇷 BR | 122 |
| 9 | 🇮🇹 IT | 116 |
| 10 | 🇨🇦 CA | 115 |
| 11 | 🇲🇽 MX | 102 |
| 12 | 🇬🇧 GB | 101 |
| 13 | 🇬🇹 GT | 86 |
| 14 | 🇫🇷 FR | 84 |
| 15 | 🇿🇦 ZA | 82 |
| 16 | 🇲🇾 MY | 81 |
| 17 | 🇨🇭 CH | 71 |
| 18 | 🇬🇷 GR | 63 |
| 19 | 🇵🇭 PH | 63 |
| 20 | 🇳🇴 NO | 59 |
| 21 | 🇹🇷 TR | 46 |
| 22 | 🇹🇭 TH | 45 |
| 23 | 🇵🇱 PL | 40 |
| 24 | 🇫🇮 FI | 38 |
| 25 | 🇧🇸 BS | 38 |
| 26 | 🇮🇩 ID | 37 |
| 27 | 🇲🇦 MA | 35 |
| 28 | 🇲🇴 MO | 32 |
| 29 | 🇳🇱 NL | 28 |
| 30 | 🇰🇷 KR | 26 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 69 |
| 2 | El Dorado International Airport |  | CO | 62 |
| 3 | La Aurora Airport |  | GT | 54 |
| 4 | Guaymaral Airport |  | CO | 51 |
| 5 | Frankfurt am Main International Airport |  | DE | 51 |
| 6 | Denver International Airport |  | US | 50 |
| 7 | Indira Gandhi International Airport |  | IN | 48 |
| 8 | Tokyo International Airport |  | JP | 44 |
| 9 | Tenerife Norte Airport |  | ES | 42 |
| 10 | Zurich Airport |  | CH | 35 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 34 |
| 12 | Chicago O'Hare International Airport |  | US | 33 |
| 13 | Harry Reid International Airport |  | US | 33 |
| 14 | Kuala Lumpur International Airport |  | MY | 33 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 32 |
| 16 | Macau International Airport |  | MO | 32 |
| 17 | O. R. Tambo International Airport |  | ZA | 29 |
| 18 | Eleftherios Venizelos International Airport |  | GR | 26 |
| 19 | Madrid Barajas International Airport |  | ES | 26 |
| 20 | Vitoria/Foronda Airport |  | ES | 26 |
| 21 | Ninoy Aquino International Airport |  | PH | 26 |
| 22 | Atizapan De Zaragoza Airport |  | MX | 26 |
| 23 | Netaji Subhash Chandra Bose International Airport |  | IN | 25 |
| 24 | Salt Lake City International Airport |  | US | 25 |
| 25 | Charlotte/Douglas International Airport |  | US | 24 |
| 26 | Miami International Airport |  | US | 24 |
| 27 | Charles de Gaulle International Airport |  | FR | 23 |
| 28 | Amsterdam Airport Schiphol |  | NL | 23 |
| 29 | Reno/Tahoe International Airport |  | US | 22 |
| 30 | Bengaluru International Airport |  | IN | 22 |
| 31 | CO86 |  |  | 21 |
| 32 | VGZR |  |  | 21 |
| 33 | Centennial Airport |  | US | 21 |
| 34 | George Bush Intcntl/Houston Airport |  | US | 20 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 19 |
| 36 | Helsinki Vantaa Airport |  | FI | 19 |
| 37 | Sydney Kingsford Smith International Airport |  | AU | 19 |
| 38 | Perales Airport |  | CO | 19 |
| 39 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 19 |
| 40 | John Paul II International Airport Kraków-Balice Airport |  | PL | 19 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 20 | 26m | - | - |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 19 | 14m | 114 km | 37.3 t |
| 3 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 15 | 26m | 99 km | 25.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 14 | 23m | 225 km | 54.3 t |
| 5 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 13 | 20m | 250 km | 56.2 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 12 | 30m | - | - |
| 7 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 12 | 24m | 152 km | 31.4 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 11 | 1h 39m | 1,423 km | 270.0 t |
| 9 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 10 | 12m | 99 km | 17.1 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 9 | 29m | 275 km | 42.6 t |
| 11 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 9 | 22m | 252 km | 39.1 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 9 | 1h 7m | 706 km | 109.6 t |
| 13 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 8 | 14m | 206 km | 28.4 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 8 | 22m | 165 km | 22.8 t |
| 15 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 8 | 52m | 136 km | 18.8 t |
| 16 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 8 | 32m | 69 km | 9.6 t |
| 17 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 7 | 28m | 304 km | 36.7 t |
| 18 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 7 | 1h 44m | 1,290 km | 155.8 t |
| 19 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 7 | 18m | 55 km | 6.7 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 6 | 52m | 546 km | 56.5 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Sepulot Airport (WBKO) | 6 | 2h 4m | 1,652 km | 171.0 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 6 | 11m | 127 km | 13.1 t |
| 23 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 6 | 8h 51m | 38 km | 3.9 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 6 | 1h 27m | 910 km | 94.2 t |
| 25 | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 6 | 12m | - | - |
| 26 | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 6 | 14m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 6 | 1h 55m | 1,304 km | 135.0 t |
| 28 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 6 | 4m | - | - |
| 29 | Dallas-Fort Worth International Airport (KDFW) | CO86 (CO86) | 5 | 1h 49m | - | - |
| 30 | Phoenix Sky Harbor International Airport (KPHX) | Reno/Tahoe International Airport (KRNO) | 5 | 1h 20m | 967 km | 83.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BRG661 | BRG | Point Hope Airport (PAPO) | Kivalina Airport (PAVL) | 2026-03-29 18:29 UTC | 2026-03-29 18:55 UTC | 26m |
| N5932U |  | Camp Bullis Als (Cals) Airport (9TX5) | Camp Bullis Als (Cals) Airport (9TX5) | 2026-03-29 18:32 UTC | 2026-03-29 18:51 UTC | 18m |
| VAR518 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Deer Valley Airport (KDVT) | 2026-03-29 18:16 UTC | 2026-03-29 18:48 UTC | 32m |
| N998TA |  | French Valley Airport (KF70) | San Gabriel Valley Airport (KEMT) | 2026-03-29 18:06 UTC | 2026-03-29 18:45 UTC | 38m |
| EZS73RK | EZS | Geneva Cointrin International Airport (LSGG) | Durham Tees Valley Airport (EGNV) | 2026-03-29 16:29 UTC | 2026-03-29 18:40 UTC | 2h 11m |
| N303SF |  | Jim & Julie's Airport (96WA) | Renton Municipal Airport (KRNT) | 2026-03-29 18:15 UTC | 2026-03-29 18:29 UTC | 14m |
| N6NR |  | Fort Lauderdale Executive Airport (KFXE) | St Paul Downtown Holman Field (KSTP) | 2026-03-29 14:46 UTC | 2026-03-29 18:25 UTC | 3h 38m |
| N824WB |  | Denton Enterprise Airport (KDTO) | Jim Sears Airport (3TA7) | 2026-03-29 18:11 UTC | 2026-03-29 18:24 UTC | 12m |
| N996PA |  | Mc Clellan-Palomar Airport (KCRQ) | Hemet-Ryan Airport (KHMT) | 2026-03-29 17:18 UTC | 2026-03-29 18:21 UTC | 1h 3m |
| N604ND |  | Republic Airport (KFRG) | Bridgeport/Sikorsky Airport (KBDR) | 2026-03-29 17:58 UTC | 2026-03-29 18:20 UTC | 22m |
| N252EA |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-03-29 17:26 UTC | 2026-03-29 18:19 UTC | 53m |
| N6341J |  | Peter Prince Field (K2R4) | Peter Prince Field (K2R4) | 2026-03-29 18:17 UTC | 2026-03-29 18:18 UTC | 0m |
| N96808 |  | John Wayne/Orange County Airport (KSNA) | Big Bear City Airport (KL35) | 2026-03-29 17:30 UTC | 2026-03-29 18:14 UTC | 44m |
| N9469H |  | Mckinney Ntl Airport (KTKI) | Flying Tiger Field (6TA2) | 2026-03-29 17:42 UTC | 2026-03-29 18:11 UTC | 28m |
| NOZ8GB | Norwegian Air | Oslo Gardermoen Airport (ENGM) | Berlin Brandenburg Airport (EDDB) | 2026-03-29 16:49 UTC | 2026-03-29 18:11 UTC | 1h 22m |
| CLX7956 | CLX | Luxembourg-Findel International Airport (ELLX) | Macau International Airport (VMMC) | 2026-03-29 04:00 UTC | 2026-03-29 18:10 UTC | 14h 9m |
| ACA1046 | Air Canada | Vancouver International Airport (CYVR) | Yucca Valley Airport (KL22) | 2026-03-29 15:45 UTC | 2026-03-29 18:09 UTC | 2h 24m |
| N65956 |  | Addison Airport (KADS) | Decatur Municipal Airport (KLUD) | 2026-03-29 17:37 UTC | 2026-03-29 18:08 UTC | 31m |
| RYR56RK | Ryanair | Napoli / Capodichino International Airport (LIRN) | Malpensa International Airport (LIMC) | 2026-03-29 16:52 UTC | 2026-03-29 18:08 UTC | 1h 15m |
| N216LT |  | De Kalb Taylor Municipal Airport (KDKB) | De Kalb Taylor Municipal Airport (KDKB) | 2026-03-29 18:07 UTC | 2026-03-29 18:07 UTC | 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
