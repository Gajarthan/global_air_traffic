# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--11_17:04:50_UTC-green)

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

**Latest saved flight:** 2026-07-11 17:04:50 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-11 17:04:50 UTC

- **137,375** saved flights
- **46,338** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **137,375** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,649,847.6 tonnes** estimated CO2 emissions
- **95,643,342 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5581 |
| 2 | SkyWest Airlines | 5027 |
| 3 | EJA | 2687 |
| 4 | IndiGo | 2534 |
| 5 | American Airlines | 2155 |
| 6 | Southwest Airlines | 2068 |
| 7 | ENY | 1721 |
| 8 | Delta Air Lines | 1635 |
| 9 | Lufthansa | 1407 |
| 10 | LATAM Airlines | 1263 |
| 11 | Vueling | 1191 |
| 12 | WIF | 1190 |
| 13 | AZU | 1177 |
| 14 | LXJ | 1054 |
| 15 | AXM | 1032 |
| 16 | Swiss International | 981 |
| 17 | All Nippon Airways | 890 |
| 18 | easyJet | 889 |
| 19 | Alaska Airlines | 865 |
| 20 | QLK | 856 |
| 21 | EJU | 845 |
| 22 | VIV | 751 |
| 23 | AEE | 743 |
| 24 | Air France | 736 |
| 25 | CXK | 733 |
| 26 | Cathay Pacific | 726 |
| 27 | JetBlue | 720 |
| 28 | United Airlines | 719 |
| 29 | MXY | 714 |
| 30 | GLO | 705 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 117898 |
| 2 | 🇪🇸 ES | 9051 |
| 3 | 🇮🇳 IN | 7946 |
| 4 | 🇦🇺 AU | 7874 |
| 5 | 🇧🇷 BR | 7754 |
| 6 | 🇨🇦 CA | 7233 |
| 7 | 🇩🇪 DE | 7185 |
| 8 | 🇮🇹 IT | 7165 |
| 9 | 🇬🇧 GB | 6229 |
| 10 | 🇯🇵 JP | 5816 |
| 11 | 🇫🇷 FR | 5466 |
| 12 | 🇨🇴 CO | 4327 |
| 13 | 🇲🇽 MX | 3976 |
| 14 | 🇬🇷 GR | 3922 |
| 15 | 🇳🇴 NO | 3716 |
| 16 | 🇨🇭 CH | 3567 |
| 17 | 🇹🇷 TR | 3190 |
| 18 | 🇲🇾 MY | 2682 |
| 19 | 🇵🇱 PL | 2298 |
| 20 | 🇿🇦 ZA | 2258 |
| 21 | 🇳🇿 NZ | 2122 |
| 22 | 🇹🇭 TH | 2091 |
| 23 | 🇰🇷 KR | 1997 |
| 24 | 🇵🇭 PH | 1883 |
| 25 | 🇬🇹 GT | 1836 |
| 26 | 🇲🇦 MA | 1443 |
| 27 | 🇲🇪 ME | 1364 |
| 28 | 🇳🇱 NL | 1280 |
| 29 | 🇭🇷 HR | 1245 |
| 30 | 🇲🇴 MO | 1186 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2854 |
| 2 | Denver International Airport |  | US | 2298 |
| 3 | Tokyo International Airport |  | JP | 1897 |
| 4 | Indira Gandhi International Airport |  | IN | 1756 |
| 5 | Harry Reid International Airport |  | US | 1715 |
| 6 | Guaymaral Airport |  | CO | 1668 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1599 |
| 8 | Zurich Airport |  | CH | 1530 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1449 |
| 10 | La Aurora Airport |  | GT | 1418 |
| 11 | Frankfurt am Main International Airport |  | DE | 1363 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1314 |
| 13 | Chicago O'Hare International Airport |  | US | 1296 |
| 14 | El Dorado International Airport |  | CO | 1222 |
| 15 | Salt Lake City International Airport |  | US | 1215 |
| 16 | Macau International Airport |  | MO | 1186 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1182 |
| 18 | Capua Airport |  | IT | 1118 |
| 19 | Madrid Barajas International Airport |  | ES | 1117 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1112 |
| 21 | Congonhas Airport |  | BR | 1107 |
| 22 | Kuala Lumpur International Airport |  | MY | 1040 |
| 23 | Charlotte/Douglas International Airport |  | US | 1003 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 990 |
| 25 | Charles de Gaulle International Airport |  | FR | 979 |
| 26 | Bengaluru International Airport |  | IN | 955 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 948 |
| 28 | Malpensa International Airport |  | IT | 900 |
| 29 | Ninoy Aquino International Airport |  | PH | 876 |
| 30 | Daniel K Inouye International Airport |  | US | 845 |
| 31 | Barcelona International Airport |  | ES | 838 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 835 |
| 33 | Tenerife Norte Airport |  | ES | 812 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 806 |
| 35 | Calgary International Airport |  | CA | 797 |
| 36 | Scottsdale Airport |  | US | 789 |
| 37 | Viracopos International Airport |  | BR | 785 |
| 38 | Seattle-Tacoma International Airport |  | US | 783 |
| 39 | Vitoria/Foronda Airport |  | ES | 772 |
| 40 | Amsterdam Airport Schiphol |  | NL | 767 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 701 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 495 | 21m | 244 km | 2,084.3 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 339 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 338 | 24m | 225 km | 1,311.3 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 330 | 1h 9m | 770 km | 4,383.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 294 | 14m | 114 km | 576.6 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 256 | 26m | 275 km | 1,213.1 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 251 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 203 | 22m | 55 km | 192.9 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 189 | 26m | 215 km | 700.0 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 189 | 44m | 241 km | 785.1 t |
| 16 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 185 | 1h 46m | 1,423 km | 4,540.2 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 185 | 20m | 99 km | 316.9 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 182 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 176 | 27m | 152 km | 460.0 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 170 | 20m | 250 km | 734.3 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 169 | 31m | 369 km | 1,075.7 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 165 | 18m | 144 km | 410.4 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 164 | 30m | 49 km | 138.6 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 163 | 44m | 452 km | 1,270.3 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 160 | 1h 16m | 961 km | 2,652.1 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 159 | 1h 1m | 695 km | 1,905.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 156 | 1h 38m | 1,156 km | 3,112.1 t |
| 28 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 156 | 54m | 136 km | 365.7 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 149 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N100RV |  | Doylestown Airport (KDYL) | Doylestown Airport (KDYL) | 2026-07-11 16:31 UTC | 2026-07-11 17:04 UTC | 33m |
| N652PA |  | Purdue University Airport (KLAF) | Purdue University Airport (KLAF) | 2026-07-11 16:23 UTC | 2026-07-11 17:02 UTC | 39m |
| CSC9614 | CSC | Frankfurt am Main International Airport (EDDF) | Tunoshna Airport (UUDL) | 2026-07-11 13:45 UTC | 2026-07-11 17:01 UTC | 3h 16m |
| MDOGA | MDO | Alderney Airport (EGJA) | Jersey Airport (EGJJ) | 2026-07-11 16:35 UTC | 2026-07-11 17:01 UTC | 25m |
| N87JF |  | Villa Char Mar Airport (1FA9) | Lake Wales Municipal Airport (KX07) | 2026-07-11 16:36 UTC | 2026-07-11 16:55 UTC | 18m |
| N901BS |  | P K Airpark (K5W4) | P K Airpark (K5W4) | 2026-07-11 13:34 UTC | 2026-07-11 16:54 UTC | 3h 19m |
| A7MBK |  | Nice-Cote d'Azur Airport (LFMN) | Al Khawr Airport (OTBK) | 2026-07-11 11:32 UTC | 2026-07-11 16:54 UTC | 5h 22m |
| N605NC |  | Fremont County Airport (K1V6) | 14CO (14CO) | 2026-07-11 16:21 UTC | 2026-07-11 16:49 UTC | 27m |
| RPA4463 | Republic Airways | Des Moines International Airport (KDSM) | Philadelphia International Airport (KPHL) | 2026-07-11 14:38 UTC | 2026-07-11 16:48 UTC | 2h 9m |
| N83076 |  | Chester County G O Carlson Airport (KMQS) | Chester County G O Carlson Airport (KMQS) | 2026-07-11 16:45 UTC | 2026-07-11 16:48 UTC | 2m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-07-11 16:30 UTC | 2026-07-11 16:47 UTC | 16m |
| N500GP |  | Doylestown Airport (KDYL) | Doylestown Airport (KDYL) | 2026-07-11 16:11 UTC | 2026-07-11 16:42 UTC | 30m |
| N944VB |  | Hampton Roads Executive Airport (KPVG) | Hampton Roads Executive Airport (KPVG) | 2026-07-11 16:05 UTC | 2026-07-11 16:37 UTC | 31m |
| FWFK | FWF | Vauxhall Airport (CEN6) | Brooks Regional (CYBP) | 2026-07-11 15:08 UTC | 2026-07-11 16:31 UTC | 1h 23m |
| N1990G |  | AR55 (AR55) | Cambridge-Dorchester Regional Airport (KCGE) | 2026-07-11 14:26 UTC | 2026-07-11 16:29 UTC | 2h 2m |
| EJA360 | EJA | Atlantic Municipal Airport (KAIO) | Lee County Airport (K0VG) | 2026-07-11 14:59 UTC | 2026-07-11 16:28 UTC | 1h 28m |
| N888KG |  | Provo Municipal Airport (KPVU) | Cokeville Municipal Airport (KU06) | 2026-07-11 16:08 UTC | 2026-07-11 16:27 UTC | 19m |
| AAH552 | AAH | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 2026-07-11 16:06 UTC | 2026-07-11 16:26 UTC | 20m |
| RYR88TZ | Ryanair | Pescara International Airport (LIBP) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-07-11 14:56 UTC | 2026-07-11 16:26 UTC | 1h 29m |
| SPSDW | SPS | Lubin Airport (EPLU) | Lubin Airport (EPLU) | 2026-07-11 15:33 UTC | 2026-07-11 16:26 UTC | 52m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
