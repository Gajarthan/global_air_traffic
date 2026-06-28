# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--28_14:30:57_UTC-green)

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

**Latest saved flight:** 2026-06-28 14:30:57 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-28 14:30:57 UTC

- **122,484** saved flights
- **42,021** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **122,484** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,481,244.2 tonnes** estimated CO2 emissions
- **85,869,229 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5022 |
| 2 | SkyWest Airlines | 4520 |
| 3 | EJA | 2368 |
| 4 | IndiGo | 2348 |
| 5 | American Airlines | 1890 |
| 6 | Southwest Airlines | 1834 |
| 7 | ENY | 1529 |
| 8 | Delta Air Lines | 1450 |
| 9 | Lufthansa | 1323 |
| 10 | LATAM Airlines | 1095 |
| 11 | Vueling | 1092 |
| 12 | WIF | 1081 |
| 13 | AZU | 1029 |
| 14 | AXM | 988 |
| 15 | LXJ | 933 |
| 16 | Swiss International | 855 |
| 17 | All Nippon Airways | 832 |
| 18 | Alaska Airlines | 803 |
| 19 | easyJet | 786 |
| 20 | QLK | 778 |
| 21 | EJU | 767 |
| 22 | Cathay Pacific | 687 |
| 23 | AEE | 679 |
| 24 | Air France | 670 |
| 25 | VIV | 667 |
| 26 | United Airlines | 659 |
| 27 | CXK | 650 |
| 28 | MXY | 639 |
| 29 | JetBlue | 613 |
| 30 | AXB | 610 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 103963 |
| 2 | 🇪🇸 ES | 8267 |
| 3 | 🇮🇳 IN | 7372 |
| 4 | 🇦🇺 AU | 7179 |
| 5 | 🇧🇷 BR | 6773 |
| 6 | 🇩🇪 DE | 6519 |
| 7 | 🇮🇹 IT | 6519 |
| 8 | 🇨🇦 CA | 6443 |
| 9 | 🇯🇵 JP | 5427 |
| 10 | 🇬🇧 GB | 5399 |
| 11 | 🇫🇷 FR | 4872 |
| 12 | 🇨🇴 CO | 4027 |
| 13 | 🇲🇽 MX | 3566 |
| 14 | 🇬🇷 GR | 3494 |
| 15 | 🇳🇴 NO | 3370 |
| 16 | 🇨🇭 CH | 3148 |
| 17 | 🇲🇾 MY | 2557 |
| 18 | 🇹🇷 TR | 2546 |
| 19 | 🇿🇦 ZA | 2039 |
| 20 | 🇵🇱 PL | 2014 |
| 21 | 🇳🇿 NZ | 1986 |
| 22 | 🇹🇭 TH | 1931 |
| 23 | 🇰🇷 KR | 1926 |
| 24 | 🇵🇭 PH | 1758 |
| 25 | 🇬🇹 GT | 1699 |
| 26 | 🇲🇦 MA | 1313 |
| 27 | 🇲🇪 ME | 1221 |
| 28 | 🇲🇴 MO | 1176 |
| 29 | 🇳🇱 NL | 1169 |
| 30 | 🇧🇸 BS | 1058 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2568 |
| 2 | Denver International Airport |  | US | 2056 |
| 3 | Tokyo International Airport |  | JP | 1797 |
| 4 | Indira Gandhi International Airport |  | IN | 1625 |
| 5 | Harry Reid International Airport |  | US | 1527 |
| 6 | Guaymaral Airport |  | CO | 1517 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1478 |
| 8 | Zurich Airport |  | CH | 1355 |
| 9 | La Aurora Airport |  | GT | 1312 |
| 10 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1301 |
| 11 | Frankfurt am Main International Airport |  | DE | 1277 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1203 |
| 13 | Chicago O'Hare International Airport |  | US | 1186 |
| 14 | Macau International Airport |  | MO | 1176 |
| 15 | El Dorado International Airport |  | CO | 1171 |
| 16 | Salt Lake City International Airport |  | US | 1063 |
| 17 | Capua Airport |  | IT | 1047 |
| 18 | Madrid Barajas International Airport |  | ES | 1021 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1019 |
| 20 | Kuala Lumpur International Airport |  | MY | 993 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 964 |
| 22 | Congonhas Airport |  | BR | 949 |
| 23 | Charlotte/Douglas International Airport |  | US | 924 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 905 |
| 25 | Charles de Gaulle International Airport |  | FR | 897 |
| 26 | Bengaluru International Airport |  | IN | 885 |
| 27 | Malpensa International Airport |  | IT | 851 |
| 28 | Ninoy Aquino International Airport |  | PH | 815 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 800 |
| 30 | Daniel K Inouye International Airport |  | US | 785 |
| 31 | Barcelona International Airport |  | ES | 769 |
| 32 | Tenerife Norte Airport |  | ES | 763 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 748 |
| 34 | Calgary International Airport |  | CA | 717 |
| 35 | Vitoria/Foronda Airport |  | ES | 713 |
| 36 | Norman Y Mineta San Jose International Airport |  | US | 706 |
| 37 | Amsterdam Airport Schiphol |  | NL | 706 |
| 38 | Scottsdale Airport |  | US | 704 |
| 39 | Seattle-Tacoma International Airport |  | US | 702 |
| 40 | Don Mueang International Airport |  | TH | 698 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 632 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 445 | 21m | 244 km | 1,873.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 320 | 24m | 225 km | 1,241.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 310 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 296 | 1h 10m | 770 km | 3,932.1 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 294 | 1h 25m | 910 km | 4,613.5 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 240 | 26m | 275 km | 1,137.3 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 231 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 178 | 22m | 55 km | 169.2 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 177 | 26m | 215 km | 655.5 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 174 | 20m | 99 km | 298.0 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 170 | 13m | - | - |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 167 | 44m | 241 km | 693.7 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 166 | 27m | 152 km | 433.8 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 158 | 31m | 369 km | 1,005.7 t |
| 20 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 156 | 1h 44m | 1,423 km | 3,828.5 t |
| 21 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 155 | 44m | 452 km | 1,208.0 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 154 | 18m | 144 km | 383.1 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 151 | 20m | 250 km | 652.2 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 143 | 1h 38m | 1,156 km | 2,852.8 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 141 | 1h 1m | 695 km | 1,690.2 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 139 | 1h 17m | 961 km | 2,304.0 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 137 | 29m | 49 km | 115.8 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 137 | 13m | - | - |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 135 | 20m | 147 km | 341.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N636CB |  | Chicago Executive Airport (KPWK) | Chicago Executive Airport (KPWK) | 2026-06-28 13:34 UTC | 2026-06-28 14:30 UTC | 56m |
| N97681 |  | Fernando Luis Ribas Dominicci Airport (TJIG) | Cuylers Airport (02PR) | 2026-06-28 14:14 UTC | 2026-06-28 14:28 UTC | 14m |
| FHDSA | FHD | Vannes-Meucon Airport (LFRV) | Vannes-Meucon Airport (LFRV) | 2026-06-28 14:09 UTC | 2026-06-28 14:25 UTC | 15m |
| LOBO715 | LOB | Albert J Ellis Airport (KOAJ) | Martin State Airport (KMTN) | 2026-06-28 13:30 UTC | 2026-06-28 14:23 UTC | 52m |
| JYRJK | JYR | Amman-Marka International Airport (OJAM) | Queen Alia International Airport (OJAI) | 2026-06-28 14:00 UTC | 2026-06-28 14:23 UTC | 22m |
| N9614H |  | Greeley-Weld County Airport (KGXY) | Laramie Regional Airport (KLAR) | 2026-06-28 13:43 UTC | 2026-06-28 14:17 UTC | 34m |
| N778AM |  | Erie Municipal Airport (KEIK) | Erie Municipal Airport (KEIK) | 2026-06-28 13:57 UTC | 2026-06-28 14:16 UTC | 19m |
| FHPCJ | FHP | Marennes Le Bournet Airport (LFJI) | Rochefort-Saint-Agnant (BA 721) Airport (LFDN) | 2026-06-28 14:05 UTC | 2026-06-28 14:16 UTC | 11m |
| N9244H |  | Grosse Ile Municipal Airport (KONZ) | Hillsdale Municipal Airport (KJYM) | 2026-06-28 13:44 UTC | 2026-06-28 14:15 UTC | 31m |
| OEEGR | OEE | Losinj Island Airport (LDLO) | Hohenems-Dornbirn Airport (LOIH) | 2026-06-28 12:57 UTC | 2026-06-28 14:15 UTC | 1h 18m |
| N87RM |  | Perrotti Skyranch Airfield (09ME) | Skydive New England Airport (ME64) | 2026-06-28 12:43 UTC | 2026-06-28 14:08 UTC | 1h 24m |
| N997SE |  | Meadows Field (KBFL) | Shafter-Minter Field (KMIT) | 2026-06-28 13:22 UTC | 2026-06-28 14:05 UTC | 43m |
| N901BS |  | P K Airpark (K5W4) | P K Airpark (K5W4) | 2026-06-28 12:04 UTC | 2026-06-28 14:02 UTC | 1h 58m |
| N2112K |  | Erie Municipal Airport (KEIK) | Erie Municipal Airport (KEIK) | 2026-06-28 13:46 UTC | 2026-06-28 14:01 UTC | 14m |
| SAMU06 | SAM | Nice-Cote d'Azur Airport (LFMN) | Nice-Cote d'Azur Airport (LFMN) | 2026-06-28 13:54 UTC | 2026-06-28 14:00 UTC | 5m |
| N4071R |  | North Las Vegas Airport (KVGT) | St George Regional Airport (KSGU) | 2026-06-28 13:10 UTC | 2026-06-28 13:59 UTC | 49m |
| N90CG |  | Palm Beach International Airport (KPBI) | Bangor International Airport (KBGR) | 2026-06-28 11:09 UTC | 2026-06-28 13:58 UTC | 2h 49m |
| GAWGB | GAW | Wolverhampton Halfpenny Green Airport (EGBO) | Wolverhampton Halfpenny Green Airport (EGBO) | 2026-06-28 13:39 UTC | 2026-06-28 13:57 UTC | 17m |
| N34HF |  | Newark Liberty International Airport (KEWR) | Francis S Gabreski Airport (KFOK) | 2026-06-28 13:21 UTC | 2026-06-28 13:56 UTC | 35m |
| HB3284 |  | Saanen Airport (LSGK) | Saanen Airport (LSGK) | 2026-06-28 12:57 UTC | 2026-06-28 13:56 UTC | 59m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
