# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--09_15:12:34_UTC-green)

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

**Latest saved flight:** 2026-06-09 15:12:34 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-09 15:12:34 UTC

- **106,957** saved flights
- **37,539** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **106,957** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,307,730.2 tonnes** estimated CO2 emissions
- **75,810,446 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4401 |
| 2 | SkyWest Airlines | 4021 |
| 3 | IndiGo | 2117 |
| 4 | EJA | 2065 |
| 5 | American Airlines | 1710 |
| 6 | Southwest Airlines | 1613 |
| 7 | ENY | 1340 |
| 8 | Delta Air Lines | 1272 |
| 9 | Lufthansa | 1223 |
| 10 | Vueling | 982 |
| 11 | LATAM Airlines | 951 |
| 12 | WIF | 935 |
| 13 | AXM | 910 |
| 14 | AZU | 874 |
| 15 | LXJ | 805 |
| 16 | Swiss International | 778 |
| 17 | All Nippon Airways | 741 |
| 18 | Alaska Airlines | 738 |
| 19 | QLK | 711 |
| 20 | easyJet | 692 |
| 21 | EJU | 682 |
| 22 | Cathay Pacific | 643 |
| 23 | AEE | 613 |
| 24 | VIV | 611 |
| 25 | Air France | 608 |
| 26 | United Airlines | 592 |
| 27 | MXY | 579 |
| 28 | CXK | 565 |
| 29 | Japan Airlines | 526 |
| 30 | AXB | 523 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 90018 |
| 2 | 🇪🇸 ES | 7350 |
| 3 | 🇮🇳 IN | 6672 |
| 4 | 🇦🇺 AU | 6403 |
| 5 | 🇧🇷 BR | 5901 |
| 6 | 🇩🇪 DE | 5737 |
| 7 | 🇮🇹 IT | 5729 |
| 8 | 🇨🇦 CA | 5598 |
| 9 | 🇯🇵 JP | 4874 |
| 10 | 🇬🇧 GB | 4541 |
| 11 | 🇫🇷 FR | 4252 |
| 12 | 🇨🇴 CO | 3707 |
| 13 | 🇲🇽 MX | 3204 |
| 14 | 🇬🇷 GR | 3033 |
| 15 | 🇳🇴 NO | 2957 |
| 16 | 🇨🇭 CH | 2732 |
| 17 | 🇲🇾 MY | 2336 |
| 18 | 🇹🇷 TR | 2069 |
| 19 | 🇿🇦 ZA | 1838 |
| 20 | 🇰🇷 KR | 1779 |
| 21 | 🇳🇿 NZ | 1776 |
| 22 | 🇹🇭 TH | 1759 |
| 23 | 🇵🇱 PL | 1745 |
| 24 | 🇵🇭 PH | 1567 |
| 25 | 🇬🇹 GT | 1545 |
| 26 | 🇲🇦 MA | 1181 |
| 27 | 🇲🇴 MO | 1118 |
| 28 | 🇳🇱 NL | 1048 |
| 29 | 🇲🇪 ME | 1026 |
| 30 | 🇭🇷 HR | 929 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2315 |
| 2 | Denver International Airport |  | US | 1819 |
| 3 | Tokyo International Airport |  | JP | 1613 |
| 4 | Indira Gandhi International Airport |  | IN | 1451 |
| 5 | Harry Reid International Airport |  | US | 1366 |
| 6 | Guaymaral Airport |  | CO | 1354 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1341 |
| 8 | Zurich Airport |  | CH | 1215 |
| 9 | Frankfurt am Main International Airport |  | DE | 1209 |
| 10 | La Aurora Airport |  | GT | 1189 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1158 |
| 12 | El Dorado International Airport |  | CO | 1128 |
| 13 | Macau International Airport |  | MO | 1118 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1079 |
| 15 | Chicago O'Hare International Airport |  | US | 1072 |
| 16 | Madrid Barajas International Airport |  | ES | 932 |
| 17 | Kuala Lumpur International Airport |  | MY | 915 |
| 18 | Capua Airport |  | IT | 913 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 912 |
| 20 | Salt Lake City International Airport |  | US | 911 |
| 21 | Charlotte/Douglas International Airport |  | US | 830 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 814 |
| 23 | Congonhas Airport |  | BR | 814 |
| 24 | Charles de Gaulle International Airport |  | FR | 811 |
| 25 | Bengaluru International Airport |  | IN | 800 |
| 26 | Malpensa International Airport |  | IT | 797 |
| 27 | Daniel K Inouye International Airport |  | US | 725 |
| 28 | Ninoy Aquino International Airport |  | PH | 718 |
| 29 | Tenerife Norte Airport |  | ES | 718 |
| 30 | Barcelona International Airport |  | ES | 701 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 696 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 693 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 693 |
| 34 | Amsterdam Airport Schiphol |  | NL | 648 |
| 35 | Don Mueang International Airport |  | TH | 643 |
| 36 | Vitoria/Foronda Airport |  | ES | 639 |
| 37 | Calgary International Airport |  | CA | 632 |
| 38 | Seattle-Tacoma International Airport |  | US | 621 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 616 |
| 40 | Netaji Subhash Chandra Bose International Airport |  | IN | 607 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 560 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 393 | 21m | 244 km | 1,654.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 284 | 24m | 225 km | 1,101.8 t |
| 4 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 281 | 1h 7m | 706 km | 3,421.2 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 279 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 274 | 14m | 114 km | 537.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 260 | 1h 25m | 910 km | 4,080.0 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 259 | 28m | 304 km | 1,357.7 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 245 | 1h 10m | 770 km | 3,254.6 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 220 | 19m | 165 km | 625.8 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 214 | 26m | 275 km | 1,014.1 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 205 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 161 | 20m | 99 km | 275.8 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 155 | 27m | 215 km | 574.1 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 155 | 22m | 55 km | 147.3 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 150 | 14m | 154 km | 397.4 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 148 | 27m | 152 km | 386.8 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 147 | 31m | 369 km | 935.7 t |
| 19 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 145 | 44m | 452 km | 1,130.1 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 144 | 13m | - | - |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 140 | 18m | 144 km | 348.2 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 138 | 20m | 250 km | 596.1 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 131 | 1h 1m | 695 km | 1,570.3 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 130 | 1h 39m | 1,156 km | 2,593.5 t |
| 26 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 126 | 44m | 241 km | 523.4 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 125 | 1h 43m | 1,423 km | 3,067.7 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 122 | 12m | - | - |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 121 | 1h 52m | 1,304 km | 2,722.2 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 120 | 1h 18m | 961 km | 1,989.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N1615A |  | Sugar Land Regional Airport (KSGR) | Sugar Land Regional Airport (KSGR) | 2026-06-09 14:48 UTC | 2026-06-09 15:12 UTC | 24m |
| N563DJ |  | Flying R Airport (11UT) | Flying R Airport (11UT) | 2026-06-09 14:39 UTC | 2026-06-09 15:12 UTC | 32m |
| N772FG |  | Trenton Mercer Airport (KTTN) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-06-09 14:07 UTC | 2026-06-09 15:09 UTC | 1h 2m |
| N611MV |  | Mc Clellan Airfield (KMCC) | Hemet-Ryan Airport (KHMT) | 2026-06-09 13:40 UTC | 2026-06-09 15:08 UTC | 1h 28m |
| PREY21 | PRE | Randolph Afb Airport (KRND) | Burris Ranch Airport (2TE6) | 2026-06-09 14:42 UTC | 2026-06-09 15:08 UTC | 26m |
| CXK452 | CXK | Long Beach (Daugherty Field) Airport (KLGB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-06-09 14:30 UTC | 2026-06-09 15:05 UTC | 34m |
| BEAK31 | BEA | Anacacho Ranch Airport (0XS7) | Anacacho Ranch Airport (0XS7) | 2026-06-09 14:54 UTC | 2026-06-09 15:04 UTC | 10m |
| RNGR841 | RNG | Waldron Field Nolf Airport (KNWL) | Mustang Beach Airport (KRAS) | 2026-06-09 14:35 UTC | 2026-06-09 15:03 UTC | 28m |
| N107MW |  | Marshdale Airport (CO52) | Marshdale Airport (CO52) | 2026-06-09 12:03 UTC | 2026-06-09 15:01 UTC | 2h 57m |
| HK5100G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-06-09 14:21 UTC | 2026-06-09 15:00 UTC | 39m |
| CXK215 | CXK | Mckinney Ntl Airport (KTKI) | Mckinney Ntl Airport (KTKI) | 2026-06-09 13:47 UTC | 2026-06-09 14:59 UTC | 1h 12m |
| N733FC |  | Hanover County Municipal Airport (KOFP) | Hanover County Municipal Airport (KOFP) | 2026-06-09 14:55 UTC | 2026-06-09 14:55 UTC | 0m |
| BAT21 | BAT | Laughlin Afb Aux Nr 1 Airport (KT70) | Laughlin Afb Aux Nr 1 Airport (KT70) | 2026-06-09 14:43 UTC | 2026-06-09 14:55 UTC | 11m |
| N619LF |  | Dawson Municipal Airport (K16J) | Dawson Municipal Airport (K16J) | 2026-06-09 12:31 UTC | 2026-06-09 14:55 UTC | 2h 23m |
| CGSSC | CGS | Vancouver International Airport (CYVR) | Victoria International Airport (CYYJ) | 2026-06-09 14:25 UTC | 2026-06-09 14:54 UTC | 29m |
| EJA652 | EJA | Burke Lakefront Airport (KBKL) | Tweed/New Haven Airport (KHVN) | 2026-06-09 13:41 UTC | 2026-06-09 14:50 UTC | 1h 9m |
| DESERT3 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-06-09 14:22 UTC | 2026-06-09 14:49 UTC | 26m |
| BOX500 | BOX | Leipzig Halle Airport (EDDP) | Macau International Airport (VMMC) | 2026-06-09 04:10 UTC | 2026-06-09 14:43 UTC | 10h 33m |
| CXK237 | CXK | Lancaster Airport (KLNS) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-06-09 14:16 UTC | 2026-06-09 14:43 UTC | 26m |
| SCA18 | SCA | Scottsdale Airport (KSDL) | Scottsdale Airport (KSDL) | 2026-06-09 14:05 UTC | 2026-06-09 14:42 UTC | 37m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
