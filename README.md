# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--11_16:52:44_UTC-green)

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

**Latest saved flight:** 2026-05-11 16:52:44 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-11 16:52:44 UTC

- **77,978** saved flights
- **28,464** unique routes
- **128** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **77,978** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **966,270.7 tonnes** estimated CO2 emissions
- **56,015,690 km** total distance flown
- **868 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3359 |
| 2 | SkyWest Airlines | 2903 |
| 3 | IndiGo | 1732 |
| 4 | EJA | 1436 |
| 5 | American Airlines | 1215 |
| 6 | Southwest Airlines | 1145 |
| 7 | Lufthansa | 1022 |
| 8 | ENY | 971 |
| 9 | Delta Air Lines | 844 |
| 10 | Vueling | 747 |
| 11 | AXM | 721 |
| 12 | LATAM Airlines | 712 |
| 13 | WIF | 674 |
| 14 | All Nippon Airways | 627 |
| 15 | AZU | 618 |
| 16 | Swiss International | 598 |
| 17 | QLK | 591 |
| 18 | LXJ | 569 |
| 19 | Alaska Airlines | 548 |
| 20 | easyJet | 522 |
| 21 | EJU | 508 |
| 22 | AEE | 506 |
| 23 | Cathay Pacific | 499 |
| 24 | VIV | 466 |
| 25 | Air France | 461 |
| 26 | Japan Airlines | 449 |
| 27 | AXB | 434 |
| 28 | CXK | 399 |
| 29 | MXY | 390 |
| 30 | AIQ | 387 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 62979 |
| 2 | 🇪🇸 ES | 5589 |
| 3 | 🇮🇳 IN | 5436 |
| 4 | 🇦🇺 AU | 5035 |
| 5 | 🇩🇪 DE | 4422 |
| 6 | 🇧🇷 BR | 4332 |
| 7 | 🇮🇹 IT | 4316 |
| 8 | 🇯🇵 JP | 4030 |
| 9 | 🇨🇦 CA | 3856 |
| 10 | 🇬🇧 GB | 3358 |
| 11 | 🇫🇷 FR | 3099 |
| 12 | 🇨🇴 CO | 2700 |
| 13 | 🇲🇽 MX | 2382 |
| 14 | 🇬🇷 GR | 2307 |
| 15 | 🇳🇴 NO | 2140 |
| 16 | 🇨🇭 CH | 2108 |
| 17 | 🇲🇾 MY | 1808 |
| 18 | 🇿🇦 ZA | 1486 |
| 19 | 🇹🇷 TR | 1412 |
| 20 | 🇳🇿 NZ | 1396 |
| 21 | 🇹🇭 TH | 1386 |
| 22 | 🇵🇱 PL | 1302 |
| 23 | 🇵🇭 PH | 1244 |
| 24 | 🇰🇷 KR | 1218 |
| 25 | 🇬🇹 GT | 1209 |
| 26 | 🇲🇦 MA | 922 |
| 27 | 🇲🇴 MO | 915 |
| 28 | 🇲🇪 ME | 836 |
| 29 | 🇳🇱 NL | 816 |
| 30 | 🇭🇷 HR | 680 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1720 |
| 2 | Tokyo International Airport |  | JP | 1354 |
| 3 | Denver International Airport |  | US | 1303 |
| 4 | Indira Gandhi International Airport |  | IN | 1151 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1131 |
| 6 | Frankfurt am Main International Airport |  | DE | 1027 |
| 7 | Harry Reid International Airport |  | US | 967 |
| 8 | Zurich Airport |  | CH | 924 |
| 9 | Macau International Airport |  | MO | 915 |
| 10 | La Aurora Airport |  | GT | 909 |
| 11 | Guaymaral Airport |  | CO | 892 |
| 12 | El Dorado International Airport |  | CO | 879 |
| 13 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 847 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 783 |
| 15 | Chicago O'Hare International Airport |  | US | 760 |
| 16 | Kuala Lumpur International Airport |  | MY | 726 |
| 17 | Madrid Barajas International Airport |  | ES | 722 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 689 |
| 19 | Malpensa International Airport |  | IT | 678 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 674 |
| 21 | Bengaluru International Airport |  | IN | 672 |
| 22 | Salt Lake City International Airport |  | US | 640 |
| 23 | Capua Airport |  | IT | 622 |
| 24 | Charlotte/Douglas International Airport |  | US | 615 |
| 25 | Charles de Gaulle International Airport |  | FR | 615 |
| 26 | Congonhas Airport |  | BR | 613 |
| 27 | Tenerife Norte Airport |  | ES | 582 |
| 28 | Ninoy Aquino International Airport |  | PH | 566 |
| 29 | Daniel K Inouye International Airport |  | US | 565 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 557 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 528 |
| 32 | Barcelona International Airport |  | ES | 527 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 526 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 510 |
| 35 | Don Mueang International Airport |  | TH | 494 |
| 36 | Vitoria/Foronda Airport |  | ES | 494 |
| 37 | Amsterdam Airport Schiphol |  | NL | 492 |
| 38 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 484 |
| 39 | O. R. Tambo International Airport |  | ZA | 468 |
| 40 | Calgary International Airport |  | CA | 462 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 371 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 279 | 21m | 244 km | 1,174.8 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 271 | 1h 8m | 706 km | 3,299.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 224 | 24m | 225 km | 869.0 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 216 | 28m | 304 km | 1,132.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 209 | 1h 27m | 910 km | 3,279.7 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 198 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 185 | 31m | - | - |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 184 | 19m | 165 km | 523.4 t |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 173 | 1h 12m | 770 km | 2,298.2 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 166 | 26m | 275 km | 786.6 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 140 | 20m | 99 km | 239.8 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 136 | 44m | 452 km | 1,059.9 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 124 | 31m | 369 km | 789.3 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 119 | 27m | 215 km | 440.7 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 119 | 27m | 152 km | 311.0 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 115 | 20m | 147 km | 291.0 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 114 | 20m | 250 km | 492.4 t |
| 20 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 111 | 59m | - | - |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 111 | 14m | 154 km | 294.1 t |
| 22 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 104 | 1h 2m | 695 km | 1,246.7 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 103 | 1h 42m | 1,423 km | 2,527.8 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 103 | 57m | 493 km | 876.3 t |
| 26 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 102 | 23m | 55 km | 96.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |
| 28 | Bodø Airport (ENBO) | ENEN (ENEN) | 98 | 13m | - | - |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 98 | 12m | - | - |
| 30 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 98 | 18m | 144 km | 243.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N9900M |  | Seattle Paine Field International Airport (KPAE) | William R Fairchild International Airport (KCLM) | 2026-05-11 16:00 UTC | 2026-05-11 16:52 UTC | 51m |
| N570JA |  | Aurora Municipal Airport (KARR) | 58IL (58IL) | 2026-05-11 16:24 UTC | 2026-05-11 16:52 UTC | 27m |
| SKW4288 | SkyWest Airlines | Ford Airport (KIMT) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-11 16:04 UTC | 2026-05-11 16:50 UTC | 46m |
| WATTS76 | WAT | AZ67 (AZ67) | Pinal Airpark (KMZJ) | 2026-05-11 16:10 UTC | 2026-05-11 16:49 UTC | 39m |
| DAL161 | Delta Air Lines | Amsterdam Airport Schiphol (EHAM) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-11 08:19 UTC | 2026-05-11 16:46 UTC | 8h 27m |
| HOOK32 | HOO | 75OK (75OK) | 1KS0 (1KS0) | 2026-05-11 16:04 UTC | 2026-05-11 16:41 UTC | 37m |
| HOBBY23 | HOB | Gulfport-Biloxi International Airport (KGPT) | Bredlow Farm Airport (17AR) | 2026-05-11 15:45 UTC | 2026-05-11 16:41 UTC | 55m |
| LHB1 | LHB | Friedrichshafen Airport (EDNY) | Saint-Flour-Coltines Airport (LFHQ) | 2026-05-11 15:47 UTC | 2026-05-11 16:39 UTC | 51m |
| N722WD |  | Rocky Mountain Metro Airport (KBJC) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-05-11 15:38 UTC | 2026-05-11 16:36 UTC | 57m |
| N55044 |  | Tweed/New Haven Airport (KHVN) | Tweed/New Haven Airport (KHVN) | 2026-05-11 16:29 UTC | 2026-05-11 16:35 UTC | 6m |
| SKW3870 | SkyWest Airlines | Joe Foss Field (KFSD) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-11 16:01 UTC | 2026-05-11 16:35 UTC | 34m |
| TJT37DR | TJT | Toulouse-Blagnac Airport (LFBO) | Rennes-Saint-Jacques Airport (LFRN) | 2026-05-11 15:13 UTC | 2026-05-11 16:34 UTC | 1h 21m |
| CXK699 | CXK | Pueblo Memorial Airport (KPUB) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-05-11 16:09 UTC | 2026-05-11 16:34 UTC | 24m |
| N4333A |  | Trenton-Robbinsville Airport (KN87) | Trenton-Robbinsville Airport (KN87) | 2026-05-11 15:50 UTC | 2026-05-11 16:33 UTC | 42m |
| N20AH |  | Grand Prairie Municipal Airport (KGPM) | Grand Prairie Municipal Airport (KGPM) | 2026-05-11 15:50 UTC | 2026-05-11 16:32 UTC | 41m |
| N125MG |  | Nelson Ranch Airport (19OR) | Nelson Ranch Airport (19OR) | 2026-05-11 16:27 UTC | 2026-05-11 16:31 UTC | 4m |
| N808CP |  | Martin State Airport (KMTN) | Martin State Airport (KMTN) | 2026-05-11 15:36 UTC | 2026-05-11 16:29 UTC | 53m |
| N4877J |  | L & M Aerodrome (MN31) | Flying Cloud Airport (KFCM) | 2026-05-11 16:00 UTC | 2026-05-11 16:29 UTC | 28m |
| N264HS |  | Vance Brand Airport (KLMO) | Laramie Regional Airport (KLAR) | 2026-05-11 15:56 UTC | 2026-05-11 16:26 UTC | 30m |
| HBZYW | HBZ | Wangen-Lachen Airport (LSPV) | Wangen-Lachen Airport (LSPV) | 2026-05-11 16:17 UTC | 2026-05-11 16:26 UTC | 9m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
