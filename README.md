# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--10_00:52:32_UTC-green)

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

**Latest saved flight:** 2026-07-10 00:52:32 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-10 00:52:32 UTC

- **135,238** saved flights
- **45,739** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **135,238** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,627,321.8 tonnes** estimated CO2 emissions
- **94,337,498 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5473 |
| 2 | SkyWest Airlines | 4984 |
| 3 | EJA | 2646 |
| 4 | IndiGo | 2498 |
| 5 | American Airlines | 2130 |
| 6 | Southwest Airlines | 2038 |
| 7 | ENY | 1703 |
| 8 | Delta Air Lines | 1617 |
| 9 | Lufthansa | 1388 |
| 10 | LATAM Airlines | 1242 |
| 11 | Vueling | 1178 |
| 12 | WIF | 1174 |
| 13 | AZU | 1159 |
| 14 | LXJ | 1040 |
| 15 | AXM | 1021 |
| 16 | Swiss International | 957 |
| 17 | All Nippon Airways | 880 |
| 18 | easyJet | 876 |
| 19 | Alaska Airlines | 860 |
| 20 | QLK | 847 |
| 21 | EJU | 831 |
| 22 | VIV | 745 |
| 23 | AEE | 733 |
| 24 | CXK | 728 |
| 25 | Cathay Pacific | 723 |
| 26 | Air France | 722 |
| 27 | JetBlue | 715 |
| 28 | United Airlines | 715 |
| 29 | MXY | 705 |
| 30 | GLO | 689 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 116235 |
| 2 | 🇪🇸 ES | 8939 |
| 3 | 🇮🇳 IN | 7837 |
| 4 | 🇦🇺 AU | 7804 |
| 5 | 🇧🇷 BR | 7627 |
| 6 | 🇨🇦 CA | 7157 |
| 7 | 🇩🇪 DE | 7027 |
| 8 | 🇮🇹 IT | 7004 |
| 9 | 🇬🇧 GB | 6072 |
| 10 | 🇯🇵 JP | 5762 |
| 11 | 🇫🇷 FR | 5360 |
| 12 | 🇨🇴 CO | 4246 |
| 13 | 🇲🇽 MX | 3941 |
| 14 | 🇬🇷 GR | 3849 |
| 15 | 🇳🇴 NO | 3659 |
| 16 | 🇨🇭 CH | 3487 |
| 17 | 🇹🇷 TR | 3083 |
| 18 | 🇲🇾 MY | 2651 |
| 19 | 🇵🇱 PL | 2229 |
| 20 | 🇿🇦 ZA | 2217 |
| 21 | 🇳🇿 NZ | 2115 |
| 22 | 🇹🇭 TH | 2064 |
| 23 | 🇰🇷 KR | 1987 |
| 24 | 🇵🇭 PH | 1854 |
| 25 | 🇬🇹 GT | 1827 |
| 26 | 🇲🇦 MA | 1428 |
| 27 | 🇲🇪 ME | 1343 |
| 28 | 🇳🇱 NL | 1260 |
| 29 | 🇭🇷 HR | 1201 |
| 30 | 🇲🇴 MO | 1186 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2821 |
| 2 | Denver International Airport |  | US | 2279 |
| 3 | Tokyo International Airport |  | JP | 1880 |
| 4 | Indira Gandhi International Airport |  | IN | 1733 |
| 5 | Harry Reid International Airport |  | US | 1694 |
| 6 | Guaymaral Airport |  | CO | 1647 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1579 |
| 8 | Zurich Airport |  | CH | 1500 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1435 |
| 10 | La Aurora Airport |  | GT | 1412 |
| 11 | Frankfurt am Main International Airport |  | DE | 1343 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1302 |
| 13 | Chicago O'Hare International Airport |  | US | 1285 |
| 14 | Salt Lake City International Airport |  | US | 1208 |
| 15 | El Dorado International Airport |  | CO | 1205 |
| 16 | Macau International Airport |  | MO | 1186 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1176 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1104 |
| 19 | Madrid Barajas International Airport |  | ES | 1102 |
| 20 | Capua Airport |  | IT | 1102 |
| 21 | Congonhas Airport |  | BR | 1085 |
| 22 | Kuala Lumpur International Airport |  | MY | 1030 |
| 23 | Charlotte/Douglas International Airport |  | US | 995 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 980 |
| 25 | Charles de Gaulle International Airport |  | FR | 964 |
| 26 | Bengaluru International Airport |  | IN | 944 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 928 |
| 28 | Malpensa International Airport |  | IT | 889 |
| 29 | Ninoy Aquino International Airport |  | PH | 863 |
| 30 | Daniel K Inouye International Airport |  | US | 839 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 829 |
| 32 | Barcelona International Airport |  | ES | 829 |
| 33 | Tenerife Norte Airport |  | ES | 807 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 795 |
| 35 | Calgary International Airport |  | CA | 786 |
| 36 | Seattle-Tacoma International Airport |  | US | 774 |
| 37 | Scottsdale Airport |  | US | 773 |
| 38 | Viracopos International Airport |  | BR | 771 |
| 39 | Vitoria/Foronda Airport |  | ES | 761 |
| 40 | Amsterdam Airport Schiphol |  | NL | 757 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 693 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 490 | 21m | 244 km | 2,063.3 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 338 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 333 | 24m | 225 km | 1,291.9 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 324 | 1h 10m | 770 km | 4,304.1 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 289 | 14m | 114 km | 566.8 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
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
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 161 | 44m | 452 km | 1,254.8 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 159 | 1h 16m | 961 km | 2,635.5 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 157 | 1h 1m | 695 km | 1,882.0 t |
| 27 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 156 | 54m | 136 km | 365.7 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 154 | 1h 38m | 1,156 km | 3,072.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 149 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BRG644 | BRG | Buckland Airport (PABL) | Deering Airport (PADE) | 2026-07-10 00:35 UTC | 2026-07-10 00:52 UTC | 16m |
| N18NR |  | Visalia Municipal Airport (KVIS) | Santa Monica Municipal Airport (KSMO) | 2026-07-09 23:49 UTC | 2026-07-10 00:45 UTC | 55m |
| N737AF |  | Long Beach (Daugherty Field) Airport (KLGB) | Riverside Airport (KRAL) | 2026-07-10 00:15 UTC | 2026-07-10 00:44 UTC | 28m |
| N565E |  | 30WA (30WA) | 0WN9 (0WN9) | 2026-07-09 23:42 UTC | 2026-07-10 00:44 UTC | 1h 1m |
| N650MC |  | Palo Alto Airport (KPAO) | Lake Tahoe Airport (KTVL) | 2026-07-10 00:01 UTC | 2026-07-10 00:33 UTC | 32m |
| N761TA |  | 14CO (14CO) | 14CO (14CO) | 2026-07-09 23:26 UTC | 2026-07-10 00:31 UTC | 1h 4m |
| N12TP |  | Waycross-Ware County Airport (KAYS) | Eagle Neck Airport (1GA0) | 2026-07-10 00:06 UTC | 2026-07-10 00:30 UTC | 24m |
| FLYER64 | FLY | Al Udeid Air Base (OTBH) | Nariya Airport (OENR) | 2026-07-09 22:40 UTC | 2026-07-10 00:28 UTC | 1h 47m |
| N4769S |  | Kodiak Airport (PADQ) | Kodiak Municipal Airport (PAKD) | 2026-07-10 00:18 UTC | 2026-07-10 00:26 UTC | 8m |
| N628SR |  | Palo Alto Airport (KPAO) | Truckee-Tahoe Airport (KTRK) | 2026-07-09 23:48 UTC | 2026-07-10 00:23 UTC | 35m |
| YVG | YVG | Perth Jandakot Airport (YPJT) | Kalannie Airport (YKAE) | 2026-07-09 23:49 UTC | 2026-07-10 00:23 UTC | 33m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-07-10 00:08 UTC | 2026-07-10 00:23 UTC | 14m |
| QLK20D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Walcha Airport (YWCH) | 2026-07-09 23:04 UTC | 2026-07-10 00:21 UTC | 1h 17m |
| N4736Y |  | Meadowlark Airport (GA75) | Meadowlark Airport (GA75) | 2026-07-10 00:17 UTC | 2026-07-10 00:19 UTC | 2m |
| N789FA |  | Falcon Field (KFFZ) | 15AZ (15AZ) | 2026-07-09 22:48 UTC | 2026-07-10 00:17 UTC | 1h 28m |
| SWOOP21 | SWO | 2TX3 (2TX3) | Dunbar Ranch Airport (0XS8) | 2026-07-09 23:52 UTC | 2026-07-10 00:14 UTC | 22m |
| N4035S |  | Fremont County Airport (K1V6) | 14CO (14CO) | 2026-07-09 22:57 UTC | 2026-07-10 00:11 UTC | 1h 13m |
| SKW4327 | SkyWest Airlines | Salt Lake City International Airport (KSLC) | Simko Field (1ID9) | 2026-07-09 23:45 UTC | 2026-07-10 00:08 UTC | 23m |
| N21754 |  | Orlando Apopka Airport (KX04) | Orlando Apopka Airport (KX04) | 2026-07-09 23:40 UTC | 2026-07-10 00:05 UTC | 24m |
| JBU1500 | JetBlue | Daytona Beach International Airport (KDAB) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-09 21:00 UTC | 2026-07-10 00:01 UTC | 3h 1m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
