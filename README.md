# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--24_15:33:06_UTC-green)

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

**Latest saved flight:** 2026-07-24 15:33:06 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-24 15:33:06 UTC

- **147,912** saved flights
- **49,375** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **147,912** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,770,273.6 tonnes** estimated CO2 emissions
- **102,624,556 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5979 |
| 2 | SkyWest Airlines | 5406 |
| 3 | EJA | 2921 |
| 4 | IndiGo | 2660 |
| 5 | American Airlines | 2350 |
| 6 | Southwest Airlines | 2236 |
| 7 | ENY | 1839 |
| 8 | Delta Air Lines | 1749 |
| 9 | Lufthansa | 1453 |
| 10 | LATAM Airlines | 1362 |
| 11 | AZU | 1278 |
| 12 | WIF | 1260 |
| 13 | Vueling | 1251 |
| 14 | LXJ | 1135 |
| 15 | AXM | 1071 |
| 16 | Swiss International | 1049 |
| 17 | easyJet | 953 |
| 18 | All Nippon Airways | 937 |
| 19 | Alaska Airlines | 926 |
| 20 | QLK | 922 |
| 21 | EJU | 904 |
| 22 | VIV | 820 |
| 23 | CXK | 793 |
| 24 | AEE | 779 |
| 25 | JetBlue | 775 |
| 26 | Air France | 774 |
| 27 | Cathay Pacific | 773 |
| 28 | MXY | 771 |
| 29 | United Airlines | 766 |
| 30 | GLO | 765 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 127484 |
| 2 | 🇪🇸 ES | 9555 |
| 3 | 🇦🇺 AU | 8459 |
| 4 | 🇧🇷 BR | 8356 |
| 5 | 🇮🇳 IN | 8351 |
| 6 | 🇨🇦 CA | 7909 |
| 7 | 🇮🇹 IT | 7666 |
| 8 | 🇩🇪 DE | 7584 |
| 9 | 🇬🇧 GB | 6758 |
| 10 | 🇯🇵 JP | 6154 |
| 11 | 🇫🇷 FR | 5872 |
| 12 | 🇨🇴 CO | 4921 |
| 13 | 🇲🇽 MX | 4288 |
| 14 | 🇬🇷 GR | 4192 |
| 15 | 🇳🇴 NO | 3949 |
| 16 | 🇨🇭 CH | 3890 |
| 17 | 🇹🇷 TR | 3469 |
| 18 | 🇲🇾 MY | 2790 |
| 19 | 🇵🇱 PL | 2497 |
| 20 | 🇿🇦 ZA | 2396 |
| 21 | 🇳🇿 NZ | 2243 |
| 22 | 🇹🇭 TH | 2166 |
| 23 | 🇰🇷 KR | 2055 |
| 24 | 🇵🇭 PH | 1977 |
| 25 | 🇬🇹 GT | 1919 |
| 26 | 🇲🇦 MA | 1517 |
| 27 | 🇲🇪 ME | 1464 |
| 28 | 🇳🇱 NL | 1376 |
| 29 | 🇭🇷 HR | 1344 |
| 30 | 🇲🇴 MO | 1235 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3039 |
| 2 | Denver International Airport |  | US | 2473 |
| 3 | Tokyo International Airport |  | JP | 1972 |
| 4 | Indira Gandhi International Airport |  | IN | 1852 |
| 5 | Harry Reid International Airport |  | US | 1840 |
| 6 | Guaymaral Airport |  | CO | 1827 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1666 |
| 8 | Zurich Airport |  | CH | 1629 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1555 |
| 10 | La Aurora Airport |  | GT | 1488 |
| 11 | Frankfurt am Main International Airport |  | DE | 1402 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1388 |
| 13 | Chicago O'Hare International Airport |  | US | 1368 |
| 14 | Salt Lake City International Airport |  | US | 1330 |
| 15 | El Dorado International Airport |  | CO | 1326 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1276 |
| 17 | Macau International Airport |  | MO | 1235 |
| 18 | Capua Airport |  | IT | 1193 |
| 19 | Congonhas Airport |  | BR | 1192 |
| 20 | Madrid Barajas International Airport |  | ES | 1174 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1153 |
| 22 | Kuala Lumpur International Airport |  | MY | 1075 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1066 |
| 24 | Charlotte/Douglas International Airport |  | US | 1053 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1038 |
| 26 | Charles de Gaulle International Airport |  | FR | 1022 |
| 27 | Bengaluru International Airport |  | IN | 998 |
| 28 | Malpensa International Airport |  | IT | 956 |
| 29 | Ninoy Aquino International Airport |  | PH | 926 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 903 |
| 31 | Barcelona International Airport |  | ES | 891 |
| 32 | Daniel K Inouye International Airport |  | US | 887 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 885 |
| 34 | Tenerife Norte Airport |  | ES | 848 |
| 35 | Seattle-Tacoma International Airport |  | US | 847 |
| 36 | Calgary International Airport |  | CA | 844 |
| 37 | Scottsdale Airport |  | US | 837 |
| 38 | Viracopos International Airport |  | BR | 836 |
| 39 | Amsterdam Airport Schiphol |  | NL | 829 |
| 40 | Oslo Gardermoen Airport |  | NO | 818 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 771 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 535 | 21m | 244 km | 2,252.7 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 360 | 24m | 225 km | 1,396.6 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 359 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 346 | 1h 9m | 770 km | 4,596.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 300 | 14m | 114 km | 588.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 289 | 1h 7m | 706 km | 3,518.6 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 268 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 265 | 27m | 275 km | 1,255.7 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 222 | 22m | 55 km | 211.0 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 200 | 44m | 241 km | 830.8 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 198 | 1h 46m | 1,423 km | 4,859.2 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 196 | 26m | 215 km | 725.9 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 195 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 191 | 20m | 99 km | 327.2 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 181 | 20m | 250 km | 781.8 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 181 | 27m | 152 km | 473.0 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 175 | 31m | 369 km | 1,113.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 174 | 18m | 144 km | 432.8 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 172 | 1h 16m | 961 km | 2,851.0 t |
| 24 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 171 | 12m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 170 | 44m | 452 km | 1,324.9 t |
| 27 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 168 | 1h 1m | 695 km | 2,013.8 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 167 | 1h 39m | 1,156 km | 3,331.6 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 162 | 14m | 154 km | 429.2 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 161 | 55m | 136 km | 377.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N3504P |  | Dupage Airport (KDPA) | Ruder Airport (59IL) | 2026-07-24 15:21 UTC | 2026-07-24 15:33 UTC | 11m |
| N702 |  | Crystal Lakes Airport (25CO) | Crystal Lakes Airport (25CO) | 2026-07-24 14:59 UTC | 2026-07-24 15:31 UTC | 31m |
| SAS4717 | Scandinavian Airlines | Oslo Gardermoen Airport (ENGM) | Malpensa International Airport (LIMC) | 2026-07-24 13:17 UTC | 2026-07-24 15:29 UTC | 2h 12m |
| DSU90 | DSU | Glidwell Flying Service Airport (MS09) | Cleveland Municipal Airport (KRNV) | 2026-07-24 15:03 UTC | 2026-07-24 15:29 UTC | 26m |
| N1026V |  | Ted Stevens Anchorage International Airport (PANC) | Kenai Municipal Airport (PAEN) | 2026-07-24 15:03 UTC | 2026-07-24 15:26 UTC | 22m |
| CHX1 | CHX | Oberschleisheim Airfield (EDNX) | Oberschleisheim Airfield (EDNX) | 2026-07-24 15:16 UTC | 2026-07-24 15:22 UTC | 5m |
| CFNQN | CFN | Humboldt Airport (CJU4) | Humboldt Airport (CJU4) | 2026-07-24 15:07 UTC | 2026-07-24 15:19 UTC | 12m |
| N39049 |  | Camarillo Airport (KCMA) | Camarillo Airport (KCMA) | 2026-07-24 14:52 UTC | 2026-07-24 15:19 UTC | 26m |
| BL502 |  | K4R4 (K4R4) | Jeremiah Denton Airport (K4R9) | 2026-07-24 14:30 UTC | 2026-07-24 15:17 UTC | 47m |
|  |  | Flying Acres Airport (MD70) | Breezecroft Airport (05MD) | 2026-07-24 13:36 UTC | 2026-07-24 15:16 UTC | 1h 39m |
| CXK437 | CXK | Long Beach (Daugherty Field) Airport (KLGB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-07-24 14:30 UTC | 2026-07-24 15:16 UTC | 46m |
| N622TP |  | Tweed/New Haven Airport (KHVN) | Laguardia Airport (KLGA) | 2026-07-24 14:43 UTC | 2026-07-24 15:13 UTC | 30m |
| CGHFB | CGH | Peterborough Airport (CYPQ) | Peterborough Airport (CYPQ) | 2026-07-24 14:47 UTC | 2026-07-24 15:11 UTC | 24m |
| N4000K |  | 14MI (14MI) | Iowa City Municipal Airport (KIOW) | 2026-07-24 14:19 UTC | 2026-07-24 15:10 UTC | 51m |
| N23AR |  | London Stansted Airport (EGSS) | Bournemouth Airport (EGHH) | 2026-07-24 14:38 UTC | 2026-07-24 15:09 UTC | 30m |
| DAL662 | Delta Air Lines | Portland International Airport (KPDX) | Fort Smith Landing Strip (K5U7) | 2026-07-24 13:49 UTC | 2026-07-24 15:07 UTC | 1h 17m |
| N967BY |  | Chicago Executive Airport (KPWK) | Stag Air Park (7NC1) | 2026-07-24 13:34 UTC | 2026-07-24 15:06 UTC | 1h 32m |
| DESERT8 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-07-24 14:43 UTC | 2026-07-24 15:04 UTC | 20m |
| N87PW |  | Boise Air Trml/Gowen Field (KBOI) | Buchanan Field (KCCR) | 2026-07-24 13:35 UTC | 2026-07-24 15:02 UTC | 1h 26m |
| N48JA |  | Aurora Municipal Airport (KARR) | De Kalb Taylor Municipal Airport (KDKB) | 2026-07-24 14:45 UTC | 2026-07-24 15:01 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
