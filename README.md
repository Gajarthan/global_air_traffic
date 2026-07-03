# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--03_21:50:02_UTC-green)

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

**Latest saved flight:** 2026-07-03 21:50:02 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-03 21:50:02 UTC

- **128,303** saved flights
- **43,739** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **128,303** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,547,694.9 tonnes** estimated CO2 emissions
- **89,721,445 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5214 |
| 2 | SkyWest Airlines | 4761 |
| 3 | EJA | 2520 |
| 4 | IndiGo | 2413 |
| 5 | American Airlines | 1979 |
| 6 | Southwest Airlines | 1929 |
| 7 | ENY | 1610 |
| 8 | Delta Air Lines | 1530 |
| 9 | Lufthansa | 1355 |
| 10 | LATAM Airlines | 1168 |
| 11 | Vueling | 1134 |
| 12 | WIF | 1127 |
| 13 | AZU | 1085 |
| 14 | AXM | 1002 |
| 15 | LXJ | 997 |
| 16 | Swiss International | 889 |
| 17 | All Nippon Airways | 853 |
| 18 | Alaska Airlines | 830 |
| 19 | easyJet | 817 |
| 20 | QLK | 803 |
| 21 | EJU | 795 |
| 22 | Cathay Pacific | 708 |
| 23 | VIV | 706 |
| 24 | AEE | 701 |
| 25 | Air France | 699 |
| 26 | CXK | 692 |
| 27 | United Airlines | 683 |
| 28 | MXY | 670 |
| 29 | JetBlue | 656 |
| 30 | GLO | 647 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 109924 |
| 2 | 🇪🇸 ES | 8533 |
| 3 | 🇮🇳 IN | 7560 |
| 4 | 🇦🇺 AU | 7451 |
| 5 | 🇧🇷 BR | 7178 |
| 6 | 🇨🇦 CA | 6760 |
| 7 | 🇩🇪 DE | 6747 |
| 8 | 🇮🇹 IT | 6724 |
| 9 | 🇬🇧 GB | 5675 |
| 10 | 🇯🇵 JP | 5567 |
| 11 | 🇫🇷 FR | 5080 |
| 12 | 🇨🇴 CO | 4072 |
| 13 | 🇲🇽 MX | 3740 |
| 14 | 🇬🇷 GR | 3645 |
| 15 | 🇳🇴 NO | 3501 |
| 16 | 🇨🇭 CH | 3258 |
| 17 | 🇹🇷 TR | 2752 |
| 18 | 🇲🇾 MY | 2597 |
| 19 | 🇿🇦 ZA | 2126 |
| 20 | 🇵🇱 PL | 2097 |
| 21 | 🇳🇿 NZ | 2063 |
| 22 | 🇹🇭 TH | 1990 |
| 23 | 🇰🇷 KR | 1958 |
| 24 | 🇵🇭 PH | 1804 |
| 25 | 🇬🇹 GT | 1761 |
| 26 | 🇲🇦 MA | 1375 |
| 27 | 🇲🇪 ME | 1271 |
| 28 | 🇳🇱 NL | 1207 |
| 29 | 🇲🇴 MO | 1184 |
| 30 | 🇭🇷 HR | 1109 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2681 |
| 2 | Denver International Airport |  | US | 2179 |
| 3 | Tokyo International Airport |  | JP | 1835 |
| 4 | Indira Gandhi International Airport |  | IN | 1664 |
| 5 | Harry Reid International Airport |  | US | 1603 |
| 6 | Guaymaral Airport |  | CO | 1559 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1520 |
| 8 | Zurich Airport |  | CH | 1407 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1368 |
| 10 | La Aurora Airport |  | GT | 1361 |
| 11 | Frankfurt am Main International Airport |  | DE | 1312 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1250 |
| 13 | Chicago O'Hare International Airport |  | US | 1236 |
| 14 | Macau International Airport |  | MO | 1184 |
| 15 | El Dorado International Airport |  | CO | 1172 |
| 16 | Salt Lake City International Airport |  | US | 1143 |
| 17 | Capua Airport |  | IT | 1067 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1060 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1057 |
| 20 | Madrid Barajas International Airport |  | ES | 1048 |
| 21 | Kuala Lumpur International Airport |  | MY | 1010 |
| 22 | Congonhas Airport |  | BR | 1008 |
| 23 | Charlotte/Douglas International Airport |  | US | 966 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 935 |
| 25 | Charles de Gaulle International Airport |  | FR | 932 |
| 26 | Bengaluru International Airport |  | IN | 916 |
| 27 | Malpensa International Airport |  | IT | 873 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 862 |
| 29 | Ninoy Aquino International Airport |  | PH | 836 |
| 30 | Daniel K Inouye International Airport |  | US | 813 |
| 31 | Barcelona International Airport |  | ES | 798 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 782 |
| 33 | Tenerife Norte Airport |  | ES | 781 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 756 |
| 35 | Calgary International Airport |  | CA | 752 |
| 36 | Seattle-Tacoma International Airport |  | US | 742 |
| 37 | Scottsdale Airport |  | US | 742 |
| 38 | Vitoria/Foronda Airport |  | ES | 739 |
| 39 | Viracopos International Airport |  | BR | 732 |
| 40 | Amsterdam Airport Schiphol |  | NL | 728 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 652 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 466 | 21m | 244 km | 1,962.2 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 328 | 24m | 225 km | 1,272.5 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 323 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 309 | 1h 10m | 770 km | 4,104.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 244 | 26m | 275 km | 1,156.2 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 236 | 31m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 189 | 22m | 55 km | 179.6 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 181 | 26m | 215 km | 670.3 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 179 | 44m | 241 km | 743.5 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 179 | 20m | 99 km | 306.6 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 177 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 172 | 27m | 152 km | 449.5 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 166 | 1h 45m | 1,423 km | 4,073.9 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 162 | 31m | 369 km | 1,031.2 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 158 | 18m | 144 km | 393.0 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 157 | 20m | 250 km | 678.1 t |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 156 | 44m | 452 km | 1,215.8 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 25 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 154 | 30m | 49 km | 130.2 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 151 | 1h 1m | 695 km | 1,810.0 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 149 | 1h 17m | 961 km | 2,469.8 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 147 | 1h 38m | 1,156 km | 2,932.6 t |
| 29 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 146 | 54m | 136 km | 342.3 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 142 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N65872 |  | Camarillo Airport (KCMA) | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | 2026-07-03 21:02 UTC | 2026-07-03 21:50 UTC | 47m |
| N810SC |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-07-03 21:34 UTC | 2026-07-03 21:48 UTC | 13m |
| N527CH |  | Merrill Field (PAMR) | King Salmon Airport (PAKN) | 2026-07-03 18:03 UTC | 2026-07-03 21:46 UTC | 3h 42m |
| N3AS |  | Scottsdale Airport (KSDL) | Rogers Field (KO05) | 2026-07-03 20:16 UTC | 2026-07-03 21:44 UTC | 1h 28m |
| DLH8P | Lufthansa | Munich International Airport (EDDM) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-03 13:50 UTC | 2026-07-03 21:40 UTC | 7h 49m |
| TKR107 | TKR | Animas Air Park (K00C) | Animas Air Park (K00C) | 2026-07-03 21:07 UTC | 2026-07-03 21:37 UTC | 30m |
| JIA5427 | JIA | Detroit Metro Wayne County Airport (KDTW) | Philadelphia International Airport (KPHL) | 2026-07-03 20:26 UTC | 2026-07-03 21:36 UTC | 1h 9m |
| N197RD |  | Santa Ynez/Kunkle Field (KIZA) | Kern Valley Airport (KL05) | 2026-07-03 20:43 UTC | 2026-07-03 21:35 UTC | 51m |
| TGKBG | TGK | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 2026-07-03 21:08 UTC | 2026-07-03 21:30 UTC | 22m |
| N234GC |  | French Valley Airport (KF70) | French Valley Airport (KF70) | 2026-07-03 21:21 UTC | 2026-07-03 21:28 UTC | 7m |
| N70075 |  | KU42 (KU42) | Wendover Airport (KENV) | 2026-07-03 20:42 UTC | 2026-07-03 21:28 UTC | 45m |
| CXK685 | CXK | Sugar Land Regional Airport (KSGR) | Sugar Land Regional Airport (KSGR) | 2026-07-03 20:24 UTC | 2026-07-03 21:28 UTC | 1h 3m |
| FFL1434 | FFL | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-07-03 21:02 UTC | 2026-07-03 21:26 UTC | 23m |
| BGR44 | BGR | Tolovana Hot Springs Airport (83AK) | Manley Hot Springs Airport (PAML) | 2026-07-03 21:07 UTC | 2026-07-03 21:24 UTC | 17m |
| TGMRP | TGM | La Aurora Airport (MGGT) | Bananera Airport (MGBN) | 2026-07-03 20:52 UTC | 2026-07-03 21:24 UTC | 31m |
| N408CA |  | Montgomery-Gibbs Executive Airport (KMYF) | Gillespie Field (KSEE) | 2026-07-03 20:50 UTC | 2026-07-03 21:21 UTC | 30m |
| LVN | LVN | Shute Harbour/Whitsunday Airport (YSHR) | Whitsunday Island Airport (YWHI) | 2026-07-03 21:09 UTC | 2026-07-03 21:21 UTC | 11m |
| N249FS |  | John Wayne/Orange County Airport (KSNA) | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | 2026-07-03 19:49 UTC | 2026-07-03 21:20 UTC | 1h 30m |
| AAL433 | American Airlines | San Diego International Airport (KSAN) | Philadelphia International Airport (KPHL) | 2026-07-03 16:45 UTC | 2026-07-03 21:18 UTC | 4h 33m |
| N269ME |  | Daniel K Inouye International Airport (PHNL) | Kawaihapai Airfield (PHDH) | 2026-07-03 20:50 UTC | 2026-07-03 21:17 UTC | 26m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
