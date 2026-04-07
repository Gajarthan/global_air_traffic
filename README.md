# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--07_11:27:12_UTC-green)

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

**Latest saved flight:** 2026-04-07 11:27:12 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-07 11:27:12 UTC

- **21,716** saved flights
- **10,721** unique routes
- **118** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **21,716** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **271,354.9 tonnes** estimated CO2 emissions
- **15,730,720 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 933 |
| 2 | Ryanair | 908 |
| 3 | IndiGo | 617 |
| 4 | American Airlines | 411 |
| 5 | EJA | 404 |
| 6 | Southwest Airlines | 308 |
| 7 | ENY | 292 |
| 8 | Lufthansa | 271 |
| 9 | Vueling | 229 |
| 10 | LATAM Airlines | 226 |
| 11 | AXM | 213 |
| 12 | All Nippon Airways | 192 |
| 13 | Delta Air Lines | 190 |
| 14 | LXJ | 186 |
| 15 | QLK | 183 |
| 16 | AZU | 169 |
| 17 | Swiss International | 162 |
| 18 | VIV | 157 |
| 19 | easyJet | 148 |
| 20 | Alaska Airlines | 147 |
| 21 | Japan Airlines | 145 |
| 22 | United Airlines | 143 |
| 23 | EJU | 141 |
| 24 | Avianca | 139 |
| 25 | AEE | 136 |
| 26 | WIF | 134 |
| 27 | EDV | 127 |
| 28 | AXB | 123 |
| 29 | Air France | 119 |
| 30 | Wizz Air | 113 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 16985 |
| 2 | 🇮🇳 IN | 1872 |
| 3 | 🇪🇸 ES | 1712 |
| 4 | 🇦🇺 AU | 1549 |
| 5 | 🇧🇷 BR | 1233 |
| 6 | 🇯🇵 JP | 1198 |
| 7 | 🇨🇴 CO | 1175 |
| 8 | 🇮🇹 IT | 1097 |
| 9 | 🇩🇪 DE | 1074 |
| 10 | 🇨🇦 CA | 963 |
| 11 | 🇬🇧 GB | 861 |
| 12 | 🇫🇷 FR | 794 |
| 13 | 🇲🇽 MX | 727 |
| 14 | 🇬🇷 GR | 614 |
| 15 | 🇨🇭 CH | 591 |
| 16 | 🇲🇾 MY | 495 |
| 17 | 🇿🇦 ZA | 488 |
| 18 | 🇬🇹 GT | 464 |
| 19 | 🇳🇴 NO | 462 |
| 20 | 🇳🇿 NZ | 444 |
| 21 | 🇹🇷 TR | 424 |
| 22 | 🇵🇭 PH | 413 |
| 23 | 🇰🇷 KR | 384 |
| 24 | 🇹🇭 TH | 343 |
| 25 | 🇵🇱 PL | 317 |
| 26 | 🇲🇦 MA | 264 |
| 27 | 🇧🇸 BS | 235 |
| 28 | 🇮🇩 ID | 231 |
| 29 | 🇲🇪 ME | 230 |
| 30 | 🇳🇱 NL | 216 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 531 |
| 2 | El Dorado International Airport |  | CO | 442 |
| 3 | Tokyo International Airport |  | JP | 405 |
| 4 | Denver International Airport |  | US | 393 |
| 5 | Indira Gandhi International Airport |  | IN | 378 |
| 6 | La Aurora Airport |  | GT | 319 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 292 |
| 8 | Harry Reid International Airport |  | US | 284 |
| 9 | Zurich Airport |  | CH | 267 |
| 10 | Frankfurt am Main International Airport |  | DE | 242 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 232 |
| 12 | Chicago O'Hare International Airport |  | US | 232 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 231 |
| 14 | Guaymaral Airport |  | CO | 230 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 217 |
| 16 | Bengaluru International Airport |  | IN | 211 |
| 17 | Charlotte/Douglas International Airport |  | US | 208 |
| 18 | Macau International Airport |  | MO | 201 |
| 19 | Madrid Barajas International Airport |  | ES | 198 |
| 20 | Tenerife Norte Airport |  | ES | 198 |
| 21 | Atizapan De Zaragoza Airport |  | MX | 191 |
| 22 | Ninoy Aquino International Airport |  | PH | 189 |
| 23 | Congonhas Airport |  | BR | 181 |
| 24 | Kuala Lumpur International Airport |  | MY | 175 |
| 25 | Malpensa International Airport |  | IT | 170 |
| 26 | Salt Lake City International Airport |  | US | 170 |
| 27 | Daniel K Inouye International Airport |  | US | 169 |
| 28 | Reno/Tahoe International Airport |  | US | 168 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 168 |
| 30 | Charles de Gaulle International Airport |  | FR | 162 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 159 |
| 32 | Miami International Airport |  | US | 153 |
| 33 | O. R. Tambo International Airport |  | ZA | 151 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 150 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 147 |
| 36 | Vitoria/Foronda Airport |  | ES | 146 |
| 37 | Pune Airport |  | IN | 145 |
| 38 | Barcelona International Airport |  | ES | 143 |
| 39 | Seattle-Tacoma International Airport |  | US | 138 |
| 40 | George Bush Intcntl/Houston Airport |  | US | 137 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 103 | 1h 8m | 706 km | 1,254.0 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 95 | 14m | 114 km | 186.3 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 84 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 82 | 24m | 225 km | 318.1 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 76 | 28m | 304 km | 398.4 t |
| 6 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 68 | 22m | 99 km | 116.5 t |
| 7 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 65 | 27m | 152 km | 169.9 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 64 | 1h 28m | 910 km | 1,004.3 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 63 | 31m | - | - |
| 10 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 60 | 1h 43m | 1,156 km | 1,197.0 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 50 | 19m | 165 km | 142.2 t |
| 13 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 49 | 1h 13m | 770 km | 650.9 t |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 48 | 27m | 275 km | 227.5 t |
| 15 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 16 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 17 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 44 | 55m | 546 km | 414.3 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 44 | 31m | 369 km | 280.1 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 43 | 52m | 556 km | 412.2 t |
| 20 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 41 | 4m | - | - |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 41 | 20m | 250 km | 177.1 t |
| 22 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 41 | 9m | - | - |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 39 | 46m | 452 km | 303.9 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 39 | 13m | 99 km | 66.9 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 38 | 1h 43m | 1,423 km | 932.6 t |
| 26 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 37 | 58m | 723 km | 461.3 t |
| 27 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 34 | 12m | 15 km | 9.0 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 32 | 20m | 147 km | 81.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| GVNEB | GVN | Leeds Bradford Airport (EGNM) | Newcastle Airport (EGNT) | 2026-04-07 10:03 UTC | 2026-04-07 11:27 UTC | 1h 23m |
| THY6802 | Turkish Airlines | Ordu–Giresun Airport (LTCB) | Ordu–Giresun Airport (LTCB) | 2026-04-07 10:38 UTC | 2026-04-07 11:19 UTC | 41m |
| CXK419 | CXK | Concord-Padgett Regional Airport (KJQF) | Lincoln County Regional Airport (KIPJ) | 2026-04-07 10:58 UTC | 2026-04-07 11:19 UTC | 20m |
| BBG101 | BBG | Thessaloniki Macedonia International Airport (LGTS) | Thessaloniki Macedonia International Airport (LGTS) | 2026-04-07 11:04 UTC | 2026-04-07 11:15 UTC | 10m |
| ANA430 | All Nippon Airways | Fukuoka Airport (RJFF) | Yao Airport (RJOY) | 2026-04-07 10:34 UTC | 2026-04-07 11:13 UTC | 39m |
| CXK687 | CXK | Lawrence Municipal Airport (KLWM) | Lawrence Municipal Airport (KLWM) | 2026-04-07 11:03 UTC | 2026-04-07 11:06 UTC | 2m |
| GAF615 | GAF | Cologne Bonn Airport (EDDK) | Trondheim Airport Vaernes (ENVA) | 2026-04-07 07:22 UTC | 2026-04-07 11:04 UTC | 3h 41m |
| WZZ504 | Wizz Air | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-07 09:10 UTC | 2026-04-07 10:56 UTC | 1h 45m |
| JANET11 | JAN | Harry Reid International Airport (KLAS) | NV11 (NV11) | 2026-04-07 10:38 UTC | 2026-04-07 10:51 UTC | 12m |
| N278FG |  | Trenton Mercer Airport (KTTN) | Doylestown Airport (KDYL) | 2026-04-07 10:29 UTC | 2026-04-07 10:50 UTC | 21m |
| VTFTO | VTF | Hosur Airport (VO95) | Mysore Airport (VOMY) | 2026-04-07 10:09 UTC | 2026-04-07 10:47 UTC | 38m |
| NKZ | NKZ | RAAF Williams Point Cook Base (YMPC) | RAAF Williams Point Cook Base (YMPC) | 2026-04-07 10:09 UTC | 2026-04-07 10:47 UTC | 37m |
| HTY107 | HTY | Gibraltar Airport (LXGB) | Gibraltar Airport (LXGB) | 2026-04-07 10:37 UTC | 2026-04-07 10:46 UTC | 8m |
| EJU97KM | EJU | Paris-Orly Airport (LFPO) | Muenster Aero Airport (LSPU) | 2026-04-07 09:26 UTC | 2026-04-07 10:42 UTC | 1h 15m |
| N536HC |  | Newton Municipal-Earl Johnson Field (KTNU) | Dubuque Regional Airport (KDBQ) | 2026-04-07 10:09 UTC | 2026-04-07 10:41 UTC | 31m |
| AIQ4108 | AIQ | Suvarnabhumi Airport (VTBS) | Lamphun Airport (VTCO) | 2026-04-07 09:49 UTC | 2026-04-07 10:35 UTC | 45m |
| BBG101 | BBG | Eleftherios Venizelos International Airport (LGAV) | Thessaloniki Macedonia International Airport (LGTS) | 2026-04-07 09:30 UTC | 2026-04-07 10:33 UTC | 1h 3m |
| RAC9004 | RAC | LDZI (LDZI) | Visoko Sport Airfield (LQVI) | 2026-04-07 10:03 UTC | 2026-04-07 10:32 UTC | 29m |
| SFJ15 | SFJ | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-04-07 09:17 UTC | 2026-04-07 10:31 UTC | 1h 14m |
| HTY206 | HTY | Malaga Airport (LEMG) | Gibraltar Airport (LXGB) | 2026-04-07 10:01 UTC | 2026-04-07 10:27 UTC | 26m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
