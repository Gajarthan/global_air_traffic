# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--19_05:06:04_UTC-green)

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

**Latest saved flight:** 2026-06-19 05:06:04 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-19 05:06:04 UTC

- **114,209** saved flights
- **39,623** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **114,209** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,391,093.3 tonnes** estimated CO2 emissions
- **80,643,090 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4704 |
| 2 | SkyWest Airlines | 4260 |
| 3 | EJA | 2211 |
| 4 | IndiGo | 2208 |
| 5 | American Airlines | 1797 |
| 6 | Southwest Airlines | 1696 |
| 7 | ENY | 1421 |
| 8 | Delta Air Lines | 1345 |
| 9 | Lufthansa | 1274 |
| 10 | Vueling | 1036 |
| 11 | WIF | 1014 |
| 12 | LATAM Airlines | 1009 |
| 13 | AZU | 958 |
| 14 | AXM | 949 |
| 15 | LXJ | 869 |
| 16 | Swiss International | 811 |
| 17 | All Nippon Airways | 789 |
| 18 | Alaska Airlines | 771 |
| 19 | QLK | 747 |
| 20 | easyJet | 733 |
| 21 | EJU | 716 |
| 22 | Cathay Pacific | 671 |
| 23 | AEE | 640 |
| 24 | VIV | 633 |
| 25 | United Airlines | 632 |
| 26 | Air France | 630 |
| 27 | CXK | 605 |
| 28 | MXY | 605 |
| 29 | AXB | 560 |
| 30 | GLO | 558 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 96323 |
| 2 | 🇪🇸 ES | 7791 |
| 3 | 🇮🇳 IN | 6972 |
| 4 | 🇦🇺 AU | 6805 |
| 5 | 🇧🇷 BR | 6319 |
| 6 | 🇮🇹 IT | 6116 |
| 7 | 🇩🇪 DE | 6107 |
| 8 | 🇨🇦 CA | 5988 |
| 9 | 🇯🇵 JP | 5144 |
| 10 | 🇬🇧 GB | 4928 |
| 11 | 🇫🇷 FR | 4541 |
| 12 | 🇨🇴 CO | 3910 |
| 13 | 🇲🇽 MX | 3373 |
| 14 | 🇬🇷 GR | 3249 |
| 15 | 🇳🇴 NO | 3156 |
| 16 | 🇨🇭 CH | 2913 |
| 17 | 🇲🇾 MY | 2456 |
| 18 | 🇹🇷 TR | 2298 |
| 19 | 🇿🇦 ZA | 1931 |
| 20 | 🇳🇿 NZ | 1886 |
| 21 | 🇰🇷 KR | 1874 |
| 22 | 🇵🇱 PL | 1865 |
| 23 | 🇹🇭 TH | 1862 |
| 24 | 🇵🇭 PH | 1663 |
| 25 | 🇬🇹 GT | 1627 |
| 26 | 🇲🇦 MA | 1248 |
| 27 | 🇲🇴 MO | 1168 |
| 28 | 🇲🇪 ME | 1122 |
| 29 | 🇳🇱 NL | 1106 |
| 30 | 🇭🇷 HR | 992 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2425 |
| 2 | Denver International Airport |  | US | 1937 |
| 3 | Tokyo International Airport |  | JP | 1708 |
| 4 | Indira Gandhi International Airport |  | IN | 1524 |
| 5 | Guaymaral Airport |  | CO | 1445 |
| 6 | Harry Reid International Airport |  | US | 1436 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1403 |
| 8 | Zurich Airport |  | CH | 1280 |
| 9 | La Aurora Airport |  | GT | 1255 |
| 10 | Frankfurt am Main International Airport |  | DE | 1243 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1225 |
| 12 | Macau International Airport |  | MO | 1168 |
| 13 | El Dorado International Airport |  | CO | 1159 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1140 |
| 15 | Chicago O'Hare International Airport |  | US | 1127 |
| 16 | Capua Airport |  | IT | 991 |
| 17 | Madrid Barajas International Airport |  | ES | 981 |
| 18 | Salt Lake City International Airport |  | US | 969 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 959 |
| 20 | Kuala Lumpur International Airport |  | MY | 951 |
| 21 | Charlotte/Douglas International Airport |  | US | 883 |
| 22 | Congonhas Airport |  | BR | 875 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 855 |
| 24 | Charles de Gaulle International Airport |  | FR | 843 |
| 25 | Bengaluru International Airport |  | IN | 843 |
| 26 | Malpensa International Airport |  | IT | 821 |
| 27 | General Edward Lawrence Logan International Airport |  | US | 819 |
| 28 | Ninoy Aquino International Airport |  | PH | 767 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 752 |
| 30 | Daniel K Inouye International Airport |  | US | 747 |
| 31 | Tenerife Norte Airport |  | ES | 743 |
| 32 | Barcelona International Airport |  | ES | 734 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 720 |
| 34 | Don Mueang International Airport |  | TH | 676 |
| 35 | Vitoria/Foronda Airport |  | ES | 674 |
| 36 | Amsterdam Airport Schiphol |  | NL | 674 |
| 37 | Calgary International Airport |  | CA | 671 |
| 38 | Seattle-Tacoma International Airport |  | US | 659 |
| 39 | Viracopos International Airport |  | BR | 655 |
| 40 | Norman Y Mineta San Jose International Airport |  | US | 653 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 600 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 413 | 21m | 244 km | 1,739.0 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 305 | 24m | 225 km | 1,183.3 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 297 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 285 | 1h 7m | 706 km | 3,469.9 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 281 | 1h 25m | 910 km | 4,409.5 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 278 | 14m | 114 km | 545.2 t |
| 8 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 272 | 1h 10m | 770 km | 3,613.3 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 228 | 26m | 275 km | 1,080.4 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 227 | 19m | 165 km | 645.7 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 212 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 168 | 22m | 55 km | 159.7 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 168 | 20m | 99 km | 287.8 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 167 | 26m | 215 km | 618.5 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 167 | 13m | - | - |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 155 | 27m | 152 km | 405.1 t |
| 18 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 153 | 31m | 369 km | 973.9 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 151 | 44m | 452 km | 1,176.8 t |
| 21 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 148 | 44m | 241 km | 614.8 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 147 | 18m | 144 km | 365.7 t |
| 23 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 145 | 20m | 250 km | 626.3 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 137 | 1h 1m | 695 km | 1,642.2 t |
| 25 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 134 | 1h 43m | 1,423 km | 3,288.6 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 133 | 1h 39m | 1,156 km | 2,653.3 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 130 | 13m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 129 | 1h 17m | 961 km | 2,138.2 t |
| 30 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 127 | 12m | 99 km | 217.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DLH423 | Lufthansa | General Edward Lawrence Logan International Airport (KBOS) | Anspach/Taunus Airport (EDFA) | 2026-06-18 22:38 UTC | 2026-06-19 05:06 UTC | 6h 27m |
| WZZ398 | Wizz Air | Budapest Ferenc Liszt International Airport (LHBP) | Anadolu University Airport (LTBY) | 2026-06-19 03:37 UTC | 2026-06-19 05:02 UTC | 1h 24m |
| DLH5HR | Lufthansa | Nuremberg Airport (EDDN) | Frankfurt am Main International Airport (EDDF) | 2026-06-19 04:29 UTC | 2026-06-19 04:53 UTC | 24m |
| ACA840 | Air Canada | Toronto Pearson International Airport (CYYZ) | Frankfurt am Main International Airport (EDDF) | 2026-06-18 21:34 UTC | 2026-06-19 04:52 UTC | 7h 17m |
| N119UV |  | Provo Municipal Airport (KPVU) | Wendover Airport (KENV) | 2026-06-19 03:43 UTC | 2026-06-19 04:49 UTC | 1h 5m |
| N258EA |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-06-19 01:58 UTC | 2026-06-19 04:45 UTC | 2h 47m |
| N9531X |  | Gainesville Municipal Airport (KGLE) | Addington Field (4TX8) | 2026-06-19 04:20 UTC | 2026-06-19 04:33 UTC | 13m |
| WIF7GT | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-06-19 04:17 UTC | 2026-06-19 04:33 UTC | 15m |
| GFA17J | Gulf Air | Indira Gandhi International Airport (VIDP) | Frankfurt am Main International Airport (EDDF) | 2026-06-18 16:40 UTC | 2026-06-19 04:31 UTC | 11h 51m |
| BHA281 | BHA | Tribhuvan International Airport (VNKT) | Thamkharka Airport (VNTH) | 2026-06-19 04:09 UTC | 2026-06-19 04:30 UTC | 20m |
| LIFELN3 | LIF | Cheyenne Regional/Jerry Olson Field (KCYS) | Crystal Lakes Airport (25CO) | 2026-06-19 04:09 UTC | 2026-06-19 04:29 UTC | 20m |
| SWR122C | Swiss International | Zurich Airport (LSZH) | Zurich Airport (LSZH) | 2026-06-18 21:13 UTC | 2026-06-19 04:28 UTC | 7h 14m |
| N828SP |  | Whiteman Airport (KWHP) | Riverside Airport (KRAL) | 2026-06-19 03:40 UTC | 2026-06-19 04:20 UTC | 39m |
| N383PS |  | Logan-Cache Airport (KLGU) | Malad City Airport (KMLD) | 2026-06-19 03:56 UTC | 2026-06-19 04:20 UTC | 23m |
| JBU2322 | JetBlue | Palm Beach International Airport (KPBI) | General Edward Lawrence Logan International Airport (KBOS) | 2026-06-19 01:33 UTC | 2026-06-19 04:18 UTC | 2h 45m |
| N512TA |  | Georgetown Executive Airport (KGTU) | Austin-Bergstrom International Airport (KAUS) | 2026-06-19 04:02 UTC | 2026-06-19 04:18 UTC | 16m |
| N266MH |  | Erie-Ottawa International Airport (KPCW) | Toledo Suburban Airport (KDUH) | 2026-06-19 03:57 UTC | 2026-06-19 04:18 UTC | 21m |
| FIRE5 | FIR | Bob Hope Airport (KBUR) | Bob Hope Airport (KBUR) | 2026-06-19 03:08 UTC | 2026-06-19 04:14 UTC | 1h 6m |
| N3128T |  | Rocky Mountain Metro Airport (KBJC) | Pine Bluffs Municipal Airport (K82V) | 2026-06-19 03:32 UTC | 2026-06-19 04:12 UTC | 40m |
| N159U |  | Logan-Cache Airport (KLGU) | Preston Airport (KU10) | 2026-06-19 03:54 UTC | 2026-06-19 04:11 UTC | 17m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
