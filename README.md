# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--02_19:44:28_UTC-green)

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

**Latest saved flight:** 2026-08-02 19:44:28 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-02 19:44:28 UTC

- **167,495** saved flights
- **54,797** unique routes
- **139** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **167,495** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,018,022.9 tonnes** estimated CO2 emissions
- **116,986,835 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6684 |
| 2 | SkyWest Airlines | 6095 |
| 3 | EJA | 3328 |
| 4 | IndiGo | 2951 |
| 5 | American Airlines | 2643 |
| 6 | Southwest Airlines | 2633 |
| 7 | ENY | 2085 |
| 8 | Delta Air Lines | 1998 |
| 9 | LATAM Airlines | 1551 |
| 10 | Lufthansa | 1543 |
| 11 | AZU | 1475 |
| 12 | WIF | 1401 |
| 13 | Vueling | 1380 |
| 14 | LXJ | 1306 |
| 15 | AXM | 1154 |
| 16 | Swiss International | 1150 |
| 17 | easyJet | 1125 |
| 18 | EJU | 1032 |
| 19 | Alaska Airlines | 1027 |
| 20 | QLK | 1020 |
| 21 | All Nippon Airways | 1017 |
| 22 | VIV | 924 |
| 23 | CXK | 891 |
| 24 | Cathay Pacific | 889 |
| 25 | United Airlines | 882 |
| 26 | AEE | 880 |
| 27 | GLO | 878 |
| 28 | Air France | 865 |
| 29 | MXY | 863 |
| 30 | JetBlue | 844 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 144369 |
| 2 | 🇪🇸 ES | 10729 |
| 3 | 🇧🇷 BR | 9538 |
| 4 | 🇦🇺 AU | 9344 |
| 5 | 🇮🇳 IN | 9253 |
| 6 | 🇨🇦 CA | 9071 |
| 7 | 🇮🇹 IT | 8651 |
| 8 | 🇩🇪 DE | 8367 |
| 9 | 🇬🇧 GB | 7780 |
| 10 | 🇯🇵 JP | 6740 |
| 11 | 🇫🇷 FR | 6648 |
| 12 | 🇨🇴 CO | 6027 |
| 13 | 🇬🇷 GR | 4871 |
| 14 | 🇲🇽 MX | 4794 |
| 15 | 🇨🇭 CH | 4416 |
| 16 | 🇳🇴 NO | 4378 |
| 17 | 🇹🇷 TR | 4059 |
| 18 | 🇲🇾 MY | 3009 |
| 19 | 🇵🇱 PL | 2830 |
| 20 | 🇿🇦 ZA | 2723 |
| 21 | 🇳🇿 NZ | 2432 |
| 22 | 🇹🇭 TH | 2424 |
| 23 | 🇵🇭 PH | 2211 |
| 24 | 🇬🇹 GT | 2169 |
| 25 | 🇰🇷 KR | 2147 |
| 26 | 🇲🇦 MA | 1691 |
| 27 | 🇭🇷 HR | 1605 |
| 28 | 🇲🇪 ME | 1550 |
| 29 | 🇳🇱 NL | 1524 |
| 30 | 🇲🇴 MO | 1426 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3433 |
| 2 | Denver International Airport |  | US | 2777 |
| 3 | Tokyo International Airport |  | JP | 2117 |
| 4 | Guaymaral Airport |  | CO | 2090 |
| 5 | Indira Gandhi International Airport |  | IN | 2049 |
| 6 | Harry Reid International Airport |  | US | 2012 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1841 |
| 8 | Zurich Airport |  | CH | 1785 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1758 |
| 10 | La Aurora Airport |  | GT | 1676 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1544 |
| 12 | El Dorado International Airport |  | CO | 1521 |
| 13 | Chicago O'Hare International Airport |  | US | 1513 |
| 14 | Frankfurt am Main International Airport |  | DE | 1510 |
| 15 | Salt Lake City International Airport |  | US | 1499 |
| 16 | Macau International Airport |  | MO | 1426 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1392 |
| 18 | Congonhas Airport |  | BR | 1376 |
| 19 | Madrid Barajas International Airport |  | ES | 1320 |
| 20 | Capua Airport |  | IT | 1303 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1274 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1179 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1176 |
| 24 | Charlotte/Douglas International Airport |  | US | 1170 |
| 25 | Charles de Gaulle International Airport |  | FR | 1143 |
| 26 | Kuala Lumpur International Airport |  | MY | 1137 |
| 27 | Malpensa International Airport |  | IT | 1124 |
| 28 | Bengaluru International Airport |  | IN | 1095 |
| 29 | Ninoy Aquino International Airport |  | PH | 1039 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1030 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1030 |
| 32 | Barcelona International Airport |  | ES | 987 |
| 33 | Daniel K Inouye International Airport |  | US | 975 |
| 34 | Seattle-Tacoma International Airport |  | US | 971 |
| 35 | Viracopos International Airport |  | BR | 955 |
| 36 | Calgary International Airport |  | CA | 946 |
| 37 | Tenerife Norte Airport |  | ES | 932 |
| 38 | Oslo Gardermoen Airport |  | NO | 929 |
| 39 | Scottsdale Airport |  | US | 929 |
| 40 | Reno/Tahoe International Airport |  | US | 924 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 870 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 609 | 21m | 244 km | 2,564.3 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 401 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 400 | 24m | 225 km | 1,551.8 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 381 | 1h 9m | 770 km | 5,061.3 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 316 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 288 | 27m | 275 km | 1,364.7 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 253 | 22m | 55 km | 240.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 245 | 19m | 165 km | 696.9 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 244 | 44m | 241 km | 1,013.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 231 | 1h 47m | 1,423 km | 5,669.1 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 221 | 20m | 250 km | 954.6 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 218 | 26m | 215 km | 807.4 t |
| 18 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 213 | 31m | 49 km | 180.0 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 210 | 13m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 210 | 20m | 99 km | 359.7 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 199 | 28m | 152 km | 520.1 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 198 | 1h 15m | 961 km | 3,282.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 197 | 19m | 144 km | 490.0 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 194 | 31m | 369 km | 1,234.9 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 190 | 50m | 556 km | 1,821.3 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 190 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 187 | 1h 38m | 1,156 km | 3,730.6 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 184 | 24m | 218 km | 693.2 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 183 | 1h 1m | 695 km | 2,193.6 t |
| 30 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 182 | 44m | 452 km | 1,418.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FTO501 | FTO | Talmage Field (03NY) | Laguardia Airport (KLGA) | 2026-08-02 19:17 UTC | 2026-08-02 19:44 UTC | 26m |
| EVA6529 | EVA Air | Taiwan Taoyuan International Airport (RCTP) | Chek Lap Kok International Airport (VHHH) | 2026-08-02 18:31 UTC | 2026-08-02 19:43 UTC | 1h 11m |
| TKR02 | TKR | Hill Afb Airport (KHIF) | Nephi Municipal Airport (KU14) | 2026-08-02 19:08 UTC | 2026-08-02 19:28 UTC | 20m |
| N234WL |  | Talmage Field (03NY) | Laguardia Airport (KLGA) | 2026-08-02 18:55 UTC | 2026-08-02 19:22 UTC | 27m |
| N6228N |  | Westchester County Airport (KHPN) | Tweed/New Haven Airport (KHVN) | 2026-08-02 18:33 UTC | 2026-08-02 19:19 UTC | 46m |
| CTM1192 | CTM | Faa'a International Airport (NTAA) | Tikehau Airport (NTGC) | 2026-08-02 18:50 UTC | 2026-08-02 19:19 UTC | 29m |
| AAL3264 | American Airlines | Chicago O'Hare International Airport (KORD) | Dallas-Fort Worth International Airport (KDFW) | 2026-08-02 17:31 UTC | 2026-08-02 19:17 UTC | 1h 46m |
| IGO9023 | IndiGo | Bakshi Ka Talab Air Force Station (VIBL) | Chaudhary Charan Singh International Airport (VILK) | 2026-08-02 18:45 UTC | 2026-08-02 19:16 UTC | 30m |
| RAM997 | Royal Air Maroc | Francisco de Sá Carneiro Airport (LPPR) | Tit Mellil Airport (GMMT) | 2026-08-02 18:03 UTC | 2026-08-02 19:11 UTC | 1h 7m |
| LXJ506 | LXJ | Van Nuys Airport (KVNY) | Polson Airport (K8S1) | 2026-08-02 17:14 UTC | 2026-08-02 19:09 UTC | 1h 55m |
| N972CC |  | Burke Lakefront Airport (KBKL) | Wadsworth Municipal Airport (K3G3) | 2026-08-02 18:50 UTC | 2026-08-02 19:07 UTC | 17m |
| N648SP |  | Roberts Field (KRDM) | Goering Ranches / Chocheta Estates Airport (50OR) | 2026-08-02 18:58 UTC | 2026-08-02 19:07 UTC | 8m |
| N728AB |  | Wayne County Airport (KBJJ) | 91OI (91OI) | 2026-08-02 18:54 UTC | 2026-08-02 19:06 UTC | 11m |
| N725FH |  | Homer Airport (PAHO) | Bootleggers Cove Airport (2AK4) | 2026-08-02 18:54 UTC | 2026-08-02 19:04 UTC | 10m |
| N219RB |  | Oakland County International Airport (KPTK) | Antrim County Airport (KACB) | 2026-08-02 18:37 UTC | 2026-08-02 19:02 UTC | 25m |
| ERU12 | ERU | Yav'Pe Ma'Ta Airport (16AZ) | Big Sandy Airport (AZ71) | 2026-08-02 18:36 UTC | 2026-08-02 19:01 UTC | 24m |
| UAL273 | United Airlines | Nice-Cote d'Azur Airport (LFMN) | Newark Liberty International Airport (KEWR) | 2026-08-02 10:34 UTC | 2026-08-02 19:00 UTC | 8h 25m |
| EZY27DV | easyJet | Glasgow International Airport (EGPF) | Bristol International Airport (EGGD) | 2026-08-02 18:05 UTC | 2026-08-02 18:56 UTC | 50m |
| ZKIWG | ZKI | Dunedin Airport (NZDN) | Taieri Airport (NZTI) | 2026-08-02 18:42 UTC | 2026-08-02 18:55 UTC | 12m |
| AAN141 | AAN | Lugano Airport (LSZA) | Santorini Airport (LGSR) | 2026-08-02 16:39 UTC | 2026-08-02 18:53 UTC | 2h 14m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
