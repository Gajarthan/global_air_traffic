# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--29_10:39:58_UTC-green)

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

**Latest saved flight:** 2026-03-29 10:39:58 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-29 10:39:58 UTC

- **1,676** saved flights
- **1,361** unique routes
- **84** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **1,676** saved routes in the archive
- **1h 22m** average flight duration

### Carbon Footprint Estimate

- **23,372.3 tonnes** estimated CO2 emissions
- **1,354,916 km** total distance flown
- **948 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 91 |
| 2 | Ryanair | 50 |
| 3 | IndiGo | 46 |
| 4 | Southwest Airlines | 40 |
| 5 | American Airlines | 33 |
| 6 | EJA | 33 |
| 7 | ENY | 30 |
| 8 | AXM | 22 |
| 9 | United Airlines | 22 |
| 10 | Delta Air Lines | 20 |
| 11 | Lufthansa | 20 |
| 12 | BRC | 17 |
| 13 | Cathay Pacific | 17 |
| 14 | Japan Airlines | 17 |
| 15 | LXJ | 17 |
| 16 | All Nippon Airways | 15 |
| 17 | LATAM Airlines | 15 |
| 18 | Vueling | 15 |
| 19 | Alaska Airlines | 13 |
| 20 | QLK | 13 |
| 21 | Avianca | 12 |
| 22 | SFR | 12 |
| 23 | APG | 11 |
| 24 | EDV | 11 |
| 25 | VIV | 11 |
| 26 | JST | 10 |
| 27 | VOE | 10 |
| 28 | Air France | 8 |
| 29 | AXB | 8 |
| 30 | AZU | 8 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 1555 |
| 2 | 🇮🇳 IN | 125 |
| 3 | 🇦🇺 AU | 117 |
| 4 | 🇯🇵 JP | 110 |
| 5 | 🇪🇸 ES | 103 |
| 6 | 🇨🇴 CO | 89 |
| 7 | 🇨🇦 CA | 69 |
| 8 | 🇲🇽 MX | 65 |
| 9 | 🇩🇪 DE | 63 |
| 10 | 🇮🇹 IT | 58 |
| 11 | 🇬🇹 GT | 55 |
| 12 | 🇵🇭 PH | 53 |
| 13 | 🇧🇷 BR | 53 |
| 14 | 🇬🇧 GB | 49 |
| 15 | 🇲🇾 MY | 47 |
| 16 | 🇿🇦 ZA | 44 |
| 17 | 🇬🇷 GR | 34 |
| 18 | 🇫🇷 FR | 34 |
| 19 | 🇹🇭 TH | 28 |
| 20 | 🇰🇷 KR | 26 |
| 21 | 🇨🇭 CH | 26 |
| 22 | 🇮🇩 ID | 24 |
| 23 | 🇲🇴 MO | 24 |
| 24 | 🇳🇿 NZ | 22 |
| 25 | 🇹🇷 TR | 22 |
| 26 | 🇫🇮 FI | 18 |
| 27 | 🇲🇦 MA | 17 |
| 28 | 🇵🇱 PL | 17 |
| 29 | 🇨🇳 CN | 16 |
| 30 | 🇧🇸 BS | 16 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 42 |
| 2 | Denver International Airport |  | US | 35 |
| 3 | Tokyo International Airport |  | JP | 34 |
| 4 | La Aurora Airport |  | GT | 34 |
| 5 | El Dorado International Airport |  | CO | 32 |
| 6 | Indira Gandhi International Airport |  | IN | 28 |
| 7 | Frankfurt am Main International Airport |  | DE | 26 |
| 8 | Macau International Airport |  | MO | 24 |
| 9 | Guaymaral Airport |  | CO | 24 |
| 10 | Phoenix Sky Harbor International Airport |  | US | 23 |
| 11 | Chicago O'Hare International Airport |  | US | 22 |
| 12 | Ninoy Aquino International Airport |  | PH | 22 |
| 13 | Harry Reid International Airport |  | US | 21 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 20 |
| 15 | Tenerife Norte Airport |  | ES | 19 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 19 |
| 17 | Kuala Lumpur International Airport |  | MY | 19 |
| 18 | Atizapan De Zaragoza Airport |  | MX | 18 |
| 19 | Netaji Subhash Chandra Bose International Airport |  | IN | 18 |
| 20 | Miami International Airport |  | US | 17 |
| 21 | Wasig Airport |  | PH | 16 |
| 22 | Salt Lake City International Airport |  | US | 16 |
| 23 | Los Angeles International Airport |  | US | 15 |
| 24 | Zhuhai Airport |  | CN | 15 |
| 25 | Zurich Airport |  | CH | 15 |
| 26 | Seattle-Tacoma International Airport |  | US | 15 |
| 27 | Amsterdam Airport Schiphol |  | NL | 15 |
| 28 | O. R. Tambo International Airport |  | ZA | 15 |
| 29 | Eleftherios Venizelos International Airport |  | GR | 14 |
| 30 | Vitoria/Foronda Airport |  | ES | 14 |
| 31 | Bengaluru International Airport |  | IN | 14 |
| 32 | Tampa International Airport |  | US | 14 |
| 33 | CO86 |  |  | 13 |
| 34 | The Florida Keys Marathon International Airport |  | US | 13 |
| 35 | Reno/Tahoe International Airport |  | US | 13 |
| 36 | Vancouver International Airport |  | CA | 13 |
| 37 | Charles de Gaulle International Airport |  | FR | 13 |
| 38 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 13 |
| 39 | Soekarno-Hatta International Airport |  | ID | 12 |
| 40 | Daniel K Inouye International Airport |  | US | 12 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 14 | 23m | 225 km | 54.3 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 10 | 26m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 9 | 14m | 114 km | 17.7 t |
| 4 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 9 | 25m | 99 km | 15.4 t |
| 5 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 9 | 20m | 250 km | 38.9 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 8 | 30m | - | - |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 7 | 28m | 304 km | 36.7 t |
| 8 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 7 | 25m | 152 km | 18.3 t |
| 9 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 6 | 14m | 206 km | 21.3 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 6 | 29m | 275 km | 28.4 t |
| 11 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 6 | 22m | 252 km | 26.1 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 6 | 1h 6m | 706 km | 73.1 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 6 | 17m | 55 km | 5.7 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 5 | 1h 40m | 1,423 km | 122.7 t |
| 15 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 5 | 52m | 546 km | 47.1 t |
| 16 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 5 | 1h 27m | 910 km | 78.5 t |
| 17 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 5 | 27m | 69 km | 6.0 t |
| 18 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 5 | 1h 55m | 1,304 km | 112.5 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 4 | 30m | 369 km | 25.5 t |
| 20 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 4 | 12m | 99 km | 6.9 t |
| 21 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 4 | 1h 43m | 1,290 km | 89.0 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Sepulot Airport (WBKO) | 4 | 2h 2m | 1,652 km | 114.0 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 4 | 11m | 127 km | 8.8 t |
| 24 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 4 | 9m | - | - |
| 25 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 4 | 9h 26m | 38 km | 2.6 t |
| 26 | Miami International Airport (KMIA) | The Florida Keys Marathon International Airport (KMTH) | 4 | 18m | 141 km | 9.8 t |
| 27 | O. R. Tambo International Airport (FAOR) | Durnacol Airport (FADH) | 4 | 22m | 275 km | 19.0 t |
| 28 | Melbourne International Airport (YMML) | Long Hill Airport (YLHL) | 4 | 37m | 431 km | 29.7 t |
| 29 | Denton Enterprise Airport (KDTO) | Denton Enterprise Airport (KDTO) | 4 | 13m | - | - |
| 30 | La Aurora Airport (MGGT) | Esquipulas Airport (MGES) | 4 | 32m | 127 km | 8.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DLH99H | Lufthansa | Munich International Airport (EDDM) | Fayence Airport (LFMF) | 2026-03-29 09:38 UTC | 2026-03-29 10:39 UTC | 1h 1m |
| CPA254 | Cathay Pacific | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-03-28 22:29 UTC | 2026-03-29 10:36 UTC | 12h 6m |
| FNG8 | FNG | Genbole Airport (EFGE) | Kymi Airport (EFKY) | 2026-03-29 09:52 UTC | 2026-03-29 10:26 UTC | 34m |
| CMA576 | CMA | Charles de Gaulle International Airport (LFPG) | Zhuhai Airport (ZGSD) | 2026-03-28 22:02 UTC | 2026-03-29 10:21 UTC | 12h 19m |
| CPA831 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-03-28 19:32 UTC | 2026-03-29 10:13 UTC | 14h 40m |
| FIN9VM | Finnair | Helsinki Vantaa Airport (EFHK) | Vaasa Airport (EFVA) | 2026-03-29 09:24 UTC | 2026-03-29 10:08 UTC | 43m |
| CSB507 | CSB | Cincinnati/Northern Kentucky International Airport (KCVG) | Austin-Bergstrom International Airport (KAUS) | 2026-03-29 07:57 UTC | 2026-03-29 10:04 UTC | 2h 7m |
| GTI8229 | GTI | Amsterdam Airport Schiphol (EHAM) | Macau International Airport (VMMC) | 2026-03-28 20:03 UTC | 2026-03-29 10:03 UTC | 13h 59m |
| OKHHH | OKH | Letnany Airport (LKLT) | Benesov Airport (LKBE) | 2026-03-29 09:47 UTC | 2026-03-29 09:59 UTC | 11m |
| GTI8507 | GTI | Luxembourg-Findel International Airport (ELLX) | Zhuhai Airport (ZGSD) | 2026-03-28 22:32 UTC | 2026-03-29 09:58 UTC | 11h 26m |
| FGSAT | FGS | Verona / Boscomantico Airport (LIPN) | Verona / Boscomantico Airport (LIPN) | 2026-03-29 09:44 UTC | 2026-03-29 09:57 UTC | 13m |
| ICE16Y | ICE | Reykjavik Airport (BIRK) | Kaldarmelar Airport (BIKA) | 2026-03-29 09:39 UTC | 2026-03-29 09:54 UTC | 15m |
| FHMLR | FHM | Rennes-Saint-Jacques Airport (LFRN) | Rennes-Saint-Jacques Airport (LFRN) | 2026-03-29 09:40 UTC | 2026-03-29 09:53 UTC | 13m |
| HKC393 | HKC | Budapest Ferenc Liszt International Airport (LHBP) | Zhuhai Airport (ZGSD) | 2026-03-28 23:05 UTC | 2026-03-29 09:50 UTC | 10h 44m |
| VOE9KR | VOE | Toulouse-Blagnac Airport (LFBO) | Rennes-Saint-Jacques Airport (LFRN) | 2026-03-29 08:47 UTC | 2026-03-29 09:48 UTC | 1h 1m |
| DLH3MU | Lufthansa | Frankfurt am Main International Airport (EDDF) | Visoko Sport Airfield (LQVI) | 2026-03-29 08:35 UTC | 2026-03-29 09:47 UTC | 1h 12m |
| DHK814 | DHK | Leipzig Halle Airport (EDDP) | Macau International Airport (VMMC) | 2026-03-28 22:47 UTC | 2026-03-29 09:47 UTC | 10h 59m |
| AXM136 | AXM | Kuala Lumpur International Airport (WMKK) | Chek Lap Kok International Airport (VHHH) | 2026-03-29 06:16 UTC | 2026-03-29 09:46 UTC | 3h 30m |
| DAH1227 | DAH | Lyon Saint-Exupery Airport (LFLL) | Mostaganem Airport (DA14) | 2026-03-29 08:18 UTC | 2026-03-29 09:45 UTC | 1h 27m |
| SFJ85 | SFJ | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-03-29 08:31 UTC | 2026-03-29 09:43 UTC | 1h 11m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
