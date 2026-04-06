# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--06_21:49:39_UTC-green)

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

**Latest saved flight:** 2026-04-06 21:49:39 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-06 21:49:39 UTC

- **20,885** saved flights
- **10,418** unique routes
- **116** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **20,885** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **261,884.3 tonnes** estimated CO2 emissions
- **15,181,698 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 912 |
| 2 | Ryanair | 870 |
| 3 | IndiGo | 582 |
| 4 | American Airlines | 403 |
| 5 | EJA | 391 |
| 6 | Southwest Airlines | 299 |
| 7 | ENY | 285 |
| 8 | Lufthansa | 264 |
| 9 | Vueling | 225 |
| 10 | LATAM Airlines | 217 |
| 11 | AXM | 198 |
| 12 | Delta Air Lines | 183 |
| 13 | LXJ | 182 |
| 14 | All Nippon Airways | 176 |
| 15 | QLK | 165 |
| 16 | AZU | 163 |
| 17 | Swiss International | 154 |
| 18 | VIV | 153 |
| 19 | easyJet | 143 |
| 20 | United Airlines | 142 |
| 21 | Alaska Airlines | 140 |
| 22 | Avianca | 135 |
| 23 | EJU | 135 |
| 24 | Japan Airlines | 134 |
| 25 | AEE | 128 |
| 26 | WIF | 126 |
| 27 | EDV | 123 |
| 28 | AXB | 119 |
| 29 | Air France | 111 |
| 30 | BRC | 111 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 16531 |
| 2 | 🇮🇳 IN | 1775 |
| 3 | 🇪🇸 ES | 1663 |
| 4 | 🇦🇺 AU | 1420 |
| 5 | 🇧🇷 BR | 1195 |
| 6 | 🇨🇴 CO | 1150 |
| 7 | 🇯🇵 JP | 1090 |
| 8 | 🇮🇹 IT | 1033 |
| 9 | 🇩🇪 DE | 1029 |
| 10 | 🇨🇦 CA | 927 |
| 11 | 🇬🇧 GB | 825 |
| 12 | 🇫🇷 FR | 758 |
| 13 | 🇲🇽 MX | 713 |
| 14 | 🇬🇷 GR | 582 |
| 15 | 🇨🇭 CH | 566 |
| 16 | 🇲🇾 MY | 464 |
| 17 | 🇬🇹 GT | 462 |
| 18 | 🇿🇦 ZA | 461 |
| 19 | 🇳🇴 NO | 433 |
| 20 | 🇳🇿 NZ | 422 |
| 21 | 🇹🇷 TR | 411 |
| 22 | 🇵🇭 PH | 380 |
| 23 | 🇰🇷 KR | 351 |
| 24 | 🇹🇭 TH | 307 |
| 25 | 🇵🇱 PL | 305 |
| 26 | 🇲🇦 MA | 257 |
| 27 | 🇧🇸 BS | 234 |
| 28 | 🇲🇪 ME | 218 |
| 29 | 🇮🇩 ID | 214 |
| 30 | 🇳🇱 NL | 208 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 520 |
| 2 | El Dorado International Airport |  | CO | 431 |
| 3 | Denver International Airport |  | US | 385 |
| 4 | Tokyo International Airport |  | JP | 377 |
| 5 | Indira Gandhi International Airport |  | IN | 364 |
| 6 | La Aurora Airport |  | GT | 317 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 276 |
| 8 | Harry Reid International Airport |  | US | 274 |
| 9 | Zurich Airport |  | CH | 256 |
| 10 | Frankfurt am Main International Airport |  | DE | 236 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 227 |
| 12 | Chicago O'Hare International Airport |  | US | 227 |
| 13 | Guaymaral Airport |  | CO | 227 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 225 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 204 |
| 16 | Macau International Airport |  | MO | 200 |
| 17 | Charlotte/Douglas International Airport |  | US | 200 |
| 18 | Bengaluru International Airport |  | IN | 200 |
| 19 | Madrid Barajas International Airport |  | ES | 195 |
| 20 | Tenerife Norte Airport |  | ES | 191 |
| 21 | Atizapan De Zaragoza Airport |  | MX | 185 |
| 22 | Congonhas Airport |  | BR | 177 |
| 23 | Ninoy Aquino International Airport |  | PH | 172 |
| 24 | Salt Lake City International Airport |  | US | 166 |
| 25 | Reno/Tahoe International Airport |  | US | 164 |
| 26 | Daniel K Inouye International Airport |  | US | 162 |
| 27 | Malpensa International Airport |  | IT | 161 |
| 28 | Kuala Lumpur International Airport |  | MY | 161 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 154 |
| 30 | Charles de Gaulle International Airport |  | FR | 153 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 153 |
| 32 | Miami International Airport |  | US | 148 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 146 |
| 34 | Vitoria/Foronda Airport |  | ES | 145 |
| 35 | O. R. Tambo International Airport |  | ZA | 143 |
| 36 | General Edward Lawrence Logan International Airport |  | US | 142 |
| 37 | Barcelona International Airport |  | ES | 139 |
| 38 | Pune Airport |  | IN | 139 |
| 39 | George Bush Intcntl/Houston Airport |  | US | 135 |
| 40 | Seattle-Tacoma International Airport |  | US | 133 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 95 | 1h 8m | 706 km | 1,156.6 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 92 | 14m | 114 km | 180.4 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 83 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 74 | 24m | 225 km | 287.1 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 69 | 28m | 304 km | 361.7 t |
| 6 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 68 | 22m | 99 km | 116.5 t |
| 7 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 65 | 27m | 152 km | 169.9 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 60 | 1h 27m | 910 km | 941.5 t |
| 9 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 59 | 1h 43m | 1,156 km | 1,177.0 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 58 | 31m | - | - |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 56 | 16m | 206 km | 199.1 t |
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
| 25 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 36 | 58m | 723 km | 448.8 t |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 36 | 46m | 452 km | 280.6 t |
| 27 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 33 | 12m | 15 km | 8.7 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 32 | 1h 22m | 961 km | 530.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N460CA |  | Palo Alto Airport (KPAO) | Tracy Municipal Airport (KTCY) | 2026-04-06 21:20 UTC | 2026-04-06 21:49 UTC | 28m |
| N468FA |  | Quakertown Airport (KUKT) | Lehigh Valley International Airport (KABE) | 2026-04-06 20:51 UTC | 2026-04-06 21:48 UTC | 57m |
| N615LF |  | Belle Plaine Municipal Airport (KTZT) | Iowa City Municipal Airport (KIOW) | 2026-04-06 21:16 UTC | 2026-04-06 21:35 UTC | 18m |
| CES570 | China Eastern | Charles de Gaulle International Airport (LFPG) | Sharypovo Airport (UNKO) | 2026-04-05 19:56 UTC | 2026-04-06 21:29 UTC | 25h 32m |
| N4032L |  | Perry-Houston County Airport (KPXE) | 1GE4 (1GE4) | 2026-04-06 21:10 UTC | 2026-04-06 21:27 UTC | 16m |
| N833CL |  | Hanover County Municipal Airport (KOFP) | 46SC (46SC) | 2026-04-06 20:41 UTC | 2026-04-06 21:25 UTC | 44m |
| N9968F |  | Dupage Airport (KDPA) | 0IL8 (0IL8) | 2026-04-06 21:10 UTC | 2026-04-06 21:25 UTC | 14m |
| N8390K |  | KU77 (KU77) | Nephi Municipal Airport (KU14) | 2026-04-06 21:10 UTC | 2026-04-06 21:24 UTC | 14m |
| N64087 |  | Hayward Executive Airport (KHWD) | Hayward Executive Airport (KHWD) | 2026-04-06 19:56 UTC | 2026-04-06 21:24 UTC | 1h 27m |
| N815SS |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-04-06 20:27 UTC | 2026-04-06 21:22 UTC | 55m |
| N5331F |  | Somerset Airport (KSMQ) | Sky Manor Airport (KN40) | 2026-04-06 21:05 UTC | 2026-04-06 21:20 UTC | 15m |
| N414FJ |  | Cincinnati Municipal/Lunken Field (KLUK) | Telluride Regional Airport (KTEX) | 2026-04-06 18:30 UTC | 2026-04-06 21:20 UTC | 2h 49m |
| COBRA31 | COB | Edwards Af Aux North Base Airport (K9L2) | Boron Airstrip (57CL) | 2026-04-06 20:53 UTC | 2026-04-06 21:17 UTC | 24m |
| NRR | NRR | Bathurst Airport (YBTH) | Sydney Bankstown Airport (YSBK) | 2026-04-06 20:52 UTC | 2026-04-06 21:16 UTC | 24m |
| N2182B |  | Abraham Lincoln Capital Airport (KSPI) | Decatur Airport (KDEC) | 2026-04-06 20:48 UTC | 2026-04-06 21:14 UTC | 25m |
| N20668 |  | Pierce County/Thun Field (KPLU) | Pierce County/Thun Field (KPLU) | 2026-04-06 21:10 UTC | 2026-04-06 21:14 UTC | 4m |
| SCU15 | SCU | Mckinney Ntl Airport (KTKI) | 19OK (19OK) | 2026-04-06 19:40 UTC | 2026-04-06 21:13 UTC | 1h 33m |
| LUZON41 | LUZ | Randolph Afb Airport (KRND) | Circle P Ranch Airport (82XS) | 2026-04-06 20:21 UTC | 2026-04-06 21:11 UTC | 49m |
| N459M |  | Palm Beach International Airport (KPBI) | Jackson County/Reynolds Field (KJXN) | 2026-04-06 18:43 UTC | 2026-04-06 21:10 UTC | 2h 27m |
| MHQ | MHQ | Sydney Bankstown Airport (YSBK) | Grenfell Airport (YGNF) | 2026-04-06 20:29 UTC | 2026-04-06 21:10 UTC | 41m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
