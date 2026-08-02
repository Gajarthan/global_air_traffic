# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--02_13:54:38_UTC-green)

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

**Latest saved flight:** 2026-08-02 13:54:38 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-02 13:54:38 UTC

- **166,559** saved flights
- **54,553** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **166,559** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,006,222.1 tonnes** estimated CO2 emissions
- **116,302,732 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6650 |
| 2 | SkyWest Airlines | 6059 |
| 3 | EJA | 3294 |
| 4 | IndiGo | 2940 |
| 5 | American Airlines | 2624 |
| 6 | Southwest Airlines | 2616 |
| 7 | ENY | 2068 |
| 8 | Delta Air Lines | 1987 |
| 9 | LATAM Airlines | 1549 |
| 10 | Lufthansa | 1541 |
| 11 | AZU | 1465 |
| 12 | WIF | 1394 |
| 13 | Vueling | 1375 |
| 14 | LXJ | 1293 |
| 15 | AXM | 1154 |
| 16 | Swiss International | 1144 |
| 17 | easyJet | 1108 |
| 18 | Alaska Airlines | 1026 |
| 19 | EJU | 1024 |
| 20 | QLK | 1020 |
| 21 | All Nippon Airways | 1017 |
| 22 | VIV | 916 |
| 23 | Cathay Pacific | 888 |
| 24 | CXK | 888 |
| 25 | United Airlines | 878 |
| 26 | AEE | 874 |
| 27 | GLO | 871 |
| 28 | Air France | 860 |
| 29 | MXY | 858 |
| 30 | JetBlue | 840 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 143506 |
| 2 | 🇪🇸 ES | 10662 |
| 3 | 🇧🇷 BR | 9480 |
| 4 | 🇦🇺 AU | 9342 |
| 5 | 🇮🇳 IN | 9219 |
| 6 | 🇨🇦 CA | 9027 |
| 7 | 🇮🇹 IT | 8615 |
| 8 | 🇩🇪 DE | 8326 |
| 9 | 🇬🇧 GB | 7712 |
| 10 | 🇯🇵 JP | 6740 |
| 11 | 🇫🇷 FR | 6610 |
| 12 | 🇨🇴 CO | 5987 |
| 13 | 🇬🇷 GR | 4816 |
| 14 | 🇲🇽 MX | 4760 |
| 15 | 🇨🇭 CH | 4396 |
| 16 | 🇳🇴 NO | 4363 |
| 17 | 🇹🇷 TR | 4021 |
| 18 | 🇲🇾 MY | 3007 |
| 19 | 🇵🇱 PL | 2816 |
| 20 | 🇿🇦 ZA | 2713 |
| 21 | 🇳🇿 NZ | 2430 |
| 22 | 🇹🇭 TH | 2422 |
| 23 | 🇵🇭 PH | 2211 |
| 24 | 🇰🇷 KR | 2146 |
| 25 | 🇬🇹 GT | 2141 |
| 26 | 🇲🇦 MA | 1680 |
| 27 | 🇭🇷 HR | 1587 |
| 28 | 🇲🇪 ME | 1549 |
| 29 | 🇳🇱 NL | 1515 |
| 30 | 🇲🇴 MO | 1423 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3400 |
| 2 | Denver International Airport |  | US | 2766 |
| 3 | Tokyo International Airport |  | JP | 2117 |
| 4 | Guaymaral Airport |  | CO | 2084 |
| 5 | Indira Gandhi International Airport |  | IN | 2042 |
| 6 | Harry Reid International Airport |  | US | 2005 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1831 |
| 8 | Zurich Airport |  | CH | 1778 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1747 |
| 10 | La Aurora Airport |  | GT | 1658 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1539 |
| 12 | El Dorado International Airport |  | CO | 1521 |
| 13 | Frankfurt am Main International Airport |  | DE | 1504 |
| 14 | Chicago O'Hare International Airport |  | US | 1502 |
| 15 | Salt Lake City International Airport |  | US | 1490 |
| 16 | Macau International Airport |  | MO | 1423 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1386 |
| 18 | Congonhas Airport |  | BR | 1370 |
| 19 | Madrid Barajas International Airport |  | ES | 1312 |
| 20 | Capua Airport |  | IT | 1300 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1264 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1175 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1175 |
| 24 | Charlotte/Douglas International Airport |  | US | 1163 |
| 25 | Charles de Gaulle International Airport |  | FR | 1137 |
| 26 | Kuala Lumpur International Airport |  | MY | 1136 |
| 27 | Malpensa International Airport |  | IT | 1118 |
| 28 | Bengaluru International Airport |  | IN | 1091 |
| 29 | Ninoy Aquino International Airport |  | PH | 1039 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1024 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1019 |
| 32 | Barcelona International Airport |  | ES | 984 |
| 33 | Daniel K Inouye International Airport |  | US | 971 |
| 34 | Seattle-Tacoma International Airport |  | US | 965 |
| 35 | Viracopos International Airport |  | BR | 949 |
| 36 | Calgary International Airport |  | CA | 944 |
| 37 | Tenerife Norte Airport |  | ES | 928 |
| 38 | Oslo Gardermoen Airport |  | NO | 926 |
| 39 | Scottsdale Airport |  | US | 926 |
| 40 | Reno/Tahoe International Airport |  | US | 917 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 868 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 606 | 21m | 244 km | 2,551.7 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 400 | 24m | 225 km | 1,551.8 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 399 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 381 | 1h 9m | 770 km | 5,061.3 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 313 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 286 | 27m | 275 km | 1,355.2 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 253 | 22m | 55 km | 240.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 245 | 19m | 165 km | 696.9 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 242 | 44m | 241 km | 1,005.2 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 229 | 1h 47m | 1,423 km | 5,620.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 220 | 20m | 250 km | 950.3 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 216 | 26m | 215 km | 800.0 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 210 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 210 | 20m | 99 km | 359.7 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 210 | 31m | 49 km | 177.5 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 198 | 1h 15m | 961 km | 3,282.0 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 197 | 19m | 144 km | 490.0 t |
| 23 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 196 | 28m | 152 km | 512.2 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 194 | 31m | 369 km | 1,234.9 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 189 | 50m | 556 km | 1,811.7 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 189 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 186 | 1h 38m | 1,156 km | 3,710.6 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 182 | 1h 1m | 695 km | 2,181.6 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 182 | 44m | 452 km | 1,418.4 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 180 | 24m | 218 km | 678.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N718DS |  | K1J6 (K1J6) | Ormond Beach Municipal Airport (KOMN) | 2026-08-02 13:08 UTC | 2026-08-02 13:54 UTC | 46m |
| A7GQD |  | Al Khawr Airport (OTBK) | Persian Gulf International Airport (OIBP) | 2026-08-02 12:04 UTC | 2026-08-02 13:49 UTC | 1h 45m |
| DKH1660 | DKH | Brussels Airport (EBBR) | Ukhta Airport (UUYH) | 2026-08-02 10:33 UTC | 2026-08-02 13:48 UTC | 3h 15m |
| N833CL |  | Hanover County Municipal Airport (KOFP) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-08-02 12:30 UTC | 2026-08-02 13:45 UTC | 1h 15m |
| FHIBY | FHI | St Florentin Cheu Airport (LFGP) | St Florentin Cheu Airport (LFGP) | 2026-08-02 13:14 UTC | 2026-08-02 13:44 UTC | 29m |
| AAL1169 | American Airlines | Toronto Pearson International Airport (CYYZ) | Dallas-Fort Worth International Airport (KDFW) | 2026-08-02 11:03 UTC | 2026-08-02 13:44 UTC | 2h 40m |
| CKS235 | CKS | Ted Stevens Anchorage International Airport (PANC) | Valleyview Airport (CEL5) | 2026-08-02 11:23 UTC | 2026-08-02 13:43 UTC | 2h 19m |
| S5DOT |  | Novo Mesto Airport (LJNM) | Novo Mesto Airport (LJNM) | 2026-08-02 13:29 UTC | 2026-08-02 13:42 UTC | 13m |
| N5327J |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-08-02 13:14 UTC | 2026-08-02 13:41 UTC | 27m |
| CXK447 | CXK | Denton Enterprise Airport (KDTO) | Denton Enterprise Airport (KDTO) | 2026-08-02 13:34 UTC | 2026-08-02 13:39 UTC | 4m |
| EIN16C | Aer Lingus | London Heathrow Airport (EGLL) | Dublin Airport (EIDW) | 2026-08-02 12:44 UTC | 2026-08-02 13:39 UTC | 54m |
| N5347L |  | Animas Air Park (K00C) | Blanding Municipal Airport (KBDG) | 2026-08-02 12:58 UTC | 2026-08-02 13:36 UTC | 37m |
| N2329D |  | Henderson Executive Airport (KHND) | Henderson Executive Airport (KHND) | 2026-08-02 13:34 UTC | 2026-08-02 13:35 UTC | 0m |
| ASI142 | ASI | Georgetown Executive Airport (KGTU) | Draughon-Miller Central Texas Regional Airport (KTPL) | 2026-08-02 13:08 UTC | 2026-08-02 13:34 UTC | 25m |
| UAE380 | Emirates | Dubai International Airport (OMDB) | Macau International Airport (VMMC) | 2026-08-02 06:46 UTC | 2026-08-02 13:28 UTC | 6h 42m |
| SRG853 | SRG | Oban Airport (EGEO) | Glasgow International Airport (EGPF) | 2026-08-02 13:11 UTC | 2026-08-02 13:28 UTC | 16m |
| TCF652 | TCF | Melbourne Orlando International Airport (KMLB) | Paxton Airport (90FL) | 2026-08-02 12:49 UTC | 2026-08-02 13:27 UTC | 38m |
| GYPDN | GYP | RAF Rufforth (EG64) | EGNU (EGNU) | 2026-08-02 13:03 UTC | 2026-08-02 13:27 UTC | 24m |
| AWH93C | AWH | Brussels Airport (EBBR) | Kiel-Holtenau Airport (EDHK) | 2026-08-02 12:13 UTC | 2026-08-02 13:27 UTC | 1h 13m |
| 00000000 |  | Coleman A Young Municipal Airport (KDET) | Kalkaska City Airport (KY89) | 2026-08-02 12:57 UTC | 2026-08-02 13:27 UTC | 29m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
