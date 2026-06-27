# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--27_23:32:39_UTC-green)

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

**Latest saved flight:** 2026-06-27 23:32:39 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-27 23:32:39 UTC

- **122,070** saved flights
- **41,915** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **122,070** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,475,861.4 tonnes** estimated CO2 emissions
- **85,557,184 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4995 |
| 2 | SkyWest Airlines | 4518 |
| 3 | EJA | 2367 |
| 4 | IndiGo | 2328 |
| 5 | American Airlines | 1890 |
| 6 | Southwest Airlines | 1834 |
| 7 | ENY | 1528 |
| 8 | Delta Air Lines | 1447 |
| 9 | Lufthansa | 1321 |
| 10 | LATAM Airlines | 1092 |
| 11 | Vueling | 1089 |
| 12 | WIF | 1076 |
| 13 | AZU | 1025 |
| 14 | AXM | 983 |
| 15 | LXJ | 931 |
| 16 | Swiss International | 850 |
| 17 | All Nippon Airways | 825 |
| 18 | Alaska Airlines | 803 |
| 19 | easyJet | 784 |
| 20 | QLK | 775 |
| 21 | EJU | 764 |
| 22 | Cathay Pacific | 686 |
| 23 | AEE | 672 |
| 24 | Air France | 667 |
| 25 | VIV | 665 |
| 26 | United Airlines | 659 |
| 27 | CXK | 649 |
| 28 | MXY | 637 |
| 29 | JetBlue | 611 |
| 30 | AXB | 604 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 103858 |
| 2 | 🇪🇸 ES | 8238 |
| 3 | 🇮🇳 IN | 7317 |
| 4 | 🇦🇺 AU | 7135 |
| 5 | 🇧🇷 BR | 6745 |
| 6 | 🇩🇪 DE | 6486 |
| 7 | 🇮🇹 IT | 6483 |
| 8 | 🇨🇦 CA | 6436 |
| 9 | 🇯🇵 JP | 5393 |
| 10 | 🇬🇧 GB | 5354 |
| 11 | 🇫🇷 FR | 4834 |
| 12 | 🇨🇴 CO | 4026 |
| 13 | 🇲🇽 MX | 3561 |
| 14 | 🇬🇷 GR | 3468 |
| 15 | 🇳🇴 NO | 3357 |
| 16 | 🇨🇭 CH | 3128 |
| 17 | 🇲🇾 MY | 2549 |
| 18 | 🇹🇷 TR | 2520 |
| 19 | 🇿🇦 ZA | 2031 |
| 20 | 🇵🇱 PL | 2003 |
| 21 | 🇳🇿 NZ | 1976 |
| 22 | 🇰🇷 KR | 1925 |
| 23 | 🇹🇭 TH | 1923 |
| 24 | 🇵🇭 PH | 1746 |
| 25 | 🇬🇹 GT | 1699 |
| 26 | 🇲🇦 MA | 1310 |
| 27 | 🇲🇪 ME | 1213 |
| 28 | 🇲🇴 MO | 1176 |
| 29 | 🇳🇱 NL | 1163 |
| 30 | 🇧🇸 BS | 1053 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2568 |
| 2 | Denver International Airport |  | US | 2055 |
| 3 | Tokyo International Airport |  | JP | 1784 |
| 4 | Indira Gandhi International Airport |  | IN | 1613 |
| 5 | Harry Reid International Airport |  | US | 1527 |
| 6 | Guaymaral Airport |  | CO | 1516 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1469 |
| 8 | Zurich Airport |  | CH | 1350 |
| 9 | La Aurora Airport |  | GT | 1312 |
| 10 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1301 |
| 11 | Frankfurt am Main International Airport |  | DE | 1276 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1203 |
| 13 | Chicago O'Hare International Airport |  | US | 1186 |
| 14 | Macau International Airport |  | MO | 1176 |
| 15 | El Dorado International Airport |  | CO | 1171 |
| 16 | Salt Lake City International Airport |  | US | 1062 |
| 17 | Capua Airport |  | IT | 1042 |
| 18 | Madrid Barajas International Airport |  | ES | 1020 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1018 |
| 20 | Kuala Lumpur International Airport |  | MY | 988 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 963 |
| 22 | Congonhas Airport |  | BR | 946 |
| 23 | Charlotte/Douglas International Airport |  | US | 923 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 901 |
| 25 | Charles de Gaulle International Airport |  | FR | 894 |
| 26 | Bengaluru International Airport |  | IN | 879 |
| 27 | Malpensa International Airport |  | IT | 850 |
| 28 | Ninoy Aquino International Airport |  | PH | 809 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 797 |
| 30 | Daniel K Inouye International Airport |  | US | 785 |
| 31 | Barcelona International Airport |  | ES | 767 |
| 32 | Tenerife Norte Airport |  | ES | 762 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 748 |
| 34 | Calgary International Airport |  | CA | 717 |
| 35 | Vitoria/Foronda Airport |  | ES | 709 |
| 36 | Norman Y Mineta San Jose International Airport |  | US | 705 |
| 37 | Amsterdam Airport Schiphol |  | NL | 704 |
| 38 | Scottsdale Airport |  | US | 704 |
| 39 | Seattle-Tacoma International Airport |  | US | 701 |
| 40 | Don Mueang International Airport |  | TH | 695 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 632 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 445 | 21m | 244 km | 1,873.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 319 | 24m | 225 km | 1,237.6 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 310 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 293 | 1h 10m | 770 km | 3,892.3 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 292 | 1h 25m | 910 km | 4,582.2 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 239 | 26m | 275 km | 1,132.5 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 226 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 178 | 22m | 55 km | 169.2 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 175 | 26m | 215 km | 648.1 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 174 | 20m | 99 km | 298.0 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 170 | 13m | - | - |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 166 | 44m | 241 km | 689.5 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 166 | 27m | 152 km | 433.8 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 158 | 31m | 369 km | 1,005.7 t |
| 20 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 154 | 1h 44m | 1,423 km | 3,779.4 t |
| 21 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 154 | 44m | 452 km | 1,200.2 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 153 | 18m | 144 km | 380.6 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 150 | 20m | 250 km | 647.9 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 142 | 1h 38m | 1,156 km | 2,832.8 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 141 | 1h 1m | 695 km | 1,690.2 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 139 | 1h 17m | 961 km | 2,304.0 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 137 | 29m | 49 km | 115.8 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 137 | 13m | - | - |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 135 | 20m | 147 km | 341.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| PERRIS1 | PER | Perris Valley Airport (KL65) | Perris Valley Airport (KL65) | 2026-06-27 16:56 UTC | 2026-06-27 23:32 UTC | 6h 36m |
| N9678W |  | Paulding Northwest Atlanta Airport (KPUJ) | Paulding Northwest Atlanta Airport (KPUJ) | 2026-06-27 22:57 UTC | 2026-06-27 23:24 UTC | 27m |
| CNS568 | CNS | Witham Field (KSUA) | Austin Executive Airport (KEDC) | 2026-06-27 20:31 UTC | 2026-06-27 23:15 UTC | 2h 44m |
| CFRT71 | CFR | Ramona Airport (KRNM) | Hemet-Ryan Airport (KHMT) | 2026-06-27 21:33 UTC | 2026-06-27 23:15 UTC | 1h 41m |
| TKR101 | TKR | Animas Air Park (K00C) | Animas Air Park (K00C) | 2026-06-27 22:43 UTC | 2026-06-27 23:06 UTC | 23m |
| EJA392 | EJA | Truckee-Tahoe Airport (KTRK) | San Francisco International Airport (KSFO) | 2026-06-27 22:13 UTC | 2026-06-27 23:01 UTC | 47m |
|  |  | Chico Regional Airport (KCIC) | Chico Regional Airport (KCIC) | 2026-06-27 22:55 UTC | 2026-06-27 22:57 UTC | 1m |
| T73 |  | Hemet-Ryan Airport (KHMT) | Hemet-Ryan Airport (KHMT) | 2026-06-27 21:30 UTC | 2026-06-27 22:52 UTC | 1h 22m |
| N2464D |  | Montgomery-Gibbs Executive Airport (KMYF) | Gillespie Field (KSEE) | 2026-06-27 22:02 UTC | 2026-06-27 22:51 UTC | 49m |
| CFR74 | CFR | 95CA (95CA) | Hemet-Ryan Airport (KHMT) | 2026-06-27 21:52 UTC | 2026-06-27 22:51 UTC | 59m |
| TKR140 | TKR | Animas Air Park (K00C) | Blanding Municipal Airport (KBDG) | 2026-06-27 22:31 UTC | 2026-06-27 22:51 UTC | 20m |
| N812BP |  | 5TS0 (5TS0) | Archer City Municipal Airport (KT39) | 2026-06-27 22:03 UTC | 2026-06-27 22:51 UTC | 47m |
| N292LK |  | Delaware Municipal/Jim Moore Field (KDLZ) | Springfield/Beckley Municipal Airport (KSGH) | 2026-06-27 22:28 UTC | 2026-06-27 22:48 UTC | 20m |
| TKR105 | TKR | Animas Air Park (K00C) | Blanding Municipal Airport (KBDG) | 2026-06-27 22:30 UTC | 2026-06-27 22:44 UTC | 13m |
| XSN25 | XSN | Vineyard Oaks Farm Airport (CN15) | Palo Alto Airport (KPAO) | 2026-06-27 22:04 UTC | 2026-06-27 22:44 UTC | 39m |
| N457TS |  | Long Beach (Daugherty Field) Airport (KLGB) | Zamperini Field (KTOA) | 2026-06-27 22:08 UTC | 2026-06-27 22:43 UTC | 34m |
| C6018 |  | Ted Stevens Anchorage International Airport (PANC) | Ted Stevens Anchorage International Airport (PANC) | 2026-06-27 22:09 UTC | 2026-06-27 22:40 UTC | 31m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-06-27 22:22 UTC | 2026-06-27 22:38 UTC | 16m |
| N6748P |  | Las Cruces International Airport (KLRU) | Yucca Valley Airport (KL22) | 2026-06-27 19:26 UTC | 2026-06-27 22:37 UTC | 3h 10m |
| DHEEZ | DHE | Lake Havasu City Airport (KHII) | Massey Farm Airport (AZ34) | 2026-06-27 22:20 UTC | 2026-06-27 22:34 UTC | 14m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
