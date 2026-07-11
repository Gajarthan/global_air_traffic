# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--11_17:57:13_UTC-green)

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

**Latest saved flight:** 2026-07-11 17:57:13 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-11 17:57:13 UTC

- **137,590** saved flights
- **46,414** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **137,590** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,652,095.6 tonnes** estimated CO2 emissions
- **95,773,660 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5588 |
| 2 | SkyWest Airlines | 5043 |
| 3 | EJA | 2697 |
| 4 | IndiGo | 2535 |
| 5 | American Airlines | 2159 |
| 6 | Southwest Airlines | 2074 |
| 7 | ENY | 1723 |
| 8 | Delta Air Lines | 1635 |
| 9 | Lufthansa | 1408 |
| 10 | LATAM Airlines | 1265 |
| 11 | Vueling | 1191 |
| 12 | WIF | 1190 |
| 13 | AZU | 1180 |
| 14 | LXJ | 1055 |
| 15 | AXM | 1032 |
| 16 | Swiss International | 982 |
| 17 | All Nippon Airways | 890 |
| 18 | easyJet | 890 |
| 19 | Alaska Airlines | 866 |
| 20 | QLK | 856 |
| 21 | EJU | 846 |
| 22 | VIV | 752 |
| 23 | AEE | 745 |
| 24 | Air France | 737 |
| 25 | CXK | 734 |
| 26 | Cathay Pacific | 726 |
| 27 | JetBlue | 720 |
| 28 | United Airlines | 720 |
| 29 | MXY | 715 |
| 30 | GLO | 706 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 118132 |
| 2 | 🇪🇸 ES | 9059 |
| 3 | 🇮🇳 IN | 7947 |
| 4 | 🇦🇺 AU | 7874 |
| 5 | 🇧🇷 BR | 7768 |
| 6 | 🇨🇦 CA | 7245 |
| 7 | 🇩🇪 DE | 7193 |
| 8 | 🇮🇹 IT | 7172 |
| 9 | 🇬🇧 GB | 6238 |
| 10 | 🇯🇵 JP | 5816 |
| 11 | 🇫🇷 FR | 5475 |
| 12 | 🇨🇴 CO | 4345 |
| 13 | 🇲🇽 MX | 3982 |
| 14 | 🇬🇷 GR | 3926 |
| 15 | 🇳🇴 NO | 3718 |
| 16 | 🇨🇭 CH | 3569 |
| 17 | 🇹🇷 TR | 3198 |
| 18 | 🇲🇾 MY | 2682 |
| 19 | 🇵🇱 PL | 2308 |
| 20 | 🇿🇦 ZA | 2258 |
| 21 | 🇳🇿 NZ | 2122 |
| 22 | 🇹🇭 TH | 2092 |
| 23 | 🇰🇷 KR | 1997 |
| 24 | 🇵🇭 PH | 1883 |
| 25 | 🇬🇹 GT | 1838 |
| 26 | 🇲🇦 MA | 1448 |
| 27 | 🇲🇪 ME | 1366 |
| 28 | 🇳🇱 NL | 1281 |
| 29 | 🇭🇷 HR | 1247 |
| 30 | 🇲🇴 MO | 1186 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2856 |
| 2 | Denver International Airport |  | US | 2299 |
| 3 | Tokyo International Airport |  | JP | 1897 |
| 4 | Indira Gandhi International Airport |  | IN | 1757 |
| 5 | Harry Reid International Airport |  | US | 1718 |
| 6 | Guaymaral Airport |  | CO | 1676 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1599 |
| 8 | Zurich Airport |  | CH | 1531 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1451 |
| 10 | La Aurora Airport |  | GT | 1420 |
| 11 | Frankfurt am Main International Airport |  | DE | 1364 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1316 |
| 13 | Chicago O'Hare International Airport |  | US | 1300 |
| 14 | El Dorado International Airport |  | CO | 1227 |
| 15 | Salt Lake City International Airport |  | US | 1221 |
| 16 | Macau International Airport |  | MO | 1186 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1184 |
| 18 | Capua Airport |  | IT | 1122 |
| 19 | Madrid Barajas International Airport |  | ES | 1118 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1113 |
| 21 | Congonhas Airport |  | BR | 1109 |
| 22 | Kuala Lumpur International Airport |  | MY | 1040 |
| 23 | Charlotte/Douglas International Airport |  | US | 1004 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 990 |
| 25 | Charles de Gaulle International Airport |  | FR | 980 |
| 26 | Bengaluru International Airport |  | IN | 955 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 949 |
| 28 | Malpensa International Airport |  | IT | 900 |
| 29 | Ninoy Aquino International Airport |  | PH | 876 |
| 30 | Daniel K Inouye International Airport |  | US | 846 |
| 31 | Barcelona International Airport |  | ES | 839 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 836 |
| 33 | Tenerife Norte Airport |  | ES | 812 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 807 |
| 35 | Calgary International Airport |  | CA | 798 |
| 36 | Scottsdale Airport |  | US | 789 |
| 37 | Viracopos International Airport |  | BR | 786 |
| 38 | Seattle-Tacoma International Airport |  | US | 784 |
| 39 | Vitoria/Foronda Airport |  | ES | 772 |
| 40 | Amsterdam Airport Schiphol |  | NL | 767 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 705 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 496 | 21m | 244 km | 2,088.5 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 340 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 338 | 24m | 225 km | 1,311.3 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 330 | 1h 9m | 770 km | 4,383.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 296 | 14m | 114 km | 580.6 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 256 | 26m | 275 km | 1,213.1 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 251 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 204 | 22m | 55 km | 193.9 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 189 | 26m | 215 km | 700.0 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 189 | 44m | 241 km | 785.1 t |
| 16 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 186 | 1h 46m | 1,423 km | 4,564.7 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 185 | 20m | 99 km | 316.9 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 182 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 176 | 27m | 152 km | 460.0 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 171 | 30m | 49 km | 144.5 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 170 | 20m | 250 km | 734.3 t |
| 22 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 169 | 31m | 369 km | 1,075.7 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 165 | 18m | 144 km | 410.4 t |
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
| CFR72 | CFR | Hemet-Ryan Airport (KHMT) | Hemet-Ryan Airport (KHMT) | 2026-07-11 17:25 UTC | 2026-07-11 17:57 UTC | 31m |
| CFR608 | CFR | Chino Airport (KCNO) | Corona Municipal Airport (KAJO) | 2026-07-11 17:33 UTC | 2026-07-11 17:55 UTC | 21m |
| N90HX |  | Fremont County Airport (K1V6) | Fremont County Airport (K1V6) | 2026-07-11 17:32 UTC | 2026-07-11 17:44 UTC | 12m |
| N955DQ |  | Dubuque Regional Airport (KDBQ) | Manchester Municipal Airport (KC27) | 2026-07-11 17:14 UTC | 2026-07-11 17:44 UTC | 29m |
| N2951F |  | Palatka Municipal/Lt Kay Larkin Field (K28J) | Palatka Municipal/Lt Kay Larkin Field (K28J) | 2026-07-11 16:13 UTC | 2026-07-11 17:43 UTC | 1h 29m |
| AAL2764 | American Airlines | Philadelphia International Airport (KPHL) | Philadelphia International Airport (KPHL) | 2026-07-11 17:28 UTC | 2026-07-11 17:43 UTC | 14m |
| CGXQZ | CGX | London / Chapeskie Field (CLC2) | CHD4 (CHD4) | 2026-07-11 17:07 UTC | 2026-07-11 17:42 UTC | 35m |
| N935MC |  | Merritt Island Airport (KCOI) | Orlando Executive Airport (KORL) | 2026-07-11 17:23 UTC | 2026-07-11 17:41 UTC | 18m |
| N14HX |  | Blanding Municipal Airport (KBDG) | Blanding Municipal Airport (KBDG) | 2026-07-11 17:04 UTC | 2026-07-11 17:39 UTC | 35m |
| N5264K |  | Kent Fort Manor Airport (7MD8) | Kent Fort Manor Airport (7MD8) | 2026-07-11 17:35 UTC | 2026-07-11 17:38 UTC | 2m |
| N5636R |  | Ogden-Hinckley Airport (KOGD) | Wendover Airport (KENV) | 2026-07-11 16:43 UTC | 2026-07-11 17:35 UTC | 52m |
| N456V |  | NV13 (NV13) | Yerington Municipal Airport (KO43) | 2026-07-11 17:23 UTC | 2026-07-11 17:35 UTC | 11m |
| N281CE |  | Laconia Municipal Airport (KLCI) | Trenton Mercer Airport (KTTN) | 2026-07-11 16:41 UTC | 2026-07-11 17:34 UTC | 53m |
| N229HL |  | IS62 (IS62) | IS62 (IS62) | 2026-07-11 16:02 UTC | 2026-07-11 17:34 UTC | 1h 32m |
| T815 |  | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-07-11 17:00 UTC | 2026-07-11 17:32 UTC | 32m |
| T825 |  | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-07-11 17:00 UTC | 2026-07-11 17:32 UTC | 32m |
| DAH2028 | DAH | Vienna International Airport (LOWW) | DAAX (DAAX) | 2026-07-11 15:20 UTC | 2026-07-11 17:30 UTC | 2h 10m |
| N216SP |  | Ockel Farms Airport (DE23) | Lee Airport (KANP) | 2026-07-11 16:47 UTC | 2026-07-11 17:29 UTC | 42m |
| N428CF |  | Fort Worth Meacham International Airport (KFTW) | 5TX4 (5TX4) | 2026-07-11 17:18 UTC | 2026-07-11 17:28 UTC | 10m |
| N744ND |  | Brackett Field (KPOC) | Brackett Field (KPOC) | 2026-07-11 16:50 UTC | 2026-07-11 17:23 UTC | 32m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
