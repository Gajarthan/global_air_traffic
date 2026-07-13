# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--13_15:57:30_UTC-green)

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

**Latest saved flight:** 2026-07-13 15:57:30 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-13 15:57:30 UTC

- **140,136** saved flights
- **47,169** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **140,136** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,682,471.8 tonnes** estimated CO2 emissions
- **97,534,596 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5712 |
| 2 | SkyWest Airlines | 5124 |
| 3 | EJA | 2760 |
| 4 | IndiGo | 2574 |
| 5 | American Airlines | 2216 |
| 6 | Southwest Airlines | 2107 |
| 7 | ENY | 1745 |
| 8 | Delta Air Lines | 1661 |
| 9 | Lufthansa | 1425 |
| 10 | LATAM Airlines | 1290 |
| 11 | Vueling | 1212 |
| 12 | WIF | 1208 |
| 13 | AZU | 1205 |
| 14 | LXJ | 1074 |
| 15 | AXM | 1048 |
| 16 | Swiss International | 1004 |
| 17 | easyJet | 914 |
| 18 | All Nippon Airways | 899 |
| 19 | Alaska Airlines | 881 |
| 20 | QLK | 877 |
| 21 | EJU | 864 |
| 22 | VIV | 773 |
| 23 | AEE | 752 |
| 24 | Air France | 752 |
| 25 | CXK | 751 |
| 26 | JetBlue | 736 |
| 27 | United Airlines | 732 |
| 28 | Cathay Pacific | 729 |
| 29 | MXY | 726 |
| 30 | GLO | 716 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 120302 |
| 2 | 🇪🇸 ES | 9204 |
| 3 | 🇮🇳 IN | 8063 |
| 4 | 🇦🇺 AU | 8016 |
| 5 | 🇧🇷 BR | 7910 |
| 6 | 🇨🇦 CA | 7341 |
| 7 | 🇮🇹 IT | 7327 |
| 8 | 🇩🇪 DE | 7315 |
| 9 | 🇬🇧 GB | 6389 |
| 10 | 🇯🇵 JP | 5895 |
| 11 | 🇫🇷 FR | 5588 |
| 12 | 🇨🇴 CO | 4435 |
| 13 | 🇲🇽 MX | 4064 |
| 14 | 🇬🇷 GR | 3990 |
| 15 | 🇳🇴 NO | 3779 |
| 16 | 🇨🇭 CH | 3651 |
| 17 | 🇹🇷 TR | 3303 |
| 18 | 🇲🇾 MY | 2731 |
| 19 | 🇵🇱 PL | 2350 |
| 20 | 🇿🇦 ZA | 2302 |
| 21 | 🇳🇿 NZ | 2142 |
| 22 | 🇹🇭 TH | 2110 |
| 23 | 🇰🇷 KR | 2013 |
| 24 | 🇵🇭 PH | 1906 |
| 25 | 🇬🇹 GT | 1851 |
| 26 | 🇲🇦 MA | 1470 |
| 27 | 🇲🇪 ME | 1394 |
| 28 | 🇳🇱 NL | 1323 |
| 29 | 🇭🇷 HR | 1269 |
| 30 | 🇲🇴 MO | 1190 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2891 |
| 2 | Denver International Airport |  | US | 2343 |
| 3 | Tokyo International Airport |  | JP | 1909 |
| 4 | Indira Gandhi International Airport |  | IN | 1786 |
| 5 | Harry Reid International Airport |  | US | 1749 |
| 6 | Guaymaral Airport |  | CO | 1708 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1612 |
| 8 | Zurich Airport |  | CH | 1566 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1468 |
| 10 | La Aurora Airport |  | GT | 1430 |
| 11 | Frankfurt am Main International Airport |  | DE | 1374 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1336 |
| 13 | Chicago O'Hare International Airport |  | US | 1317 |
| 14 | Salt Lake City International Airport |  | US | 1247 |
| 15 | El Dorado International Airport |  | CO | 1242 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1202 |
| 17 | Macau International Airport |  | MO | 1190 |
| 18 | Capua Airport |  | IT | 1149 |
| 19 | Madrid Barajas International Airport |  | ES | 1140 |
| 20 | Congonhas Airport |  | BR | 1126 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1122 |
| 22 | Kuala Lumpur International Airport |  | MY | 1057 |
| 23 | Charlotte/Douglas International Airport |  | US | 1022 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1011 |
| 25 | Charles de Gaulle International Airport |  | FR | 995 |
| 26 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 974 |
| 27 | Bengaluru International Airport |  | IN | 965 |
| 28 | Malpensa International Airport |  | IT | 912 |
| 29 | Ninoy Aquino International Airport |  | PH | 889 |
| 30 | Daniel K Inouye International Airport |  | US | 857 |
| 31 | Barcelona International Airport |  | ES | 857 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 855 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 823 |
| 34 | Tenerife Norte Airport |  | ES | 818 |
| 35 | Calgary International Airport |  | CA | 804 |
| 36 | Viracopos International Airport |  | BR | 799 |
| 37 | Amsterdam Airport Schiphol |  | NL | 797 |
| 38 | Seattle-Tacoma International Airport |  | US | 796 |
| 39 | Scottsdale Airport |  | US | 795 |
| 40 | Vitoria/Foronda Airport |  | ES | 780 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 720 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 507 | 21m | 244 km | 2,134.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 344 | 24m | 225 km | 1,334.6 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 342 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 333 | 1h 9m | 770 km | 4,423.6 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 298 | 14m | 114 km | 584.5 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 258 | 26m | 275 km | 1,222.6 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 254 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 206 | 22m | 55 km | 195.8 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 191 | 26m | 215 km | 707.4 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 190 | 44m | 241 km | 789.2 t |
| 16 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 188 | 1h 46m | 1,423 km | 4,613.8 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 187 | 20m | 99 km | 320.3 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 185 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 176 | 27m | 152 km | 460.0 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 175 | 20m | 250 km | 755.9 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 22 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 170 | 31m | 369 km | 1,082.1 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 168 | 18m | 144 km | 417.9 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 164 | 44m | 452 km | 1,278.1 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 162 | 1h 16m | 961 km | 2,685.2 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 161 | 1h 1m | 695 km | 1,929.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 160 | 1h 38m | 1,156 km | 3,191.9 t |
| 28 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 157 | 54m | 136 km | 368.1 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 156 | 14m | 154 km | 413.3 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 154 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N746TW |  | KU42 (KU42) | KU42 (KU42) | 2026-07-13 15:41 UTC | 2026-07-13 15:57 UTC | 16m |
| N500EH |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-07-13 14:52 UTC | 2026-07-13 15:54 UTC | 1h 1m |
| N747CV |  | Sky Manor Airport (KN40) | Sky Manor Airport (KN40) | 2026-07-13 15:40 UTC | 2026-07-13 15:51 UTC | 10m |
| SWR51D | Swiss International | Manchester Airport (EGCC) | Zurich Airport (LSZH) | 2026-07-13 14:21 UTC | 2026-07-13 15:51 UTC | 1h 29m |
| LOT4CE | LOT Polish Airlines | Warsaw Chopin Airport (EPWA) | Oksywie Military Air Base (EPOK) | 2026-07-13 15:20 UTC | 2026-07-13 15:47 UTC | 26m |
| AAL109 | American Airlines | London Heathrow Airport (EGLL) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-13 09:14 UTC | 2026-07-13 15:45 UTC | 6h 30m |
| N6269D |  | Montgomery County Airpark (KGAI) | Lancaster Airport (KLNS) | 2026-07-13 14:50 UTC | 2026-07-13 15:34 UTC | 43m |
| ABK361 | ABK | Montréal (Mirabel) Airport (CYMX) | Montréal (Mirabel) Airport (CYMX) | 2026-07-13 14:01 UTC | 2026-07-13 15:32 UTC | 1h 31m |
| N115CJ |  | Gnoss Field (KDVO) | Blue Canyon - Nyack Airport (KBLU) | 2026-07-13 15:09 UTC | 2026-07-13 15:31 UTC | 22m |
| SWR5MT | Swiss International | Zurich Airport (LSZH) | Zurich Airport (LSZH) | 2026-07-13 15:31 UTC | 2026-07-13 15:31 UTC | 0m |
| N216GH |  | Fremont County Airport (K1V6) | 14CO (14CO) | 2026-07-13 14:52 UTC | 2026-07-13 15:31 UTC | 38m |
| WARBEVR7 | WAR | Lake Riverside Estates Airport (54CL) | Borrego Air Ranch Airport (58CL) | 2026-07-13 15:19 UTC | 2026-07-13 15:30 UTC | 10m |
| N63456 |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-07-13 15:09 UTC | 2026-07-13 15:30 UTC | 20m |
| GPD388 | GPD | Philadelphia International Airport (KPHL) | Philadelphia International Airport (KPHL) | 2026-07-13 15:28 UTC | 2026-07-13 15:28 UTC | 0m |
| N36MK |  | Woodbine Municipal Airport (KOBI) | NJ96 (NJ96) | 2026-07-13 15:10 UTC | 2026-07-13 15:27 UTC | 17m |
| N999VP |  | Vogen Airport (IS41) | Vogen Airport (IS41) | 2026-07-13 14:52 UTC | 2026-07-13 15:27 UTC | 34m |
| CHETA55 | CHE | Halifax Robert L. Stanfield International Airport (CYHZ) | Halifax Robert L. Stanfield International Airport (CYHZ) | 2026-07-13 14:45 UTC | 2026-07-13 15:26 UTC | 41m |
| MUSL | MUS | Joint Base Andrews Airport (KADW) | KW32 (KW32) | 2026-07-13 15:07 UTC | 2026-07-13 15:26 UTC | 18m |
| BOMR711 | BOM | Corpus Christi Nas (Truax Field) Airport (KNGP) | Corpus Christi Nas (Truax Field) Airport (KNGP) | 2026-07-13 14:43 UTC | 2026-07-13 15:25 UTC | 41m |
| KEN46 | KEN | Seattle Paine Field International Airport (KPAE) | Mineral County Airport (K9S4) | 2026-07-13 14:12 UTC | 2026-07-13 15:25 UTC | 1h 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
