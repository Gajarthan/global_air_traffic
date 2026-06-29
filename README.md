# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--29_21:28:48_UTC-green)

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

**Latest saved flight:** 2026-06-29 21:28:48 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-29 21:28:48 UTC

- **124,198** saved flights
- **42,552** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **124,198** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,501,243.0 tonnes** estimated CO2 emissions
- **87,028,580 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5070 |
| 2 | SkyWest Airlines | 4610 |
| 3 | EJA | 2434 |
| 4 | IndiGo | 2364 |
| 5 | American Airlines | 1922 |
| 6 | Southwest Airlines | 1860 |
| 7 | ENY | 1561 |
| 8 | Delta Air Lines | 1478 |
| 9 | Lufthansa | 1335 |
| 10 | LATAM Airlines | 1119 |
| 11 | Vueling | 1105 |
| 12 | WIF | 1098 |
| 13 | AZU | 1043 |
| 14 | AXM | 990 |
| 15 | LXJ | 964 |
| 16 | Swiss International | 875 |
| 17 | All Nippon Airways | 836 |
| 18 | Alaska Airlines | 814 |
| 19 | easyJet | 794 |
| 20 | QLK | 779 |
| 21 | EJU | 776 |
| 22 | Cathay Pacific | 693 |
| 23 | AEE | 686 |
| 24 | VIV | 676 |
| 25 | Air France | 675 |
| 26 | United Airlines | 665 |
| 27 | CXK | 661 |
| 28 | MXY | 648 |
| 29 | JetBlue | 631 |
| 30 | GLO | 621 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 105863 |
| 2 | 🇪🇸 ES | 8346 |
| 3 | 🇮🇳 IN | 7419 |
| 4 | 🇦🇺 AU | 7229 |
| 5 | 🇧🇷 BR | 6900 |
| 6 | 🇩🇪 DE | 6602 |
| 7 | 🇮🇹 IT | 6579 |
| 8 | 🇨🇦 CA | 6512 |
| 9 | 🇬🇧 GB | 5487 |
| 10 | 🇯🇵 JP | 5459 |
| 11 | 🇫🇷 FR | 4924 |
| 12 | 🇨🇴 CO | 4031 |
| 13 | 🇲🇽 MX | 3614 |
| 14 | 🇬🇷 GR | 3542 |
| 15 | 🇳🇴 NO | 3419 |
| 16 | 🇨🇭 CH | 3184 |
| 17 | 🇹🇷 TR | 2612 |
| 18 | 🇲🇾 MY | 2563 |
| 19 | 🇿🇦 ZA | 2047 |
| 20 | 🇵🇱 PL | 2038 |
| 21 | 🇳🇿 NZ | 2000 |
| 22 | 🇹🇭 TH | 1940 |
| 23 | 🇰🇷 KR | 1932 |
| 24 | 🇵🇭 PH | 1762 |
| 25 | 🇬🇹 GT | 1714 |
| 26 | 🇲🇦 MA | 1339 |
| 27 | 🇲🇪 ME | 1237 |
| 28 | 🇳🇱 NL | 1178 |
| 29 | 🇲🇴 MO | 1177 |
| 30 | 🇧🇸 BS | 1078 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2609 |
| 2 | Denver International Airport |  | US | 2095 |
| 3 | Tokyo International Airport |  | JP | 1804 |
| 4 | Indira Gandhi International Airport |  | IN | 1633 |
| 5 | Harry Reid International Airport |  | US | 1550 |
| 6 | Guaymaral Airport |  | CO | 1519 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1493 |
| 8 | Zurich Airport |  | CH | 1378 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1326 |
| 10 | La Aurora Airport |  | GT | 1324 |
| 11 | Frankfurt am Main International Airport |  | DE | 1288 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1225 |
| 13 | Chicago O'Hare International Airport |  | US | 1204 |
| 14 | Macau International Airport |  | MO | 1177 |
| 15 | El Dorado International Airport |  | CO | 1171 |
| 16 | Salt Lake City International Airport |  | US | 1095 |
| 17 | Capua Airport |  | IT | 1058 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1035 |
| 19 | Madrid Barajas International Airport |  | ES | 1032 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 997 |
| 21 | Kuala Lumpur International Airport |  | MY | 996 |
| 22 | Congonhas Airport |  | BR | 970 |
| 23 | Charlotte/Douglas International Airport |  | US | 936 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 910 |
| 25 | Charles de Gaulle International Airport |  | FR | 904 |
| 26 | Bengaluru International Airport |  | IN | 893 |
| 27 | Malpensa International Airport |  | IT | 858 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 821 |
| 29 | Ninoy Aquino International Airport |  | PH | 817 |
| 30 | Daniel K Inouye International Airport |  | US | 795 |
| 31 | Barcelona International Airport |  | ES | 777 |
| 32 | Tenerife Norte Airport |  | ES | 767 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 758 |
| 34 | Calgary International Airport |  | CA | 727 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 725 |
| 36 | Vitoria/Foronda Airport |  | ES | 719 |
| 37 | Seattle-Tacoma International Airport |  | US | 718 |
| 38 | Amsterdam Airport Schiphol |  | NL | 715 |
| 39 | Scottsdale Airport |  | US | 715 |
| 40 | Don Mueang International Airport |  | TH | 702 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 633 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 451 | 21m | 244 km | 1,899.0 t |
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
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 158 | 1h 44m | 1,423 km | 3,877.6 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 158 | 31m | 369 km | 1,005.7 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 156 | 18m | 144 km | 388.0 t |
| 22 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 155 | 44m | 452 km | 1,208.0 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 152 | 20m | 250 km | 656.5 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 144 | 1h 38m | 1,156 km | 2,872.7 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 142 | 1h 1m | 695 km | 1,702.2 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 141 | 1h 17m | 961 km | 2,337.1 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 141 | 13m | - | - |
| 29 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 139 | 30m | 49 km | 117.5 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 136 | 54m | 136 km | 318.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N33RK |  | North Perry Airport (KHWO) | Orlando Executive Airport (KORL) | 2026-06-29 19:18 UTC | 2026-06-29 21:28 UTC | 2h 9m |
| BPX263 | BPX | Huntsville Executive Tom Sharp Jr Field (KMDQ) | Huntsville Executive Tom Sharp Jr Field (KMDQ) | 2026-06-29 20:27 UTC | 2026-06-29 21:19 UTC | 52m |
| PRDRS | PRD | Campo de Marte Airport (SBMT) | Bacacheri Airport (SBBI) | 2026-06-29 20:17 UTC | 2026-06-29 21:12 UTC | 55m |
| 0   P |  | Whidbey Island Nas (Ault Field) Airport (KNUW) | KS98 (KS98) | 2026-06-29 18:25 UTC | 2026-06-29 21:11 UTC | 2h 45m |
| N780U |  | Ona Airpark (K12V) | West Virginia International Yeager Airport (KCRW) | 2026-06-29 20:51 UTC | 2026-06-29 21:09 UTC | 18m |
| N689CM |  | Central Wisconsin Airport (KCWA) | Rochester International Airport (KRST) | 2026-06-29 20:34 UTC | 2026-06-29 21:07 UTC | 33m |
| TKR02 | TKR | Blanding Municipal Airport (KBDG) | Animas Air Park (K00C) | 2026-06-29 20:50 UTC | 2026-06-29 21:04 UTC | 14m |
| TKR140 | TKR | Grand Junction Regional Airport (KGJT) | Animas Air Park (K00C) | 2026-06-29 20:08 UTC | 2026-06-29 21:00 UTC | 52m |
| N94MN |  | Whiteman Airport (KWHP) | Whiteman Airport (KWHP) | 2026-06-29 19:48 UTC | 2026-06-29 21:00 UTC | 1h 11m |
| BOE251 | BOE | Renton Municipal Airport (KRNT) | Lind Airport (K0S0) | 2026-06-29 19:21 UTC | 2026-06-29 20:58 UTC | 1h 37m |
| N541RL |  | Ted Stevens Anchorage International Airport (PANC) | Ted Stevens Anchorage International Airport (PANC) | 2026-06-29 20:44 UTC | 2026-06-29 20:56 UTC | 12m |
| GRIM69 | GRI | Flysooner Field (OK50) | Christman Airfield (KO65) | 2026-06-29 20:46 UTC | 2026-06-29 20:53 UTC | 7m |
| AAL1970 | American Airlines | Chicago O'Hare International Airport (KORD) | Hot Springs County Airport (KHSG) | 2026-06-29 18:36 UTC | 2026-06-29 20:50 UTC | 2h 14m |
| ATCK103 | ATC | Blanding Municipal Airport (KBDG) | Blanding Municipal Airport (KBDG) | 2026-06-29 20:02 UTC | 2026-06-29 20:48 UTC | 45m |
| N236MA |  | KU77 (KU77) | KU77 (KU77) | 2026-06-29 20:31 UTC | 2026-06-29 20:47 UTC | 15m |
| HAMMR69 | HAM | Flysooner Field (OK50) | Cherokee Municipal Airport (K4O5) | 2026-06-29 20:38 UTC | 2026-06-29 20:46 UTC | 7m |
| N6453J |  | Manassas Regional/Harry P Davis Field (KHEF) | Culpeper Regional Airport (KCJR) | 2026-06-29 20:04 UTC | 2026-06-29 20:46 UTC | 42m |
| ZKSUZ | ZKS | Waipukurau Airport (NZYP) | Napier Airport (NZNR) | 2026-06-29 20:32 UTC | 2026-06-29 20:46 UTC | 13m |
| XBNLT | XBN | Atizapan De Zaragoza Airport (MMJC) | Atizapan De Zaragoza Airport (MMJC) | 2026-06-29 20:02 UTC | 2026-06-29 20:45 UTC | 43m |
| CXK160 | CXK | Martin State Airport (KMTN) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-06-29 19:47 UTC | 2026-06-29 20:41 UTC | 53m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
