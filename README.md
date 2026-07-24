# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--24_17:05:06_UTC-green)

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

**Latest saved flight:** 2026-07-24 17:05:06 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-24 17:05:06 UTC

- **148,175** saved flights
- **49,445** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **148,175** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,772,535.5 tonnes** estimated CO2 emissions
- **102,755,682 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5989 |
| 2 | SkyWest Airlines | 5415 |
| 3 | EJA | 2926 |
| 4 | IndiGo | 2665 |
| 5 | American Airlines | 2355 |
| 6 | Southwest Airlines | 2241 |
| 7 | ENY | 1844 |
| 8 | Delta Air Lines | 1750 |
| 9 | Lufthansa | 1454 |
| 10 | LATAM Airlines | 1365 |
| 11 | AZU | 1280 |
| 12 | WIF | 1262 |
| 13 | Vueling | 1255 |
| 14 | LXJ | 1137 |
| 15 | AXM | 1071 |
| 16 | Swiss International | 1050 |
| 17 | easyJet | 955 |
| 18 | All Nippon Airways | 937 |
| 19 | Alaska Airlines | 927 |
| 20 | QLK | 922 |
| 21 | EJU | 904 |
| 22 | VIV | 820 |
| 23 | CXK | 793 |
| 24 | AEE | 779 |
| 25 | Air France | 777 |
| 26 | JetBlue | 775 |
| 27 | Cathay Pacific | 773 |
| 28 | MXY | 771 |
| 29 | GLO | 767 |
| 30 | United Airlines | 766 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 127738 |
| 2 | 🇪🇸 ES | 9576 |
| 3 | 🇦🇺 AU | 8459 |
| 4 | 🇧🇷 BR | 8369 |
| 5 | 🇮🇳 IN | 8366 |
| 6 | 🇨🇦 CA | 7926 |
| 7 | 🇮🇹 IT | 7676 |
| 8 | 🇩🇪 DE | 7602 |
| 9 | 🇬🇧 GB | 6776 |
| 10 | 🇯🇵 JP | 6154 |
| 11 | 🇫🇷 FR | 5882 |
| 12 | 🇨🇴 CO | 4948 |
| 13 | 🇲🇽 MX | 4293 |
| 14 | 🇬🇷 GR | 4196 |
| 15 | 🇳🇴 NO | 3959 |
| 16 | 🇨🇭 CH | 3897 |
| 17 | 🇹🇷 TR | 3475 |
| 18 | 🇲🇾 MY | 2790 |
| 19 | 🇵🇱 PL | 2500 |
| 20 | 🇿🇦 ZA | 2402 |
| 21 | 🇳🇿 NZ | 2243 |
| 22 | 🇹🇭 TH | 2167 |
| 23 | 🇰🇷 KR | 2055 |
| 24 | 🇵🇭 PH | 1977 |
| 25 | 🇬🇹 GT | 1921 |
| 26 | 🇲🇦 MA | 1517 |
| 27 | 🇲🇪 ME | 1467 |
| 28 | 🇳🇱 NL | 1378 |
| 29 | 🇭🇷 HR | 1347 |
| 30 | 🇲🇴 MO | 1236 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3046 |
| 2 | Denver International Airport |  | US | 2480 |
| 3 | Tokyo International Airport |  | JP | 1972 |
| 4 | Indira Gandhi International Airport |  | IN | 1857 |
| 5 | Guaymaral Airport |  | CO | 1843 |
| 6 | Harry Reid International Airport |  | US | 1841 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1666 |
| 8 | Zurich Airport |  | CH | 1631 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1560 |
| 10 | La Aurora Airport |  | GT | 1489 |
| 11 | Frankfurt am Main International Airport |  | DE | 1404 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1392 |
| 13 | Chicago O'Hare International Airport |  | US | 1370 |
| 14 | El Dorado International Airport |  | CO | 1331 |
| 15 | Salt Lake City International Airport |  | US | 1330 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1276 |
| 17 | Macau International Airport |  | MO | 1236 |
| 18 | Congonhas Airport |  | BR | 1195 |
| 19 | Capua Airport |  | IT | 1193 |
| 20 | Madrid Barajas International Airport |  | ES | 1176 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1156 |
| 22 | Kuala Lumpur International Airport |  | MY | 1075 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1066 |
| 24 | Charlotte/Douglas International Airport |  | US | 1056 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1041 |
| 26 | Charles de Gaulle International Airport |  | FR | 1025 |
| 27 | Bengaluru International Airport |  | IN | 1000 |
| 28 | Malpensa International Airport |  | IT | 960 |
| 29 | Ninoy Aquino International Airport |  | PH | 926 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 903 |
| 31 | Barcelona International Airport |  | ES | 894 |
| 32 | Daniel K Inouye International Airport |  | US | 888 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 886 |
| 34 | Seattle-Tacoma International Airport |  | US | 849 |
| 35 | Tenerife Norte Airport |  | ES | 848 |
| 36 | Calgary International Airport |  | CA | 845 |
| 37 | Scottsdale Airport |  | US | 839 |
| 38 | Viracopos International Airport |  | BR | 836 |
| 39 | Amsterdam Airport Schiphol |  | NL | 829 |
| 40 | Oslo Gardermoen Airport |  | NO | 821 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 778 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 536 | 21m | 244 km | 2,256.9 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 360 | 24m | 225 km | 1,396.6 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 359 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 346 | 1h 9m | 770 km | 4,596.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 300 | 14m | 114 km | 588.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 289 | 1h 7m | 706 km | 3,518.6 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 269 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 265 | 27m | 275 km | 1,255.7 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 222 | 22m | 55 km | 211.0 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 201 | 44m | 241 km | 834.9 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 199 | 1h 46m | 1,423 km | 4,883.8 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 197 | 26m | 215 km | 729.6 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 195 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 192 | 20m | 99 km | 328.9 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 182 | 20m | 250 km | 786.1 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 181 | 27m | 152 km | 473.0 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 175 | 31m | 369 km | 1,113.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 174 | 18m | 144 km | 432.8 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 173 | 1h 16m | 961 km | 2,867.6 t |
| 24 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 171 | 12m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 170 | 44m | 452 km | 1,324.9 t |
| 27 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 168 | 1h 1m | 695 km | 2,013.8 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 167 | 1h 39m | 1,156 km | 3,331.6 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 162 | 14m | 154 km | 429.2 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 162 | 55m | 136 km | 379.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N7614Y |  | Lenawee County Airport (KADG) | Lenawee County Airport (KADG) | 2026-07-24 16:47 UTC | 2026-07-24 17:05 UTC | 17m |
| CGNSS | CGN | Prince George Airport (CYXS) | Prince George Airport (CYXS) | 2026-07-24 16:10 UTC | 2026-07-24 17:04 UTC | 53m |
| OKFUA74 | OKF | Usti Mad Orlici Airport (LKUO) | Usti Mad Orlici Airport (LKUO) | 2026-07-24 16:51 UTC | 2026-07-24 17:04 UTC | 12m |
| OOVOL | OOV | Spa (la Sauveniere) Airport (EBSP) | Spa (la Sauveniere) Airport (EBSP) | 2026-07-24 16:38 UTC | 2026-07-24 16:57 UTC | 19m |
| N606LB |  | 5IA7 (5IA7) | 5IA7 (5IA7) | 2026-07-24 15:47 UTC | 2026-07-24 16:52 UTC | 1h 4m |
| WMU63 | WMU | Battle Creek Executive At Kellogg Field (KBTL) | Battle Creek Executive At Kellogg Field (KBTL) | 2026-07-24 16:18 UTC | 2026-07-24 16:51 UTC | 33m |
| N3299D |  | Chorman Airport (KD74) | Whalen Field (25MD) | 2026-07-24 16:39 UTC | 2026-07-24 16:51 UTC | 11m |
| RYR3QN | Ryanair | Malpensa International Airport (LIMC) | Malpensa International Airport (LIMC) | 2026-07-24 16:36 UTC | 2026-07-24 16:50 UTC | 13m |
| N522PM |  | Centennial Airport (KAPA) | Tinnes Airport (CD03) | 2026-07-24 15:52 UTC | 2026-07-24 16:47 UTC | 54m |
| N32403 |  | Lake In The Hills Airport (K3CK) | De Kalb Taylor Municipal Airport (KDKB) | 2026-07-24 16:07 UTC | 2026-07-24 16:42 UTC | 34m |
| N72LA |  | La Cabana Airport (MSLC) | Laredo International Airport (KLRD) | 2026-07-24 14:03 UTC | 2026-07-24 16:41 UTC | 2h 38m |
| 96FUJ |  | Fujairah International Airport (OMFJ) | Ras Al Khaimah International Airport (OMRK) | 2026-07-24 16:13 UTC | 2026-07-24 16:41 UTC | 27m |
| N262WJ |  | Aurora Municipal Airport (KARR) | Walnut Creek Airport (49IL) | 2026-07-24 16:33 UTC | 2026-07-24 16:40 UTC | 6m |
| EXP800 | EXP | Klawock Airport (PAKW) | Sitka Rocky Gutierrez Airport (PASI) | 2026-07-24 15:58 UTC | 2026-07-24 16:39 UTC | 41m |
| ORCA70 | ORC | Travis Afb Airport (KSUU) | Truth Or Consequences Municipal Airport (KTCS) | 2026-07-24 14:28 UTC | 2026-07-24 16:38 UTC | 2h 10m |
| N491SF |  | Jim & Julie's Airport (96WA) | Jim & Julie's Airport (96WA) | 2026-07-24 16:13 UTC | 2026-07-24 16:38 UTC | 25m |
| N602RE |  | Fulton County Airport (KUSE) | Fulton County Airport (KUSE) | 2026-07-24 15:38 UTC | 2026-07-24 16:36 UTC | 58m |
| CGJKI | CGJ | Halifax Robert L. Stanfield International Airport (CYHZ) | CRM4 (CRM4) | 2026-07-24 16:21 UTC | 2026-07-24 16:35 UTC | 14m |
| SCREE10 | SCR | Hunter Army Air Field (KSVN) | Hunter Army Air Field (KSVN) | 2026-07-24 16:23 UTC | 2026-07-24 16:34 UTC | 10m |
| N518TA |  | Goshute Airport (UT65) | Michael Army Air Field (Dugway Proving Ground) Airport (KDPG) | 2026-07-24 16:22 UTC | 2026-07-24 16:32 UTC | 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
