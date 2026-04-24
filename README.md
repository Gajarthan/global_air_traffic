# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--24_21:03:22_UTC-green)

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

**Latest saved flight:** 2026-04-24 21:03:22 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-24 21:03:22 UTC

- **52,600** saved flights
- **21,014** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **52,600** saved routes in the archive
- **1h 13m** average flight duration

### Carbon Footprint Estimate

- **627,926.1 tonnes** estimated CO2 emissions
- **36,401,512 km** total distance flown
- **833 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2213 |
| 2 | SkyWest Airlines | 1986 |
| 3 | IndiGo | 1196 |
| 4 | EJA | 929 |
| 5 | American Airlines | 849 |
| 6 | Southwest Airlines | 748 |
| 7 | ENY | 667 |
| 8 | Lufthansa | 614 |
| 9 | Vueling | 528 |
| 10 | AXM | 507 |
| 11 | LATAM Airlines | 506 |
| 12 | All Nippon Airways | 465 |
| 13 | AZU | 445 |
| 14 | WIF | 437 |
| 15 | Delta Air Lines | 434 |
| 16 | QLK | 412 |
| 17 | Swiss International | 402 |
| 18 | LXJ | 389 |
| 19 | AEE | 355 |
| 20 | Alaska Airlines | 346 |
| 21 | EJU | 332 |
| 22 | VIV | 332 |
| 23 | easyJet | 331 |
| 24 | Japan Airlines | 304 |
| 25 | Air France | 303 |
| 26 | AXB | 280 |
| 27 | Cathay Pacific | 275 |
| 28 | JetBlue | 272 |
| 29 | United Airlines | 270 |
| 30 | GLO | 266 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 41978 |
| 2 | 🇪🇸 ES | 3803 |
| 3 | 🇮🇳 IN | 3770 |
| 4 | 🇦🇺 AU | 3570 |
| 5 | 🇧🇷 BR | 3041 |
| 6 | 🇮🇹 IT | 2823 |
| 7 | 🇯🇵 JP | 2809 |
| 8 | 🇩🇪 DE | 2800 |
| 9 | 🇨🇦 CA | 2618 |
| 10 | 🇨🇴 CO | 2427 |
| 11 | 🇬🇧 GB | 2186 |
| 12 | 🇫🇷 FR | 2042 |
| 13 | 🇲🇽 MX | 1620 |
| 14 | 🇬🇷 GR | 1586 |
| 15 | 🇨🇭 CH | 1474 |
| 16 | 🇳🇴 NO | 1418 |
| 17 | 🇲🇾 MY | 1238 |
| 18 | 🇿🇦 ZA | 1087 |
| 19 | 🇳🇿 NZ | 984 |
| 20 | 🇹🇷 TR | 947 |
| 21 | 🇹🇭 TH | 943 |
| 22 | 🇵🇭 PH | 897 |
| 23 | 🇰🇷 KR | 858 |
| 24 | 🇵🇱 PL | 839 |
| 25 | 🇬🇹 GT | 806 |
| 26 | 🇲🇦 MA | 649 |
| 27 | 🇲🇪 ME | 560 |
| 28 | 🇳🇱 NL | 532 |
| 29 | 🇲🇴 MO | 501 |
| 30 | 🇧🇸 BS | 462 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1204 |
| 2 | Tokyo International Airport |  | JP | 955 |
| 3 | Denver International Airport |  | US | 871 |
| 4 | El Dorado International Airport |  | CO | 825 |
| 5 | Indira Gandhi International Airport |  | IN | 805 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 787 |
| 7 | Guaymaral Airport |  | CO | 723 |
| 8 | Harry Reid International Airport |  | US | 676 |
| 9 | Zurich Airport |  | CH | 618 |
| 10 | La Aurora Airport |  | GT | 602 |
| 11 | Frankfurt am Main International Airport |  | DE | 601 |
| 12 | Chicago O'Hare International Airport |  | US | 521 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 516 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 503 |
| 15 | Macau International Airport |  | MO | 501 |
| 16 | Kuala Lumpur International Airport |  | MY | 491 |
| 17 | Madrid Barajas International Airport |  | ES | 486 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 465 |
| 19 | Bengaluru International Airport |  | IN | 449 |
| 20 | Congonhas Airport |  | BR | 439 |
| 21 | Malpensa International Airport |  | IT | 437 |
| 22 | Charlotte/Douglas International Airport |  | US | 431 |
| 23 | Tenerife Norte Airport |  | ES | 415 |
| 24 | Ninoy Aquino International Airport |  | PH | 414 |
| 25 | Charles de Gaulle International Airport |  | FR | 398 |
| 26 | Atizapan De Zaragoza Airport |  | MX | 392 |
| 27 | Salt Lake City International Airport |  | US | 390 |
| 28 | Daniel K Inouye International Airport |  | US | 380 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 378 |
| 30 | Capua Airport |  | IT | 368 |
| 31 | Vitoria/Foronda Airport |  | ES | 358 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 355 |
| 33 | Barcelona International Airport |  | ES | 353 |
| 34 | Reno/Tahoe International Airport |  | US | 351 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 350 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 349 |
| 37 | O. R. Tambo International Airport |  | ZA | 343 |
| 38 | Don Mueang International Airport |  | TH | 319 |
| 39 | Calgary International Airport |  | CA | 315 |
| 40 | Viracopos International Airport |  | BR | 309 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 292 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 241 | 1h 7m | 706 km | 2,934.2 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 200 | 14m | 114 km | 392.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 174 | 24m | 225 km | 675.0 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 157 | 21m | 244 km | 661.1 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 153 | 28m | 304 km | 802.1 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 147 | 1h 27m | 910 km | 2,306.8 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 136 | 19m | 165 km | 386.9 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 130 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 129 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 123 | 26m | 275 km | 582.8 t |
| 12 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 105 | 44m | 452 km | 818.3 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 104 | 54m | 546 km | 979.2 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 96 | 20m | 99 km | 164.4 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 92 | 1h 12m | 770 km | 1,222.1 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 88 | 31m | 369 km | 560.1 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 88 | 20m | 250 km | 380.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 87 | 27m | 215 km | 322.2 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 83 | 20m | 147 km | 210.0 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 81 | 52m | 556 km | 776.5 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 81 | 27m | 152 km | 211.7 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 75 | 1h 41m | 1,156 km | 1,496.2 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 74 | 1h 0m | 695 km | 887.0 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 72 | 13m | 99 km | 123.5 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 70 | 58m | 493 km | 595.5 t |
| 26 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 69 | 12m | 15 km | 18.2 t |
| 27 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 68 | 24m | 55 km | 64.6 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 68 | 1h 53m | 1,304 km | 1,529.8 t |
| 29 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 67 | 16m | 162 km | 187.8 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 67 | 1h 20m | 961 km | 1,110.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N383MF |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-04-24 19:38 UTC | 2026-04-24 21:03 UTC | 1h 25m |
| N750GJ |  | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-04-24 20:40 UTC | 2026-04-24 21:02 UTC | 21m |
| CGLDP | CGL | Chilliwack Airport (CYCW) | Pitt Meadows Airport (CYPK) | 2026-04-24 20:46 UTC | 2026-04-24 20:59 UTC | 13m |
| N782LA |  | Northeast Philadelphia Airport (KPNE) | Doylestown Airport (KDYL) | 2026-04-24 20:40 UTC | 2026-04-24 20:58 UTC | 18m |
| N36GB |  | Homer Airport (PAHO) | Seldovia Airport (PASO) | 2026-04-24 20:42 UTC | 2026-04-24 20:54 UTC | 12m |
| N150B |  | Lake Havasu City Airport (KHII) | Chemehuevi Valley Airport (K49X) | 2026-04-24 20:24 UTC | 2026-04-24 20:54 UTC | 29m |
| N68310 |  | North Perry Airport (KHWO) | Peter O Knight Airport (KTPF) | 2026-04-24 19:51 UTC | 2026-04-24 20:52 UTC | 1h 1m |
| N588ND |  | Orlando Apopka Airport (KX04) | Orlando Apopka Airport (KX04) | 2026-04-24 19:49 UTC | 2026-04-24 20:50 UTC | 1h 1m |
| BOE401 | BOE | Boeing Field/King County International Airport (KBFI) | Boeing Field/King County International Airport (KBFI) | 2026-04-24 18:47 UTC | 2026-04-24 20:50 UTC | 2h 2m |
| N86SF |  | Tyler Pounds Regional Airport (KTYR) | Aero Saylee Airport (43TS) | 2026-04-24 20:47 UTC | 2026-04-24 20:49 UTC | 2m |
| OXF9846 | OXF | Falcon Field (KFFZ) | Casa Grande Municipal Airport (KCGZ) | 2026-04-24 19:54 UTC | 2026-04-24 20:47 UTC | 52m |
| 00000000 |  | Tatui Airport (SDTF) | Lencois Paulista Airport (SDLP) | 2026-04-24 20:24 UTC | 2026-04-24 20:45 UTC | 20m |
| EJA960 | EJA | North Palm Beach County General Aviation Airport (KF45) | Louis Armstrong New Orleans International Airport (KMSY) | 2026-04-24 18:56 UTC | 2026-04-24 20:44 UTC | 1h 47m |
| BOE242 | BOE | Rnr Farms Airport (79WA) | Boeing Field/King County International Airport (KBFI) | 2026-04-24 20:20 UTC | 2026-04-24 20:43 UTC | 23m |
| TKR106 | TKR | GA25 (GA25) | Brantley County Airport (K4J1) | 2026-04-24 20:32 UTC | 2026-04-24 20:43 UTC | 10m |
| AEE4321 | AEE | Oulu Airport (EFOU) | Nida Airport (EYND) | 2026-04-24 19:45 UTC | 2026-04-24 20:42 UTC | 57m |
| N256RC |  | Birmingham-Shuttlesworth International Airport (KBHM) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-04-24 20:14 UTC | 2026-04-24 20:42 UTC | 27m |
| N8583Y |  | Cheyenne Regional/Jerry Olson Field (KCYS) | Pine Bluffs Municipal Airport (K82V) | 2026-04-24 20:04 UTC | 2026-04-24 20:40 UTC | 35m |
| CPA843 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-04-24 05:59 UTC | 2026-04-24 20:40 UTC | 14h 40m |
| N60244 |  | North Las Vegas Airport (KVGT) | Creech Afb Airport (KINS) | 2026-04-24 20:23 UTC | 2026-04-24 20:39 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
