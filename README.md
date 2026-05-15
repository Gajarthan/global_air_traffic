# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--15_14:15:18_UTC-green)

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

**Latest saved flight:** 2026-05-15 14:15:18 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-15 14:15:18 UTC

- **82,991** saved flights
- **30,022** unique routes
- **129** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **82,991** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,022,266.9 tonnes** estimated CO2 emissions
- **59,261,852 km** total distance flown
- **865 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3554 |
| 2 | SkyWest Airlines | 3067 |
| 3 | IndiGo | 1808 |
| 4 | EJA | 1555 |
| 5 | American Airlines | 1278 |
| 6 | Southwest Airlines | 1211 |
| 7 | Lufthansa | 1068 |
| 8 | ENY | 1034 |
| 9 | Delta Air Lines | 907 |
| 10 | Vueling | 785 |
| 11 | LATAM Airlines | 753 |
| 12 | AXM | 751 |
| 13 | WIF | 722 |
| 14 | AZU | 655 |
| 15 | All Nippon Airways | 652 |
| 16 | Swiss International | 644 |
| 17 | QLK | 615 |
| 18 | LXJ | 603 |
| 19 | Alaska Airlines | 587 |
| 20 | easyJet | 546 |
| 21 | EJU | 532 |
| 22 | AEE | 527 |
| 23 | Cathay Pacific | 518 |
| 24 | VIV | 496 |
| 25 | Air France | 487 |
| 26 | Japan Airlines | 468 |
| 27 | AXB | 443 |
| 28 | CXK | 436 |
| 29 | MXY | 412 |
| 30 | AIQ | 410 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 67763 |
| 2 | 🇪🇸 ES | 5890 |
| 3 | 🇮🇳 IN | 5653 |
| 4 | 🇦🇺 AU | 5322 |
| 5 | 🇩🇪 DE | 4649 |
| 6 | 🇧🇷 BR | 4596 |
| 7 | 🇮🇹 IT | 4580 |
| 8 | 🇯🇵 JP | 4195 |
| 9 | 🇨🇦 CA | 4129 |
| 10 | 🇬🇧 GB | 3541 |
| 11 | 🇫🇷 FR | 3304 |
| 12 | 🇨🇴 CO | 2762 |
| 13 | 🇲🇽 MX | 2509 |
| 14 | 🇬🇷 GR | 2412 |
| 15 | 🇳🇴 NO | 2324 |
| 16 | 🇨🇭 CH | 2210 |
| 17 | 🇲🇾 MY | 1889 |
| 18 | 🇿🇦 ZA | 1568 |
| 19 | 🇹🇷 TR | 1471 |
| 20 | 🇳🇿 NZ | 1463 |
| 21 | 🇹🇭 TH | 1452 |
| 22 | 🇵🇱 PL | 1385 |
| 23 | 🇵🇭 PH | 1308 |
| 24 | 🇰🇷 KR | 1272 |
| 25 | 🇬🇹 GT | 1257 |
| 26 | 🇲🇦 MA | 965 |
| 27 | 🇲🇴 MO | 952 |
| 28 | 🇲🇪 ME | 882 |
| 29 | 🇳🇱 NL | 854 |
| 30 | 🇭🇷 HR | 743 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1822 |
| 2 | Tokyo International Airport |  | JP | 1406 |
| 3 | Denver International Airport |  | US | 1389 |
| 4 | Indira Gandhi International Airport |  | IN | 1201 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1175 |
| 6 | Frankfurt am Main International Airport |  | DE | 1078 |
| 7 | Harry Reid International Airport |  | US | 1034 |
| 8 | Zurich Airport |  | CH | 986 |
| 9 | La Aurora Airport |  | GT | 952 |
| 10 | Macau International Airport |  | MO | 952 |
| 11 | Guaymaral Airport |  | CO | 929 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 924 |
| 13 | El Dorado International Airport |  | CO | 890 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 829 |
| 15 | Chicago O'Hare International Airport |  | US | 804 |
| 16 | Madrid Barajas International Airport |  | ES | 756 |
| 17 | Kuala Lumpur International Airport |  | MY | 751 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 720 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 699 |
| 20 | Malpensa International Airport |  | IT | 696 |
| 21 | Bengaluru International Airport |  | IN | 694 |
| 22 | Salt Lake City International Airport |  | US | 685 |
| 23 | Capua Airport |  | IT | 675 |
| 24 | Charles de Gaulle International Airport |  | FR | 650 |
| 25 | Congonhas Airport |  | BR | 647 |
| 26 | Charlotte/Douglas International Airport |  | US | 646 |
| 27 | Tenerife Norte Airport |  | ES | 605 |
| 28 | Daniel K Inouye International Airport |  | US | 601 |
| 29 | Ninoy Aquino International Airport |  | PH | 598 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 589 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 557 |
| 32 | Barcelona International Airport |  | ES | 557 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 554 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 537 |
| 35 | Vitoria/Foronda Airport |  | ES | 526 |
| 36 | Don Mueang International Airport |  | TH | 523 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 520 |
| 38 | Amsterdam Airport Schiphol |  | NL | 516 |
| 39 | O. R. Tambo International Airport |  | ZA | 492 |
| 40 | Calgary International Airport |  | CA | 485 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 387 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 299 | 21m | 244 km | 1,259.0 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 273 | 1h 8m | 706 km | 3,323.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 237 | 24m | 225 km | 919.4 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 222 | 28m | 304 km | 1,163.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 221 | 1h 26m | 910 km | 3,468.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 212 | 14m | 114 km | 415.8 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 211 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 197 | 31m | - | - |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 189 | 19m | 165 km | 537.6 t |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 188 | 1h 11m | 770 km | 2,497.4 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 173 | 26m | 275 km | 819.8 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 142 | 20m | 99 km | 243.2 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 139 | 44m | 452 km | 1,083.3 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 128 | 31m | 369 km | 814.8 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 125 | 27m | 215 km | 462.9 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 125 | 27m | 152 km | 326.7 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 122 | 20m | 147 km | 308.7 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 119 | 14m | 154 km | 315.3 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 116 | 20m | 250 km | 501.1 t |
| 21 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 115 | 23m | 55 km | 109.3 t |
| 22 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 114 | 1h 2m | 695 km | 1,366.5 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 110 | 57m | 493 km | 935.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 107 | 1h 43m | 1,423 km | 2,625.9 t |
| 26 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |
| 27 | Bodø Airport (ENBO) | ENEN (ENEN) | 106 | 13m | - | - |
| 28 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 105 | 18m | 144 km | 261.2 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 104 | 12m | - | - |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 100 | 1h 18m | 961 km | 1,657.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| OE7144 |  | Schaerding-Suben Airport (LOLS) | Schaerding-Suben Airport (LOLS) | 2026-05-15 14:02 UTC | 2026-05-15 14:15 UTC | 13m |
| ISR596 | ISR | Paphos International Airport (LCPH) | Ben Gurion International Airport (LLBG) | 2026-05-15 13:14 UTC | 2026-05-15 14:09 UTC | 55m |
| N1297F |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-05-15 13:55 UTC | 2026-05-15 14:09 UTC | 13m |
| N595KW |  | Willow Run Airport (KYIP) | Olive Branch/Taylor Field (KOLV) | 2026-05-15 12:25 UTC | 2026-05-15 14:06 UTC | 1h 40m |
| N77NG |  | Montgomery-Gibbs Executive Airport (KMYF) | Palmdale Usaf Plant 42 Airport (KPMD) | 2026-05-15 13:35 UTC | 2026-05-15 14:05 UTC | 30m |
| ZUIAZ | ZUI | Delta 200 Airstrip (FADX) | Delta 200 Airstrip (FADX) | 2026-05-15 13:50 UTC | 2026-05-15 14:03 UTC | 13m |
| N707DJ |  | North Perry Airport (KHWO) | North Perry Airport (KHWO) | 2026-05-15 12:52 UTC | 2026-05-15 14:02 UTC | 1h 10m |
| N310BF |  | SC10 (SC10) | Spartanburg Downtown Memorial/Simpson Field (KSPA) | 2026-05-15 12:57 UTC | 2026-05-15 14:02 UTC | 1h 5m |
| N6150M |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-05-15 13:50 UTC | 2026-05-15 14:02 UTC | 12m |
| GPTRK | GPT | Kemble Airport (EGBP) | RAF Woodvale (EGOW) | 2026-05-15 12:59 UTC | 2026-05-15 14:00 UTC | 1h 1m |
| N704MR |  | Merritt Island Airport (KCOI) | Marco Island Executive Airport (KMKY) | 2026-05-15 12:19 UTC | 2026-05-15 13:59 UTC | 1h 40m |
| N265PS |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-05-15 12:51 UTC | 2026-05-15 13:57 UTC | 1h 6m |
| RTV2M | RTV | Vilar Da Luz Airport (LPVL) | Alijo Airport (LPJO) | 2026-05-15 13:23 UTC | 2026-05-15 13:56 UTC | 32m |
| KNIFE84 | KNI | Los Alamitos Army Air Field (KSLI) | Meadows Field (KBFL) | 2026-05-15 12:40 UTC | 2026-05-15 13:54 UTC | 1h 13m |
| BPX213 | BPX | Daytona Beach International Airport (KDAB) | Ormond Beach Municipal Airport (KOMN) | 2026-05-15 13:26 UTC | 2026-05-15 13:53 UTC | 26m |
| TASI313 | TAS | Perot Field/Fort Worth Alliance Airport (KAFW) | Shreveport Regional Airport (KSHV) | 2026-05-15 13:04 UTC | 2026-05-15 13:53 UTC | 48m |
| MARVA | MAR | Ben Gurion International Airport (LLBG) | Diagoras Airport (LGRP) | 2026-05-15 12:28 UTC | 2026-05-15 13:46 UTC | 1h 18m |
| CGSAG | CGS | Montréal / St-Hubert Airport (CYHU) | Princeton Municipal Airport (KPNN) | 2026-05-15 12:36 UTC | 2026-05-15 13:45 UTC | 1h 8m |
| GHBTG | GHB | Bruntingthorpe Airport (EG74) | Bruntingthorpe Airport (EG74) | 2026-05-15 13:27 UTC | 2026-05-15 13:44 UTC | 16m |
| FHOKE | FHO | Lille/Marcq-en-Baroeul Airport (LFQO) | Lille/Marcq-en-Baroeul Airport (LFQO) | 2026-05-15 13:23 UTC | 2026-05-15 13:44 UTC | 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
