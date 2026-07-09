# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--09_23:07:13_UTC-green)

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

**Latest saved flight:** 2026-07-09 23:07:13 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-09 23:07:13 UTC

- **135,080** saved flights
- **45,694** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **135,080** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,625,775.6 tonnes** estimated CO2 emissions
- **94,247,863 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5473 |
| 2 | SkyWest Airlines | 4974 |
| 3 | EJA | 2644 |
| 4 | IndiGo | 2498 |
| 5 | American Airlines | 2128 |
| 6 | Southwest Airlines | 2034 |
| 7 | ENY | 1697 |
| 8 | Delta Air Lines | 1614 |
| 9 | Lufthansa | 1388 |
| 10 | LATAM Airlines | 1240 |
| 11 | Vueling | 1178 |
| 12 | WIF | 1174 |
| 13 | AZU | 1155 |
| 14 | LXJ | 1040 |
| 15 | AXM | 1021 |
| 16 | Swiss International | 956 |
| 17 | All Nippon Airways | 878 |
| 18 | easyJet | 876 |
| 19 | Alaska Airlines | 858 |
| 20 | QLK | 842 |
| 21 | EJU | 831 |
| 22 | VIV | 743 |
| 23 | AEE | 733 |
| 24 | CXK | 728 |
| 25 | Cathay Pacific | 723 |
| 26 | Air France | 722 |
| 27 | United Airlines | 714 |
| 28 | JetBlue | 712 |
| 29 | MXY | 702 |
| 30 | GLO | 688 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 116039 |
| 2 | 🇪🇸 ES | 8939 |
| 3 | 🇮🇳 IN | 7837 |
| 4 | 🇦🇺 AU | 7776 |
| 5 | 🇧🇷 BR | 7614 |
| 6 | 🇨🇦 CA | 7154 |
| 7 | 🇩🇪 DE | 7027 |
| 8 | 🇮🇹 IT | 7004 |
| 9 | 🇬🇧 GB | 6072 |
| 10 | 🇯🇵 JP | 5755 |
| 11 | 🇫🇷 FR | 5360 |
| 12 | 🇨🇴 CO | 4243 |
| 13 | 🇲🇽 MX | 3934 |
| 14 | 🇬🇷 GR | 3849 |
| 15 | 🇳🇴 NO | 3659 |
| 16 | 🇨🇭 CH | 3486 |
| 17 | 🇹🇷 TR | 3078 |
| 18 | 🇲🇾 MY | 2651 |
| 19 | 🇵🇱 PL | 2229 |
| 20 | 🇿🇦 ZA | 2217 |
| 21 | 🇳🇿 NZ | 2111 |
| 22 | 🇹🇭 TH | 2064 |
| 23 | 🇰🇷 KR | 1984 |
| 24 | 🇵🇭 PH | 1854 |
| 25 | 🇬🇹 GT | 1827 |
| 26 | 🇲🇦 MA | 1428 |
| 27 | 🇲🇪 ME | 1342 |
| 28 | 🇳🇱 NL | 1260 |
| 29 | 🇭🇷 HR | 1201 |
| 30 | 🇲🇴 MO | 1186 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2813 |
| 2 | Denver International Airport |  | US | 2277 |
| 3 | Tokyo International Airport |  | JP | 1878 |
| 4 | Indira Gandhi International Airport |  | IN | 1733 |
| 5 | Harry Reid International Airport |  | US | 1689 |
| 6 | Guaymaral Airport |  | CO | 1647 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1579 |
| 8 | Zurich Airport |  | CH | 1499 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1435 |
| 10 | La Aurora Airport |  | GT | 1412 |
| 11 | Frankfurt am Main International Airport |  | DE | 1343 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1299 |
| 13 | Chicago O'Hare International Airport |  | US | 1285 |
| 14 | El Dorado International Airport |  | CO | 1204 |
| 15 | Salt Lake City International Airport |  | US | 1201 |
| 16 | Macau International Airport |  | MO | 1186 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1170 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1103 |
| 19 | Madrid Barajas International Airport |  | ES | 1102 |
| 20 | Capua Airport |  | IT | 1102 |
| 21 | Congonhas Airport |  | BR | 1080 |
| 22 | Kuala Lumpur International Airport |  | MY | 1030 |
| 23 | Charlotte/Douglas International Airport |  | US | 995 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 975 |
| 25 | Charles de Gaulle International Airport |  | FR | 964 |
| 26 | Bengaluru International Airport |  | IN | 944 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 927 |
| 28 | Malpensa International Airport |  | IT | 889 |
| 29 | Ninoy Aquino International Airport |  | PH | 863 |
| 30 | Daniel K Inouye International Airport |  | US | 838 |
| 31 | Barcelona International Airport |  | ES | 829 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 826 |
| 33 | Tenerife Norte Airport |  | ES | 807 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 793 |
| 35 | Calgary International Airport |  | CA | 786 |
| 36 | Seattle-Tacoma International Airport |  | US | 773 |
| 37 | Scottsdale Airport |  | US | 773 |
| 38 | Viracopos International Airport |  | BR | 771 |
| 39 | Vitoria/Foronda Airport |  | ES | 761 |
| 40 | Amsterdam Airport Schiphol |  | NL | 757 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 693 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 489 | 21m | 244 km | 2,059.0 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 338 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 333 | 24m | 225 km | 1,291.9 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 324 | 1h 10m | 770 km | 4,304.1 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 288 | 14m | 114 km | 564.9 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 251 | 26m | 275 km | 1,189.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 244 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 198 | 22m | 55 km | 188.2 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 188 | 44m | 241 km | 780.9 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 187 | 26m | 215 km | 692.6 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 185 | 20m | 99 km | 316.9 t |
| 17 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 182 | 1h 46m | 1,423 km | 4,466.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 180 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 175 | 27m | 152 km | 457.3 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 166 | 31m | 369 km | 1,056.6 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 163 | 20m | 250 km | 704.1 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 163 | 18m | 144 km | 405.5 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 162 | 30m | 49 km | 136.9 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 160 | 44m | 452 km | 1,247.0 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 159 | 1h 16m | 961 km | 2,635.5 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 157 | 1h 1m | 695 km | 1,882.0 t |
| 27 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 156 | 54m | 136 km | 365.7 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 154 | 1h 38m | 1,156 km | 3,072.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 148 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N1455T |  | Seattle Paine Field International Airport (KPAE) | Boeing Field/King County International Airport (KBFI) | 2026-07-09 22:49 UTC | 2026-07-09 23:07 UTC | 18m |
| N653PA |  | Purdue University Airport (KLAF) | Purdue University Airport (KLAF) | 2026-07-09 22:03 UTC | 2026-07-09 23:03 UTC | 1h 0m |
| ABY195 | ABY | Sharjah International Airport (OMSJ) | Sirri Island Airport (OIBS) | 2026-07-09 08:57 UTC | 2026-07-09 23:02 UTC | 14h 4m |
| N240TS |  | Logan-Cache Airport (KLGU) | Preston Airport (KU10) | 2026-07-09 22:33 UTC | 2026-07-09 22:59 UTC | 26m |
|  |  | Litchfield Municipal Airport (KLJF) | Litchfield Municipal Airport (KLJF) | 2026-07-09 22:58 UTC | 2026-07-09 22:58 UTC | 0m |
| EPI925 | EPI | New Smyrna Beach Municipal (Jack Bolt Field) Airport (KEVB) | New Smyrna Beach Municipal (Jack Bolt Field) Airport (KEVB) | 2026-07-09 22:43 UTC | 2026-07-09 22:57 UTC | 14m |
| LXJ607 | LXJ | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Montauk Airport (KMTP) | 2026-07-09 20:40 UTC | 2026-07-09 22:56 UTC | 2h 15m |
| N691DK |  | Mc Clellan Airfield (KMCC) | Rogers Field (KO05) | 2026-07-09 22:28 UTC | 2026-07-09 22:52 UTC | 24m |
| N737ME |  | Lake Elmo Airport (K21D) | Lake Elmo Airport (K21D) | 2026-07-09 22:32 UTC | 2026-07-09 22:52 UTC | 19m |
| JIA5658 | JIA | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Philadelphia International Airport (KPHL) | 2026-07-09 20:15 UTC | 2026-07-09 22:48 UTC | 2h 33m |
| N507RP |  | Charlotte/Douglas International Airport (KCLT) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-07-09 21:33 UTC | 2026-07-09 22:47 UTC | 1h 14m |
| N625MC |  | Texada Gillies Bay Airport (CYGB) | Boeing Field/King County International Airport (KBFI) | 2026-07-09 22:00 UTC | 2026-07-09 22:41 UTC | 41m |
| N168BL |  | Johnston Regional Airport (KJNX) | Johnston Regional Airport (KJNX) | 2026-07-09 21:25 UTC | 2026-07-09 22:41 UTC | 1h 15m |
| N459MM |  | Cape May County Airport (KWWD) | Cape May County Airport (KWWD) | 2026-07-09 22:17 UTC | 2026-07-09 22:40 UTC | 22m |
| BURNY6 | BUR | Wichita Valley Airport (KF14) | Smiley Johnson Municipal/Bass Field (KE34) | 2026-07-09 22:21 UTC | 2026-07-09 22:38 UTC | 17m |
| N721EC |  | Osborne Airport (8CA0) | Depue Airport (6CA8) | 2026-07-09 19:36 UTC | 2026-07-09 22:37 UTC | 3h 1m |
| N490PD |  | Shepard Strip (07ID) | KU42 (KU42) | 2026-07-09 21:58 UTC | 2026-07-09 22:36 UTC | 37m |
| N565TA |  | Talkeetna Airport (PATK) | Helio Airport (2AK7) | 2026-07-09 21:53 UTC | 2026-07-09 22:36 UTC | 43m |
| JRE743 | JRE | Augusta Regional At Bush Field (KAGS) | The Florida Keys Marathon International Airport (KMTH) | 2026-07-09 21:06 UTC | 2026-07-09 22:36 UTC | 1h 30m |
| N950CH |  | Blanding Municipal Airport (KBDG) | Blanding Municipal Airport (KBDG) | 2026-07-09 22:10 UTC | 2026-07-09 22:35 UTC | 25m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
