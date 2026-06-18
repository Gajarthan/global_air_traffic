# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--18_21:55:31_UTC-green)

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

**Latest saved flight:** 2026-06-18 21:55:31 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-18 21:55:31 UTC

- **114,122** saved flights
- **39,606** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **114,122** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,390,013.1 tonnes** estimated CO2 emissions
- **80,580,466 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4704 |
| 2 | SkyWest Airlines | 4259 |
| 3 | EJA | 2210 |
| 4 | IndiGo | 2205 |
| 5 | American Airlines | 1797 |
| 6 | Southwest Airlines | 1696 |
| 7 | ENY | 1421 |
| 8 | Delta Air Lines | 1344 |
| 9 | Lufthansa | 1272 |
| 10 | Vueling | 1036 |
| 11 | WIF | 1013 |
| 12 | LATAM Airlines | 1009 |
| 13 | AZU | 957 |
| 14 | AXM | 948 |
| 15 | LXJ | 869 |
| 16 | Swiss International | 810 |
| 17 | All Nippon Airways | 788 |
| 18 | Alaska Airlines | 770 |
| 19 | QLK | 744 |
| 20 | easyJet | 733 |
| 21 | EJU | 716 |
| 22 | Cathay Pacific | 671 |
| 23 | AEE | 639 |
| 24 | VIV | 633 |
| 25 | United Airlines | 632 |
| 26 | Air France | 630 |
| 27 | CXK | 605 |
| 28 | MXY | 605 |
| 29 | AXB | 558 |
| 30 | GLO | 558 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 96255 |
| 2 | 🇪🇸 ES | 7791 |
| 3 | 🇮🇳 IN | 6961 |
| 4 | 🇦🇺 AU | 6786 |
| 5 | 🇧🇷 BR | 6317 |
| 6 | 🇮🇹 IT | 6116 |
| 7 | 🇩🇪 DE | 6098 |
| 8 | 🇨🇦 CA | 5984 |
| 9 | 🇯🇵 JP | 5138 |
| 10 | 🇬🇧 GB | 4928 |
| 11 | 🇫🇷 FR | 4541 |
| 12 | 🇨🇴 CO | 3909 |
| 13 | 🇲🇽 MX | 3369 |
| 14 | 🇬🇷 GR | 3244 |
| 15 | 🇳🇴 NO | 3155 |
| 16 | 🇨🇭 CH | 2911 |
| 17 | 🇲🇾 MY | 2454 |
| 18 | 🇹🇷 TR | 2293 |
| 19 | 🇿🇦 ZA | 1931 |
| 20 | 🇳🇿 NZ | 1881 |
| 21 | 🇰🇷 KR | 1874 |
| 22 | 🇵🇱 PL | 1863 |
| 23 | 🇹🇭 TH | 1859 |
| 24 | 🇵🇭 PH | 1661 |
| 25 | 🇬🇹 GT | 1627 |
| 26 | 🇲🇦 MA | 1248 |
| 27 | 🇲🇴 MO | 1168 |
| 28 | 🇲🇪 ME | 1122 |
| 29 | 🇳🇱 NL | 1106 |
| 30 | 🇭🇷 HR | 992 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2424 |
| 2 | Denver International Airport |  | US | 1937 |
| 3 | Tokyo International Airport |  | JP | 1706 |
| 4 | Indira Gandhi International Airport |  | IN | 1519 |
| 5 | Guaymaral Airport |  | CO | 1445 |
| 6 | Harry Reid International Airport |  | US | 1434 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1402 |
| 8 | Zurich Airport |  | CH | 1278 |
| 9 | La Aurora Airport |  | GT | 1255 |
| 10 | Frankfurt am Main International Airport |  | DE | 1240 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1225 |
| 12 | Macau International Airport |  | MO | 1168 |
| 13 | El Dorado International Airport |  | CO | 1159 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1140 |
| 15 | Chicago O'Hare International Airport |  | US | 1127 |
| 16 | Capua Airport |  | IT | 991 |
| 17 | Madrid Barajas International Airport |  | ES | 981 |
| 18 | Salt Lake City International Airport |  | US | 969 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 959 |
| 20 | Kuala Lumpur International Airport |  | MY | 950 |
| 21 | Charlotte/Douglas International Airport |  | US | 883 |
| 22 | Congonhas Airport |  | BR | 875 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 852 |
| 24 | Charles de Gaulle International Airport |  | FR | 843 |
| 25 | Bengaluru International Airport |  | IN | 842 |
| 26 | Malpensa International Airport |  | IT | 821 |
| 27 | General Edward Lawrence Logan International Airport |  | US | 814 |
| 28 | Ninoy Aquino International Airport |  | PH | 766 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 752 |
| 30 | Daniel K Inouye International Airport |  | US | 747 |
| 31 | Tenerife Norte Airport |  | ES | 743 |
| 32 | Barcelona International Airport |  | ES | 734 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 719 |
| 34 | Don Mueang International Airport |  | TH | 675 |
| 35 | Vitoria/Foronda Airport |  | ES | 674 |
| 36 | Amsterdam Airport Schiphol |  | NL | 674 |
| 37 | Calgary International Airport |  | CA | 670 |
| 38 | Seattle-Tacoma International Airport |  | US | 658 |
| 39 | Viracopos International Airport |  | BR | 655 |
| 40 | Norman Y Mineta San Jose International Airport |  | US | 653 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 600 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 413 | 21m | 244 km | 1,739.0 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 304 | 24m | 225 km | 1,179.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 297 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 285 | 1h 7m | 706 km | 3,469.9 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 280 | 1h 25m | 910 km | 4,393.9 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 278 | 14m | 114 km | 545.2 t |
| 8 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 272 | 1h 10m | 770 km | 3,613.3 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 228 | 26m | 275 km | 1,080.4 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 227 | 19m | 165 km | 645.7 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 212 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 168 | 22m | 55 km | 159.7 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 168 | 20m | 99 km | 287.8 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 167 | 26m | 215 km | 618.5 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 166 | 13m | - | - |
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
| GMN82 | GMN | Mcnary Field (KSLE) | Mcnary Field (KSLE) | 2026-06-18 20:53 UTC | 2026-06-18 21:55 UTC | 1h 2m |
| SYS115 | SYS | RAF Shawbury (EGOS) | RAF Shawbury (EGOS) | 2026-06-18 21:34 UTC | 2026-06-18 21:53 UTC | 18m |
| N250RM |  | Pioneer Village Field (K0V3) | Lincoln Airport (KLNK) | 2026-06-18 21:32 UTC | 2026-06-18 21:52 UTC | 20m |
| AIC314 | Air India | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-06-18 17:12 UTC | 2026-06-18 21:51 UTC | 4h 38m |
| CPA234 | Cathay Pacific | Malpensa International Airport (LIMC) | Zhuhai Airport (ZGSD) | 2026-06-18 11:01 UTC | 2026-06-18 21:47 UTC | 10h 45m |
| CPA260 | Cathay Pacific | Charles de Gaulle International Airport (LFPG) | Macau International Airport (VMMC) | 2026-06-18 10:40 UTC | 2026-06-18 21:44 UTC | 11h 4m |
| ORO1042 | ORO | Barcelona International Airport (LEBL) | Ibiza Airport (LEIB) | 2026-06-18 21:03 UTC | 2026-06-18 21:42 UTC | 38m |
| BOE001 | BOE | Boeing Field/King County International Airport (KBFI) | Ephrata Municipal Airport (KEPH) | 2026-06-18 20:28 UTC | 2026-06-18 21:35 UTC | 1h 7m |
| N670CW |  | Anoka County/Blaine (Janes Field) Airport (KANE) | Dubuque Regional Airport (KDBQ) | 2026-06-18 20:53 UTC | 2026-06-18 21:33 UTC | 39m |
| N60CN |  | Tyler Pounds Regional Airport (KTYR) | 9TE3 (9TE3) | 2026-06-18 20:11 UTC | 2026-06-18 21:31 UTC | 1h 20m |
| LYRE71 | LYR | Burris Ranch Airport (2TE6) | Richie Rich Airport (8TE1) | 2026-06-18 21:06 UTC | 2026-06-18 21:30 UTC | 24m |
| N512HW |  | Palo Alto Airport (KPAO) | Tracy Municipal Airport (KTCY) | 2026-06-18 21:03 UTC | 2026-06-18 21:30 UTC | 26m |
| N82LL |  | Baton Rouge Metro, Ryan Field (KBTR) | Fred Netterville Lumber Company/Wilkinson Commnty Airport (MS57) | 2026-06-18 21:11 UTC | 2026-06-18 21:30 UTC | 18m |
| N99DQ |  | Republic Airport (KFRG) | Laguardia Airport (KLGA) | 2026-06-18 21:11 UTC | 2026-06-18 21:28 UTC | 16m |
| N68344 |  | Zamperini Field (KTOA) | Zamperini Field (KTOA) | 2026-06-18 20:38 UTC | 2026-06-18 21:21 UTC | 43m |
| N6338D |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-06-18 20:55 UTC | 2026-06-18 21:20 UTC | 25m |
| N744DA |  | Fairbanks International Airport (PAFA) | Edward G Pitka Sr Airport (PAGA) | 2026-06-18 20:14 UTC | 2026-06-18 21:18 UTC | 1h 4m |
| N598DR |  | St Paul Downtown Holman Field (KSTP) | WS05 (WS05) | 2026-06-18 20:59 UTC | 2026-06-18 21:18 UTC | 18m |
| N717FH |  | SN59 (SN59) | Arledge Field (KF56) | 2026-06-18 19:57 UTC | 2026-06-18 21:17 UTC | 1h 20m |
| N415HS |  | Tampa International Airport (KTPA) | Orlando Executive Airport (KORL) | 2026-06-18 20:47 UTC | 2026-06-18 21:15 UTC | 28m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
