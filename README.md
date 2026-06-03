# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--03_01:56:07_UTC-green)

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

**Latest saved flight:** 2026-06-03 01:56:07 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-03 01:56:07 UTC

- **101,351** saved flights
- **35,933** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **101,351** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,240,765.1 tonnes** estimated CO2 emissions
- **71,928,409 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4184 |
| 2 | SkyWest Airlines | 3808 |
| 3 | IndiGo | 2036 |
| 4 | EJA | 1931 |
| 5 | American Airlines | 1637 |
| 6 | Southwest Airlines | 1537 |
| 7 | ENY | 1259 |
| 8 | Delta Air Lines | 1191 |
| 9 | Lufthansa | 1184 |
| 10 | Vueling | 944 |
| 11 | LATAM Airlines | 900 |
| 12 | WIF | 888 |
| 13 | AXM | 876 |
| 14 | AZU | 818 |
| 15 | LXJ | 762 |
| 16 | Swiss International | 736 |
| 17 | All Nippon Airways | 717 |
| 18 | Alaska Airlines | 710 |
| 19 | QLK | 681 |
| 20 | easyJet | 658 |
| 21 | EJU | 636 |
| 22 | Cathay Pacific | 615 |
| 23 | AEE | 589 |
| 24 | Air France | 586 |
| 25 | VIV | 586 |
| 26 | United Airlines | 566 |
| 27 | CXK | 545 |
| 28 | MXY | 544 |
| 29 | Japan Airlines | 509 |
| 30 | AXB | 500 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 85043 |
| 2 | 🇪🇸 ES | 7006 |
| 3 | 🇮🇳 IN | 6440 |
| 4 | 🇦🇺 AU | 6139 |
| 5 | 🇧🇷 BR | 5537 |
| 6 | 🇩🇪 DE | 5472 |
| 7 | 🇮🇹 IT | 5396 |
| 8 | 🇨🇦 CA | 5253 |
| 9 | 🇯🇵 JP | 4689 |
| 10 | 🇬🇧 GB | 4301 |
| 11 | 🇫🇷 FR | 4038 |
| 12 | 🇨🇴 CO | 3505 |
| 13 | 🇲🇽 MX | 3069 |
| 14 | 🇬🇷 GR | 2881 |
| 15 | 🇳🇴 NO | 2813 |
| 16 | 🇨🇭 CH | 2605 |
| 17 | 🇲🇾 MY | 2234 |
| 18 | 🇹🇷 TR | 1919 |
| 19 | 🇿🇦 ZA | 1765 |
| 20 | 🇳🇿 NZ | 1709 |
| 21 | 🇹🇭 TH | 1685 |
| 22 | 🇰🇷 KR | 1643 |
| 23 | 🇵🇱 PL | 1625 |
| 24 | 🇬🇹 GT | 1501 |
| 25 | 🇵🇭 PH | 1481 |
| 26 | 🇲🇦 MA | 1132 |
| 27 | 🇲🇴 MO | 1074 |
| 28 | 🇳🇱 NL | 1008 |
| 29 | 🇲🇪 ME | 960 |
| 30 | 🇭🇷 HR | 892 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2206 |
| 2 | Denver International Airport |  | US | 1739 |
| 3 | Tokyo International Airport |  | JP | 1557 |
| 4 | Indira Gandhi International Airport |  | IN | 1402 |
| 5 | Harry Reid International Airport |  | US | 1298 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 1296 |
| 7 | Guaymaral Airport |  | CO | 1267 |
| 8 | Frankfurt am Main International Airport |  | DE | 1184 |
| 9 | Zurich Airport |  | CH | 1156 |
| 10 | La Aurora Airport |  | GT | 1154 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1096 |
| 12 | El Dorado International Airport |  | CO | 1075 |
| 13 | Macau International Airport |  | MO | 1074 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1027 |
| 15 | Chicago O'Hare International Airport |  | US | 1014 |
| 16 | Kuala Lumpur International Airport |  | MY | 884 |
| 17 | Madrid Barajas International Airport |  | ES | 882 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 872 |
| 19 | Salt Lake City International Airport |  | US | 855 |
| 20 | Capua Airport |  | IT | 838 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 789 |
| 22 | Charlotte/Douglas International Airport |  | US | 787 |
| 23 | Charles de Gaulle International Airport |  | FR | 780 |
| 24 | Malpensa International Airport |  | IT | 770 |
| 25 | Bengaluru International Airport |  | IN | 769 |
| 26 | Congonhas Airport |  | BR | 769 |
| 27 | Daniel K Inouye International Airport |  | US | 701 |
| 28 | Tenerife Norte Airport |  | ES | 697 |
| 29 | Ninoy Aquino International Airport |  | PH | 677 |
| 30 | Barcelona International Airport |  | ES | 669 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 661 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 659 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 646 |
| 34 | Amsterdam Airport Schiphol |  | NL | 623 |
| 35 | Don Mueang International Airport |  | TH | 617 |
| 36 | Vitoria/Foronda Airport |  | ES | 614 |
| 37 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 38 | Calgary International Airport |  | CA | 596 |
| 39 | Seattle-Tacoma International Airport |  | US | 585 |
| 40 | John Paul II International Airport Kraków-Balice Airport |  | PL | 575 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 522 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 370 | 21m | 244 km | 1,558.0 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 279 | 1h 7m | 706 km | 3,396.8 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 271 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 266 | 24m | 225 km | 1,032.0 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 256 | 14m | 114 km | 502.1 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 249 | 1h 26m | 910 km | 3,907.4 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 245 | 28m | 304 km | 1,284.4 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 233 | 1h 10m | 770 km | 3,095.2 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 214 | 19m | 165 km | 608.7 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 203 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 199 | 26m | 275 km | 943.0 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 159 | 20m | 99 km | 272.4 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 149 | 27m | 215 km | 551.8 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 149 | 22m | 55 km | 141.6 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 146 | 14m | 154 km | 386.8 t |
| 17 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 143 | 44m | 452 km | 1,114.5 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 142 | 31m | 369 km | 903.9 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 141 | 27m | 152 km | 368.5 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 135 | 13m | - | - |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 134 | 20m | 250 km | 578.8 t |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 130 | 20m | 147 km | 329.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 130 | 18m | 144 km | 323.4 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 128 | 1h 39m | 1,156 km | 2,553.6 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 127 | 1h 1m | 695 km | 1,522.4 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 119 | 1h 43m | 1,423 km | 2,920.4 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 117 | 1h 18m | 961 km | 1,939.3 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 117 | 1h 52m | 1,304 km | 2,632.2 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 117 | 12m | - | - |
| 30 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N40VA |  | Richmond Executive/Chesterfield County Airport (KFCI) | 4VA3 (4VA3) | 2026-06-03 01:24 UTC | 2026-06-03 01:56 UTC | 32m |
| BK702 |  | Catalina Airport (KAVX) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-06-03 00:57 UTC | 2026-06-03 01:51 UTC | 54m |
| URSA23 | URS | Nenana Municipal Airport (PANN) | Ladd Army Air Field (PAFB) | 2026-06-03 00:30 UTC | 2026-06-03 01:43 UTC | 1h 13m |
| N925ZG |  | Lebanon Municipal Airport (KM54) | Mesquite Metro Airport (KHQZ) | 2026-06-02 23:13 UTC | 2026-06-03 01:38 UTC | 2h 25m |
| EXV | EXV | Sydney Kingsford Smith International Airport (YSSY) | Sydney Kingsford Smith International Airport (YSSY) | 2026-06-03 01:14 UTC | 2026-06-03 01:33 UTC | 18m |
| N115SE |  | Brown Field Municipal Airport (KSDM) | Van Nuys Airport (KVNY) | 2026-06-03 00:52 UTC | 2026-06-03 01:29 UTC | 36m |
| N264V |  | Manassas Regional/Harry P Davis Field (KHEF) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-06-02 20:29 UTC | 2026-06-03 01:22 UTC | 4h 52m |
| VIQ | VIQ | Sydney Bankstown Airport (YSBK) | Sydney Bankstown Airport (YSBK) | 2026-06-03 00:59 UTC | 2026-06-03 01:21 UTC | 22m |
| N379R |  | Savannah/Hilton Head International Airport (KSAV) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-06-03 00:27 UTC | 2026-06-03 01:17 UTC | 50m |
| STT62 | STT | Portland-Hillsboro Airport (KHIO) | Florence Municipal Airport (K6S2) | 2026-06-03 00:37 UTC | 2026-06-03 01:08 UTC | 30m |
| N239FG |  | Trenton Mercer Airport (KTTN) | Lancaster Airport (KLNS) | 2026-06-03 00:20 UTC | 2026-06-03 01:07 UTC | 46m |
| MXD2407 | MXD | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 2026-06-03 00:45 UTC | 2026-06-03 01:06 UTC | 20m |
| ASA1072 | Alaska Airlines | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 2026-06-03 00:39 UTC | 2026-06-03 01:00 UTC | 21m |
| KSU38 | KSU | Salina Regional Airport (KSLN) | Salina Regional Airport (KSLN) | 2026-06-03 00:38 UTC | 2026-06-03 00:58 UTC | 19m |
| JZA298 | JZA | Vancouver International Airport (CYVR) | Kaslo Airport (CBR2) | 2026-06-03 00:09 UTC | 2026-06-03 00:58 UTC | 48m |
| N681MA |  | Trenton Mercer Airport (KTTN) | Lehigh Valley International Airport (KABE) | 2026-06-02 23:50 UTC | 2026-06-03 00:57 UTC | 1h 7m |
| AXM5301 | AXM | Kota Kinabalu International Airport (WBKK) | Senai International Airport (WMKJ) | 2026-06-02 23:01 UTC | 2026-06-03 00:56 UTC | 1h 54m |
| N917SH |  | Joe Foss Field (KFSD) | Watertown Regional Airport (KATY) | 2026-06-03 00:34 UTC | 2026-06-03 00:55 UTC | 21m |
| PNC0616 | PNC | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-06-03 00:08 UTC | 2026-06-03 00:54 UTC | 46m |
| TKR140 | TKR | San Bernardino International Airport (KSBD) | San Bernardino International Airport (KSBD) | 2026-06-03 00:02 UTC | 2026-06-03 00:54 UTC | 51m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
