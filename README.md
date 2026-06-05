# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--05_13:14:42_UTC-green)

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

**Latest saved flight:** 2026-06-05 13:14:42 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-05 13:14:42 UTC

- **102,884** saved flights
- **36,408** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **102,884** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,256,069.8 tonnes** estimated CO2 emissions
- **72,815,643 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4231 |
| 2 | SkyWest Airlines | 3860 |
| 3 | IndiGo | 2059 |
| 4 | EJA | 1969 |
| 5 | American Airlines | 1659 |
| 6 | Southwest Airlines | 1553 |
| 7 | ENY | 1275 |
| 8 | Delta Air Lines | 1210 |
| 9 | Lufthansa | 1191 |
| 10 | Vueling | 950 |
| 11 | LATAM Airlines | 912 |
| 12 | WIF | 905 |
| 13 | AXM | 886 |
| 14 | AZU | 828 |
| 15 | LXJ | 776 |
| 16 | Swiss International | 743 |
| 17 | All Nippon Airways | 727 |
| 18 | Alaska Airlines | 719 |
| 19 | QLK | 692 |
| 20 | easyJet | 668 |
| 21 | EJU | 643 |
| 22 | Cathay Pacific | 616 |
| 23 | AEE | 599 |
| 24 | Air France | 590 |
| 25 | VIV | 590 |
| 26 | United Airlines | 571 |
| 27 | MXY | 558 |
| 28 | CXK | 552 |
| 29 | Japan Airlines | 511 |
| 30 | AXB | 506 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 86460 |
| 2 | 🇪🇸 ES | 7083 |
| 3 | 🇮🇳 IN | 6504 |
| 4 | 🇦🇺 AU | 6265 |
| 5 | 🇧🇷 BR | 5635 |
| 6 | 🇩🇪 DE | 5532 |
| 7 | 🇮🇹 IT | 5464 |
| 8 | 🇨🇦 CA | 5351 |
| 9 | 🇯🇵 JP | 4752 |
| 10 | 🇬🇧 GB | 4346 |
| 11 | 🇫🇷 FR | 4083 |
| 12 | 🇨🇴 CO | 3541 |
| 13 | 🇲🇽 MX | 3093 |
| 14 | 🇬🇷 GR | 2930 |
| 15 | 🇳🇴 NO | 2866 |
| 16 | 🇨🇭 CH | 2638 |
| 17 | 🇲🇾 MY | 2258 |
| 18 | 🇹🇷 TR | 1949 |
| 19 | 🇿🇦 ZA | 1790 |
| 20 | 🇳🇿 NZ | 1727 |
| 21 | 🇹🇭 TH | 1701 |
| 22 | 🇰🇷 KR | 1677 |
| 23 | 🇵🇱 PL | 1645 |
| 24 | 🇬🇹 GT | 1506 |
| 25 | 🇵🇭 PH | 1502 |
| 26 | 🇲🇦 MA | 1138 |
| 27 | 🇲🇴 MO | 1076 |
| 28 | 🇳🇱 NL | 1016 |
| 29 | 🇲🇪 ME | 969 |
| 30 | 🇭🇷 HR | 903 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2228 |
| 2 | Denver International Airport |  | US | 1759 |
| 3 | Tokyo International Airport |  | JP | 1577 |
| 4 | Indira Gandhi International Airport |  | IN | 1411 |
| 5 | Harry Reid International Airport |  | US | 1319 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 1315 |
| 7 | Guaymaral Airport |  | CO | 1286 |
| 8 | Frankfurt am Main International Airport |  | DE | 1191 |
| 9 | Zurich Airport |  | CH | 1172 |
| 10 | La Aurora Airport |  | GT | 1159 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1111 |
| 12 | El Dorado International Airport |  | CO | 1083 |
| 13 | Macau International Airport |  | MO | 1076 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1041 |
| 15 | Chicago O'Hare International Airport |  | US | 1028 |
| 16 | Madrid Barajas International Airport |  | ES | 899 |
| 17 | Kuala Lumpur International Airport |  | MY | 891 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 883 |
| 19 | Salt Lake City International Airport |  | US | 866 |
| 20 | Capua Airport |  | IT | 856 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 799 |
| 22 | Charlotte/Douglas International Airport |  | US | 798 |
| 23 | Charles de Gaulle International Airport |  | FR | 784 |
| 24 | Congonhas Airport |  | BR | 781 |
| 25 | Bengaluru International Airport |  | IN | 779 |
| 26 | Malpensa International Airport |  | IT | 773 |
| 27 | Daniel K Inouye International Airport |  | US | 709 |
| 28 | Tenerife Norte Airport |  | ES | 703 |
| 29 | Ninoy Aquino International Airport |  | PH | 686 |
| 30 | Barcelona International Airport |  | ES | 675 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 668 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 664 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 660 |
| 34 | Amsterdam Airport Schiphol |  | NL | 628 |
| 35 | Don Mueang International Airport |  | TH | 623 |
| 36 | Vitoria/Foronda Airport |  | ES | 621 |
| 37 | Calgary International Airport |  | CA | 608 |
| 38 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 39 | Seattle-Tacoma International Airport |  | US | 595 |
| 40 | Norman Y Mineta San Jose International Airport |  | US | 581 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 531 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 377 | 21m | 244 km | 1,587.4 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 279 | 1h 7m | 706 km | 3,396.8 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 272 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 270 | 24m | 225 km | 1,047.5 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 257 | 14m | 114 km | 504.1 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 251 | 1h 26m | 910 km | 3,938.8 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 249 | 28m | 304 km | 1,305.3 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 237 | 1h 10m | 770 km | 3,148.4 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 216 | 19m | 165 km | 614.4 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 204 | 26m | 275 km | 966.7 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 203 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 159 | 20m | 99 km | 272.4 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 155 | 22m | 55 km | 147.3 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 150 | 27m | 215 km | 555.5 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 147 | 14m | 154 km | 389.5 t |
| 17 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 144 | 44m | 452 km | 1,122.3 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 143 | 31m | 369 km | 910.2 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 143 | 27m | 152 km | 373.7 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 139 | 13m | - | - |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 138 | 20m | 250 km | 596.1 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 134 | 18m | 144 km | 333.3 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 132 | 20m | 147 km | 334.0 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 129 | 1h 39m | 1,156 km | 2,573.5 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 127 | 1h 1m | 695 km | 1,522.4 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 120 | 1h 43m | 1,423 km | 2,945.0 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 118 | 1h 18m | 961 km | 1,955.9 t |
| 28 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 117 | 44m | 241 km | 486.0 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 117 | 1h 52m | 1,304 km | 2,632.2 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 117 | 12m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N835FG |  | Trenton Mercer Airport (KTTN) | Quakertown Airport (KUKT) | 2026-06-05 12:46 UTC | 2026-06-05 13:14 UTC | 28m |
| LFA555 | LFA | Orlando Sanford International Airport (KSFB) | Orlando Sanford International Airport (KSFB) | 2026-06-05 13:02 UTC | 2026-06-05 13:14 UTC | 11m |
| RN246 |  | Whiting Field Nas North Airport (KNSE) | Evergreen Regional/Middleton Field (KGZH) | 2026-06-05 12:59 UTC | 2026-06-05 13:10 UTC | 11m |
| DHK528 | DHK | Malpensa International Airport (LIMC) | Zhuhai Airport (ZGSD) | 2026-06-05 02:31 UTC | 2026-06-05 13:08 UTC | 10h 36m |
| QTR120 | Qatar Airways | London Heathrow Airport (EGLL) | Queen Alia International Airport (OJAI) | 2026-06-05 09:05 UTC | 2026-06-05 13:03 UTC | 3h 58m |
| SGE64 | SGE | Fort Worth Meacham International Airport (KFTW) | Kenneth Copeland Airport (K4T2) | 2026-06-05 12:53 UTC | 2026-06-05 13:03 UTC | 10m |
| EWG7SU | EWG | Valencia Airport (LEVC) | Spa (la Sauveniere) Airport (EBSP) | 2026-06-05 10:45 UTC | 2026-06-05 13:01 UTC | 2h 15m |
| RYR838P | Ryanair | Pisa / San Giusto - Galileo Galilei International Airport (LIRP) | Spangdahlem Air Base (ETAD) | 2026-06-05 11:38 UTC | 2026-06-05 13:01 UTC | 1h 22m |
| N779RA |  | Brooksville-Tampa Bay Regional Airport (KBKV) | Ocala International-Jim Taylor Field (KOCF) | 2026-06-05 12:38 UTC | 2026-06-05 13:00 UTC | 22m |
| N1469T |  | Bridgeport/Sikorsky Airport (KBDR) | Chester Airport (KSNC) | 2026-06-05 12:37 UTC | 2026-06-05 12:57 UTC | 20m |
| MSR735 | EgyptAir | HE32 (HE32) | Queen Alia International Airport (OJAI) | 2026-06-05 12:26 UTC | 2026-06-05 12:55 UTC | 28m |
| FJJJY | FJJ | Saint-Nazaire-Montoir Airport (LFRZ) | Saint-Nazaire-Montoir Airport (LFRZ) | 2026-06-05 12:16 UTC | 2026-06-05 12:50 UTC | 34m |
| N769FG |  | Trenton Mercer Airport (KTTN) | Doylestown Airport (KDYL) | 2026-06-05 12:33 UTC | 2026-06-05 12:49 UTC | 15m |
| OKHHA | OKH | Hradec Kralove Airport (LKHK) | Hradec Kralove Airport (LKHK) | 2026-06-05 12:28 UTC | 2026-06-05 12:48 UTC | 19m |
| N841DS |  | Columbus Airport (KCSG) | Atlanta Regional Falcon Field (KFFC) | 2026-06-05 12:18 UTC | 2026-06-05 12:46 UTC | 27m |
| WIF69D | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-06-05 12:09 UTC | 2026-06-05 12:44 UTC | 35m |
| HBKPL | HBK | St Gallen Altenrhein Airport (LSZR) | Friedrichshafen Airport (EDNY) | 2026-06-05 11:57 UTC | 2026-06-05 12:43 UTC | 46m |
| N630AC |  | Georgetown-Scott County Regional Airport (K27K) | Lebanon Springfield/George Hoerter Field (K6I2) | 2026-06-05 12:10 UTC | 2026-06-05 12:42 UTC | 32m |
| ABY322 | ABY | Istanbul Airport (LTFM) | Queen Alia International Airport (OJAI) | 2026-06-05 11:31 UTC | 2026-06-05 12:42 UTC | 1h 10m |
| ETD99P | Etihad Airways | Munich International Airport (EDDM) | Queen Alia International Airport (OJAI) | 2026-06-05 09:36 UTC | 2026-06-05 12:41 UTC | 3h 4m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
