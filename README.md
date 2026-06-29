# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--29_22:29:35_UTC-green)

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

**Latest saved flight:** 2026-06-29 22:29:35 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-29 22:29:35 UTC

- **124,321** saved flights
- **42,580** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **124,321** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,502,821.5 tonnes** estimated CO2 emissions
- **87,120,086 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5074 |
| 2 | SkyWest Airlines | 4617 |
| 3 | EJA | 2435 |
| 4 | IndiGo | 2364 |
| 5 | American Airlines | 1926 |
| 6 | Southwest Airlines | 1864 |
| 7 | ENY | 1563 |
| 8 | Delta Air Lines | 1480 |
| 9 | Lufthansa | 1335 |
| 10 | LATAM Airlines | 1122 |
| 11 | Vueling | 1105 |
| 12 | WIF | 1099 |
| 13 | AZU | 1046 |
| 14 | AXM | 990 |
| 15 | LXJ | 965 |
| 16 | Swiss International | 875 |
| 17 | All Nippon Airways | 836 |
| 18 | Alaska Airlines | 815 |
| 19 | easyJet | 794 |
| 20 | QLK | 780 |
| 21 | EJU | 776 |
| 22 | Cathay Pacific | 694 |
| 23 | AEE | 686 |
| 24 | VIV | 677 |
| 25 | Air France | 675 |
| 26 | United Airlines | 666 |
| 27 | CXK | 662 |
| 28 | MXY | 648 |
| 29 | JetBlue | 634 |
| 30 | GLO | 623 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 106023 |
| 2 | 🇪🇸 ES | 8348 |
| 3 | 🇮🇳 IN | 7419 |
| 4 | 🇦🇺 AU | 7235 |
| 5 | 🇧🇷 BR | 6916 |
| 6 | 🇩🇪 DE | 6602 |
| 7 | 🇮🇹 IT | 6582 |
| 8 | 🇨🇦 CA | 6522 |
| 9 | 🇬🇧 GB | 5488 |
| 10 | 🇯🇵 JP | 5459 |
| 11 | 🇫🇷 FR | 4925 |
| 12 | 🇨🇴 CO | 4032 |
| 13 | 🇲🇽 MX | 3617 |
| 14 | 🇬🇷 GR | 3543 |
| 15 | 🇳🇴 NO | 3421 |
| 16 | 🇨🇭 CH | 3184 |
| 17 | 🇹🇷 TR | 2612 |
| 18 | 🇲🇾 MY | 2563 |
| 19 | 🇿🇦 ZA | 2047 |
| 20 | 🇵🇱 PL | 2042 |
| 21 | 🇳🇿 NZ | 2006 |
| 22 | 🇹🇭 TH | 1940 |
| 23 | 🇰🇷 KR | 1932 |
| 24 | 🇵🇭 PH | 1764 |
| 25 | 🇬🇹 GT | 1716 |
| 26 | 🇲🇦 MA | 1340 |
| 27 | 🇲🇪 ME | 1238 |
| 28 | 🇳🇱 NL | 1178 |
| 29 | 🇲🇴 MO | 1177 |
| 30 | 🇧🇸 BS | 1078 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2613 |
| 2 | Denver International Airport |  | US | 2099 |
| 3 | Tokyo International Airport |  | JP | 1804 |
| 4 | Indira Gandhi International Airport |  | IN | 1633 |
| 5 | Harry Reid International Airport |  | US | 1556 |
| 6 | Guaymaral Airport |  | CO | 1520 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1493 |
| 8 | Zurich Airport |  | CH | 1378 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1326 |
| 10 | La Aurora Airport |  | GT | 1325 |
| 11 | Frankfurt am Main International Airport |  | DE | 1288 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1225 |
| 13 | Chicago O'Hare International Airport |  | US | 1206 |
| 14 | Macau International Airport |  | MO | 1177 |
| 15 | El Dorado International Airport |  | CO | 1171 |
| 16 | Salt Lake City International Airport |  | US | 1097 |
| 17 | Capua Airport |  | IT | 1060 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1039 |
| 19 | Madrid Barajas International Airport |  | ES | 1032 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1000 |
| 21 | Kuala Lumpur International Airport |  | MY | 996 |
| 22 | Congonhas Airport |  | BR | 971 |
| 23 | Charlotte/Douglas International Airport |  | US | 938 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 910 |
| 25 | Charles de Gaulle International Airport |  | FR | 904 |
| 26 | Bengaluru International Airport |  | IN | 893 |
| 27 | Malpensa International Airport |  | IT | 859 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 825 |
| 29 | Ninoy Aquino International Airport |  | PH | 818 |
| 30 | Daniel K Inouye International Airport |  | US | 796 |
| 31 | Barcelona International Airport |  | ES | 778 |
| 32 | Tenerife Norte Airport |  | ES | 767 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 758 |
| 34 | Calgary International Airport |  | CA | 732 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 728 |
| 36 | Seattle-Tacoma International Airport |  | US | 719 |
| 37 | Vitoria/Foronda Airport |  | ES | 719 |
| 38 | Amsterdam Airport Schiphol |  | NL | 715 |
| 39 | Scottsdale Airport |  | US | 715 |
| 40 | Viracopos International Airport |  | BR | 703 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 633 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 452 | 21m | 244 km | 1,903.2 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 322 | 24m | 225 km | 1,249.2 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 312 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 297 | 1h 10m | 770 km | 3,945.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 297 | 1h 25m | 910 km | 4,660.6 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 242 | 26m | 275 km | 1,146.7 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 231 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 183 | 22m | 55 km | 173.9 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 179 | 26m | 215 km | 662.9 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 175 | 20m | 99 km | 299.8 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 173 | 13m | - | - |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 172 | 44m | 241 km | 714.5 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 168 | 27m | 152 km | 439.0 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 159 | 31m | 369 km | 1,012.1 t |
| 20 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 158 | 1h 44m | 1,423 km | 3,877.6 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 156 | 18m | 144 km | 388.0 t |
| 22 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 155 | 44m | 452 km | 1,208.0 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 152 | 20m | 250 km | 656.5 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 144 | 1h 38m | 1,156 km | 2,872.7 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 142 | 1h 1m | 695 km | 1,702.2 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 142 | 1h 17m | 961 km | 2,353.7 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 141 | 13m | - | - |
| 29 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 139 | 30m | 49 km | 117.5 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 136 | 54m | 136 km | 318.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CPA318 | Cathay Pacific | Barcelona International Airport (LEBL) | Zhuhai Airport (ZGSD) | 2026-06-29 11:32 UTC | 2026-06-29 22:29 UTC | 10h 57m |
| AERT9 | AER | King Salmon Airport (PAKN) | Homer Airport (PAHO) | 2026-06-29 21:31 UTC | 2026-06-29 22:18 UTC | 47m |
| TRP6 | TRP | Forest Hill Airport (MD31) | Baltimore/Washington International Thurgood Marshall Airport (KBWI) | 2026-06-29 22:02 UTC | 2026-06-29 22:12 UTC | 10m |
| N715DL |  | Raleigh-Durham International Airport (KRDU) | Logan County Airport (K6L4) | 2026-06-29 21:29 UTC | 2026-06-29 22:10 UTC | 41m |
| ZKSUZ | ZKS | Napier Airport (NZNR) | Napier Airport (NZNR) | 2026-06-29 21:00 UTC | 2026-06-29 22:09 UTC | 1h 8m |
| N614LF |  | Cincinnati Municipal/Lunken Field (KLUK) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-06-29 21:49 UTC | 2026-06-29 22:07 UTC | 17m |
| EJA589 | EJA | Laurence G Hanscom Field (KBED) | New Castle Airport (KILG) | 2026-06-29 21:02 UTC | 2026-06-29 22:02 UTC | 1h 0m |
| N65JA |  | Aurora Municipal Airport (KARR) | De Kalb Taylor Municipal Airport (KDKB) | 2026-06-29 21:43 UTC | 2026-06-29 22:00 UTC | 16m |
| TKR140 | TKR | Animas Air Park (K00C) | Blanding Municipal Airport (KBDG) | 2026-06-29 21:39 UTC | 2026-06-29 22:00 UTC | 21m |
| ICY50 | ICY | Elmendorf Afb Airport (PAED) | Jewell Airport (AK72) | 2026-06-29 21:15 UTC | 2026-06-29 21:59 UTC | 43m |
| N83076 |  | Chester County G O Carlson Airport (KMQS) | Easton/Newnam Field (KESN) | 2026-06-29 21:15 UTC | 2026-06-29 21:59 UTC | 43m |
| N705SG |  | Oakland San Francisco Bay Airport (KOAK) | 33CA (33CA) | 2026-06-29 21:16 UTC | 2026-06-29 21:59 UTC | 42m |
| N742TW |  | KU42 (KU42) | Wendover Airport (KENV) | 2026-06-29 21:06 UTC | 2026-06-29 21:58 UTC | 51m |
| N9535H |  | Harvey's Acres Airport (OR28) | Portland-Hillsboro Airport (KHIO) | 2026-06-29 21:39 UTC | 2026-06-29 21:54 UTC | 14m |
| TKR02 | TKR | CD82 (CD82) | Blanding Municipal Airport (KBDG) | 2026-06-29 21:38 UTC | 2026-06-29 21:54 UTC | 15m |
| N98EG |  | Linden Airport (KLDJ) | Laguardia Airport (KLGA) | 2026-06-29 20:56 UTC | 2026-06-29 21:52 UTC | 56m |
| DCM4087 | DCM | Marksville Municipal Airport (KMKV) | Lakefront Airport (KNEW) | 2026-06-29 21:25 UTC | 2026-06-29 21:50 UTC | 25m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-06-29 21:32 UTC | 2026-06-29 21:49 UTC | 16m |
| ASP814 | ASP | Calgary International Airport (CYYC) | Vancouver International Airport (CYVR) | 2026-06-29 20:40 UTC | 2026-06-29 21:49 UTC | 1h 8m |
| LOT7JF | LOT Polish Airlines | Warsaw Chopin Airport (EPWA) | EPGY (EPGY) | 2026-06-29 21:41 UTC | 2026-06-29 21:48 UTC | 6m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
