# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--04_18:00:16_UTC-green)

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

**Latest saved flight:** 2026-08-04 18:00:16 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-04 18:00:16 UTC

- **170,808** saved flights
- **55,620** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **170,808** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,058,479.5 tonnes** estimated CO2 emissions
- **119,332,143 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6802 |
| 2 | SkyWest Airlines | 6235 |
| 3 | EJA | 3389 |
| 4 | IndiGo | 3004 |
| 5 | Southwest Airlines | 2687 |
| 6 | American Airlines | 2686 |
| 7 | ENY | 2127 |
| 8 | Delta Air Lines | 2032 |
| 9 | LATAM Airlines | 1581 |
| 10 | Lufthansa | 1564 |
| 11 | AZU | 1502 |
| 12 | WIF | 1429 |
| 13 | Vueling | 1405 |
| 14 | LXJ | 1338 |
| 15 | AXM | 1176 |
| 16 | Swiss International | 1164 |
| 17 | easyJet | 1149 |
| 18 | EJU | 1046 |
| 19 | Alaska Airlines | 1042 |
| 20 | QLK | 1041 |
| 21 | All Nippon Airways | 1036 |
| 22 | VIV | 942 |
| 23 | Cathay Pacific | 916 |
| 24 | CXK | 909 |
| 25 | United Airlines | 897 |
| 26 | GLO | 893 |
| 27 | AEE | 892 |
| 28 | Air France | 878 |
| 29 | MXY | 869 |
| 30 | JetBlue | 856 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 147177 |
| 2 | 🇪🇸 ES | 10956 |
| 3 | 🇧🇷 BR | 9701 |
| 4 | 🇦🇺 AU | 9521 |
| 5 | 🇮🇳 IN | 9408 |
| 6 | 🇨🇦 CA | 9304 |
| 7 | 🇮🇹 IT | 8840 |
| 8 | 🇩🇪 DE | 8502 |
| 9 | 🇬🇧 GB | 7922 |
| 10 | 🇯🇵 JP | 6872 |
| 11 | 🇫🇷 FR | 6783 |
| 12 | 🇨🇴 CO | 6202 |
| 13 | 🇬🇷 GR | 4974 |
| 14 | 🇲🇽 MX | 4889 |
| 15 | 🇨🇭 CH | 4494 |
| 16 | 🇳🇴 NO | 4459 |
| 17 | 🇹🇷 TR | 4174 |
| 18 | 🇲🇾 MY | 3057 |
| 19 | 🇵🇱 PL | 2871 |
| 20 | 🇿🇦 ZA | 2764 |
| 21 | 🇹🇭 TH | 2486 |
| 22 | 🇳🇿 NZ | 2471 |
| 23 | 🇵🇭 PH | 2255 |
| 24 | 🇬🇹 GT | 2199 |
| 25 | 🇰🇷 KR | 2161 |
| 26 | 🇲🇦 MA | 1721 |
| 27 | 🇭🇷 HR | 1644 |
| 28 | 🇲🇪 ME | 1572 |
| 29 | 🇳🇱 NL | 1553 |
| 30 | 🇲🇴 MO | 1460 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3514 |
| 2 | Denver International Airport |  | US | 2822 |
| 3 | Tokyo International Airport |  | JP | 2156 |
| 4 | Guaymaral Airport |  | CO | 2115 |
| 5 | Indira Gandhi International Airport |  | IN | 2085 |
| 6 | Harry Reid International Airport |  | US | 2050 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1867 |
| 8 | Zurich Airport |  | CH | 1806 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1799 |
| 10 | La Aurora Airport |  | GT | 1697 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1572 |
| 12 | Chicago O'Hare International Airport |  | US | 1549 |
| 13 | El Dorado International Airport |  | CO | 1548 |
| 14 | Salt Lake City International Airport |  | US | 1530 |
| 15 | Frankfurt am Main International Airport |  | DE | 1527 |
| 16 | Macau International Airport |  | MO | 1460 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1402 |
| 18 | Congonhas Airport |  | BR | 1398 |
| 19 | Madrid Barajas International Airport |  | ES | 1339 |
| 20 | Capua Airport |  | IT | 1331 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1290 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1203 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1193 |
| 24 | Charlotte/Douglas International Airport |  | US | 1186 |
| 25 | Charles de Gaulle International Airport |  | FR | 1158 |
| 26 | Malpensa International Airport |  | IT | 1152 |
| 27 | Kuala Lumpur International Airport |  | MY | 1151 |
| 28 | Bengaluru International Airport |  | IN | 1120 |
| 29 | Ninoy Aquino International Airport |  | PH | 1061 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1059 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1053 |
| 32 | Barcelona International Airport |  | ES | 1012 |
| 33 | Daniel K Inouye International Airport |  | US | 991 |
| 34 | Seattle-Tacoma International Airport |  | US | 985 |
| 35 | Viracopos International Airport |  | BR | 970 |
| 36 | Calgary International Airport |  | CA | 968 |
| 37 | Reno/Tahoe International Airport |  | US | 957 |
| 38 | Oslo Gardermoen Airport |  | NO | 951 |
| 39 | Tenerife Norte Airport |  | ES | 949 |
| 40 | Scottsdale Airport |  | US | 939 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 877 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 624 | 21m | 244 km | 2,627.5 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 405 | 24m | 225 km | 1,571.2 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 405 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 387 | 1h 8m | 770 km | 5,141.0 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 318 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 292 | 27m | 275 km | 1,383.7 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 255 | 22m | 55 km | 242.4 t |
| 13 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 254 | 44m | 241 km | 1,055.1 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 235 | 1h 47m | 1,423 km | 5,767.3 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 223 | 20m | 250 km | 963.2 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 222 | 26m | 215 km | 822.2 t |
| 18 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 216 | 13m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 211 | 20m | 99 km | 361.4 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 203 | 1h 15m | 961 km | 3,364.8 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 203 | 19m | 144 km | 505.0 t |
| 23 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 202 | 50m | 556 km | 1,936.3 t |
| 24 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 199 | 28m | 152 km | 520.1 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 199 | 12m | - | - |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 197 | 31m | 369 km | 1,254.0 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 192 | 1h 38m | 1,156 km | 3,830.3 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 188 | 24m | 218 km | 708.3 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 186 | 1h 1m | 695 km | 2,229.6 t |
| 30 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 185 | 8m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N626LM |  | Sussex Airport (KFWN) | Sussex Airport (KFWN) | 2026-08-04 17:43 UTC | 2026-08-04 18:00 UTC | 16m |
| JPR41 | JPR | Alpine County Airport (KM45) | Alpine County Airport (KM45) | 2026-08-04 17:46 UTC | 2026-08-04 17:57 UTC | 10m |
| N586EF |  | Monmouth Executive Airport (KBLM) | Lehigh Valley International Airport (KABE) | 2026-08-04 17:16 UTC | 2026-08-04 17:56 UTC | 40m |
| N509LM |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-08-04 17:04 UTC | 2026-08-04 17:56 UTC | 51m |
|  |  | Livermore Municipal Airport (KLVK) | Livermore Municipal Airport (KLVK) | 2026-08-04 17:53 UTC | 2026-08-04 17:53 UTC | 0m |
| N331RF |  | Sparwood Elk Valley Airport (CYSW) | Sparwood Elk Valley Airport (CYSW) | 2026-08-04 17:27 UTC | 2026-08-04 17:44 UTC | 16m |
| ERU98 | ERU | Robin Airport (59AZ) | Montezuma Airport (19AZ) | 2026-08-04 17:28 UTC | 2026-08-04 17:42 UTC | 13m |
| CPA2046 | Cathay Pacific | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-08-04 13:09 UTC | 2026-08-04 17:41 UTC | 4h 31m |
| N27AU |  | Andrews University Airpark (KC20) | Southwest Michigan Regional Airport (KBEH) | 2026-08-04 16:42 UTC | 2026-08-04 17:40 UTC | 58m |
| N41369 |  | Van Nuys Airport (KVNY) | San Bernardino International Airport (KSBD) | 2026-08-04 16:53 UTC | 2026-08-04 17:34 UTC | 41m |
| GRA325 | GRA | Tambor Airport (MRTR) | Juan Santamaria International Airport (MROC) | 2026-08-04 17:10 UTC | 2026-08-04 17:33 UTC | 23m |
| RDHWK08 | RDH | Kelso Valley Airport (CN37) | Boron Airstrip (57CL) | 2026-08-04 17:14 UTC | 2026-08-04 17:33 UTC | 18m |
| N193CP |  | Winter Haven Regional Airport (KGIF) | Gore Airport (4FL9) | 2026-08-04 17:20 UTC | 2026-08-04 17:31 UTC | 11m |
| JPR41 | JPR | Minden-Tahoe Airport (KMEV) | Lake Tahoe Airport (KTVL) | 2026-08-04 17:20 UTC | 2026-08-04 17:31 UTC | 10m |
| XCGNL | XCG | Del Norte International Airport (MMAN) | Del Norte International Airport (MMAN) | 2026-08-04 17:09 UTC | 2026-08-04 17:28 UTC | 18m |
| N173AC |  | Elefsis Airport (LGEL) | Megara Airport (LGMG) | 2026-08-04 17:08 UTC | 2026-08-04 17:26 UTC | 17m |
| N711FP |  | Denton Enterprise Airport (KDTO) | Easterwood Field (KCLL) | 2026-08-04 16:51 UTC | 2026-08-04 17:25 UTC | 33m |
| N9251W |  | Vance Brand Airport (KLMO) | Rocky Mountain Metro Airport (KBJC) | 2026-08-04 16:54 UTC | 2026-08-04 17:23 UTC | 29m |
| N521NG |  | Carson City Airport (KCXP) | Lake Tahoe Airport (KTVL) | 2026-08-04 17:06 UTC | 2026-08-04 17:23 UTC | 16m |
| LYM5411 | LYM | Dallas-Fort Worth International Airport (KDFW) | 30XS (30XS) | 2026-08-04 16:31 UTC | 2026-08-04 17:20 UTC | 48m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
