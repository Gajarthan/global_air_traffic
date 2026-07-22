# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--22_22:13:15_UTC-green)

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

**Latest saved flight:** 2026-07-22 22:13:15 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-22 22:13:15 UTC

- **144,787** saved flights
- **48,489** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **144,787** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,735,875.8 tonnes** estimated CO2 emissions
- **100,630,479 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5888 |
| 2 | SkyWest Airlines | 5302 |
| 3 | EJA | 2851 |
| 4 | IndiGo | 2623 |
| 5 | American Airlines | 2318 |
| 6 | Southwest Airlines | 2187 |
| 7 | ENY | 1799 |
| 8 | Delta Air Lines | 1719 |
| 9 | Lufthansa | 1444 |
| 10 | LATAM Airlines | 1330 |
| 11 | AZU | 1246 |
| 12 | WIF | 1237 |
| 13 | Vueling | 1236 |
| 14 | LXJ | 1115 |
| 15 | AXM | 1063 |
| 16 | Swiss International | 1029 |
| 17 | easyJet | 942 |
| 18 | All Nippon Airways | 922 |
| 19 | Alaska Airlines | 912 |
| 20 | QLK | 906 |
| 21 | EJU | 886 |
| 22 | VIV | 806 |
| 23 | CXK | 777 |
| 24 | AEE | 766 |
| 25 | JetBlue | 765 |
| 26 | Air France | 764 |
| 27 | MXY | 758 |
| 28 | Cathay Pacific | 756 |
| 29 | United Airlines | 752 |
| 30 | GLO | 742 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 124816 |
| 2 | 🇪🇸 ES | 9392 |
| 3 | 🇦🇺 AU | 8244 |
| 4 | 🇮🇳 IN | 8217 |
| 5 | 🇧🇷 BR | 8165 |
| 6 | 🇨🇦 CA | 7670 |
| 7 | 🇮🇹 IT | 7540 |
| 8 | 🇩🇪 DE | 7465 |
| 9 | 🇬🇧 GB | 6604 |
| 10 | 🇯🇵 JP | 6036 |
| 11 | 🇫🇷 FR | 5756 |
| 12 | 🇨🇴 CO | 4721 |
| 13 | 🇲🇽 MX | 4219 |
| 14 | 🇬🇷 GR | 4099 |
| 15 | 🇳🇴 NO | 3869 |
| 16 | 🇨🇭 CH | 3753 |
| 17 | 🇹🇷 TR | 3397 |
| 18 | 🇲🇾 MY | 2775 |
| 19 | 🇵🇱 PL | 2440 |
| 20 | 🇿🇦 ZA | 2350 |
| 21 | 🇳🇿 NZ | 2211 |
| 22 | 🇹🇭 TH | 2130 |
| 23 | 🇰🇷 KR | 2037 |
| 24 | 🇵🇭 PH | 1934 |
| 25 | 🇬🇹 GT | 1887 |
| 26 | 🇲🇦 MA | 1502 |
| 27 | 🇲🇪 ME | 1439 |
| 28 | 🇳🇱 NL | 1357 |
| 29 | 🇭🇷 HR | 1320 |
| 30 | 🇲🇴 MO | 1211 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2987 |
| 2 | Denver International Airport |  | US | 2429 |
| 3 | Tokyo International Airport |  | JP | 1942 |
| 4 | Indira Gandhi International Airport |  | IN | 1824 |
| 5 | Harry Reid International Airport |  | US | 1815 |
| 6 | Guaymaral Airport |  | CO | 1775 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1644 |
| 8 | Zurich Airport |  | CH | 1601 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1523 |
| 10 | La Aurora Airport |  | GT | 1462 |
| 11 | Frankfurt am Main International Airport |  | DE | 1391 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1368 |
| 13 | Chicago O'Hare International Airport |  | US | 1349 |
| 14 | Salt Lake City International Airport |  | US | 1299 |
| 15 | El Dorado International Airport |  | CO | 1288 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1262 |
| 17 | Macau International Airport |  | MO | 1211 |
| 18 | Capua Airport |  | IT | 1179 |
| 19 | Congonhas Airport |  | BR | 1160 |
| 20 | Madrid Barajas International Airport |  | ES | 1155 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1144 |
| 22 | Kuala Lumpur International Airport |  | MY | 1072 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1043 |
| 24 | Charlotte/Douglas International Airport |  | US | 1039 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1011 |
| 26 | Charles de Gaulle International Airport |  | FR | 1009 |
| 27 | Bengaluru International Airport |  | IN | 981 |
| 28 | Malpensa International Airport |  | IT | 936 |
| 29 | Ninoy Aquino International Airport |  | PH | 903 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 889 |
| 31 | Barcelona International Airport |  | ES | 880 |
| 32 | Daniel K Inouye International Airport |  | US | 877 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 863 |
| 34 | Tenerife Norte Airport |  | ES | 829 |
| 35 | Seattle-Tacoma International Airport |  | US | 825 |
| 36 | Viracopos International Airport |  | BR | 823 |
| 37 | Calgary International Airport |  | CA | 822 |
| 38 | Scottsdale Airport |  | US | 820 |
| 39 | Amsterdam Airport Schiphol |  | NL | 817 |
| 40 | Oslo Gardermoen Airport |  | NO | 795 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 748 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 526 | 21m | 244 km | 2,214.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 351 | 24m | 225 km | 1,361.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 351 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 340 | 1h 9m | 770 km | 4,516.6 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 300 | 14m | 114 km | 588.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 261 | 26m | 275 km | 1,236.8 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 257 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 217 | 22m | 55 km | 206.3 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 194 | 26m | 215 km | 718.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 193 | 1h 46m | 1,423 km | 4,736.5 t |
| 16 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 193 | 44m | 241 km | 801.7 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 192 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 190 | 20m | 99 km | 325.5 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 179 | 20m | 250 km | 773.2 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 179 | 28m | 152 km | 467.8 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 173 | 31m | 369 km | 1,101.2 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 173 | 18m | 144 km | 430.3 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 168 | 44m | 452 km | 1,309.3 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 168 | 1h 16m | 961 km | 2,784.7 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 166 | 1h 1m | 695 km | 1,989.8 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 165 | 1h 39m | 1,156 km | 3,291.7 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 164 | 13m | - | - |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 162 | 14m | 154 km | 429.2 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 157 | 54m | 136 km | 368.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SH248 |  | Asheville Regional Airport (KAVL) | Green Pond Airport (SC39) | 2026-07-22 21:22 UTC | 2026-07-22 22:13 UTC | 50m |
| N760PS |  | Tampa Executive Airport (KVDF) | Zephyrhills Municipal Airport (KZPH) | 2026-07-22 21:56 UTC | 2026-07-22 22:10 UTC | 14m |
| N4126U |  | Fernando Luis Ribas Dominicci Airport (TJIG) | Cuylers Airport (02PR) | 2026-07-22 21:55 UTC | 2026-07-22 22:10 UTC | 15m |
| BCS694 | BCS | Bengaluru International Airport (VOBL) | Zhuhai Airport (ZGSD) | 2026-07-22 16:55 UTC | 2026-07-22 22:07 UTC | 5h 11m |
| N106DE |  | Minden-Tahoe Airport (KMEV) | Sweetwater (Usmc) Airport (NV72) | 2026-07-22 19:47 UTC | 2026-07-22 22:07 UTC | 2h 19m |
| CPA372 | Cathay Pacific | Torrejon Airport (LETO) | Zhuhai Airport (ZGSD) | 2026-07-22 10:53 UTC | 2026-07-22 22:05 UTC | 11h 12m |
| N445B |  | Doylestown Airport (KDYL) | Lehigh Valley International Airport (KABE) | 2026-07-22 21:40 UTC | 2026-07-22 22:04 UTC | 24m |
| CPA382 | Cathay Pacific | Zurich Airport (LSZH) | Zhuhai Airport (ZGSD) | 2026-07-22 11:52 UTC | 2026-07-22 22:04 UTC | 10h 11m |
| BCS7837 | BCS | Eleftherios Venizelos International Airport (LGAV) | Leipzig Halle Airport (EDDP) | 2026-07-22 19:25 UTC | 2026-07-22 22:02 UTC | 2h 36m |
| CXK1039 | CXK | Smyrna Airport (KMQY) | KM33 (KM33) | 2026-07-22 21:08 UTC | 2026-07-22 22:01 UTC | 53m |
| XBPBH | XBP | Hermanos Serdan International Airport (MMPB) | Tehuacan Airport (MMHC) | 2026-07-22 21:37 UTC | 2026-07-22 22:01 UTC | 24m |
| JIA5063 | JIA | Birmingham-Shuttlesworth International Airport (KBHM) | Dallas-Fort Worth International Airport (KDFW) | 2026-07-22 20:28 UTC | 2026-07-22 22:00 UTC | 1h 32m |
| N68VU |  | Eagle Creek Airpark (KEYE) | Baird-Wolford Airport (2II6) | 2026-07-22 21:39 UTC | 2026-07-22 21:57 UTC | 17m |
| N7603C |  | Gillespie Field (KSEE) | Gillespie Field (KSEE) | 2026-07-22 21:32 UTC | 2026-07-22 21:57 UTC | 24m |
| N427DM |  | Williams Flying Service Airport (6LA6) | KL38 (KL38) | 2026-07-22 21:20 UTC | 2026-07-22 21:56 UTC | 35m |
| N186SG |  | Mirth Airport (WA22) | Boeing Field/King County International Airport (KBFI) | 2026-07-22 21:41 UTC | 2026-07-22 21:56 UTC | 14m |
| FAD232 | FAD | Riyadh Air Base (OERY) | Riyadh Air Base (OERY) | 2026-07-22 21:52 UTC | 2026-07-22 21:55 UTC | 3m |
| SH079 |  | Thomas C Russell Field (KALX) | Evergreen Regional/Middleton Field (KGZH) | 2026-07-22 21:27 UTC | 2026-07-22 21:53 UTC | 25m |
| N232HC |  | Tallahassee International Airport (KTLH) | Warren County Memorial Airport (KRNC) | 2026-07-22 20:58 UTC | 2026-07-22 21:52 UTC | 54m |
| N4360C |  | Gardiner Airport (5NY5) | Lawrence Municipal Airport (KLWM) | 2026-07-22 20:51 UTC | 2026-07-22 21:51 UTC | 59m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
